---
title: Argo CD 학습 순서
category: devops
tags:
- argocd
- ci-cd
- devops
- gitops
status: note
reviewed_at: '2026-10-06'
applies_to: Argo CD stable 문서의 GitOps 동기화 개념
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# Argo CD 학습 순서

## Git과 클러스터의 상태 연결

Argo CD는 Git의 원하는 상태와 Kubernetes의 실제 상태를 비교한다. Application에는 source, destination, project를 지정한다. source는 manifest·Helm·Kustomize 등을 사용할 수 있으며 destination의 cluster·namespace와 권한을 함께 확인한다.

## 비교, 동기화, 상태

OutOfSync는 원하는 상태와 차이가 있다는 뜻이고 Healthy는 health 평가 결과다. 둘은 같은 판단이 아니다. 먼저 diff와 대상 context를 확인한 뒤 개인 실습 환경에서 sync를 연습한다.

자동 sync, prune, self-heal은 별도 설정이다. prune은 Git에서 없어진 자원의 삭제로 이어질 수 있고 self-heal은 수동 변경을 원하는 상태로 되돌릴 수 있다. ApplicationSet이 관리하는 Application은 상위 설정의 영향을 받는다.

## 진단 예시

이미지 tag가 변경되어도 Git manifest가 같은지, destination namespace가 맞는지, Secret과 CRD가 먼저 준비됐는지 확인한다. sync 실패와 앱의 런타임 실패를 구분한다. 원격 Git에 비밀 원문을 저장하지 않는다. 상세 메모는 [Argo CD와 GitOps](argocd.md)를 참고한다.

## 적용 범위와 확인

Argo CD stable 문서의 GitOps 동기화 개념 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [Argo CD 자동 동기화](https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#argocd](../../tags.md#argocd) · [#ci-cd](../../tags.md#ci-cd) · [#devops](../../tags.md#devops) · [#gitops](../../tags.md#gitops)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
