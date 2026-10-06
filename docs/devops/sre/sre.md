---
title: SRE
category: devops
tags:
- automation
- devops
- monitoring
- sre
status: note
reviewed_at: '2026-10-06'
applies_to: 일반적인 SRE 학습 개념
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# SRE

SRE는 사용자에게 필요한 신뢰성을 목표로 운영과 개발을 연결하는 접근이다. 모든 오류를 없애겠다는 목표보다 측정 가능한 서비스 수준을 합의하는 것이 출발점이다.

## SLI, SLO, 오류 예산

SLI는 성공 요청 비율이나 지연 같은 실제 지표다. SLO는 측정 기간과 목표값을 함께 정의한다. 예를 들어 학습용 목표를 “30일 동안 적격 요청의 99.9%가 성공”으로 두면 허용 실패 비율은 0.1%다. 제외 요청과 성공의 정의를 먼저 정해야 한다.

오류 예산을 얼마나 빨리 소모하는지로 경보를 설계하고, 소모가 지속되면 배포 속도와 안정화 작업을 조정한다. 가용성과 지연 목표는 서로 다른 지표일 수 있다.

## 반복 가능한 운영

수동 반복 작업을 측정하고 자동화 후보를 정한다. 장애 대응은 영향 확인, 완화, 복구 검증, 원인 분석으로 나누고 담당자와 의사소통 경로를 정한다. 회고에는 시간순 사실, 기여 요인, 검증 가능한 후속 작업을 남긴다. 특정인의 실수만으로 원인을 끝내지 않는다.

## 적용 범위와 확인

일반적인 SRE 학습 개념 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#automation](../../tags.md#automation) · [#devops](../../tags.md#devops) · [#monitoring](../../tags.md#monitoring) · [#sre](../../tags.md#sre)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
