---
title: Service와 Ingress 네트워킹
category: containers
tags:
- containers
- ingress
- kubernetes
- load-balancing
- networking
status: note
reviewed_at: '2026-10-06'
applies_to: Kubernetes 공통 Pod/Service/Ingress 모델
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# Service와 Ingress 네트워킹

## Pod의 네트워크 경계

같은 Pod의 컨테이너들은 IP와 포트 공간을 공유하여 localhost로 통신한다. 같은 노드의 서로 다른 Pod는 일반적으로 별도 네트워크 공간에 있으며 localhost가 서로를 가리키지 않는다. Pod IP 간 경로는 CNI가 구성하며 항상 bridge를 거친다고 단정할 수 없다.

## Service와 Ingress

Service는 선택된 endpoint에 접근할 안정적인 주소를 제공한다. selector, targetPort, Ready endpoint와 EndpointSlice를 확인한다. ClusterIP, NodePort, LoadBalancer는 접근 방식이며 LoadBalancer의 실제 구현은 환경과 controller에 의존한다.

Ingress는 HTTP(S) host/path 라우팅 규칙이다. Ingress 객체만 만들어서는 트래픽 처리가 생기지 않으며 대응 controller가 필요하다. controller별 TLS·annotation·라우팅 동작을 확인한다. Gateway API는 더 표현력 있는 라우팅 API이지만 설치한 구현의 지원 범위를 확인해야 한다.

```sh
kubectl -n demo get service <service> -o yaml
kubectl -n demo get endpointslices -l kubernetes.io/service-name=<service>
kubectl -n demo get ingress
```

DNS, 외부 load balancer, controller, Service와 앱을 구간별로 진단한다. 앱의 사용자 인증·인가는 네트워크 노출 설정과 별도로 검증한다.

## 적용 범위와 확인

Kubernetes 공통 Pod/Service/Ingress 모델 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [Kubernetes Pods](https://kubernetes.io/docs/concepts/workloads/pods/)
- [Service](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#containers](../../tags.md#containers) · [#ingress](../../tags.md#ingress) · [#kubernetes](../../tags.md#kubernetes) · [#load-balancing](../../tags.md#load-balancing) · [#networking](../../tags.md#networking)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
