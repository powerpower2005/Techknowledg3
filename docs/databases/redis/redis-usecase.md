---
title: Redis 활용 패턴
category: databases
tags:
- caching
- databases
- redis
status: note
reviewed_at: '2026-10-06'
applies_to: Redis Sorted Set 점수·rank와 일반적인 캐시 패턴
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# Redis 활용 패턴

## 최근 항목 다섯 개 유지

Sorted Set에 시간 점수와 유일한 item ID를 저장할 수 있다. 최신 다섯 개를 유지하려면 추가 뒤 `ZREMRANGEBYRANK key 0 -6`으로 오래된 범위를 삭제한다. `-6 -6`은 한 항목만 삭제하므로 기존 다섯 개 이하에서 한 건씩 추가한다는 제한적인 전제가 필요하다.

```text
ZADD recent:user:demo 1700000000000 item-a
ZREMRANGEBYRANK recent:user:demo 0 -6
ZREVRANGE recent:user:demo 0 4 WITHSCORES
```

점수는 double이며 정수는 2^53 범위까지 정확하게 표현한다. epoch 나노초는 이 범위를 넘으므로 정밀도를 잃을 수 있다. 밀리초 등 단위를 정하고 같은 점수의 member는 사전식으로 정렬된다는 점을 반영한다. 동점에서 엄격한 시간 순서가 필요하면 별도 sequence 설계가 필요하다.

동시 갱신 때 항상 크기 제한을 유지하려면 추가와 삭제를 Lua나 MULTI/EXEC 같은 원자적인 단위로 처리한다. pipelining은 왕복을 줄일 뿐 원자성을 보장하지 않는다. 여러 key를 쓰는 cluster script는 같은 hash slot 조건을 확인한다.

## 다른 활용과 한계

캐시는 TTL·무효화·stampede 대응, rate limit은 시간 창과 원자적 갱신, lock은 만료·소유자 확인과 fencing 요구를 함께 설계한다. Redis가 있다는 이유만으로 중복 결제·분산 트랜잭션·영구 보존 문제가 해결되지 않는다. 제품별 benchmark 수치를 현재 서비스 성능으로 일반화하지 않고 자신의 부하로 검증한다.

## 적용 범위와 확인

Redis Sorted Set 점수·rank와 일반적인 캐시 패턴 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [ZREMRANGEBYRANK](https://redis.io/docs/latest/commands/zremrangebyrank/)
- [ZADD 점수 정밀도](https://redis.io/docs/latest/commands/zadd/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#caching](../../tags.md#caching) · [#databases](../../tags.md#databases) · [#redis](../../tags.md#redis)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
