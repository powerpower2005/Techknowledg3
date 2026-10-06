---
title: Linux 커널 네트워크 설정
category: operating-systems
tags:
- kernel
- linux
- networking
- operating-systems
- performance
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# Linux Kernel Parameter

목적
- Network 성능 튜닝
- 파일시스템 성능 튜닝

/proc/sys 디렉터리

/etc/sysctl.conf 파일에는 많이 사용하는 커널 변수가 존재함


# 설정 방법
파라미터는 /proc/sys 디렉터리나 sysctl 명령어를 통해 동적으로 관리하거나 
/etc/sysctl.conf를 통해 영구적으로 설정


## 임시 설정
임시로 적용하며 시스템 재부팅 후에는 초기화

echo <값> > /proc/sys/<경로>/<파라미터>

## sysctl 명령어를 사용한 설정
즉시 적용되며, 재부팅 시 유지X

sysctl -w <파라미터>=<값>

## 영구 설정
/etc/sysctl.conf 파일에 값을 추가하고 sysctl -p 명령으로 로드합니다.

echo "<파라미터>=<값>" >> /etc/sysctl.conf
sysctl -p



-----
리눅스 서버의 TCP 네트워크 성능을 결정짓는 커널 파라미터 이야기
https://meetup.nhncloud.com/posts/53
https://meetup.nhncloud.com/posts/54
https://meetup.nhncloud.com/posts/55

-> 네트워크 성능에 가장 중요한 요소는 결국엔 애플리케이션에 있다는 점을 강조

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#kernel](../../../tags.md#kernel) · [#linux](../../../tags.md#linux) · [#networking](../../../tags.md#networking) · [#operating-systems](../../../tags.md#operating-systems) · [#performance](../../../tags.md#performance)

[주제 목차](../../index.md) · [위키 홈](../../../index.md)

<!-- END WIKI NAV -->
