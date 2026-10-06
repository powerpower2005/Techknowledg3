---
title: X.509 인증서
category: security
tags:
- cryptography
- security
- tls
status: note
reviewed_at: '2026-10-06'
applies_to: X.509 공개 인증서 조회와 TLS 1.3; OpenSSL 3.0 CLI
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# X.509 인증서

X.509 인증서는 공개키와 주체 정보를 발급자의 서명으로 연결한다. 인증서 자체는 보통 공개 정보이며 대응 개인키와 구분해야 한다. DER는 바이너리 인코딩, PEM은 Base64와 표식으로 표현한 형식이다. DER 파일을 “암호화된 인증서”라고 부르는 것은 부정확하다.

## HTTPS에서 확인할 것

신뢰할 수 있는 루트까지의 체인, 유효 기간, 서버 이름의 SAN 일치, 키 용도와 서명을 검증한다. 파일 확장자만으로 인증서·개인키·체인을 판정하지 않는다. self-signed 인증서는 클라이언트가 별도로 신뢰해야 한다.

```sh
# 공개 인증서 정보만 조회한다.
openssl x509 -in server-cert.pem -noout -subject -issuer -dates
openssl x509 -in server-cert.pem -noout -ext subjectAltName
```

TLS 1.3은 RSA로 premaster secret을 암호화해 보내는 방식의 key exchange를 사용하지 않는다. 일반적인 인증서 기반 연결은 (EC)DHE로 공유 비밀을 만들고 인증서 키의 서명으로 서버를 인증한다. PSK 기반 모드도 있으므로 모든 연결이 동일한 handshake라는 전제는 피한다. 인증서 RSA 키와 RSA key exchange는 다른 개념이다.

## 적용 범위와 확인

X.509 공개 인증서 조회와 TLS 1.3; OpenSSL 3.0 CLI 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446)
- [OpenSSL x509](https://docs.openssl.org/3.0/man1/openssl-x509/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#cryptography](../tags.md#cryptography) · [#security](../tags.md#security) · [#tls](../tags.md#tls)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
