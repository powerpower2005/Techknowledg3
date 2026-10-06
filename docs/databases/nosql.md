---
title: NoSQL
category: databases
tags:
- databases
- nosql
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
reviewed_at: '2026-10-06'
applies_to: 여러 NoSQL 제품의 비교 기준; 개별 보장은 제품·버전별 확인
content_origin: original-summary
---

# NoSQL 데이터베이스

NoSQL은 문서, key-value, wide-column, graph 등 여러 데이터 모델을 묶어 부르는 용어다. 모든 제품이 같은 스키마·트랜잭션·복제 특성을 가지는 것은 아니다.

## 비교할 기준

- 읽기·쓰기 패턴과 필요한 쿼리 기능
- 한 레코드와 여러 레코드의 원자성, 격리와 일관성 범위
- 인덱스, 스키마 검증과 데이터 변경 절차
- 샤딩·복제·failover·백업 및 운영 비용

유연한 문서 모델에도 데이터 규칙과 스키마 검증이 필요할 수 있다. 수평 확장이나 빠른 처리는 데이터 분배와 워크로드에 따라 달라지며 NoSQL이라는 이름만으로 보장되지 않는다. MongoDB처럼 다중 문서 트랜잭션을 지원하는 제품도 있으므로 “NoSQL은 ACID가 없다”는 이분법을 피한다.

[MongoDB](mongodb.md) · [Redis](redis/redis.md) · [SQL과 NoSQL 비교](sql.md)

## 참고 자료

- [MongoDB 트랜잭션](https://www.mongodb.com/docs/manual/core/transactions/)
- [MongoDB 스키마 검증](https://www.mongodb.com/docs/manual/core/schema-validation/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#databases](../tags.md#databases) · [#nosql](../tags.md#nosql)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
