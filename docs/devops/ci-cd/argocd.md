---
title: Argo CD와 GitOps
category: devops
tags:
- argocd
- ci-cd
- deployment
- devops
- gitops
- kubernetes
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
reviewed_at: '2026-10-06'
applies_to: Argo CD 일반 개념; 설정은 사용하는 버전에서 확인
content_origin: original-summary
---

# Argo CD와 GitOps

Argo CD는 선언된 Kubernetes 애플리케이션 상태와 클러스터 상태를 비교하고 동기화하는 CD 도구다. Application에 원본 저장소·경로와 대상 클러스터·namespace 등을 지정한다.

## 비교와 적용

OutOfSync는 원하는 상태와 차이가 있다는 의미다. 차이를 표시하는 것과 실제 변경을 적용하는 것은 별도 단계이며 수동 sync 또는 설정된 자동 정책에 따라 적용한다. 자동 동기화를 사용한다고 모든 리소스 삭제와 drift 복구가 기본으로 켜지는 것은 아니다. `prune`, `selfHeal`, `allowEmpty`의 의미를 각각 확인한다.

Git 명세와 이미지 식별자를 검토한 뒤 동기화 결과와 애플리케이션 health를 확인한다. health와 sync 상태는 다른 지표다. 권한, sync window와 배포 실패 시의 대응을 환경에 맞게 정한다.

## 점진적 배포

Argo Rollouts는 별도 controller와 Rollout 리소스로 canary나 blue-green 같은 전략을 지원한다. Argo CD 자체가 모든 분석과 트래픽 전환을 수행하는 것은 아니다. 새·이전 버전의 공존, 트래픽 경로와 데이터 호환성을 고려한다.

[실습 개요](argocd-outline.md)

## 참고 자료

- [Argo CD 자동 동기화](https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/)
- [Argo Rollouts](https://argoproj.github.io/argo-rollouts/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#argocd](../../tags.md#argocd) · [#ci-cd](../../tags.md#ci-cd) · [#deployment](../../tags.md#deployment) · [#devops](../../tags.md#devops) · [#gitops](../../tags.md#gitops) · [#kubernetes](../../tags.md#kubernetes)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
