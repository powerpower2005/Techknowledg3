---
title: 비동기 I/O 사례
category: computer-science
tags:
- async
- case-study
- computer-science
status: note
reviewed_at: '2026-10-06'
applies_to: Python 3.12+, 로컬 loopback mock I/O 실험
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# 비동기 I/O 로컬 실험

I/O를 기다리는 동안 다른 작업을 진행하면 전체 처리 시간이 줄어들 수 있다. 이것은 CPU 연산 속도가 빨라졌다는 뜻은 아니다. CPython의 GIL이 있는 구현에서도 blocking I/O를 기다리는 스레드는 다른 스레드의 진행을 허용할 수 있다. 코루틴은 await 지점에서 협력적으로 제어를 돌려주므로 이벤트 루프에서 blocking 함수를 그대로 호출하면 다른 작업을 막는다.

## 재현 가능한 예제

[실험 코드](examples/async_io_demo.py)는 Python 표준 라이브러리만 사용한다. 임의의 빈 loopback 포트에서 mock HTTP 서버를 시작하고 순차·스레드 풀·asyncio 방식으로 같은 개수의 요청을 보낸다. 응답 상태와 모든 ID를 확인하며 서버는 실험 후 정리한다. 기업 주소나 실제 알림 서비스에 요청하지 않는다.

```powershell
.\.venv\Scripts\python.exe docs/computer-science/examples/async_io_demo.py --count 40 --concurrency 8 --delay 0.01
```

## 비교 조건과 해석

세 방식은 요청마다 새 연결을 만들고 서버의 같은 인위적 지연을 기다린다. 동시성은 스레드 풀과 asyncio 모두 8로 제한한다. 출력의 seconds는 해당 PC의 로컬 모의 실험 결과이며 운영 처리량·CPU 작업·일반 HTTP client 성능으로 확대 해석하지 않는다. 최소 HTTP parser는 mock 응답만 처리하며 범용 HTTP client를 대신하지 않는다.

실제 외부 호출에는 재사용 연결, timeout, 취소, 제한된 retry, rate limit과 중복 처리 정책이 필요하다. 동시성 무제한 증가는 downstream 과부하를 만들 수 있다.

## 적용 범위와 확인

Python 3.12+, 로컬 loopback mock I/O 실험 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [asyncio streams](https://docs.python.org/3.12/library/asyncio-stream.html)
- [로컬 HTTP 서버](https://docs.python.org/3.12/library/http.server.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#async](../tags.md#async) · [#case-study](../tags.md#case-study) · [#computer-science](../tags.md#computer-science)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
