---
title: Kubernetes 스토리지 장애 진단
category: containers
tags:
- containers
- kubernetes
- storage
- troubleshooting
status: note
reviewed_at: '2026-10-06'
applies_to: Kubernetes 공통 진단; 실제 API와 기능은 설치 버전 확인
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# Kubernetes 스토리지 장애 진단

개인 실습 클러스터에서만 아래 조회 예제를 사용한다. 먼저 `kubectl config current-context`로 대상과 namespace를 확인한다. `<이름>` 표시는 실제 리소스 이름으로 바꾼다. 변경·삭제보다 이벤트와 상태에서 실패 원인을 좁히는 것을 우선한다.

PVC Pending, attach 실패, mount 실패, 앱 쓰기 실패를 서로 다른 단계로 다룬다. StorageClass와 provisioner, 용량·access mode·volume mode, topology와 권한을 함께 확인한다.

```sh
kubectl -n demo describe pvc <pvc>
kubectl get storageclass
kubectl get pv
kubectl -n demo describe pod <pod>
```

## 복구와 데이터 보호

동적 provisioning은 PVC 요청으로 PV를 만들 수 있으므로 항상 관리자가 PV를 먼저 만들어야 하는 것은 아니다. Reclaim 정책은 PV의 `persistentVolumeReclaimPolicy`이며 Delete와 Retain의 실제 저장소 처리 결과를 이해해야 한다.

volume이 붙어도 fs 권한, read-only mount, 파일 시스템이나 디스크 용량 때문에 쓰기가 실패할 수 있다. PVC 삭제를 일반적인 진단 단계로 사용하지 않는다. 복구 후 읽기·쓰기와 앱 일관성을 확인하고 별도 백업의 복구 가능성도 검증한다.

## 적용 범위와 확인

Kubernetes 공통 진단; 실제 API와 기능은 설치 버전 확인 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [Kubernetes 스토리지 장애 진단 공식 참고](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#containers](../../../tags.md#containers) · [#kubernetes](../../../tags.md#kubernetes) · [#storage](../../../tags.md#storage) · [#troubleshooting](../../../tags.md#troubleshooting)

[주제 목차](../../index.md) · [위키 홈](../../../index.md)

<!-- END WIKI NAV -->
