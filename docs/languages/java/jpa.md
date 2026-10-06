---
title: JPA와 ORM
category: languages
tags:
- databases
- java
- jpa
- languages
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
reviewed_at: '2026-10-06'
applies_to: Jakarta Persistence 3.2 개념; 구현체별 성능·설정은 별도 확인
content_origin: original-summary
---

# JPA와 ORM

Jakarta Persistence는 Java 객체와 관계형 데이터의 매핑·영속성 관리를 위한 표준 API와 규약이다. Hibernate 같은 구현체와 Spring Data JPA 같은 추상화 계층을 구분한다. Jakarta Persistence 3.x는 `jakarta.persistence` 이름 공간을 사용한다.

## 엔티티와 영속성 컨텍스트

EntityManager의 `persist`, `find`, `remove` 등으로 엔티티를 다룬다. 관리 중인 엔티티의 상태 변경은 flush 시점에 DB에 동기화될 수 있다. 관리되지 않는 객체의 필드 변경까지 자동으로 저장되는 것은 아니다. 트랜잭션 경계와 엔티티 상태를 확인한다.

flush는 영속성 컨텍스트의 변경을 DB에 동기화하는 동작이며 commit과 같지 않다. SQL 실행 시점이나 batch 효과는 구현체·식별자 전략·설정에 따라 달라진다.

## 조회와 성능

JPQL, Criteria와 native query 등으로 질의할 수 있다. 연관 관계의 fetch 전략과 질의 설계에 따라 추가 조회가 많아지는 N+1 문제가 생길 수 있다. 모든 관계가 기본으로 지연 로딩된다고 설명하지 않는다. 필요한 데이터와 실행 SQL·쿼리 수를 확인한다.

ORM을 사용해도 인덱스, DB 제약, 잠금과 스키마 변경 계획은 필요하다. 스키마 자동 생성 기능과 운영 데이터 migration을 같은 것으로 취급하지 않는다.

## 참고 자료

- [Jakarta Persistence 3.2 규약](https://jakarta.ee/specifications/persistence/3.2/jakarta-persistence-spec-3.2)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#databases](../../tags.md#databases) · [#java](../../tags.md#java) · [#jpa](../../tags.md#jpa) · [#languages](../../tags.md#languages)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
