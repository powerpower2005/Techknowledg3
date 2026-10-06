---
title: 리버스 프록시와 HAProxy
category: networking
tags:
- load-balancing
- networking
- proxy
status: note
reviewed_at: '2026-10-06'
applies_to: HAProxy 3.0 HTTP 모드의 개념 예시
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# 리버스 프록시와 HAProxy

리버스 프록시는 클라이언트 요청을 받아 백엔드로 전달한다. TLS 종료, 라우팅, 부하 분산, 접근 로그를 담당할 수 있으며 애플리케이션의 사용자 권한 검사까지 자동으로 대신하지는 않는다.

## 학습용 HTTP 구성

```text
frontend demo_http
    bind 127.0.0.1:8080
    mode http
    default_backend demo_app

backend demo_app
    mode http
    balance roundrobin
    option httpchk GET /health
    server app1 127.0.0.1:9001 check
    server app2 127.0.0.1:9002 check
```

백엔드에 `/health`가 구현되어 있어야 한다. 이 예시는 로컬 실습용이며 TLS나 운영 인증을 구성하지 않는다. 실제 배포에서는 연결·서버 시간 제한, 신뢰하는 프록시 범위, 전달 헤더 처리, TLS 인증서와 종료 시 동작을 명시한다.

## 진단

DNS가 프록시를 가리키는지 → 프록시 listener → 라우팅 규칙 → 백엔드 health → 애플리케이션 응답 순서로 확인한다. 직접 백엔드 요청 성공과 프록시 경유 성공을 구분한다. `X-Forwarded-For`는 클라이언트가 보낼 수도 있으므로 신뢰 경계를 정하지 않은 채 인증 근거로 사용하지 않는다.

## 적용 범위와 확인

HAProxy 3.0 HTTP 모드의 개념 예시 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [HAProxy 구성 설명서](https://docs.haproxy.org/3.0/configuration.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#load-balancing](../tags.md#load-balancing) · [#networking](../tags.md#networking) · [#proxy](../tags.md#proxy)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
