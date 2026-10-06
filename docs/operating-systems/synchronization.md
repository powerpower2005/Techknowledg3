---
title: 동기화와 교착 상태
category: operating-systems
tags:
- operating-systems
- concurrency
- thread
status: note
visibility: public
reviewed_at: '2026-10-07'
publication_reviewed_at: '2026-10-07'
applies_to: 일반적인 동기화 개념과 Python 3.12 threading
---

# 동기화와 교착 상태

공유 상태를 여러 실행 흐름이 접근하면 순서에 따라 결과가 달라질 수 있다. 동기화는 함께 지켜야 하는 데이터 규칙과 작업 순서를 보호하는 방법이다.

## 경쟁 상태: 원자적이지 않은 증가

`count += 1`을 읽기 → 계산 → 쓰기로 생각하면 두 작업이 모두 0을 읽고 각각 1을 써서 두 번 증가했는데 결과가 1이 될 수 있다.

| 순서 | 작업 A | 작업 B | 공유 count |
| --- | --- | --- | ---: |
| 1 | 0 읽기 | | 0 |
| 2 | | 0 읽기 | 0 |
| 3 | 1 쓰기 | | 1 |
| 4 | | 1 쓰기 | 1 |

이 표는 가능한 실행 순서를 보여주는 개념 예시다. 특정 Python 버전에서 이 코드가 매번 재현된다는 뜻은 아니다. GIL이 있다는 이유만으로 여러 단계의 애플리케이션 규칙까지 안전하다고 가정하지 않는다.

## mutex, semaphore, condition variable

| 도구 | 목적 | 예시 |
| --- | --- | --- |
| mutex·상호 배제 락 | 임계 구역을 한 실행 흐름만 수행 | 잔액과 거래 기록의 메모리 상태 갱신 |
| semaphore | 허용된 수만큼 진입 | 동시에 사용하는 연결 수 제한 |
| condition variable | 조건 변화까지 락을 놓고 대기 | 큐가 비어 있으면 소비자 대기 |

condition variable에서 깨어났다는 사실은 조건이 충족됐다는 보장이 아니다. 락을 다시 잡고 `while`로 조건을 재검사한다. 알림을 보낸 쪽도 같은 공유 상태의 보호 규칙을 지켜야 한다.

## 락으로 보호하는 예제

```python
from threading import Lock, Thread

count = 0
guard = Lock()

def add_many():
    global count
    for _ in range(1000):
        with guard:
            count += 1

workers = [Thread(target=add_many) for _ in range(4)]
for worker in workers:
    worker.start()
for worker in workers:
    worker.join()
print(count)  # 4000
```

모든 갱신이 같은 guard를 사용해야 한다. 락 안에서 오래 걸리는 I/O를 하면 다른 작업의 대기가 길어질 수 있다. 예제는 공유 카운터의 정확성을 보여주며 스레드 방식의 속도가 빠르다는 증거는 아니다.

## 교착 상태의 네 조건

상호 배제, 자원을 보유한 채 다른 자원 대기, 강제로 회수할 수 없음, 순환 대기가 동시에 성립하면 교착 상태가 발생할 수 있다. A가 락 X를 잡고 Y를 기다리고, B가 Y를 잡고 X를 기다리는 경우가 대표적이다.

예방하려면 모든 코드가 X → Y처럼 동일한 순서로 락을 획득하게 하거나, 필요한 자원을 확보하지 못했을 때 보유 자원을 놓는 설계를 고려한다. timeout은 멈춘 상태에서 빠져나오는 수단이지만 중간 작업의 취소·재시도도 안전해야 한다. DB가 교착을 감지해 트랜잭션 하나를 중단하는 것은 애플리케이션의 재시도 책임을 없애지 않는다.

## 교착, 기아, livelock 구분

교착은 서로 기다려 진행하지 못하고, 기아는 다른 작업이 계속 기회를 가져 특정 작업이 진행하지 못한다. livelock은 서로 양보하거나 재시도하며 상태가 변해도 유용한 작업을 완료하지 못한다. 재시도 backoff와 jitter가 경합을 줄일 수 있지만 정확성 규칙을 대신하지는 않는다.

acquire-release는 락이나 원자 연산의 메모리 순서 계약과 관련된다. 특정 release와 그 결과를 관찰하는 acquire 사이에 앞선 쓰기가 뒤의 읽기에 보이도록 하는 관계를 구성한다. 언어의 메모리 모델과 API를 확인하며 CPU가 모든 명령을 항상 소스 순서로 실행한다고 설명하지 않는다.

[프로세스와 스레드](../computer-science/process-thread.md) · [트랜잭션과 격리 수준](../databases/transactions.md)

## 참고 자료와 확인

2026-10-07에 로컬 Python 3.12에서 락 예제의 최종 카운터 4000을 확인했다. 운영 부하·교착 재현 시험과는 구분한다.

- [Python threading: Lock와 Condition](https://docs.python.org/3.12/library/threading.html)
- [OSTEP: 동시성 오류](https://pages.cs.wisc.edu/~remzi/OSTEP/threads-bugs.pdf)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#operating-systems](../tags.md#operating-systems) · [#concurrency](../tags.md#concurrency) · [#thread](../tags.md#thread)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
