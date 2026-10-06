---
title: 데이터 레이크와 테이블 계층
category: databases
tags:
- big-data
- databases
status: note
reviewed_at: '2026-10-06'
applies_to: Apache Iceberg 공식 문서의 테이블·snapshot·commit 개념
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# 데이터 레이크와 테이블 계층

데이터 레이크는 다양한 원천 데이터를 저장하고 분석하는 구조다. 원시 파일 저장소, 메타데이터/catalog, 테이블 형식과 query engine을 분리해서 생각한다.

## 트랜잭션을 어디서 제공하는가

단순 파일 저장만으로 DB와 같은 트랜잭션이 생기지는 않는다. 하지만 “데이터 레이크에는 트랜잭션이 없다”는 단정도 틀리다. Iceberg 같은 테이블 계층은 snapshot과 원자적인 metadata commit을 이용하여 일관된 읽기와 변경을 지원한다.

실제 보장은 table format, catalog, engine과 작업 종류에 의존한다. 한 테이블의 원자적 commit을 여러 시스템 전체의 분산 트랜잭션과 혼동하지 않는다. 스키마·partition 진화, 작은 파일, compaction과 snapshot 보관도 운영 비용이다.

## 학습 질문

동시 writer가 충돌하면 어떻게 처리되는가, 실패한 commit의 파일은 어떻게 정리되는가, 읽기가 어느 snapshot을 보는가, catalog 장애에서 무엇이 가능한가를 확인한다. 레이크·warehouse라는 이름보다 데이터 갱신, 지연, 일관성과 조회 요구로 비교한다.

## 적용 범위와 확인

Apache Iceberg 공식 문서의 테이블·snapshot·commit 개념 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [Apache Iceberg](https://iceberg.apache.org/docs/latest/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#big-data](../tags.md#big-data) · [#databases](../tags.md#databases)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
