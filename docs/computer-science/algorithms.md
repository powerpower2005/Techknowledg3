---
title: 탐색과 그래프 알고리즘
category: computer-science
tags:
- algorithms
- computer-science
- data-structures
status: note
visibility: public
reviewed_at: '2026-10-07'
publication_reviewed_at: '2026-10-07'
applies_to: 정렬된 배열의 이진 탐색과 인접 리스트 그래프; Python 3.12
---

# 탐색과 그래프 알고리즘

먼저 입력의 조건을 확인한다. 정렬된 배열인지, 간선에 가중치가 있는지, 중복·순환이 가능한지에 따라 알고리즘이 달라진다. 아래 함수는 외부 패키지 없이 실행할 수 있다.

## 이진 탐색: 경계가 핵심

정렬된 배열에서 탐색 범위를 절반씩 줄이면 O(log n)번 비교한다. 아래는 반열린 구간 `[left, right)`를 사용해 target 이상인 첫 위치를 구하는 lower bound다. 값이 없어도 삽입할 위치를 반환한다.

```python
def lower_bound(values, target):
    left, right = 0, len(values)
    while left < right:
        mid = (left + right) // 2
        if values[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

print(lower_bound([1, 3, 3, 7], 3))  # 1
print(lower_bound([1, 3, 3, 7], 4))  # 3
print(lower_bound([], 3))           # 0
```

범위를 줄이면서 left 왼쪽은 target보다 작고 right부터는 target 이상이라는 조건을 유지한다. 배열 전체를 먼저 정렬해야 한다면 그 비용도 포함한다. 빈 입력, 중복, 첫·마지막 원소와 없는 값을 확인한다.

## BFS: 가중치 없는 최단 거리

너비 우선 탐색은 큐로 거리 0, 1, 2인 정점 순서로 탐색한다. 간선의 비용이 동일한 그래프에서 간선 수 기준 최단 거리를 찾는다. 방문 표시는 큐에 넣을 때 해서 같은 정점을 중복 예약하지 않는다.

```python
from collections import deque

def bfs_distances(graph, start):
    distances = {start: 0}
    pending = deque([start])
    while pending:
        node = pending.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in distances:
                distances[neighbor] = distances[node] + 1
                pending.append(neighbor)
    return distances

graph = {"a": ["b", "c"], "b": ["a", "d"], "c": ["a"], "d": []}
print(bfs_distances(graph, "a"))  # {'a': 0, 'b': 1, 'c': 1, 'd': 2}
```

인접 리스트를 사용하면 방문한 정점·간선에 대해 O(V + E)이며, 전체 그래프를 탐색할 때 공간도 그래프와 방문 정보에 따라 결정된다. 인접 행렬에서는 이웃 확인 비용이 달라진다. 도달할 수 없는 정점은 결과에 들어가지 않는다.

## DFS와 가중치

깊이 우선 탐색은 스택이나 재귀로 한 경로를 먼저 따라간다. 연결 요소 탐색 등에 쓸 수 있지만 최초로 발견한 경로가 최단 경로라는 보장은 없다. 긴 경로는 재귀 깊이 제한에 걸릴 수 있으므로 명시적인 스택을 고려한다. 방향 그래프의 순환 판별에는 단순 방문 여부 외에 현재 탐색 경로의 상태도 필요하다.

가중치가 다르면 BFS를 그대로 쓰지 않는다. 음이 아닌 가중치에는 Dijkstra를, 음수 간선이 있는 문제에는 조건에 맞는 다른 알고리즘을 검토한다. 이진 힙을 쓰는 일반적인 Dijkstra 구현은 O((V + E) log V)로 설명할 수 있다.

## 정렬과 공간

병합 정렬은 일반적인 배열 구현에서 O(n log n) 시간과 O(n) 보조 공간을 사용한다. 퀵 정렬은 보통 평균 O(n log n)이지만 피벗 선택과 입력에 따라 최악 O(n²)이 될 수 있다. 같은 키의 상대 순서를 유지하는 안정 정렬이 필요한지, 입력을 직접 변경해도 되는지도 선택 조건이다.

## 면접 꼬리 질문

- 이진 탐색에서 `right = len(values) - 1`로 바꾸면 무엇도 함께 바꿔야 하는가? 구간 정의와 종료 조건을 설명한다.
- BFS와 DFS가 모두 선형이라면 왜 답이 다른가? 방문 순서와 요구사항을 연결한다.
- 알고리즘이 빠른데 메모리가 부족하면? 보조 공간, 데이터 표현과 입력 크기를 고려한다.

[자료구조와 시간 복잡도](data-structures.md)

## 참고 자료와 확인

2026-10-07에 로컬 Python 3.12에서 예제 출력, 이진 탐색의 빈 배열·중복·범위 밖 입력, BFS의 순환과 도달 불가 정점을 확인했다. 실제 서비스의 성능 비교를 뜻하지 않는다.

- [MIT 6.006 BFS](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/resources/mit6_006f11_lec13/)
- [MIT 6.006 Dijkstra](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/resources/mit6_006f11_lec16/)
- [Python deque](https://docs.python.org/3.12/library/collections.html#collections.deque)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#algorithms](../tags.md#algorithms) · [#computer-science](../tags.md#computer-science) · [#data-structures](../tags.md#data-structures)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
