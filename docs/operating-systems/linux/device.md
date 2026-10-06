---
title: Linux 장치
category: operating-systems
tags:
- kernel
- linux
- operating-systems
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# 프로세스에서의 장치 접근

프로세스는 장치에 직접 접근하지 못함

하나의 인터페이스를 갖고 있음

프로세스 대신 커널이 장치에 접근함


/dev/sda
/dev/sdb
위와 같은 파일이 디바이스 파일


리눅스는 프로세스가 디바이스 파일을 조작하면
커널 내부의 *디바이스 드라이버*라고 부르는 소프트웨어가 사용자 대신에 장치에 접근함

프로세스는 디바이스 파일을 조작함
디바이스 파일 변경에 따른 커널이 디바이스 드라이버를 사용함
드라이버가 장치에 접근에 사용함


# 디바이스 파일
- 파일 종류 : 캐릭터 장치(c) 또는 블록 장치(b)
- 디바이스 메이저 번호, 마이너 번호


디바이스 파일은 보통 /dev/ 에 있음


## 캐릭터 장치
- 단말
- 키보드
- 마우스


## 블록 장치

- HDD
- SSD

블록 장치에 데이터를 읽고 쓰면 일반 파일처럼 저장 장치 특정 위치에 있는 데이터에 접근 할 수 있음



# 디바이스 드라이버

프로세스가 디바이스 파일에 접근할 때 동작하는 디바이스 드라이버 커널 기능



# 디바이스 파일명 유의
같은 종류의 장치를 여러 개 연결한 경우라면 디바이스 파일명을 조심해서 다뤄야함
재시작 시, 저장장치 인식 순서가 바뀌게 되면, 서로 장치명이 바뀔 수 있음

-> systemd의 udev 프로그램으로 영구 장치명을 이용해서 해결할 수 있음

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#kernel](../../tags.md#kernel) · [#linux](../../tags.md#linux) · [#operating-systems](../../tags.md#operating-systems)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
