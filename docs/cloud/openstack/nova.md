---
title: OpenStack Nova
category: cloud
tags:
- cloud
- openstack
- virtualization
status: note
reviewed_at: '2026-10-06'
applies_to: Nova Cells v2의 공통 아키텍처; 배포 릴리스별 설정은 별도 확인
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# OpenStack Nova

Nova는 가상 머신의 생성·배치·수명 주기를 관리한다. 이미지 저장은 Glance, 네트워크는 Neutron, 블록 스토리지는 Cinder와 연계하며 Nova가 이 기능을 모두 직접 구현하는 것은 아니다.

## 주요 구성 요소

API는 요청을 받으며 Scheduler는 자원과 배치 조건을 고려해 Compute 호스트를 선택한다. Placement는 자원 공급자·사용량·할당 정보를 다룬다. Conductor는 데이터베이스 접근을 중개하는 등 Compute를 지원한다. Cells v2는 API 계층과 셀별 실행·DB·메시징을 나누는 구조다.

## 진단 순서

API 요청 ID를 기준으로 인스턴스 상태, 스케줄링 이벤트, Placement 자원, Compute 서비스, Neutron 포트와 볼륨 연결을 차례로 확인한다. `NoValidHost`는 단순히 서버 부족만 의미하지 않는다. flavor, 자원 예약, trait, affinity, 가용 영역 조건도 함께 본다.

조회 예시는 다음과 같다. 인증 환경 변수는 자신이 권한을 가진 학습 환경에서 별도로 설정한다.

```sh
openstack server show <server-id>
openstack compute service list
openstack hypervisor list
```

Nova 구성은 릴리스와 virt driver에 따라 다르므로 설치 릴리스의 문서를 함께 확인한다. 서비스 재시작이나 DB 직접 수정은 이 조회 절차에 포함하지 않는다.

## 적용 범위와 확인

Nova Cells v2의 공통 아키텍처; 배포 릴리스별 설정은 별도 확인 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [Nova 아키텍처](https://docs.openstack.org/nova/latest/admin/architecture.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#cloud](../../tags.md#cloud) · [#openstack](../../tags.md#openstack) · [#virtualization](../../tags.md#virtualization)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
