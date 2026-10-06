---
title: 운영·개발 도구
category: devops
tags:
- devops
- tooling
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
---

Rest Api Test
https://www.getpostman.com/ 

cross platform 지원
컬렉션 공유


Http Archive Viewer
https://toolbox.googleapps.com/apps/har_analyzer/



------------------------------



Windows에서 리소스 성능 테스트할 때 사용할 수 있는 도구에 대해서 작성합니다.

VMMap
https://learn.microsoft.com/ko-kr/sysinternals/downloads/vmmap

실행 후 프로세스 선택 (F5로 새로고침 해주어야 현재 사용량 반영됨)

각 메모리의 타입 (Heap, Image, Private Data 등) 을 구분해서 확인할 수 있음

*수집하는 메모리 종류 설명 (KB 단위로 수집)

Size : 해당 프로세스가 할당한 전체 가상 메모리 크기

Committed : 커밋된 가상 메모리. 현재 물리 메모리에 상주하는 양인 working set과 구분한다.

Private : 다른 프로세스와 공유하지 않는 커밋된 가상 메모리. 현재 RAM에 상주하는 private working set과 구분한다.

Total WS (Total Working Set) : 현재 시스템 RAM에 로드되어 있는 프로세스의 실제 메모리 양

Private WS (Private Working Set) : 현재 시스템 RAM에 로드된 메모리 중 해당 프로세스만 사용하는 메모리



Perfmon
https://en.wikipedia.org/wiki/Performance_Monitor

windows 기본 프로그램 성능 모니터

각 프로세스별 리소스 모니터링 등 카운터를 선택하고 특정 주기를 설정하여 수집할 수 있음

PID별로도 가능하고 같은 종류 프로그램의 모든 프로세스에 대해 한번에 수집도 가능

카운터 설명
주로 수집하는 리소스 카운터에 대해 설명합니다.



Process (pid 혹은 프로세스 이름으로 인스턴스 생성)

% processor time : cpu 사용률 (최대 퍼센티지 = 100%*코어 수)

working set : 프로세스에 대한 작업 집합의 현재 크기 (bytes) - VMMap의 Total WS과 같음

working set - private : 공유 작업 집합을 제외한 현재 프로세서만 사용하고 있는 작업 집합의 크기 (bytes) - 작업관리자의 프로세스별 메모리 / VMMap의 Private WS과 같음

private bytes : 현재 프로세스가 할당하여 다른 프로세스와 공유할 수 없는 메모리의 현재 크기 (bytes) - VMMap의 Private와 같음

virtual bytes : 프로세스가 사용하고 있는 가상 주소 공간의 바이트 수 (bytes) - VMmap의 Size와 같음



 GPU Process Memory (pid-gpu luid로 인스턴스 생성)

dedicated usage : 해당 프로세스가 독점적으로 사용하는 메모리 (bytes)

total committed : 해당 프로세스가 GPU에서 예약한 총 메모리 양 (bytes)




-------

메모리 지표 참고: [Microsoft VMMap](https://learn.microsoft.com/en-us/sysinternals/downloads/vmmap). 커밋과 working set은 같은 수치가 아니다.

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#devops](../tags.md#devops) · [#tooling](../tags.md#tooling)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
