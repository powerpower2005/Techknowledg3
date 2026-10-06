---
title: 가상화
category: computer-science
tags:
- computer-science
- virtualization
status: note
visibility: public
reviewed_at: '2026-10-07'
publication_reviewed_at: '2026-10-07'
applies_to: Linux KVM·QEMU와 일반적인 VM·컨테이너 비교
---

# 가상화

가상화는 물리 자원을 추상화해 여러 실행 환경에 나누어 제공하는 방법이다. VM은 가상 CPU·메모리·장치 위에서 게스트 운영체제를 실행한다. 하이퍼바이저와 호스트는 VM의 실행과 자원 사용을 관리한다.

## VM과 컨테이너

| 관점 | 가상머신 | 일반적인 Linux 컨테이너 |
| --- | --- | --- |
| OS 커널 | 게스트 커널 별도 실행 | 호스트 커널 공유 |
| 격리 방식 | 가상 하드웨어·하이퍼바이저 경계 | namespace·cgroup 등의 OS 기능 |
| 실행 환경 | 호스트가 지원하는 게스트 OS 실행 | 공유 커널과 호환되는 사용자 공간 |
| 시작·자원 비용 | 게스트 부팅과 OS 자원 비용 | 보통 작지만 이미지·앱·설정에 의존 |
| 고려할 장애·보안 | 하이퍼바이저와 가상 장치도 공격 표면 | 커널 공유, 권한·mount·capability 관리 |

VM도 호스트 자원을 공유하므로 다른 VM의 I/O 과부하 영향을 받을 수 있다. 격리가 있다고 모든 장애와 자원 경합이 사라지지는 않는다. 컨테이너가 항상 같은 보안 경계를 제공하는 것도 아니다.

Docker Desktop처럼 VM 안에서 Linux 컨테이너를 실행하는 구조도 있다. 따라서 VM과 컨테이너는 함께 사용할 수 있는 계층이다.

## KVM, QEMU와 virt-manager

- KVM은 Linux의 가상화 기능과 사용자 공간이 VM을 관리할 수 있는 API를 제공한다. 지원 환경에서 하드웨어 가상화 기능을 활용한다.
- QEMU는 머신·장치를 모델링하고 게스트를 실행한다. KVM 같은 accelerator와 함께 동작할 수 있고 TCG로 CPU를 에뮬레이션할 수도 있다.
- virt-manager는 libvirt 등을 통해 VM을 만들고 관리하는 GUI다. 게스트의 CPU 명령을 직접 실행하는 역할과 구분한다.

같은 아키텍처의 하드웨어 가상화와 다른 아키텍처를 소프트웨어로 에뮬레이션하는 것은 성능과 호환성 조건이 다르다. QEMU를 사용한다는 사실만으로 KVM 가속이 켜졌다고 단정하지 않는다.

## 선택하는 예시

서로 다른 OS 커널과 강한 격리 요구가 있으면 VM을 검토한다. 같은 커널에서 앱을 재현 가능한 사용자 공간으로 배포하려면 컨테이너가 적합할 수 있다. 호환성·보안·관찰·업데이트·백업 책임도 함께 정한다.

면접에서는 “가볍다”로 끝내지 않고 무엇을 공유해서 비용이 달라지는지 설명한다. VM snapshot이나 컨테이너 이미지가 모든 애플리케이션 데이터의 일관된 백업을 대신하는지도 별도로 판단한다.

[Docker 개요](../containers/docker/docker.md) · [가상 메모리](../operating-systems/virtual-memory.md)

## 참고 자료와 확인

공식 구조 설명을 검토했다. 이번 작성에서는 VM 생성·부팅이나 성능 비교를 실행하지 않았다.

- [QEMU system emulation과 accelerator](https://www.qemu.org/docs/master/system/introduction.html)
- [KVM API](https://docs.kernel.org/virt/kvm/api.html)
- [virt-manager](https://virt-manager.org/)
- [Docker 컨테이너](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#computer-science](../tags.md#computer-science) · [#virtualization](../tags.md#virtualization)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
