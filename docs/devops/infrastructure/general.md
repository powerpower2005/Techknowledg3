---
title: 인프라 설계
category: devops
tags:
- devops
- infrastructure
status: note
reviewed_at: '2026-10-06'
applies_to: 일반 인프라 설계와 RPO/RTO
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# 인프라 설계

## 요구를 자원으로 바꾸기

처리량·응답 시간·가용성과 RPO/RTO를 먼저 정하고 계산·네트워크·저장소를 배치한다. RPO는 허용 데이터 손실의 시간 범위, RTO는 복구 목표 시간이다. 목표는 복구 시험에서 확인해야 한다.

## 점검할 경계

장애 영역, 단일 실패 지점, 관리 접근, 비밀 정보, 용량·quota와 백업을 확인한다. replica 두 개가 같은 노드나 장애 영역에 있으면 기대한 가용성을 얻지 못할 수 있다. 관찰 도구도 업무 서비스와 함께 실패할 가능성을 고려한다.

## 설계 연습

단일 웹 서버를 두 영역으로 확장할 때 load balancer, 상태 저장, DB failover와 데이터 복구를 각각 그린다. 평상시 비용과 장애 시 추가 용량을 함께 추정한다. [IaC](iac.md)로 설정을 재현하고 변경 전에 계획을 비교한다.

## 적용 범위와 확인

일반 인프라 설계와 RPO/RTO 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [AWS 재해 복구 목표](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/introduction.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#devops](../../tags.md#devops) · [#infrastructure](../../tags.md#infrastructure)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
