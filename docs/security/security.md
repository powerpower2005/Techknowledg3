---
title: 보안 개요
category: security
tags:
- cryptography
- ddos
- security
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
reviewed_at: '2026-10-06'
applies_to: 일반 웹 보안 개념; 실제 방어 구성은 서비스 요건별 검증
content_origin: original-summary
---

# 보안 기본 개념

보안 대책은 데이터의 기밀성·무결성·가용성과 접근 권한을 함께 다룬다. 인증은 누구인지 확인하고 인가는 어떤 작업을 허용할지 결정한다. 인증된 사용자도 모든 데이터에 접근할 수 있는 것은 아니다.

## 암호화, 서명, 해시

대칭키 암호화는 공유된 비밀키를 사용한다. 공개키 암호는 공개키·개인키와 알고리즘의 정해진 연산을 사용하며 모든 알고리즘이 양쪽 키로 서로 암호화·복호화할 수 있는 것은 아니다. 디지털 서명은 무결성과 서명자 확인에 사용하며 내용을 숨기는 암호화와 구분한다.

해시는 데이터를 요약하는 함수다. 일반 해시 하나만으로 비밀번호 저장이나 메시지 인증을 해결하지 않는다. 목적에 맞는 password hashing, MAC, 서명 등의 구성을 선택한다.

## 방어 계층

네트워크 필터와 WAF는 서로 다른 관찰 지점과 규칙으로 트래픽을 제한할 수 있다. 제품 이름만으로 검사 가능한 계층이나 방어 효과를 단정하지 않는다. WAF가 애플리케이션의 CSRF 방어와 접근 제어를 자동으로 대체하는 것은 아니다.

가용성 보호에는 요청 제한, 용량·의존성 관찰과 장애 대응을 함께 설계한다. 로그와 예제에는 실제 인증 정보가 들어가지 않도록 한다.

[TLS와 중간자 공격](mitm/mitm.md) · [세션과 토큰](session-token/session-token.md) · [CORS](cors/cors.md)

## 참고 자료

- [OWASP TLS](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)
- [OWASP CSRF](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
- [OWASP 비밀번호 저장](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#cryptography](../tags.md#cryptography) · [#ddos](../tags.md#ddos) · [#security](../tags.md#security)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
