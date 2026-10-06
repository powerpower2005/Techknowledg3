---
title: 인덱스와 실행 계획
category: databases
tags:
- databases
- performance
- sql
status: note
reviewed_at: '2026-10-06'
applies_to: PostgreSQL 18 학습 예시; 다른 DB의 planner는 별도 확인
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# 인덱스와 실행 계획

인덱스는 조건·정렬·join을 지원할 수 있지만 갱신 비용과 저장 공간을 늘린다. 인덱스가 있다는 이유만으로 모든 쿼리가 빨라지거나 planner가 반드시 사용하지는 않는다.

## 작은 예제로 확인하기

```sql
EXPLAIN SELECT id, created_at
FROM orders
WHERE customer_id = 42
ORDER BY created_at DESC
LIMIT 20;
```

이 패턴에는 `(customer_id, created_at)` 복합 인덱스를 후보로 생각할 수 있다. 실제 효용은 행 수, 선택도, 통계, 필요한 컬럼과 읽기/쓰기 비율로 확인한다. 작은 테이블이나 많은 행을 읽는 쿼리에서는 sequential scan이 합리적일 수 있다.

`EXPLAIN ANALYZE`는 쿼리를 실제로 실행한다. 쓰기 쿼리나 비용이 큰 쿼리에 읽기 전용 진단처럼 사용하지 않는다. 추정 행 수와 실제 행 수의 차이, scan 방식, sort, buffer 접근과 실행 시간을 함께 본다.

## 흔한 오해

OR 조건이나 IS NULL이 항상 인덱스를 못 쓰는 것은 아니다. DB 제품·연산자·인덱스 방식·통계에 따라 계획이 달라진다. 함수 적용과 타입 변환도 인덱스 조건이 되지 못하는 원인이 될 수 있다. SQL 모양만으로 결과를 단정하지 않고 대표 데이터와 계획으로 확인한다.

## 적용 범위와 확인

PostgreSQL 18 학습 예시; 다른 DB의 planner는 별도 확인 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#databases](../tags.md#databases) · [#performance](../tags.md#performance) · [#sql](../tags.md#sql)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
