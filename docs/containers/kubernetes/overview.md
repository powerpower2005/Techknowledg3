---
title: Kubernetes 아키텍처와 핵심 개념
category: containers
tags:
- containers
- kubernetes
status: note
reviewed_at: '2026-10-06'
applies_to: Kubernetes 일반 구성과 v1.24 이후 CRI; 종료 상세는 사용 버전 확인
content_origin: original-summary
visibility: public
publication_reviewed_at: '2026-10-06'
---

# Kubernetes 아키텍처와 핵심 개념

## 컨트롤 플레인

API server는 Kubernetes API와 인증·인가 등의 경계를 제공한다. etcd는 클러스터 상태를 저장한다. scheduler는 배치되지 않은 Pod에 노드를 할당하고 controller는 관찰한 상태를 원하는 상태에 가깝게 조정한다. 일반적인 컴포넌트는 API server를 통해 상태를 다룬다.

## 노드

kubelet은 노드에서 Pod 명세에 맞게 컨테이너를 관리하고 상태를 보고한다. kubelet은 CRI를 통해 containerd나 CRI-O 등의 런타임과 통신한다. 내장 dockershim은 v1.24에서 제거되었으며 Docker 이미지 사용 가능 여부와 런타임 인터페이스를 구분한다.

Service의 전달 경로는 kube-proxy의 모드 또는 이를 대체하는 네트워크 구현에 따라 달라진다. 모든 클러스터가 동일한 iptables 구성으로 동작하는 것은 아니다. CNI 기반 네트워크 플러그인은 Pod 네트워크 구성을 담당한다.

## Pod 수명과 종료

Pod는 재생성될 수 있으므로 IP나 로컬 쓰기 계층이 영속적이라고 가정하지 않는다. 일반적인 종료에서 `preStop`과 종료 신호 처리는 grace period 안에서 진행된다. preStop 뒤에 전체 grace period가 새로 시작하는 것은 아니다. 제한 시간 이후 강제 종료될 수 있으므로 애플리케이션의 요청 수락 중단과 진행 중 작업 정리를 시험한다.

## 학습 순서

Pod → [Deployment](deployment.md) → [Service와 Ingress](service-ingress.md) → [볼륨](volumes.md) → [운영](application-operations.md) 순서로 읽는다. 같은 Pod의 여러 컨테이너는 sidecar, adapter, proxy 역할을 나눌 수 있다. 네이티브 sidecar의 동작은 해당 Kubernetes 버전 문서로 확인한다.

## 참고 자료

- [클러스터 아키텍처](https://kubernetes.io/docs/concepts/architecture/)
- [Pod 수명과 종료](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)
- [dockershim 제거](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#containers](../../tags.md#containers) · [#kubernetes](../../tags.md#kubernetes)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
