---
title: Kubernetes 네트워크 장애 진단
category: containers
tags:
- containers
- kubernetes
- networking
- troubleshooting
status: note
reviewed_at: '2026-10-06'
applies_to: Kubernetes 공통 진단; 실제 API와 기능은 설치 버전 확인
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# Kubernetes 네트워크 장애 진단

개인 실습 클러스터에서만 아래 조회 예제를 사용한다. 먼저 `kubectl config current-context`로 대상과 namespace를 확인한다. `<이름>` 표시는 실제 리소스 이름으로 바꾼다. 변경·삭제보다 이벤트와 상태에서 실패 원인을 좁히는 것을 우선한다.

## 경로를 나누기

DNS → Service/EndpointSlice → Pod IP/port → 앱 응답 순서로 비교한다. 같은 Pod의 컨테이너는 localhost를 공유하지만 같은 노드의 서로 다른 Pod는 일반적으로 localhost를 공유하지 않는다.

```sh
kubectl -n demo get svc <service> -o yaml
kubectl -n demo get endpointslices -l kubernetes.io/service-name=<service>
kubectl -n demo get pods -o wide
kubectl -n demo get networkpolicy
```

## 대표 원인

Service selector와 Pod label 불일치, 잘못된 targetPort, Ready endpoint 부재, NetworkPolicy, DNS 설정과 CNI 문제를 확인한다. endpoint가 있어도 앱이 해당 주소에 listen하지 않으면 실패한다.

Pod 간 경로가 bridge·overlay·routing·eBPF 중 무엇인지는 CNI와 dataplane에 따라 다르다. node 간 MTU와 방화벽도 확인한다. 정책 변경 후 허용 경로와 의도한 차단 경로를 각각 검증한다.

## 적용 범위와 확인

Kubernetes 공통 진단; 실제 API와 기능은 설치 버전 확인 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [Kubernetes 네트워크 장애 진단 공식 참고](https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#containers](../../../tags.md#containers) · [#kubernetes](../../../tags.md#kubernetes) · [#networking](../../../tags.md#networking) · [#troubleshooting](../../../tags.md#troubleshooting)

[주제 목차](../../index.md) · [위키 홈](../../../index.md)

<!-- END WIKI NAV -->
