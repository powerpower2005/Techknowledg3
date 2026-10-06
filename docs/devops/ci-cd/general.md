---
title: CI/CD 개요
category: devops
tags:
- ci-cd
- deployment
- devops
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
reviewed_at: '2026-10-06'
applies_to: 일반 소프트웨어 개발·배포 프로세스
content_origin: original-summary
---

# CI/CD 개요

CI는 변경을 자주 통합하고 자동 빌드·검사·테스트로 문제를 빨리 발견하는 작업 방식이다. 자동화가 있다고 충돌이나 결함이 모두 사라지는 것은 아니다.

Continuous Delivery는 변경을 배포 가능한 상태로 유지하고 필요할 때 배포하는 방식이다. Continuous Deployment는 정해진 검증을 통과한 변경을 자동으로 운영에 반영한다. 승인 유무와 배포 조건을 명확히 구분한다.

## 파이프라인 예

변경 제안 → 정적 검사·테스트 → 재현 가능한 산출물 빌드 → 테스트 환경 검증 → 배포 조건 확인 → 운영 반영 → 결과 관찰 순서로 구성할 수 있다. 환경별 차이, 산출물 식별자와 접근 권한을 관리한다.

공통 템플릿은 반복 설정을 줄이지만 애플리케이션별 테스트·데이터 변경·복구 요건을 함께 표현해야 한다. 배포 후 오류율과 지연을 관찰하고 중단·롤백 기준을 준비한다. 무중단 배포는 상태 호환성, 연결 종료와 데이터 변경까지 맞아야 성립한다.

## 참고 자료

- [Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html)
- [Continuous Delivery](https://martinfowler.com/bliki/ContinuousDelivery.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#ci-cd](../../tags.md#ci-cd) · [#deployment](../../tags.md#deployment) · [#devops](../../tags.md#devops)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
