---
title: 애드온과 사이드카 장애 진단
category: containers
tags:
- containers
- kubernetes
- sidecar
- troubleshooting
status: note
reviewed_at: '2026-10-06'
applies_to: Kubernetes 공통 진단; 실제 API와 기능은 설치 버전 확인
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# 애드온과 사이드카 장애 진단

개인 실습 클러스터에서만 아래 조회 예제를 사용한다. 먼저 `kubectl config current-context`로 대상과 namespace를 확인한다. `<이름>` 표시는 실제 리소스 이름으로 바꾼다. 변경·삭제보다 이벤트와 상태에서 실패 원인을 좁히는 것을 우선한다.

## 본체와 보조 컨테이너 분리

로그 수집기·프록시·보안 agent가 실패했는지 앱 본체가 실패했는지 container별 상태를 본다. Pod의 공유 네트워크에서 포트 충돌, 공유 볼륨의 권한·경로, CPU/메모리 경쟁을 확인한다.

```sh
kubectl -n demo describe pod <pod>
kubectl -n demo logs <pod> -c <sidecar> --tail=100
kubectl -n demo get pod <pod> -o yaml
```

## 수명 주기와 복구

native sidecar는 `initContainers`의 `restartPolicy: Always`를 사용하며 일반 init container와 종료·재시작 방식이 다르다. 이 기능은 Kubernetes 1.33에서 stable이므로 오래된 클러스터에는 같은 설정이 적용되지 않을 수 있다. Job 종료가 보조 컨테이너 때문에 지연되는지도 확인한다.

공통 애드온 장애는 여러 namespace의 동시 영향을 본다. 설정 변경 후 로그 전달, 앱 readiness, 종료 시 버퍼 유실을 함께 검증한다.

## 적용 범위와 확인

Kubernetes 공통 진단; 실제 API와 기능은 설치 버전 확인 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [애드온과 사이드카 장애 진단 공식 참고](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#containers](../../../tags.md#containers) · [#kubernetes](../../../tags.md#kubernetes) · [#sidecar](../../../tags.md#sidecar) · [#troubleshooting](../../../tags.md#troubleshooting)

[주제 목차](../../index.md) · [위키 홈](../../../index.md)

<!-- END WIKI NAV -->
