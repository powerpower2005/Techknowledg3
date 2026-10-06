---
title: 가상 메모리와 페이지 폴트
category: operating-systems
tags:
- operating-systems
- memory
status: note
visibility: public
reviewed_at: '2026-10-07'
publication_reviewed_at: '2026-10-07'
applies_to: MMU와 페이징을 사용하는 일반적인 운영체제
---

# 가상 메모리와 페이지 폴트

가상 메모리는 프로세스가 사용하는 주소와 실제 물리 메모리의 위치를 분리한다. 프로세스마다 주소 공간과 접근 권한을 관리하므로 같은 가상 주소가 서로 다른 물리 페이지를 가리킬 수 있다. 메모리 매핑을 통해 같은 물리 페이지를 공유하는 경우도 있다.

## 주소를 변환하는 흐름

가상 주소를 페이지 번호와 페이지 안의 offset으로 나눈다. 페이지 테이블이 페이지 번호를 물리 프레임과 권한에 연결하고 offset은 그대로 사용한다. 아래 수치는 개념 계산이며 실제 시스템의 페이지 크기는 확인해야 한다.

```text
페이지 크기: 4096바이트
가상 주소:   0x1234 → 가상 페이지 1, offset 0x234
페이지 1이 물리 프레임 9에 매핑됨
물리 주소:   9 × 4096 + 0x234 = 0x9234
```

페이지 테이블 자체도 메모리를 사용하므로 다단계 테이블 등으로 공간과 조회 비용을 조절한다. 모든 가상 주소가 물리 RAM에 즉시 할당돼 있다는 뜻은 아니다.

## TLB와 CPU 캐시

TLB는 최근 주소 변환을 저장한다. TLB hit이면 변환 정보를 재사용하고, miss이면 페이지 테이블에서 변환을 구해야 한다. TLB miss가 반드시 페이지 폴트라는 뜻은 아니다. 유효한 매핑을 찾으면 디스크 접근 없이 진행할 수 있다.

CPU 데이터 캐시는 데이터 자체를, TLB는 주소 변환을 저장한다. 파일의 page cache와도 역할이 다르다. 컨텍스트 전환 시 TLB를 어떻게 관리하는지는 주소 공간 식별자와 CPU·OS 구현에 따라 달라진다.

## 페이지 폴트의 여러 이유

필요한 페이지가 준비되지 않았거나 권한 문제가 있으면 예외가 발생하고 OS가 처리한다. 처음 접근한 메모리를 할당하거나 copy-on-write로 사본을 만드는 경우, 파일·swap에서 내용을 가져오는 경우가 있다. 유효하지 않은 주소나 허용되지 않은 쓰기는 정상 실행으로 복구되지 않고 프로세스에 오류가 전달될 수 있다.

Linux의 minor fault는 보통 저장소에서 페이지를 읽어 올 필요 없이 처리하며, major fault는 저장소에서 읽는 작업이 필요한 경우다. 페이지 폴트가 모두 디스크 I/O이거나 버그라는 설명은 부정확하다.

## copy-on-write와 메모리 압박

Linux의 일반적인 `fork`에서는 처음부터 모든 사용자 메모리를 복사하기보다 페이지를 공유하고 쓰기 시 사본을 만드는 copy-on-write를 활용한다. 쓰기량이 늘면 실제 메모리 비용도 늘 수 있다.

물리 메모리가 부족하면 회수 가능한 캐시를 줄이거나 일부 페이지를 내보낸다. 쓰던 페이지를 계속 내보냈다가 다시 읽으면 thrashing으로 지연이 커질 수 있다. 프로세스의 가상 주소 공간 크기, 실제 상주 메모리 RSS와 swap 사용량을 따로 관찰한다.

## 면접 꼬리 질문

- 가상 메모리가 있으면 RAM이 무한한가? 주소 공간과 실제 자원·OS 제한을 구분한다.
- 같은 가상 주소를 쓰는 두 프로세스가 서로 덮어쓰는가? 주소 공간별 매핑을 설명한다.
- TLB miss와 page fault는 무엇이 다른가? 변환 캐시와 페이지 상태를 구분한다.

[Linux 메모리와 캐시](linux/memory.md) · [프로세스와 스레드](../computer-science/process-thread.md)

## 참고 자료와 확인

주소 변환 수치는 설명용 계산이다. 특정 CPU의 성능이나 실제 페이지 폴트 측정을 뜻하지 않는다.

- [OSTEP: TLB](https://pages.cs.wisc.edu/~remzi/OSTEP/vm-tlbs.pdf)
- [OSTEP: 물리 메모리 밖의 페이지](https://pages.cs.wisc.edu/~remzi/OSTEP/vm-beyondphys.pdf)
- [Linux 메모리 개념](https://docs.kernel.org/admin-guide/mm/concepts.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#operating-systems](../tags.md#operating-systems) · [#memory](../tags.md#memory)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
