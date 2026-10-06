---
title: RBAC 장애 진단
category: containers
tags:
- authorization
- containers
- kubernetes
- troubleshooting
status: note
reviewed_at: '2026-10-06'
applies_to: Kubernetes 공통 진단; 실제 API와 기능은 설치 버전 확인
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# RBAC 장애 진단

개인 실습 클러스터에서만 아래 조회 예제를 사용한다. 먼저 `kubectl config current-context`로 대상과 namespace를 확인한다. `<이름>` 표시는 실제 리소스 이름으로 바꾼다. 변경·삭제보다 이벤트와 상태에서 실패 원인을 좁히는 것을 우선한다.

Role은 namespace 범위, ClusterRole은 cluster 범위의 권한 집합을 표현한다. RoleBinding과 ClusterRoleBinding은 권한을 주체에 연결한다. ClusterRole을 RoleBinding으로 참조하면 그 binding의 namespace에 권한이 적용된다.

```sh
kubectl auth can-i list pods -n demo
kubectl -n demo get rolebindings
kubectl -n demo get role <role> -o yaml
```

## 최소 권한으로 확인

오류의 verb·API group·resource/subresource·namespace·주체를 기록한다. ServiceAccount는 `system:serviceaccount:<namespace>:<name>` 형태의 주체이며 사용자가 실행한 kubectl 권한과 다를 수 있다. impersonation 조회는 그 자체의 별도 권한이 필요하다.

무조건 cluster-admin을 부여하지 않는다. Secrets 읽기, workload 생성, bind/escalate 권한은 간접적인 권한 확대로 이어질 수 있다. 의도한 허용 작업과 거부 작업을 각각 확인한다.

## 적용 범위와 확인

Kubernetes 공통 진단; 실제 API와 기능은 설치 버전 확인 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [RBAC 장애 진단 공식 참고](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#authorization](../../../tags.md#authorization) · [#containers](../../../tags.md#containers) · [#kubernetes](../../../tags.md#kubernetes) · [#troubleshooting](../../../tags.md#troubleshooting)

[주제 목차](../../index.md) · [위키 홈](../../../index.md)

<!-- END WIKI NAV -->
