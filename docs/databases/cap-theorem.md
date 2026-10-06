---
title: CAP와 PACELC
category: databases
tags:
- databases
- distributed-systems
status: note
reviewed_at: '2026-10-06'
applies_to: CAP 논문의 비동기 분산 모델과 PACELC 개념
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# CAP와 PACELC

CAP의 Consistency는 일반적으로 선형화 가능한 단일 복사본처럼 보이는 읽기·쓰기를 뜻한다. Availability는 실패하지 않은 노드에 도달한 연산이 완료되는 성질이다. “분할 때문에 수행할 수 없음”이라는 오류를 반환하는 것으로 읽기·쓰기 가용성을 충족시키지는 않는다.

## 분할 상황의 선택

서로 통신하지 못하는 두 복제본에 쓰기와 읽기가 들어오면 모든 정상 노드의 연산을 계속 완료하면서 최신 쓰기를 일관되게 반영하는 두 보장을 함께 유지할 수 없다. 분할 중 일부 요청을 거부·대기시키거나, 서로 다른 상태를 허용하고 나중에 조정하는 선택이 필요하다. CAP의 availability와 운영 SLO의 가용성은 같은 측정 단위가 아니다.

RDBMS를 전부 CP, NoSQL을 전부 AP로 분류하지 않는다. 제품의 복제 방식, 읽기·쓰기 concern, quorum과 장애 처리 조건을 봐야 한다. 정상 상태에서 두 특성을 쓰다가 분할 때 무엇을 포기하는지를 묻는 것이 유용하다.

## PACELC

분할(P)이 있으면 A와 C의 tradeoff, 그 외(E) 정상 상황에서는 지연(L)과 일관성(C)의 tradeoff를 설명한다. 멀리 떨어진 복제본의 확인을 기다리는 쓰기는 강한 일관성을 얻는 대신 지연이 증가할 수 있다. 이것은 “정상 때 가용성과 일관성”이라는 설명과 다르다.

## 생각해 볼 예시

두 region의 재고 서비스에서 분할 중 양쪽 판매를 계속 허용하면 재고 초과 판매가 생길 수 있다. 일부 판매를 제한하면 사용자 요청을 완료하지 못한다. 요구사항에 허용 오차와 실패 응답·대기 정책을 적고 실제 장애 시험으로 결과를 확인한다.

## 적용 범위와 확인

CAP 논문의 비동기 분산 모델과 PACELC 개념 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [Gilbert/Lynch 원 논문 §2–3](https://cs.nyu.edu/~apanda/classes/sp25/papers/gilbert02brewers.pdf)
- [PACELC 제안자 Daniel Abadi](https://dbmsmusings.blogspot.com/2010/04/problems-with-cap-and-yahoos-little.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#databases](../tags.md#databases) · [#distributed-systems](../tags.md#distributed-systems)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
