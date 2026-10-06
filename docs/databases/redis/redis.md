---
title: Redis 운영
category: databases
tags:
- databases
- memory
- performance
- redis
status: note
reviewed_at: '2026-10-06'
applies_to: Redis 공식 persistence·eviction·메모리 관리 개념
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# Redis 운영

Redis는 메모리 중심의 데이터 저장소이며 RDB와 AOF 영속성 기능을 제공한다. 캐시로 사용하는지 권위 있는 데이터를 저장하는지에 따라 유실 허용 범위·복구·eviction 설정이 달라진다.

## 영속성과 메모리

RDB는 시점 snapshot, AOF는 변경 기록을 이용한다. 각각의 저장·fsync 정책과 복구 조건을 확인한다. background 저장/재작성의 fork와 copy-on-write는 추가 메모리를 요구하며 쓰기량에 따라 비용이 달라진다.

메모리를 일률적으로 45% 또는 95%만 사용하라는 기준은 적용하지 않는다. 데이터, allocator fragmentation, 복제·클라이언트 버퍼, COW와 OS 여유를 측정해 maxmemory를 정한다. 저장이 끝날 때의 peak와 복구 중 메모리도 확인한다.

## 만료와 축출

expiration은 TTL이 지난 키를 제거하는 것이고 eviction은 maxmemory 상황에서 정책에 따라 키를 축출하는 것이다. `volatile-lru`는 TTL이 설정된 키를 후보로 LRU를 적용하며 이미 만료된 키만 고르는 정책이 아니다. allkeys/volatile과 LRU/LFU/random/TTL 등 정책의 차이를 확인한다. noeviction이나 후보가 없는 volatile 정책에서는 쓰기가 실패할 수 있다.

```text
INFO memory
INFO persistence
INFO stats
```

관찰 대상은 used memory/RSS, 저장 실패, evicted keys, hit/miss, 지연과 복제 상태다. 누적 counter는 구간 차이로 비율을 계산한다. 캐시 hit rate만 높다고 사용자 요청이 빨라졌다고 단정하지 않는다. 장애·재시작·백업 복구와 정책 적용 후 데이터 동작을 함께 검증한다.

## 적용 범위와 확인

Redis 공식 persistence·eviction·메모리 관리 개념 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [Redis 축출 정책](https://redis.io/docs/latest/develop/reference/eviction/)
- [Redis 운영](https://redis.io/docs/latest/operate/oss_and_stack/management/admin/)
- [Redis 영속성](https://redis.io/docs/latest/management/persistence/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#databases](../../tags.md#databases) · [#memory](../../tags.md#memory) · [#performance](../../tags.md#performance) · [#redis](../../tags.md#redis)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
