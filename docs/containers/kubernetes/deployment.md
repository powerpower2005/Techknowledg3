---
title: Deployment와 배포 관리
category: containers
tags:
- containers
- deployment
- kubernetes
- workloads
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# 애플리케이션을 쿠버네티스에 배포하기


## 직접 애플리케이션 배포 및 관리
kubectl apply 명령어를 실행하는 것
하지만 app 별로 관리하는 것은 공수가 많이 들기 떄문에 한 종류(네임스페이스) 단위로 관리함


### 오브젝트 명세 파일(yaml) 관리하는 법
대부분 git 으로 관리함



## Kustomize 이용
- 여러 이용방법이 있지만 환경별 오브젝트를 오버라이드 하는 방식으로 관리함



## Helm 이용
패키지 매니저 프로그램
헬름에서는 패키지는 chart라고 함

헬름 차트에는 실행하기 위한 네트워크, 저장소, 설정 등 오브젝트도 포함할 수 있음
차트만 알고 있다면 클러스터에 바로 적용 가능함

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#containers](../../tags.md#containers) · [#deployment](../../tags.md#deployment) · [#kubernetes](../../tags.md#kubernetes) · [#workloads](../../tags.md#workloads)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
