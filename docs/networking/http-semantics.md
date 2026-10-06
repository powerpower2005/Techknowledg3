---
title: HTTP 메서드, 캐시와 재시도
category: networking
tags:
- http
- networking
- caching
- reliability
status: note
visibility: public
reviewed_at: '2026-10-07'
publication_reviewed_at: '2026-10-07'
applies_to: RFC 9110 HTTP 의미와 RFC 9111 캐시
---

# HTTP 메서드, 캐시와 재시도

HTTP는 요청 메서드, 대상 URI, 헤더와 본문으로 요청을 표현하고 응답 상태와 표현을 돌려준다. 메서드의 의미를 지키면 클라이언트, 프록시와 캐시가 요청을 올바르게 처리하기 쉬워진다.

## 안전성과 멱등성

안전한 메서드는 클라이언트가 서버의 상태 변경을 요청하지 않는다. 멱등성은 동일 요청을 여러 번 보내도 의도한 서버 효과가 한 번 보냈을 때와 같다는 성질이다. 요청마다 로그가 쌓이거나 응답 코드가 달라지는 것은 가능하다.

| 메서드 | 의도 | 표준 의미의 안전성 / 멱등성 |
| --- | --- | --- |
| GET | 표현 조회 | 안전 / 멱등 |
| HEAD | GET과 대응하는 응답 헤더 조회, 응답 본문 없음 | 안전 / 멱등 |
| POST | 대상에 따른 처리·생성 요청 | 기본적으로 둘 다 보장하지 않음 |
| PUT | 대상 표현 생성 또는 교체 | 비안전 / 멱등 |
| DELETE | 대상과 현재 기능의 연결 제거 | 비안전 / 멱등 |

DELETE를 처음 보내면 204, 다시 보내면 404가 나올 수 있어도 대상이 제거된 효과는 같을 수 있다. 반대로 GET으로 결제를 수행하는 구현은 안전한 메서드의 계약을 어긴다. PATCH는 부분 변경에 쓰지만 연산 내용에 따라 멱등일 수도 아닐 수도 있다.

## 상태 코드를 읽기

200은 성공, 201은 생성, 204는 응답 본문 없는 성공이다. 304는 조건부 조회에서 기존 캐시 표현을 재사용할 수 있음을 알린다. 400은 잘못된 요청, 401은 유효한 인증 정보가 필요함, 403은 요청 수행 거부, 404는 대상 없음 또는 존재를 공개하지 않는 경우다. 409는 현재 상태와의 충돌, 429는 요청 빈도 제한을 표현한다.

500은 서버 내부 오류, 503은 현재 서비스 제공 불가를 표현한다. 코드만으로 재시도가 안전한지 정하지 않는다. 502·504처럼 중간 서버가 낸 오류에서도 뒤의 서버가 변경을 완료했을 가능성이 있다.

## 캐시: 저장과 재검증 구분

| 응답 Cache-Control | 의미 |
| --- | --- |
| `max-age=60` | freshness lifetime을 60초로 지정. age를 반영해서 남은 신선도를 계산 |
| `no-cache` | 저장 가능하지만 재사용 전에 성공적인 재검증 필요 |
| `no-store` | 이 응답을 저장하지 않도록 요구 |
| `private` | 공유 캐시 저장 제한, 개인 캐시는 사용 가능 |

no-store가 이전에 저장된 모든 사본을 자동 삭제하는 것은 아니다. 개인화된 데이터와 공개 정적 파일은 서로 다른 정책으로 다룬다. `Vary`는 응답 선택에 영향을 준 요청 헤더를 캐시에 알린다.

아래는 학습용 요청·응답 일부다. ETag가 바뀌지 않았다고 서버가 확인하면 본문 전송을 줄일 수 있다.

```http
HTTP/1.1 200 OK
ETag: "article-v3"
Cache-Control: no-cache
```

```http
GET /articles/42 HTTP/1.1
Host: example.test
If-None-Match: "article-v3"
```

```http
HTTP/1.1 304 Not Modified
ETag: "article-v3"
Cache-Control: no-cache
```

캐시 재검증과 로그인 인증은 다른 과정이다. 304에는 새 표현 본문이 없으며 클라이언트는 이미 저장한 표현을 사용한다.

## 응답을 못 받았을 때

주문 POST 후 timeout이 나면 주문이 실패했다고 단정할 수 없다. 요청이 도달하지 않았거나, 서버가 처리한 뒤 응답만 사라졌을 수 있다. 자동 재시도에는 중복을 막는 계약이 필요하다.

같은 논리적 주문에 같은 idempotency key를 재사용하고 서버는 사용자·키·요청 내용·처리 결과를 함께 관리한다. 같은 키로 다른 주문 내용이 오면 거부해야 한다. 키의 유효 기간과 처리 중 응답도 정의한다. 이것은 POST가 기본적으로 멱등이라는 뜻이 아니라 API에 추가한 계약이다.

재시도 횟수와 전체 deadline을 제한하고 지수 backoff와 jitter를 사용한다. rate limit이나 서비스가 안내한 Retry-After도 고려한다. 취소가 뒤 서버의 작업까지 반드시 취소시키는 것은 아니다.

## 면접 꼬리 질문

- PUT과 POST의 차이는 단순히 수정과 생성인가? 대상 URI와 처리 의미를 설명한다.
- no-cache와 no-store는 왜 다른가? 저장과 재사용을 나눈다.
- timeout 후 결제를 다시 요청해도 되는가? 중복 처리와 결과 확인을 설명한다.

[네트워크 개요](network.md) · [CDN](../cloud/aws/cloudfront.md) · [주문 서비스 설계](../architecture/web-service-design.md)

## 참고 자료와 확인

HTTP 블록은 프로토콜 설명용이다. 실제 서버와 캐시를 대상으로 동작을 시험한 결과는 아니다.

- [RFC 9110 §9: 메서드](https://www.rfc-editor.org/rfc/rfc9110.html#section-9)
- [RFC 9111 §5.2: Cache-Control](https://www.rfc-editor.org/rfc/rfc9111.html#section-5.2)
- [AWS Builders Library: 멱등 API와 재시도](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#http](../tags.md#http) · [#networking](../tags.md#networking) · [#caching](../tags.md#caching) · [#reliability](../tags.md#reliability)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
