---
title: 중간자 공격 (MITM)
category: security
tags:
- cryptography
- networking
- security
- tls
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
reviewed_at: '2026-10-06'
applies_to: 일반 인증서 기반 TLS 보호와 상대 검증
content_origin: original-summary
---

# 중간자 공격과 TLS

중간자 공격은 통신 상대 사이에 끼어 데이터를 관찰하거나 바꾸는 공격이다. 암호화만 있고 상대 인증이 없으면 공격자와 별도의 암호화 연결을 맺을 수도 있으므로 상대 검증이 필요하다.

## 인증서 확인

TLS 인증서의 CA 서명은 공개키와 이름 등의 인증서 정보를 연결한다. CA가 공개키를 비밀스럽게 암호화해 전달하는 구조가 아니다. 클라이언트는 신뢰 체인, 유효 기간, 접속 이름과 SAN의 일치 등을 확인해야 한다.

인증서 검증을 끄거나 잘못된 신뢰 루트를 추가하면 보호가 약해질 수 있다. 단순히 인증서가 존재하거나 발급 대상 도메인이 같다는 사실만으로 안전성을 판단하지 않는다.

## 범위

TLS는 연결 구간을 보호한다. TLS 종료 지점과 백엔드 사이의 보호는 별도로 정한다. endpoint의 악성 코드, 유출된 키와 애플리케이션의 권한 오류까지 TLS가 해결하는 것은 아니다. 진단 시 오류를 우회하기보다 이름·신뢰 체인·시간·설정에서 원인을 찾는다.

## 참고 자료

- [TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446)
- [OWASP TLS 안내](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#cryptography](../../tags.md#cryptography) · [#networking](../../tags.md#networking) · [#security](../../tags.md#security) · [#tls](../../tags.md#tls)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
