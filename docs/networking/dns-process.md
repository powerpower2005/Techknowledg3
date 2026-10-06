---
title: DNS와 HTTP 요청 관찰
category: networking
tags:
- dns
- http
- networking
- troubleshooting
status: note
reviewed_at: '2026-10-06'
applies_to: Windows PowerShell의 로컬 HTTP 조회와 Linux foreground 추적 절차
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# DNS와 HTTP 요청 관찰

DNS 주소 해석, TCP 연결, HTTP 응답을 따로 확인한다. IP 하나의 TCP 연결 성공은 해당 hostname의 모든 주소나 HTTPS 인증서·HTTP routing 성공을 뜻하지 않는다.

## Windows 로컬 실습

[PowerShell 예제](examples/inspect-http.ps1)는 loopback URL만 허용한다. DNS 결과가 여러 개면 IPv4 한 개를 선택하고, HTTP 요청에는 원래 URI를 사용하여 Host/TLS 이름을 유지한다. 짧은 본문도 `min(500, length)`로 안전하게 출력한다.

```powershell
powershell -NoProfile -File docs/networking/examples/inspect-http.ps1 -Url http://127.0.0.1:8001/Techknowledg3/
```

Test-NetConnection과 Invoke-WebRequest는 각각 별도의 연결을 만든다. 선택한 IP의 연결 검사와 실제 HTTP 연결이 동일하다는 뜻이 아니다. 기본 URL은 먼저 로컬 위키 서버를 실행해야 한다. IPv6 환경은 지원 cmdlet과 주소 처리를 별도로 확인한다.

## Linux: 추적 결과를 끝난 뒤 읽기

```sh
strace -f -o strace_output.txt curl --max-time 10 http://127.0.0.1:8001/Techknowledg3/
# foreground strace와 curl이 끝난 다음 읽는다.
cat strace_output.txt
perf stat -- curl --max-time 10 http://127.0.0.1:8001/Techknowledg3/
```

PATH의 curl을 사용하며 `./curl`이 있다고 가정하지 않는다. perf는 커널·권한 설정에 따라 사용할 수 없을 수 있다.

패킷 캡처가 필요하면 첫 터미널에서 `sudo tcpdump -i lo -w local-http.pcap 'tcp port 8001'`를 foreground로 실행한다. “listening”을 확인한 뒤 둘째 터미널에서 로컬 curl을 실행한다. 첫 터미널에서 Ctrl+C로 캡처 종료와 flush를 기다린 **후에** `tcpdump -r local-http.pcap`로 읽는다. 수집 중인 파일을 곧바로 완성된 결과처럼 읽지 않는다. 이 Linux 절차는 이번 Windows 검증에서 실제 실행하지 않았다.

## 적용 범위와 확인

Windows PowerShell의 로컬 HTTP 조회와 Linux foreground 추적 절차 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [strace](https://man7.org/linux/man-pages/man1/strace.1.html)
- [Resolve-DnsName](https://learn.microsoft.com/en-us/powershell/module/dnsclient/resolve-dnsname?view=windowsserver2025-ps)
- [Test-NetConnection](https://learn.microsoft.com/en-us/powershell/module/nettcpip/test-netconnection?view=windowsserver2025-ps)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#dns](../tags.md#dns) · [#http](../tags.md#http) · [#networking](../tags.md#networking) · [#troubleshooting](../tags.md#troubleshooting)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
