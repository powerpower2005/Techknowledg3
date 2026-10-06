---
title: Prometheus Pull과 Pushgateway
category: devops
tags:
- devops
- high-availability
- monitoring
- prometheus
status: note
reviewed_at: '2026-10-06'
applies_to: Prometheus 공식 Pushgateway 권장 사용 범위
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# Prometheus Pull과 Pushgateway

Prometheus는 일반적으로 target의 metric endpoint를 scrape한다. service discovery는 target 발견, scrape는 수집, alert는 평가·알림이라는 서로 다른 단계다.

## Pushgateway의 범위

짧게 실행되고 종료하는 서비스 단위 batch job의 결과 metric에는 Pushgateway를 고려할 수 있다. 모든 exporter나 오래 실행하는 서비스를 push 방식으로 바꾸는 기본 대안은 아니다. gateway가 metric을 보관하므로 더 이상 유효하지 않은 series의 삭제와 grouping key 수명 관리가 필요하다.

Prometheus와 Pushgateway가 반드시 1:1이어야 한다는 제약은 없다. 여러 Prometheus가 scrape할 수 있지만 동일 metric 중복, 장애 지점과 보관 수명 문제를 따로 설계해야 한다. gateway 도입만으로 target의 up 관찰과 전체 HA가 해결되지 않는다.

## 선택과 검증

수집 장애, target 발견 실패, scrape 지연과 저장소 문제를 구분한다. 고가용성 수집·장기 보관은 replica와 중복 제거·원격 저장 등의 요구로 검토한다. Kafka나 Druid 도입은 데이터 종류, 수집량, 조회와 보관 요구를 근거로 판단하고 이름만으로 성능 우위를 단정하지 않는다.

## 적용 범위와 확인

Prometheus 공식 Pushgateway 권장 사용 범위 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [Pushgateway 사용 지침](https://prometheus.io/docs/practices/pushing/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#devops](../../tags.md#devops) · [#high-availability](../../tags.md#high-availability) · [#monitoring](../../tags.md#monitoring) · [#prometheus](../../tags.md#prometheus)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
