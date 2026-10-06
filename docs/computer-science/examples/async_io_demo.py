"""Local-only I/O experiment. Python 3.12+, no external packages or endpoints."""
import argparse
import asyncio
from concurrent.futures import ThreadPoolExecutor
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import re
import socket
import threading
import time


class Server(ThreadingHTTPServer):
    request_queue_size = 128
    daemon_threads = True


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        match = re.fullmatch(r'/items/(\d+)', self.path)
        if not match:
            self.send_error(404)
            return
        time.sleep(self.server.delay)
        body = json.dumps({'id': int(match[1])}).encode()
        self.send_response(200)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Connection', 'close')
        self.end_headers()
        self.wfile.write(body)
        self.close_connection = True

    def log_message(self, *args):
        pass


def request_bytes(port, item):
    return (f'GET /items/{item} HTTP/1.1\r\nHost: 127.0.0.1:{port}\r\n'
            'Connection: close\r\n\r\n').encode()


def parse_response(raw):
    headers, body = raw.split(b'\r\n\r\n', 1)
    assert headers.split(b'\r\n', 1)[0].split()[1] == b'200'
    return json.loads(body)['id']


def sync_request(port, item):
    with socket.create_connection(('127.0.0.1', port), timeout=10) as connection:
        connection.sendall(request_bytes(port, item))
        chunks = []
        while chunk := connection.recv(4096):
            chunks.append(chunk)
    return parse_response(b''.join(chunks))


async def async_requests(port, count, concurrency):
    semaphore = asyncio.Semaphore(concurrency)

    async def request(item):
        async with semaphore, asyncio.timeout(10):
            reader, writer = await asyncio.open_connection('127.0.0.1', port)
            try:
                writer.write(request_bytes(port, item))
                await writer.drain()
                return parse_response(await reader.read())
            finally:
                writer.close()
                await writer.wait_closed()

    return await asyncio.gather(*(request(i) for i in range(count)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--count', type=int, default=40)
    parser.add_argument('--concurrency', type=int, default=8)
    parser.add_argument('--delay', type=float, default=0.01)
    args = parser.parse_args()
    if not (1 <= args.count <= 1000 and 1 <= args.concurrency <= 64 and 0 <= args.delay <= 1):
        parser.error('count: 1..1000; concurrency: 1..64; delay: 0..1 seconds')
    server = Server(('127.0.0.1', 0), Handler)
    server.delay = args.delay
    worker = threading.Thread(target=server.serve_forever, daemon=True)
    worker.start()
    port = server.server_address[1]
    results = {'count': args.count, 'concurrency': args.concurrency, 'delay': args.delay,
               'target': 'loopback mock only', 'runs': {}}
    try:
        for method in ('sequential', 'thread-pool', 'asyncio'):
            started = time.perf_counter()
            if method == 'sequential':
                ids = [sync_request(port, i) for i in range(args.count)]
            elif method == 'thread-pool':
                with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
                    ids = list(pool.map(lambda i: sync_request(port, i), range(args.count)))
            else:
                ids = asyncio.run(async_requests(port, args.count, args.concurrency))
            assert ids == list(range(args.count)), (method, ids)
            results['runs'][method] = {'seconds': round(time.perf_counter() - started, 6),
                                      'verified_responses': len(ids)}
    finally:
        server.shutdown()
        server.server_close()
        worker.join(timeout=5)
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
