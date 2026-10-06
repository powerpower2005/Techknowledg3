---
title: SQL과 NoSQL 비교
category: databases
tags:
- databases
- sql
status: note
reviewed_at: '2026-10-06'
applies_to: 일반 관계형 DB 비교; 복제 예는 MySQL 공식 문서 기준
content_origin: original-summary
visibility: public
publication_reviewed_at: '2026-10-06'
---

# SQL과 NoSQL 비교

SQL은 데이터 질의 언어이며 관계형 DB는 테이블과 관계를 중심으로 데이터를 다룬다. 제품은 트랜잭션, 인덱스, 복제와 분산 처리 기능을 각각 제공한다. SQL 사용 여부만으로 수평 확장 가능성이나 모든 저장 엔진의 ACID 보장을 결정하지 않는다.

## 질의와 모델링

INNER JOIN은 조인 조건에 맞는 행을 결합한다. OUTER JOIN은 선택한 쪽의 일치하지 않는 행도 남긴다. 지원하는 종류는 제품별로 확인한다. 인덱스는 읽기 접근을 개선할 수 있지만 쓰기·공간 비용을 더한다. 실제 실행 계획과 워크로드로 선택한다.

정규화는 중복과 변경 이상을 줄이는 데 쓰인다. 비정규화는 특정 읽기를 단순화할 수 있지만 중복 데이터를 갱신하는 책임을 더한다. 어느 쪽이 언제나 빠른지는 실제 질의로 확인한다.

## 샤딩과 복제

샤딩은 데이터를 나눠 분배하고 복제는 같은 데이터의 사본을 유지한다. 한 샤드가 다시 여러 복제본을 가질 수 있다. 복제 지연과 failover 정책에 따라 읽기가 오래된 결과를 보이거나 장애 때 손실이 생길 수 있다. 복제는 잘못된 삭제도 전파할 수 있으므로 독립적인 백업과 복구가 필요하다.

## MySQL 복제 로그

statement, row, mixed 방식은 기록하는 내용과 unsafe 문장 처리 방식이 다르다. row image에 포함되는 열도 설정에 따라 달라진다. MySQL은 `NOW()`를 statement 복제에 안전한 함수로 취급한다. `SYSDATE()`와 `UUID()` 같은 예는 버전·설정과 공식 safe/unsafe 목록을 확인한다. 복제 지연이 항상 100ms 이내라는 일반 보장은 없다.

[NoSQL](nosql.md) · [인덱스 튜닝](index-tuning.md) · [CAP](cap-theorem.md)

## 참고 자료

- [PostgreSQL 조인](https://www.postgresql.org/docs/current/queries-table-expressions.html)
- [MySQL safe/unsafe 문장](https://dev.mysql.com/doc/en/replication-rbr-safe-unsafe.html)
- [MySQL row image](https://dev.mysql.com/doc/refman/8.4/en/replication-options-binary-log.html#sysvar_binlog_row_image)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#databases](../tags.md#databases) · [#sql](../tags.md#sql)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
