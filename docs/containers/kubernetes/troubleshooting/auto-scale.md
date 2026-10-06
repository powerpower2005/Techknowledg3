---
title: 자동 확장 장애 진단
category: containers
tags:
- containers
- kubernetes
- scaling
- troubleshooting
status: note
reviewed_at: '2026-10-06'
applies_to: Kubernetes 공통 진단; 실제 API와 기능은 설치 버전 확인
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# 자동 확장 장애 진단

개인 실습 클러스터에서만 아래 조회 예제를 사용한다. 먼저 `kubectl config current-context`로 대상과 namespace를 확인한다. `<이름>` 표시는 실제 리소스 이름으로 바꾼다. 변경·삭제보다 이벤트와 상태에서 실패 원인을 좁히는 것을 우선한다.

HPA는 workload의 replica 수를 조정하고 노드 autoscaler는 Pod를 수용할 노드 용량을 다룬다. VPA는 자원 requests 등의 크기를 다룬다. Pod가 늘었어도 노드 부족으로 Pending이면 두 계층을 나누어 확인한다.

```sh
kubectl -n demo get hpa
kubectl -n demo describe hpa <hpa>
kubectl -n demo top pods
kubectl -n demo get deployment <deployment>
```

## 판단 기준

metric 수집 API, CPU requests, min/max replicas, 현재와 목표 값, stabilization과 scale 정책을 본다. `top`과 metrics API는 해당 수집기가 있어야 한다. CPU utilization 기준은 requests에 대한 비율이므로 requests가 없으면 지표 계산에 문제가 생길 수 있다.

부하 감소 후 과도한 축소·진동, cold start와 readiness, DB 연결 수 증가까지 확인한다. replica 수만 늘리고 병목이 사라졌다고 결론 내리지 않는다.

## 적용 범위와 확인

Kubernetes 공통 진단; 실제 API와 기능은 설치 버전 확인 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [자동 확장 장애 진단 공식 참고](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#containers](../../../tags.md#containers) · [#kubernetes](../../../tags.md#kubernetes) · [#scaling](../../../tags.md#scaling) · [#troubleshooting](../../../tags.md#troubleshooting)

[주제 목차](../../index.md) · [위키 홈](../../../index.md)

<!-- END WIKI NAV -->
