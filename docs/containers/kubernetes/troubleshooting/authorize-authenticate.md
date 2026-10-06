---
title: 인증과 인가 장애 진단
category: containers
tags:
- authentication
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

# 인증과 인가 장애 진단

개인 실습 클러스터에서만 아래 조회 예제를 사용한다. 먼저 `kubectl config current-context`로 대상과 namespace를 확인한다. `<이름>` 표시는 실제 리소스 이름으로 바꾼다. 변경·삭제보다 이벤트와 상태에서 실패 원인을 좁히는 것을 우선한다.

인증은 요청 주체 확인, 인가는 그 주체가 어떤 작업을 할 수 있는지의 판단이다. 401은 인증 실패, 403은 인가 거부를 우선 의심하되 인증 proxy가 있는 경우 해당 계층도 확인한다.

```sh
kubectl config current-context
kubectl auth can-i get pods -n demo
kubectl -n demo get serviceaccount
```

## 확인할 정보

kubeconfig의 context·user·cluster, 인증서 유효 기간, OIDC issuer/audience, ServiceAccount token의 용도·만료를 확인한다. 토큰 원문이나 전체 kubeconfig를 티켓·로그에 붙이지 않는다. TLS 서버 검증 실패는 RBAC 권한 추가로 해결되지 않는다.

인증이 통과했으면 [RBAC 진단](rbac.md)으로 resource·verb·namespace와 binding을 확인한다. 해결 후 필요한 조회만 가능하고 불필요한 쓰기는 거부되는지 검증한다.

## 적용 범위와 확인

Kubernetes 공통 진단; 실제 API와 기능은 설치 버전 확인 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [인증과 인가 장애 진단 공식 참고](https://kubernetes.io/docs/reference/access-authn-authz/authentication/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#authentication](../../../tags.md#authentication) · [#containers](../../../tags.md#containers) · [#kubernetes](../../../tags.md#kubernetes) · [#troubleshooting](../../../tags.md#troubleshooting)

[주제 목차](../../index.md) · [위키 홈](../../../index.md)

<!-- END WIKI NAV -->
