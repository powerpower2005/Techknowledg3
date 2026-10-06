---
title: 인덱스와 실행 계획
category: databases
tags:
- databases
- performance
- sql
status: note
reviewed_at: '2026-10-07'
applies_to: PostgreSQL 18 학습 예시
visibility: public
publication_reviewed_at: '2026-10-07'
---

# 인덱스와 실행 계획

인덱스는 조건·정렬·join을 지원하는 접근 경로지만 쓰기와 저장 비용을 더한다. 인덱스가 있다는 이유만으로 planner가 반드시 사용하거나 모든 질의가 빨라지는 것은 아니다.

## B-tree와 복합 인덱스

B-tree 계열은 많은 키를 노드에 저장하고 트리 높이를 줄이는 방식으로 정렬·범위 접근을 지원한다. PostgreSQL의 B-tree 인덱스는 동등·범위 비교와 적합한 정렬에 사용할 수 있다. 디스크 페이지와 여러 행의 접근 비용까지 고려해야 하므로 메모리 자료구조의 O(log n)만으로 DB 응답 시간을 설명하지 않는다.

`(customer_id, created_at)`은 고객별 시간 순서로 정렬한 접근 경로다. customer_id를 고정하고 created_at으로 정렬하는 질의에 후보가 된다. 선두 열 조건이 없으면 효용이 달라지지만 이후 열만으로 인덱스를 절대 사용할 수 없다고 단정하지 않는다. 제품의 planner와 실제 계획을 확인한다.

## 준비: 재현 가능한 데이터

아래 전체 실습은 별도의 로컬 학습 DB 한 세션에서 수행한다. 임시 테이블을 사용하므로 기존 orders 테이블을 변경하지 않는다. 세션이 끝나면 임시 테이블도 사라진다.

```sql
CREATE TEMP TABLE wiki_orders (
    id bigint PRIMARY KEY,
    customer_id integer NOT NULL,
    created_at timestamp NOT NULL
);

INSERT INTO wiki_orders
SELECT n, (n % 1000)::integer,
       TIMESTAMP '2026-01-01 00:00:00' + n * INTERVAL '1 second'
FROM generate_series(1, 100000) AS series(n);

ANALYZE wiki_orders;
```

## 인덱스 전후 비교

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT id, created_at
FROM wiki_orders
WHERE customer_id = 42
ORDER BY created_at DESC
LIMIT 20;

CREATE INDEX wiki_orders_customer_created_idx
ON wiki_orders (customer_id, created_at);

ANALYZE wiki_orders;

EXPLAIN (ANALYZE, BUFFERS)
SELECT id, created_at
FROM wiki_orders
WHERE customer_id = 42
ORDER BY created_at DESC
LIMIT 20;
```

처음에는 많은 행을 읽고 조건으로 거른 뒤 정렬하는 계획을, 이후에는 고객 범위의 인덱스를 역방향으로 읽어 정렬 비용을 줄이는 계획을 기대할 수 있다. 이는 고정된 실행 결과가 아니며 서버 통계·설정에 따라 달라진다. 실제 plan과 시간이 없으면 성능 개선 배수를 적지 않는다.

| 확인 항목 | 질문 |
| --- | --- |
| estimated rows와 actual rows | 추정이 실제 분포와 크게 다른가? |
| scan 종류 | seq scan, index scan, bitmap scan 중 무엇을 선택했는가? |
| sort | 별도 정렬이 필요한가, 메모리·디스크 비용은? |
| buffers | 읽거나 hit한 페이지는 얼마나 되는가? |
| loops | 내부 작업이 몇 번 반복됐는가? |
| execution time | 캐시와 동시 부하 조건을 맞춰 비교했는가? |

임시 테이블은 local buffer 통계가 나타날 수 있으므로 모든 buffer를 shared로 가정하지 않는다. 같은 고객의 created_at은 예제에서 서로 다르지만 실제 서비스에서는 id 같은 tie-breaker가 필요할 수 있다.

## 비용과 흔한 오해

작은 테이블이나 대부분의 행을 반환하는 질의에서는 sequential scan이 합리적일 수 있다. 인덱스가 늘면 INSERT·UPDATE·DELETE의 유지 비용과 공간도 늘어난다. 실제 읽기·쓰기 비율과 대표 데이터를 사용한다.

OR 조건이나 IS NULL이 항상 인덱스를 못 쓰는 것은 아니다. 함수·타입 변환, 연산자, 인덱스 방식과 통계에 따라 계획이 달라진다. covering index를 만들었다고 무조건 heap 접근 없는 index-only scan이 발생하는 것도 아니다.

`EXPLAIN`은 계획을 보여주고 `EXPLAIN ANALYZE`는 질의를 실제 실행한다. 읽기 쿼리도 큰 비용이 들 수 있으며 쓰기 쿼리는 실제 변경을 일으킨다.

[자료구조](../computer-science/data-structures.md) · [트랜잭션](transactions.md) · [게시판 설계](../architecture/web-service-design.md)

## 참고 자료와 확인

SQL과 기대되는 접근 경로를 공식 문서와 대조했다. 이번 작성 환경에서는 PostgreSQL 서버가 실행되지 않아 실제 실행 계획·시간을 측정하지 않았다.

- [PostgreSQL 18 인덱스 종류](https://www.postgresql.org/docs/18/indexes-types.html)
- [PostgreSQL 18 EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#databases](../tags.md#databases) · [#performance](../tags.md#performance) · [#sql](../tags.md#sql)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
