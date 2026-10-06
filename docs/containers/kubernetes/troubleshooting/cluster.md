---
title: 클러스터 장애 진단
category: containers
tags:
- containers
- kubernetes
- troubleshooting
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# P1. Node - NotReady 상태

- Situation
클러스터의 한 노드가 NotReady 상태로 표시되고, 해당 노드에 스케줄링된 파드들이 Pending 상태로 남아 있음.

- 상황 인식
kubectl get nodes를 실행했을 때 NotReady 상태의 노드 확인.
kubectl describe node <노드 이름> 명령어로 노드 이벤트를 조사
```
Warning  NodeNotReady  Kubelet stopped posting node status.

```

journalctl -u kubelet
```
Unable to register node with API server: timed out waiting for the condition

```

- 문제해결
1. 네트워크 연결 확인
2. Kubelet 상태 점검
3. 인증서 만료 확인
4. 리소스 확인


- 해결 확인
1. 노드 상태가 정상으로 복구됐는지 확인:
kubectl get nodes

2. 해당 노드의 파드들이 Running 상태로 복구됐는지 확인:
kubectl get pods -o wide

3. 추가적으로 Kubelet 로그에서 오류 메시지가 더 이상 발생하지 않는지 확인:
journalctl -u kubelet

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#containers](../../../tags.md#containers) · [#kubernetes](../../../tags.md#kubernetes) · [#troubleshooting](../../../tags.md#troubleshooting)

[주제 목차](../../index.md) · [위키 홈](../../../index.md)

<!-- END WIKI NAV -->
