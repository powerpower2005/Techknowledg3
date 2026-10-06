---
title: 로그인, 게시판과 주문 서비스 설계
category: architecture
tags:
- architecture
- reliability
- transactions
- caching
status: note
visibility: public
reviewed_at: '2026-10-07'
publication_reviewed_at: '2026-10-07'
applies_to: 공개 학습용 웹 서비스 설계 사례
---

# 로그인, 게시판과 주문 서비스 설계

시스템 설계는 구성 요소를 많이 나열하는 것보다 요구사항, 데이터 규칙과 실패 조건을 연결하는 작업이다. 아래 사례는 특정 기업의 운영 구조가 아닌 학습 예시다.

## 먼저 정할 것

기능, 사용자 수, 요청 패턴, 데이터 보존, 허용 지연과 장애 시 동작을 적는다. 읽기가 대부분인지, 한 상품에 쓰기가 몰리는지에 따라 병목이 달라진다. 초당 100요청에 평균 2KiB 응답이라는 가정이면 본문 전송량은 약 200KiB/s다. 헤더·TLS·재전송과 peak 여유는 별도로 계산한다.

```text
브라우저 → HTTPS 진입점 → 애플리케이션 → 관계형 DB
                                  ├→ 캐시 (필요한 조회에 도입)
                                  └→ worker → 외부 서비스
```

처음에는 기능과 데이터 규칙을 명확히 구현한다. 캐시, 큐, 복제는 관찰한 병목·가용성 요구에 맞춰 추가하며 각 구성의 장애도 설계한다.

## 로그인: 인증과 인가

인증은 누가 요청했는지, 인가는 그 사용자가 해당 작업을 할 수 있는지 확인한다. 로그인 세션 ID를 얻었어도 다른 사용자의 게시글 수정이 허용되는 것은 아니다.

서버 세션은 불투명한 ID로 서버 상태를 찾고, 서명된 토큰은 서명과 발급자·대상·만료 등을 검증한다. 즉시 로그아웃·권한 철회 요구가 있으면 상태 조회나 철회 정책을 포함한다. 비밀번호 저장, 로그인 시도 제한과 쿠키 정책도 함께 정한다.

학습 질문: “토큰이 유효한데 계정이 정지되면 어떻게 할 것인가?” 짧은 만료, 서버 측 계정 상태 확인과 철회 목록의 비용을 비교한다.

## 게시판: 페이지 조회와 캐시

글 목록을 `created_at DESC, id DESC`로 정렬하면 같은 시각의 글도 안정적으로 순서를 정할 수 있다. 큰 OFFSET은 앞 행을 건너뛰는 비용이 커질 수 있다. 마지막 글의 `(created_at, id)`를 커서로 사용하면 그 뒤 범위를 조회할 수 있지만 임의 페이지 번호 접근과 정렬 키 변경의 처리도 고려한다.

캐시에는 공개 글과 개인화된 응답을 구분하고 키·TTL·무효화를 정한다. 글을 수정한 뒤 DB commit 전에 캐시를 갱신하면 rollback된 내용이 보일 수 있다. commit 후 무효화도 동시 읽기와 경합할 수 있으므로 오래된 값의 허용 시간, 버전과 갱신 순서를 정의한다.

DB 복제본에서 읽으면 복제 지연으로 방금 쓴 글이 안 보일 수 있다. 작성 직후 일정 시간 primary에서 읽는 정책 등으로 사용자 요구를 맞춘다. 복제본을 추가해도 모든 조회가 즉시 최신이 되는 것은 아니다.

## 주문: 재고와 중복 처리

1. 사용자와 상품을 검증하고 같은 논리적 요청의 idempotency key와 요청 내용 hash를 확인한다.
2. 사용자·키의 유일성, 재고 조건부 차감, pending 주문과 전송할 이벤트를 같은 DB 트랜잭션으로 기록한다.
3. 재고가 없거나 요청 내용이 충돌하면 실패 규칙대로 종료한다. 성공 시 commit하고 주문 식별자를 반환한다.
4. worker가 저장된 이벤트를 읽어 결제를 요청한다. 공급자의 계약에 맞는 안정적인 키로 중복 결제를 제어한다.
5. 결제 결과를 상태 전이 조건으로 반영한다. timeout으로 결과를 모르면 확인·조정 후 성공 또는 실패로 확정한다.

2번의 이벤트 저장은 transactional outbox 방식의 예다. DB 기록과 외부 전송의 사이에서 프로세스가 죽어도 다시 전송할 근거가 남는다. 전송과 완료 표시 사이에 죽으면 같은 이벤트가 다시 갈 수 있으므로 소비자도 중복을 처리해야 한다. outbox만으로 모든 시스템에서 exactly-once가 보장되지는 않는다.

예를 들어 결제는 성공했는데 응답만 사라진 경우 주문을 곧바로 취소하고 재고를 돌리면 결제된 주문의 재고가 다시 팔릴 수 있다. `pending → paid`, `pending → failed`와 취소·환불 상태를 명시하고 결과 미확정 상태의 조사·만료·보상 정책을 둔다. 결제 공급자의 실제 멱등·조회·환불 기능은 별도로 확인한다.

## 장애와 검증 질문

| 실패 상황 | 확인할 설계 |
| --- | --- |
| 클라이언트가 같은 주문을 동시에 보냄 | 유일 제약, 같은 키의 요청 내용 검사, 처리 중 결과 |
| 재고가 1개인데 두 주문이 도착 | 조건부 갱신 또는 적절한 락과 격리 수준 |
| DB commit 뒤 worker가 정지 | 이벤트 재전송, backlog 감시와 복구 |
| 결제 응답을 못 받음 | 공급자 결과 확인, 중복 요청 계약, 미확정 상태 |
| 캐시가 모두 만료 | 동시 재생성 제한, DB 과부하와 fallback |
| 재시도가 몰림 | 제한된 횟수, deadline, backoff·jitter와 과부하 제어 |

처리량뿐 아니라 p95·p99 지연, 오류율, DB 대기와 queue backlog를 관찰한다. 중복 요청, 프로세스 중단과 외부 timeout을 넣었을 때도 재고·주문·결제 규칙이 유지되는지 시험해야 한다.

[세션과 토큰](../security/session-token/session-token.md) · [인덱스](../databases/index-tuning.md) · [트랜잭션](../databases/transactions.md) · [HTTP 재시도](../networking/http-semantics.md) · [SRE](../devops/sre/sre.md)

## 참고 자료와 확인

위 흐름은 설계 연습이다. 결제 서비스나 실제 사용자 데이터에 요청하지 않았으며 부하·장애 실험 결과를 제시하지 않는다.

- [AWS Builders Library: 멱등 API와 재시도](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)
- [PostgreSQL 제약](https://www.postgresql.org/docs/18/ddl-constraints.html)
- [AWS transactional outbox](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#architecture](../tags.md#architecture) · [#reliability](../tags.md#reliability) · [#transactions](../tags.md#transactions) · [#caching](../tags.md#caching)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
