---
title: GitOps
category: devops
tags:
- ci-cd
- deployment
- devops
- gitops
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
reviewed_at: '2026-10-06'
applies_to: OpenGitOps의 선언·버전·pull·조정 원칙
content_origin: original-summary
---

# GitOps

GitOps는 원하는 시스템 상태를 선언하고 버전으로 관리하며 에이전트가 그 상태를 가져와 지속적으로 실제 상태와 조정하는 운영 방식이다. 변경 제안과 검토 이력으로 상태의 의도를 설명할 수 있다.

## 변경 흐름

애플리케이션을 빌드하고 산출물을 식별한다. 배포 명세에서 그 산출물을 참조하도록 변경하고 검토한다. 조정 도구가 명세와 실제 상태의 차이를 확인해 정해진 정책에 따라 적용한다.

Git 명세를 되돌리는 것은 목표 상태를 바꾸는 방법이다. DB 데이터, 외부 서비스나 이미 수행된 작업까지 자동으로 원복되는 것은 아니다. secret은 저장 방식과 접근 권한을 별도로 설계하고 Git에 평문 인증 정보를 넣지 않는다.

GitOps와 Git Flow 같은 브랜치 전략은 같은 개념이 아니다. 어떤 브랜치 전략을 쓰든 상태 변경의 검증과 조정 정책을 일관되게 운영한다.

[Argo CD](argocd.md) · [CI/CD](general.md)

## 참고 자료

- [OpenGitOps 원칙](https://opengitops.dev/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#ci-cd](../../tags.md#ci-cd) · [#deployment](../../tags.md#deployment) · [#devops](../../tags.md#devops) · [#gitops](../../tags.md#gitops)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
