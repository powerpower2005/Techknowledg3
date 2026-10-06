---
title: DaemonSet
category: containers
tags:
- containers
- kubernetes
- workloads
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
---

## What is DaemonSet? and Why do we need it?
- 데몬셋은 쿠버네티스의 오브젝트 중 하나
클러스터의 노드에서 특정 파드가 실행되도록 보장하는데 사용됨(즉, 스케쥴링 될 때, 빈틈 없이 노드에 띄워지는 파드생성)
예를 들면 로그를 위해 특정 노드의 볼륨을 사용하여 전송하는 역할을 하는 파드가 있다면
노드당 최소한 1개는 무조건 필요
필요 시에는 필요 시 스케줄링되는 노드를 제한할 수 있음(노드 셀렉터나 taint/toleration 사용)


- DeamonSet is one of object in kubernetes
It is used to assure speicific pod is operating on node.
For example, log collector have to be operated on each node. So We can deploy log collector pod with DaemonSet
if you need, Node selector or toleration can control access node of DaemonSet

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#containers](../../tags.md#containers) · [#kubernetes](../../tags.md#kubernetes) · [#workloads](../../tags.md#workloads)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
