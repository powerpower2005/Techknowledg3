---
title: OpenStack Neutron
category: cloud
tags:
- cloud
- networking
- openstack
status: note
reviewed_at: '2026-10-06'
applies_to: Neutron의 공통 자원 모델; ML2/OVN/OVS 데이터 경로는 구성 의존
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# OpenStack Neutron

Neutron은 네트워크·서브넷·포트·라우터 같은 논리 자원을 API로 관리한다. 실제 패킷 전달은 선택한 ML2 mechanism driver와 OVN/OVS 등의 데이터 경로에 따라 달라진다.

## 자원 관계

네트워크는 연결 영역, 서브넷은 주소 범위와 게이트웨이/DHCP 설정, 포트는 인터페이스의 MAC·IP·바인딩 정보다. 라우터는 서브넷과 외부 네트워크를 연결하며 floating IP는 외부 도달성과 주소 변환에 관여한다. 보안 그룹은 포트에 적용되는 필터 정책이다.

## 연결 장애를 좁히는 방법

포트 상태·바인딩 → VM 주소/경로 → DHCP와 DNS → 보안 그룹 → 라우터/외부 경로 순서로 확인한다. 논리 자원이 생성됐다는 사실만으로 호스트의 실제 인터페이스나 데이터 경로가 정상이라고 단정하지 않는다.

```sh
openstack port show <port-id>
openstack network show <network-id>
openstack subnet show <subnet-id>
openstack router show <router-id>
```

OVN 환경에 OVS agent 전용 진단 절차를 그대로 적용하지 않는다. 소스 코드의 릴리스 태그, mechanism driver, 배포 설정을 기록한 뒤 해당 구현을 추적한다.

## 적용 범위와 확인

Neutron의 공통 자원 모델; ML2/OVN/OVS 데이터 경로는 구성 의존 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [Neutron 개요](https://docs.openstack.org/neutron/latest/admin/intro-os-networking.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#cloud](../../tags.md#cloud) · [#networking](../../tags.md#networking) · [#openstack](../../tags.md#openstack)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
