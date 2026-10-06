---
title: Linux 블록 계층
category: operating-systems
tags:
- linux
- operating-systems
- storage
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
reviewed_at: '2026-10-06'
applies_to: Linux 블록 I/O의 일반 개념; 성능 수치는 워크로드별 측정
content_origin: original-summary
---

# Linux 블록 장치

블록 장치는 정해진 단위의 데이터를 읽고 쓰는 장치 인터페이스다. 물리 디스크 외에도 loop, LVM, 소프트웨어 RAID, dm-crypt와 네트워크 기반 블록 장치가 있다. 모든 클라우드 볼륨이 iSCSI를 사용하는 것은 아니다.

RAM 디스크는 메모리를 블록 장치로 제공할 수 있다. `tmpfs`는 메모리 기반 파일 시스템이며 블록 장치 자체가 아니다. tmpfs의 내용은 설정에 따라 swap으로 이동할 수 있고 영구 저장을 보장하지 않는다.

## 성능 지표

| 지표 | 의미 | 함께 기록할 조건 |
| --- | --- | --- |
| IOPS | 초당 완료한 I/O 수 | 블록 크기, 읽기·쓰기 비율 |
| 처리량 | 초당 전송한 바이트 | 순차·랜덤 접근, 캐시 여부 |
| 지연 | 요청 완료까지 걸린 시간 | 평균과 tail 지연, 큐 깊이 |

작은 랜덤 I/O와 큰 순차 I/O는 다른 병목을 만든다. 동시 요청 수를 늘리면 처리량이 증가할 수 있지만 대기 시간도 늘 수 있다. 평균 I/O 크기가 같을 때 처리량은 IOPS × I/O 크기로 연결되며, IOPS 하나만으로 애플리케이션 성능을 판단하지 않는다.

I/O 스케줄러는 요청 처리 정책에 관여한다. readahead는 순차 접근 등을 예상해 데이터를 미리 읽는 기능이다. 두 기능을 요청 정렬의 같은 이름으로 취급하지 않는다.

조회 예: `lsblk`, `cat /proc/partitions`. 실험 결과에는 장치 종류와 워크로드 조건을 붙인다.

## 참고 자료

- [Linux 블록 계층](https://docs.kernel.org/block/index.html)
- [tmpfs](https://docs.kernel.org/filesystems/tmpfs.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#linux](../../tags.md#linux) · [#operating-systems](../../tags.md#operating-systems) · [#storage](../../tags.md#storage)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
