---
title: 애플리케이션 장애 진단
category: containers
tags:
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

# 애플리케이션 장애 진단

개인 실습 클러스터에서만 아래 조회 예제를 사용한다. 먼저 `kubectl config current-context`로 대상과 namespace를 확인한다. `<이름>` 표시는 실제 리소스 이름으로 바꾼다. 변경·삭제보다 이벤트와 상태에서 실패 원인을 좁히는 것을 우선한다.

## 상태별 분기

Pending은 스케줄링과 볼륨, ImagePullBackOff는 이미지 이름·인증·레지스트리 연결, CrashLoopBackOff는 이전 종료와 설정을 확인한다. Running만으로 readiness나 실제 사용자 요청 성공을 보장하지 않는다.

```sh
kubectl -n demo get pod <pod> -o wide
kubectl -n demo describe pod <pod>
kubectl -n demo logs <pod> -c <container> --previous --tail=100
kubectl -n demo get endpointslices
```

## 다음 확인

OOMKilled는 메모리 제한과 사용 추세, probe 실패는 경로·포트·초기화 시간을 확인한다. Pod 직접 연결과 Service 경유 연결을 비교하여 앱과 네트워크를 구분한다. 완화 후 새 Pod의 Ready, 오류율과 의존 서비스 연결까지 검증한다.

## 적용 범위와 확인

Kubernetes 공통 진단; 실제 API와 기능은 설치 버전 확인 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [애플리케이션 장애 진단 공식 참고](https://kubernetes.io/docs/tasks/debug/debug-application/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#containers](../../../tags.md#containers) · [#kubernetes](../../../tags.md#kubernetes) · [#troubleshooting](../../../tags.md#troubleshooting)

[주제 목차](../../index.md) · [위키 홈](../../../index.md)

<!-- END WIKI NAV -->
