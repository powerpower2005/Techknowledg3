---
title: 스케줄링 장애 진단
category: containers
tags:
- containers
- kubernetes
- scheduling
- troubleshooting
status: note
reviewed_at: '2026-10-06'
applies_to: Kubernetes 공통 진단; 실제 API와 기능은 설치 버전 확인
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# 스케줄링 장애 진단

개인 실습 클러스터에서만 아래 조회 예제를 사용한다. 먼저 `kubectl config current-context`로 대상과 namespace를 확인한다. `<이름>` 표시는 실제 리소스 이름으로 바꾼다. 변경·삭제보다 이벤트와 상태에서 실패 원인을 좁히는 것을 우선한다.

Pending Pod는 scheduler 이벤트로 실패 조건을 확인한다. CPU/메모리 requests, nodeSelector·affinity, taint/toleration, topology 제약, PVC 바인딩이 흔한 원인이다.

```sh
kubectl -n demo describe pod <pod>
kubectl get nodes
kubectl describe node <node>
kubectl -n demo get pvc
```

## 구분할 점

requests는 스케줄링 판단에 쓰이고 실제 사용량과 같지 않다. toleration은 배치를 허용할 뿐 해당 노드에 반드시 배치하는 조건이 아니다. 노드가 Ready여도 자원·정책 조건 때문에 배치하지 못할 수 있다.

WaitForFirstConsumer 스토리지에서는 Pod 배치와 볼륨 위치가 연결된다. 원인에 맞게 제약이나 용량을 조정한 뒤 Scheduled, Ready와 실제 서비스 동작을 확인한다. 자원 제한을 무조건 제거하거나 모든 taint를 지우지 않는다.

## 적용 범위와 확인

Kubernetes 공통 진단; 실제 API와 기능은 설치 버전 확인 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [스케줄링 장애 진단 공식 참고](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#containers](../../../tags.md#containers) · [#kubernetes](../../../tags.md#kubernetes) · [#scheduling](../../../tags.md#scheduling) · [#troubleshooting](../../../tags.md#troubleshooting)

[주제 목차](../../index.md) · [위키 홈](../../../index.md)

<!-- END WIKI NAV -->
