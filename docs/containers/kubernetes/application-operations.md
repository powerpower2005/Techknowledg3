---
title: Kubernetes 애플리케이션 운영
category: containers
tags:
- containers
- kubernetes
- logging
- storage
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
reviewed_at: '2026-10-06'
applies_to: 일반 Kubernetes 운영 설계; DB별 복구 보장은 제품 구성에 따라 확인
content_origin: original-summary
---

# Kubernetes 애플리케이션 운영

## 로그

일반적인 애플리케이션 로그는 stdout·stderr로 내보내고 노드별 수집기 등을 통해 별도 저장소로 보낸다. 컨테이너나 노드의 로컬 로그는 수명과 로테이션의 영향을 받으므로 장기 보존을 따로 설계한다. PV나 NFS만이 로그 보존의 유일한 방법은 아니다.

## 상태 있는 워크로드

데이터베이스 운영에는 저장소 수명, 재스케줄링·재연결, 복제, 백업·복구와 업데이트가 필요하다. StatefulSet과 PVC는 안정적인 식별자와 저장소 연결을 지원하지만 DB 복제나 백업을 자동으로 해결하지 않는다. 복구 목표와 실제 restore 절차를 시험한다. Redis도 persistence와 데이터 중요도에 따라 저장소 요건이 달라진다.

## 세션

Pod 메모리에만 있는 세션은 종료나 다른 Pod로의 요청에서 사용할 수 없을 수 있다. 외부 세션 저장소를 사용할 때 만료·무효화·장애 정책을 정한다. sticky routing은 도움이 될 수 있지만 Pod 종료 시의 상태 보존을 대신하지 않는다.

## 리소스와 배치

namespace와 ResourceQuota로 관리 범위를 나누되 RBAC와 네트워크 정책도 별도로 정한다. Job은 완료되는 작업, CronJob은 일정에 따른 Job 생성에 사용한다. 재시도와 중복 실행을 고려해 작업을 설계한다.

## 참고 자료

- [Kubernetes 로그 아키텍처](https://kubernetes.io/docs/concepts/cluster-administration/logging/)
- [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
- [CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#containers](../../tags.md#containers) · [#kubernetes](../../tags.md#kubernetes) · [#logging](../../tags.md#logging) · [#storage](../../tags.md#storage)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
