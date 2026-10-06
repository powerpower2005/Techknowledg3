---
title: Linux 메모리와 캐시
category: operating-systems
tags:
- caching
- linux
- memory
- operating-systems
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
reviewed_at: '2026-10-06'
applies_to: MMU가 있는 일반적인 Linux 시스템
content_origin: original-summary
---

# Linux 메모리와 캐시

가상 메모리는 프로세스가 사용하는 주소 공간을 물리 메모리와 분리한다. MMU가 있는 일반적인 환경에서는 페이지 테이블을 통해 주소를 변환한다.

CPU 캐시는 메모리 접근의 시간·공간 지역성을 활용한다. CPU 캐시의 L1/L2/L3와 파일 데이터를 저장하는 커널의 page cache는 서로 다른 계층이다. 캐시 구성과 SMT의 효과는 CPU와 워크로드에 따라 달라진다.

## Page cache와 쓰기

파일을 읽으면 내용을 page cache에 저장해 후속 읽기에 활용할 수 있다. 쓰기로 변경된 페이지는 dirty 상태가 되고 이후 backing storage에 반영된다. writeback 완료 전의 장애에서는 데이터가 손실될 수 있으므로 메모리에 썼다는 사실과 내구성을 구분한다.

메모리 압박 시 커널은 회수 가능한 캐시를 버리거나 일부 익명 메모리를 swap으로 내보낼 수 있다. swap이 있어도 OOM을 무조건 방지하는 것은 아니다.

## 관찰

`free`, `vmstat`, `sar -r`로 메모리 사용과 추세를 확인한다. cache가 많다는 이유만으로 메모리 부족이라고 판단하지 말고 회수 가능성, swap I/O와 애플리케이션 지연을 함께 본다.

## 참고 자료

[주소 변환·TLB·페이지 폴트 자세히 보기](../virtual-memory.md)

- [커널 메모리 개념](https://docs.kernel.org/admin-guide/mm/concepts.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#caching](../../tags.md#caching) · [#linux](../../tags.md#linux) · [#memory](../../tags.md#memory) · [#operating-systems](../../tags.md#operating-systems)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
