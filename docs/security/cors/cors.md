---
title: CORS
category: security
tags:
- cors
- networking
- security
status: note
reviewed_at: '2026-10-06'
applies_to: 현행 URL/Fetch 표준의 HTTP(S) origin과 웹 브라우저
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# CORS

Origin은 scheme, host, port의 조합이다. HTTP 기본 포트는 80, HTTPS는 443이다. `https://app.example.test`와 `https://app.example.test:443`은 기본 포트 기준으로 같은 origin이지만 `http://app.example.test`는 다르다.

## 브라우저의 응답 접근 제어

Same-Origin Policy는 다른 origin의 응답을 읽는 동작을 제한한다. CORS는 서버가 허용한 origin에 브라우저의 응답 접근을 허용하는 프로토콜이다. 단순 요청은 preflight 없이 전송될 수 있다. CORS 오류가 났다는 사실만으로 요청이 서버에 도착하지 않았다고 판단하지 않는다.

```http
Access-Control-Allow-Origin: https://app.example.test
Access-Control-Allow-Credentials: true
Vary: Origin
```

쿠키 등 credentials를 포함한 요청에는 `Access-Control-Allow-Origin: *`를 사용할 수 없다. 허용 목록으로 검증한 origin만 응답에 반영한다. preflight는 요청 메서드와 헤더 허용 여부를 먼저 확인하며 실제 요청에도 서버 인증·인가를 수행해야 한다.

## CSRF와 구분

CORS 설정만으로 CSRF를 막을 수 없다. 쿠키 인증에서는 CSRF 토큰, Origin/Referer 검증, SameSite 정책 등 요청 위조에 대응하는 장치를 별도로 설계한다. 서버 간 호출에는 브라우저의 CORS 제약이 적용되지 않는다.

## 적용 범위와 확인

현행 URL/Fetch 표준의 HTTP(S) origin과 웹 브라우저 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [URL 기본 포트](https://url.spec.whatwg.org/#default-port)
- [Fetch CORS 프로토콜](https://fetch.spec.whatwg.org/#http-cors-protocol)
- [OWASP CSRF](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#cors](../../tags.md#cors) · [#networking](../../tags.md#networking) · [#security](../../tags.md#security)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
