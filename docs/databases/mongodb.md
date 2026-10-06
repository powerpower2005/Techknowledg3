---
title: MongoDB
category: databases
tags:
- databases
- mongodb
- nosql
status: note
reviewed_at: '2026-10-06'
applies_to: MongoDB 8.0 문서 및 5.0 이후 재샤딩 기능
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# MongoDB

MongoDB는 BSON 문서를 저장한다. JSON의 값에는 문자열·숫자 외에도 객체, 배열, boolean, null이 있다. BSON은 여기에 날짜 등 추가 타입을 지원한다. 필드 부재와 `null` 값은 서로 다르며 `{field: null}` 조회는 둘 모두와 일치할 수 있다.

```javascript
// 값이 있는 필드만 조회하려면 존재 여부와 null을 구분한다.
db.accounts.find({ email: { $exists: true, $ne: null } })
```

## 복제와 샤딩

Replica Set은 primary와 secondary로 복제한다. 선거에서는 투표 멤버의 과반수가 필요하다. 홀수의 투표 멤버를 권장하지만 전체 멤버 수가 항상 홀수여야 하는 것은 아니다. 비투표 멤버도 둘 수 있다. 읽기 선호, read concern, write concern을 별도로 선택하고 장애 때의 지연과 데이터 손실 가능성을 검증한다.

샤딩은 shard key로 데이터를 분산한다. 카디널리티, 특정 값 집중, 단조 증가, 주요 조회의 targetability를 함께 고려한다. “shard key는 영구히 변경 불가능”이라는 설명은 현재 버전에 맞지 않는다. MongoDB 5.0부터 `reshardCollection`으로 키 변경이 가능하며 조건과 비용을 확인해야 한다. 키 정제와 재샤딩은 다른 작업이다.

## 운영 확인

복제 지연, 선거 이력, 느린 쿼리, 인덱스 크기, 디스크 여유, chunk 분포를 본다. 백업은 복구 시험과 함께 검증한다. 예시 컬렉션에는 실제 고객 주소나 전화번호를 넣지 않는다.

## 적용 범위와 확인

MongoDB 8.0 문서 및 5.0 이후 재샤딩 기능 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [JSON 값 타입](https://www.rfc-editor.org/rfc/rfc8259)
- [null과 필드 존재](https://www.mongodb.com/docs/v8.0/reference/operator/query/exists/)
- [샤드 키 변경](https://www.mongodb.com/docs/manual/core/sharding-change-a-shard-key/)
- [Replica Set 구성원](https://www.mongodb.com/docs/manual/core/replica-set-members/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#databases](../tags.md#databases) · [#mongodb](../tags.md#mongodb) · [#nosql](../tags.md#nosql)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
