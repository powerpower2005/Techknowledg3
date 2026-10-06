---
title: 서비스 메시와 Canary 배포
category: containers
tags:
- containers
- kubernetes
- service-mesh
- troubleshooting
status: note
reviewed_at: '2026-10-06'
applies_to: Kubernetes 공통 진단; 실제 API와 기능은 설치 버전 확인
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# 서비스 메시와 Canary 배포

개인 실습 클러스터에서만 아래 조회 예제를 사용한다. 먼저 `kubectl config current-context`로 대상과 namespace를 확인한다. `<이름>` 표시는 실제 리소스 이름으로 바꾼다. 변경·삭제보다 이벤트와 상태에서 실패 원인을 좁히는 것을 우선한다.

## 기능과 비용

Service mesh는 서비스 간 트래픽 정책, 인증과 관찰을 제공할 수 있다. sidecar·ambient 등 구현에 따라 자원 비용과 장애 경로가 달라진다. 작은 서비스에서 무조건 도입할 필요는 없으며 인증·관찰 요구와 운영 역량으로 판단한다.

Canary는 새 버전에 일부 트래픽을 보내며 결과를 관찰하는 배포 방식이다. Kubernetes Deployment의 replica 비율만으로 정밀한 사용자 트래픽 비율을 보장하지 않는다. ingress·gateway·mesh·배포 controller가 제공하는 라우팅 방식과 sticky session을 확인한다.

## 안전한 실습

구버전·신버전의 Service selector, Ready endpoint, 실제 응답 버전, 오류율과 지연을 비교한다. DB 스키마와 메시지 형식이 두 버전에서 호환되어야 한다. rollback 기준과 중단 담당자를 배포 전에 정한다.

```sh
kubectl -n demo get deployment,service
kubectl -n demo get endpointslices
```

mesh의 mTLS 실패를 앱의 500 오류와 구분하고 proxy와 앱의 timeout·retry가 증폭되지 않는지 본다.

## 적용 범위와 확인

Kubernetes 공통 진단; 실제 API와 기능은 설치 버전 확인 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [서비스 메시와 Canary 배포 공식 참고](https://kubernetes.io/docs/concepts/services-networking/ingress/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#containers](../../../tags.md#containers) · [#kubernetes](../../../tags.md#kubernetes) · [#service-mesh](../../../tags.md#service-mesh) · [#troubleshooting](../../../tags.md#troubleshooting)

[주제 목차](../../index.md) · [위키 홈](../../../index.md)

<!-- END WIKI NAV -->
