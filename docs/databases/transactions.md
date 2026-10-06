---
title: 트랜잭션과 격리 수준
category: databases
tags:
- databases
- sql
- transactions
- concurrency
status: note
visibility: public
reviewed_at: '2026-10-07'
publication_reviewed_at: '2026-10-07'
applies_to: PostgreSQL 18의 MVCC, 격리 수준과 행 잠금
---

# 트랜잭션과 격리 수준

트랜잭션은 여러 DB 작업을 하나의 성공·실패 단위로 묶는다. 재고만 차감되고 주문은 저장되지 않는 상황을 막으려면 두 변경을 같은 트랜잭션에 넣어야 한다. DB 밖의 결제 호출까지 자동으로 롤백되는 것은 아니다.

## ACID와 MVCC

| 성질 | 의미 | 주문 예시 |
| --- | --- | --- |
| Atomicity | 묶인 변경을 모두 반영하거나 취소 | 재고 차감과 주문 생성 함께 성공 |
| Consistency | 트랜잭션이 정해진 제약과 규칙을 유지 | 재고 음수 금지, 유효한 상품 참조 |
| Isolation | 동시 작업 사이의 관찰·간섭을 제어 | 같은 재고를 두 주문이 다룰 때 허용할 결과 정의 |
| Durability | 성공한 commit의 변경을 지속 | 장애 후에도 완료된 주문 복구 |

Consistency는 업무 규칙을 DB가 자동으로 알아낸다는 뜻이 아니다. 제약과 애플리케이션 로직을 직접 정의한다. 내구성은 로그·동기화 설정과 장애 모델을 함께 확인하며 백업도 별도로 필요하다.

MVCC는 데이터의 여러 버전과 스냅샷으로 읽을 수 있는 값을 정한다. 일반 조회가 쓰기와의 경합을 줄일 수 있지만 쓰기 충돌이나 명시적인 락까지 사라지는 것은 아니다.

## PostgreSQL의 격리 수준

dirty read는 미확정 변경을 읽는 것, nonrepeatable read는 같은 행을 다시 읽었을 때 값이 달라지는 것, phantom read는 같은 조건의 조회에 포함되는 행 집합이 달라지는 것이다. serialization anomaly는 동시 실행 결과를 어떤 순차 실행 순서로도 설명할 수 없는 경우다.

| 수준 | 조회 기준과 주의점 |
| --- | --- |
| Read Committed | 기본값. 각 일반 SELECT 시작 시점의 스냅샷이므로 같은 트랜잭션의 다음 조회에 다른 commit이 보일 수 있음 |
| Repeatable Read | 첫 일반 조회·변경 명령이 정한 스냅샷을 유지. PostgreSQL에서는 phantom read도 방지하지만 serialization anomaly 가능 |
| Serializable | 성공한 트랜잭션의 효과를 순차 실행으로 설명 가능하도록 보장. 충돌 시 전체 트랜잭션을 재시도해야 할 수 있음 |

PostgreSQL의 Read Uncommitted는 Read Committed처럼 동작한다. SQL 표준의 최소 보장과 다른 DB의 구현을 이 표로 일반화하지 않는다. sequence의 값 증가처럼 rollback되지 않는 동작도 있다.

## 두 세션으로 스냅샷 관찰하기

별도의 로컬 학습 DB에서 한 번 준비한다. 아래 이름의 테이블이 이미 있으면 기존 데이터를 덮어쓰지 말고 별도 DB나 이름을 사용한다.

```sql
CREATE TABLE wiki_stock (
    product_id integer PRIMARY KEY,
    quantity integer NOT NULL CHECK (quantity >= 0),
    version integer NOT NULL DEFAULT 0
);
INSERT INTO wiki_stock (product_id, quantity) VALUES (1, 5);
```

1. 세션 A: `BEGIN ISOLATION LEVEL READ COMMITTED;` 다음 `SELECT quantity FROM wiki_stock WHERE product_id = 1;` 실행. 초기 값은 5다.
2. 세션 B: `BEGIN; UPDATE wiki_stock SET quantity = 4 WHERE product_id = 1; COMMIT;` 실행.
3. 세션 A: 같은 SELECT를 다시 실행하면 4를 볼 수 있다. `ROLLBACK;`으로 종료한다.
4. 두 세션의 트랜잭션을 끝낸 뒤 재고를 5로 초기화하고 A를 Repeatable Read로 시작해 비교한다. 첫 SELECT 뒤 B가 4로 commit해도 A의 두 번째 일반 SELECT는 5를 본다.

## 초과 판매를 막는 조건부 갱신

조회 결과를 애플리케이션에서 계산해 `SET quantity = 4`처럼 덮어쓰면 동시 주문의 갱신을 잃을 수 있다. 고정 상품의 수량 차감은 DB에서 조건을 함께 검사한다.

```sql
BEGIN;
UPDATE wiki_stock
SET quantity = quantity - 1, version = version + 1
WHERE product_id = 1 AND quantity >= 1
RETURNING quantity;
-- 반환 행이 1개이면 같은 트랜잭션에서 주문을 기록한 뒤 COMMIT.
-- 반환 행이 없으면 품절로 처리하고 ROLLBACK.
ROLLBACK;  -- 이 학습 예제는 실제 재고 변경을 남기지 않는다.
```

PostgreSQL Read Committed에서 같은 행을 먼저 바꾼 트랜잭션이 있으면 기다린 뒤 갱신된 행의 조건을 다시 검사한다. 여러 상품의 합계 같은 복잡한 규칙은 이 한 행 예제로 해결되지 않는다.

## 낙관적·비관적 제어

낙관적 제어는 읽은 version이 아직 같은지 갱신 조건에 넣어 충돌을 발견한다. `WHERE product_id = 1 AND version = :expected_version`은 개념 표기이며 사용 라이브러리의 parameter 문법으로 바꾼다. 영향받은 행이 0개이면 최신 상태를 다시 읽고 정책에 따라 재시도한다.

비관적 제어는 `SELECT ... FOR UPDATE` 등으로 필요한 행을 잠근 뒤 읽기·변경을 한다. 단일 조건부 UPDATE도 DB 내부에서는 락을 사용하므로 낙관적 제어가 락을 전혀 쓰지 않는다는 뜻은 아니다. 여러 행을 잠글 때는 일관된 순서와 짧은 트랜잭션을 유지한다.

교착이나 serialization failure에 대한 재시도는 전체 트랜잭션을 대상으로 제한된 횟수로 수행한다. 이미 수행한 외부 결제까지 무조건 다시 호출하지 않는다.

[인덱스](index-tuning.md) · [동기화](../operating-systems/synchronization.md) · [주문 서비스 설계](../architecture/web-service-design.md)

## 참고 자료와 확인

SQL은 PostgreSQL 18 공식 동작과 함께 검토한 학습 절차다. 이번 작성 환경에서는 DB 서버를 실행하지 않았으므로 실제 결과·시간 측정은 아직 수행하지 않았다.

- [PostgreSQL 트랜잭션](https://www.postgresql.org/docs/18/tutorial-transactions.html)
- [PostgreSQL 격리 수준](https://www.postgresql.org/docs/18/transaction-iso.html)
- [PostgreSQL 명시적 잠금과 교착](https://www.postgresql.org/docs/18/explicit-locking.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#databases](../tags.md#databases) · [#sql](../tags.md#sql) · [#transactions](../tags.md#transactions) · [#concurrency](../tags.md#concurrency)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
