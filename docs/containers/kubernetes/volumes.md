---
title: Kubernetes 볼륨
category: containers
tags:
- containers
- kubernetes
- storage
status: note
reviewed_at: '2026-10-06'
applies_to: Kubernetes PV/PVC와 StorageClass 공통 API
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# Kubernetes 볼륨

Pod의 컨테이너 파일 시스템은 컨테이너 교체 시 유지되는 저장소로 간주하지 않는다. emptyDir은 Pod 수명에 연결되고 PV/PVC는 외부 저장소와 요청을 연결한다. ConfigMap·Secret 볼륨은 설정 전달 용도이며 일반 데이터 백업의 대체가 아니다.

## 정적·동적 provisioning

정적 방식에서는 관리자가 준비한 PV에 PVC가 binding된다. 동적 방식에서는 StorageClass의 provisioner가 PVC 요청을 처리하여 PV와 실제 저장소를 만들 수 있으므로 항상 PV를 먼저 수동 생성할 필요는 없다. 용량, access mode, volume mode와 topology를 확인한다.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: demo-data
  namespace: demo
spec:
  accessModes: [ReadWriteOnce]
  resources:
    requests:
      storage: 1Gi
```

이 예시는 default StorageClass와 적절한 provisioner가 있다는 전제다. 없으면 Pending일 수 있다. ReadWriteOnce는 하나의 노드에서 read-write mount를 허용하는 mode이며 반드시 하나의 Pod만 접근한다는 뜻은 아니다.

## 회수와 복구

PV의 필드명은 `spec.persistentVolumeReclaimPolicy`다. PVC가 삭제되어 PV가 해제되면 Retain은 수동 회수를 위해 저장소를 남기고 Delete는 지원하는 plugin에서 PV와 대응 저장소 삭제로 이어진다. Pod 삭제, PVC 삭제, PV 회수는 같은 사건이 아니다.

삭제 전 보관·백업·복구 요구를 확인한다. snapshot 지원과 복구 일관성은 CSI driver와 애플리케이션에 의존한다. 볼륨이 mount됐다는 사실만으로 데이터 복구 성공을 판정하지 않는다.

## 적용 범위와 확인

Kubernetes PV/PVC와 StorageClass 공통 API 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [PV 회수 정책](https://kubernetes.io/docs/tasks/administer-cluster/change-pv-reclaim-policy/)
- [동적 프로비저닝](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/)
- [PV 상세](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#containers](../../tags.md#containers) · [#kubernetes](../../tags.md#kubernetes) · [#storage](../../tags.md#storage)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
