---
title: Linux 프로세스
category: operating-systems
tags:
- linux
- operating-systems
- process
- thread
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
reviewed_at: '2026-10-06'
applies_to: Linux 시스템 호출 및 일반 터미널 시그널 동작
content_origin: original-summary
---

# Linux 프로세스와 시그널

`fork()`는 호출한 프로세스에서 자식 프로세스를 만든다. Linux에서는 일반적으로 copy-on-write를 활용해 메모리 페이지의 즉시 전체 복사를 피한다. 부모는 자식 PID를, 자식은 0을 반환받아 실행을 나눈다.

`execve()`는 새 프로세스를 만드는 함수가 아니라 현재 프로세스의 프로그램 이미지를 교체하는 함수다. 성공하면 기존 호출 지점으로 돌아오지 않으며 실패하면 오류를 반환한다. 프로세스 생성과 프로그램 교체를 구분한다.

## 시그널

| 시그널 | 기본 용도와 주의점 |
| --- | --- |
| `SIGCHLD` | 자식의 상태 변화 알림 |
| `SIGTERM` | 종료 요청; 프로그램이 처리할 수 있음 |
| `SIGKILL` | 처리하거나 무시할 수 없는 강제 종료 |
| `SIGSTOP` | 처리하거나 무시할 수 없는 정지 |
| `SIGCONT` | 정지한 프로세스 재개 |
| `SIGINT` | 터미널에서 보통 Ctrl+C로 전달 |
| `SIGTSTP` | 터미널에서 보통 Ctrl+Z로 전달 |
| `SIGHUP` | 연결 종료 등의 알림; 재설정 용도로 처리하는 데몬도 있음 |

시그널 이름 자체가 설정 재로드 성공을 보장하지 않는다. 수신 프로그램의 동작을 확인한다. 셸의 `trap`은 처리 가능한 시그널에 대한 동작을 지정할 수 있다.

프로세스 간 통신에는 pipe, socket, 공유 메모리 등도 사용한다. 데이터 공유 방식과 동기화, 프로세스 종료 시 정리 절차를 함께 설계한다.

## 참고 자료

- [fork(2)](https://man7.org/linux/man-pages/man2/fork.2.html)
- [execve(2)](https://man7.org/linux/man-pages/man2/execve.2.html)
- [signal(7)](https://man7.org/linux/man-pages/man7/signal.7.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#linux](../../tags.md#linux) · [#operating-systems](../../tags.md#operating-systems) · [#process](../../tags.md#process) · [#thread](../../tags.md#thread)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
