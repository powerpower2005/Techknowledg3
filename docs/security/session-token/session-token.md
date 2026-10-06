---
title: 세션과 인증 토큰
category: security
tags:
- authentication
- security
status: note
reviewed_at: '2026-10-06'
applies_to: 일반적인 웹 인증 세션과 서명 토큰
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# 세션과 인증 토큰

인증 세션은 사용자의 인증 상태를 후속 요청과 연결하는 논리적 상태다. TCP 연결이나 브라우저 프로세스와 동일하지 않다. 연결이 다시 만들어져도 쿠키나 토큰으로 세션을 이어갈 수 있으며 브라우저 종료가 서버 세션을 즉시 삭제한다는 보장은 없다.

## 서버 세션과 토큰

서버 세션은 불투명한 난수 ID와 서버 측 상태를 연결한다. 서명된 토큰은 내용과 서명을 검증할 수 있지만 서명은 암호화가 아니다. JWT payload에 비밀번호나 불필요한 개인정보를 넣지 않는다. 발급자, audience, 만료, 허용 알고리즘과 키를 검증한다.

## 수명 주기

로그인·권한 변경 후 세션 ID를 재발급하여 fixation을 방지한다. idle timeout과 절대 만료를 구분하고 로그아웃·탈퇴·비밀번호 변경 시 무효화 정책을 정한다. refresh token은 재사용 탐지와 회전을 검토한다. 즉시 철회가 필요하면 완전한 무상태 토큰만으로 요구를 충족하기 어려울 수 있다.

쿠키는 HTTPS와 `Secure`, 스크립트 접근 제한인 `HttpOnly`, 서비스 흐름에 맞는 `SameSite`를 사용한다. 쿠키 인증에는 CSRF 대응을 별도로 둔다. 토큰을 로그나 URL query로 전달하지 않는다.

## 적용 범위와 확인

일반적인 웹 인증 세션과 서명 토큰 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [OWASP 세션 관리](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#authentication](../../tags.md#authentication) · [#security](../../tags.md#security)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
