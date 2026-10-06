---
title: 네임스페이스 장애 진단
category: containers
tags:
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

# 네임스페이스 장애 진단

개인 실습 클러스터에서만 아래 조회 예제를 사용한다. 먼저 `kubectl config current-context`로 대상과 namespace를 확인한다. `<이름>` 표시는 실제 리소스 이름으로 바꾼다. 변경·삭제보다 이벤트와 상태에서 실패 원인을 좁히는 것을 우선한다.

Namespace는 이름과 정책의 범위를 나누지만 완전한 보안 경계를 자동으로 만들지는 않는다. cluster 범위 자원인 Node·PV·ClusterRole은 namespace 밖에 존재한다.

```sh
kubectl get namespaces
kubectl -n demo get resourcequota,limitrange
kubectl -n demo get events --sort-by=.metadata.creationTimestamp
```

## 자원이 없거나 생성이 거부될 때

현재 context와 `-n`을 먼저 확인한다. 같은 이름의 Secret이나 Service도 다른 namespace에 있으면 같은 자원이 아니다. quota 초과, LimitRange, admission 정책과 RBAC를 구분한다.

Terminating 상태에서는 남은 자원과 finalizer가 담당하는 외부 정리를 확인한다. finalizer를 강제로 제거하면 외부 자원을 남길 수 있으므로 일반 해결책으로 제시하지 않는다. 처리 후 quota 사용과 예상 자원 정리를 검증한다.

## 적용 범위와 확인

Kubernetes 공통 진단; 실제 API와 기능은 설치 버전 확인 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [네임스페이스 장애 진단 공식 참고](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#containers](../../../tags.md#containers) · [#kubernetes](../../../tags.md#kubernetes) · [#troubleshooting](../../../tags.md#troubleshooting)

[주제 목차](../../index.md) · [위키 홈](../../../index.md)

<!-- END WIKI NAV -->
