---
title: Linux 부팅
category: operating-systems
tags:
- boot
- linux
- operating-systems
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
reviewed_at: '2026-10-06'
applies_to: 일반 Linux 부팅 개념; 배포판별 설정 경로는 별도 확인
content_origin: original-summary
---

# Linux 부팅

일반적인 흐름은 펌웨어 → 부트로더 또는 EFI 커널 → 커널·초기 사용자 공간 → 실제 루트 파일 시스템 → init과 서비스다. 배포판, 펌웨어 모드와 부팅 구성에 따라 단계가 달라진다.

## 펌웨어와 로더

전통적인 BIOS 부팅과 UEFI 부팅은 같은 방식이 아니다. UEFI는 설정된 부팅 항목 등을 이용해 EFI 실행 파일을 실행할 수 있다. 모든 UEFI 부팅이 MBR의 첫 섹터를 읽고 2단계 로더를 거친다고 설명하면 안 된다. GRUB이나 systemd-boot가 커널과 초기 이미지 선택을 담당할 수 있다.

## initramfs와 initrd

initramfs는 커널이 rootfs에 풀어 사용하는 cpio 아카이브다. 필요한 드라이버를 준비하고 실제 루트 파일 시스템으로 전환하는 초기 사용자 공간을 제공할 수 있다. initrd는 초기 RAM 디스크 이미지 방식이며 두 이름을 같은 구현으로 취급하지 않는다. 커널과 부팅 구성에 따라 별도 초기 이미지 없이 부팅하는 경우도 있다.

실제 루트로 전환한 뒤 init 프로그램이 사용자 공간 서비스를 시작한다. systemd를 사용하는 시스템에서는 서비스 의존성과 target에 따라 시작 순서를 관리한다.

## 확인 순서

펌웨어의 디스크 인식, 선택된 부팅 항목, 커널 인수, 루트 장치 발견, 초기 이미지, init 로그 순서로 실패 구간을 좁힌다. 로더 설정 파일 위치는 배포판마다 확인한다.

## 참고 자료

- [커널 initramfs 설명](https://docs.kernel.org/filesystems/ramfs-rootfs-initramfs.html)
- [systemd-boot](https://www.freedesktop.org/software/systemd/man/latest/systemd-boot.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#boot](../../tags.md#boot) · [#linux](../../tags.md#linux) · [#operating-systems](../../tags.md#operating-systems)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
