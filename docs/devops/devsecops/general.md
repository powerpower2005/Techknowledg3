---
title: DevSecOps
category: devops
tags:
- ci-cd
- devops
- security
status: note
reviewed_at: '2026-10-06'
applies_to: 일반적인 개발·운영 보안 실천
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# DevSecOps

DevSecOps는 개발·배포·운영 흐름에서 보안을 지속적으로 확인하는 접근이다. 한 scanner의 통과를 서비스 안전의 증명으로 간주하지 않는다.

## 단계별 확인

설계에서는 자산·신뢰 경계·공격 경로를 정리한다. 개발 단계는 코드 리뷰, Secret 검사와 dependency 분석을 포함한다. 빌드에서는 변경 불가능한 artifact와 provenance를 관리하고 배포에서는 최소 권한·정책과 승인 범위를 확인한다. 운영에서는 취약점 대응과 실제 접근·오류를 관찰한다.

## 작은 실습

테스트 문자열을 실제 키로 오인하는 경우와 실제 키 패턴을 놓치는 경우를 각각 검사한다. 발견 결과에는 원문 secret 대신 경로·유형·fingerprint를 남긴다. dependency 경보는 사용 여부와 공격 조건을 확인하여 우선순위를 정한다.

## 완료 기준

담당자, 영향 범위, 수정·검증과 예외의 만료를 기록한다. 저장소에서 키를 지워도 이미 노출된 키는 유효할 수 있어 철회·교체를 별도로 판단한다. CI 로그·artifact·Git 이력도 검사 범위에 포함한다.

## 적용 범위와 확인

일반적인 개발·운영 보안 실천 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#ci-cd](../../tags.md#ci-cd) · [#devops](../../tags.md#devops) · [#security](../../tags.md#security)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
