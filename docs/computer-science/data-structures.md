---
title: 자료구조와 시간 복잡도
category: computer-science
tags:
- computer-science
- data-structures
- algorithms
status: note
visibility: public
reviewed_at: '2026-10-07'
publication_reviewed_at: '2026-10-07'
applies_to: 기본 자료구조의 계산 모델과 Python 3.12 예제
---

# 자료구조와 시간 복잡도

자료구조는 데이터를 저장하고 접근하는 규칙이다. 같은 데이터라도 자주 하는 연산이 다르면 적합한 구조가 달라진다. 사용자 ID 조회에는 해시 테이블, 우선순위 작업에는 힙, 순서대로 처리하는 대기열에는 큐를 생각할 수 있다.

## Big O를 읽는 법

입력 크기 n이 커질 때 연산량이 어떻게 증가하는지 표현한다. O(1), O(log n), O(n), O(n log n), O(n²)는 상수·로그·선형·선형 로그·이차 증가의 예다. Big O는 상한을 나타내며 정의 자체가 최악의 경우를 뜻하지는 않는다. 평균, 최악, 분할 상환 중 무엇을 분석했는지 함께 말한다.

동적 배열 끝에 원소를 넣으면 보통 여유 공간을 사용하지만 확장 시 기존 원소를 복사한다. 개별 삽입은 O(n)이 될 수 있어도 일련의 삽입 비용을 나누면 분할 상환 O(1)이다. 복잡도가 같아도 캐시 지역성, 할당과 상수 비용에 따라 실제 시간이 달라진다.

## 구조별 비교

| 자료구조 | 대표 연산과 비용 | 선택 조건과 한계 |
| --- | --- | --- |
| 배열·동적 배열 | 인덱스 접근 O(1), 중간 삽입·삭제 O(n) | 연속 원소 순회에 유리, 크기 증가나 이동 비용 고려 |
| 연결 리스트 | 위치 탐색 O(n), 위치를 알고 필요한 링크가 있으면 삽입·삭제 O(1) | 노드·링크 메모리와 지역성 비용 발생 |
| 스택 | 끝에서 push/pop O(1), 동적 배열은 push 분할 상환 | 마지막 작업부터 되돌리기, DFS |
| 큐·deque | 적절한 구현에서 양 끝 삽입·삭제 O(1) | 도착 순서 처리, BFS |
| 해시 테이블 | 좋은 해시·적절한 부하율에서 조회 평균 O(1), 단순 충돌 모델의 최악 O(n) | 정확한 키 조회에 적합, 정렬·범위 조회에는 별도 구조 필요 |
| 균형 이진 탐색 트리 | 탐색·삽입·삭제 O(log n) | 순서와 범위 유지, 일반적인 불균형 BST는 최악 O(n) |
| 이진 힙 | 최솟값 조회 O(1), 삽입·최솟값 제거 O(log n) | 우선순위 처리, 임의 원소 검색은 보통 O(n) |

위 표는 표준적인 구현 가정이다. 언어별 컨테이너의 보장은 구현 문서를 확인한다. Python `list`는 연결 리스트가 아니라 동적 배열이며 `pop(0)`은 뒤 원소를 이동시킨다.

## 해시 충돌과 부하율

서로 다른 키가 같은 버킷으로 가는 것이 충돌이다. 체이닝은 버킷에 여러 항목을 연결하고, 오픈 어드레싱은 다른 슬롯을 탐색한다. 부하율은 원소 수와 저장 공간의 비율이다. 공간이 너무 차면 충돌 탐색이 늘어나므로 확장과 재해싱 비용을 고려한다. 같은 해시값을 가진 키도 키 비교로 구분해야 한다.

## 큐의 작은 예제

```python
from collections import deque

waiting = deque(["job-a", "job-b"])
waiting.append("job-c")
print(waiting.popleft())  # job-a
print(list(waiting))     # ['job-b', 'job-c']
```

업무 처리 큐에서 앞 원소를 반복 제거한다면 `list.pop(0)`보다 deque가 적합하다. 여러 소비자의 작업 분배·동기화·재시도는 이 컨테이너 예제와 별도의 문제다.

## 면접 꼬리 질문

- 연결 리스트의 삽입이 O(1)이라면 배열보다 항상 빠른가? 위치 탐색, 메모리 할당과 캐시 비용을 함께 설명한다.
- 해시 테이블의 조회는 언제 느려지는가? 충돌, 부하율과 재해싱을 구분한다.
- 정렬된 키의 범위를 자주 조회한다면 무엇을 고르는가? 트리와 해시의 지원 연산을 비교한다.

[탐색과 그래프 알고리즘](algorithms.md) · [메모리와 포인터](memory-and-pointers.md) · [인덱스](../databases/index-tuning.md)

## 참고 자료와 확인

Python 큐 예제는 2026-10-07에 로컬 Python 3.12에서 표시된 출력을 확인했다. 자료구조의 복잡도와 프로그램의 실제 처리량은 구분한다.

- [Python 자료구조](https://docs.python.org/3.12/tutorial/datastructures.html)
- [Python deque](https://docs.python.org/3.12/library/collections.html#collections.deque)
- [MIT 6.006 자료구조·알고리즘 강의](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/pages/lecture-notes/)
- [Python heapq](https://docs.python.org/3.12/library/heapq.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#computer-science](../tags.md#computer-science) · [#data-structures](../tags.md#data-structures) · [#algorithms](../tags.md#algorithms)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
