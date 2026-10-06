---
title: 로그 분석과 Cloudflare 사례
category: devops
tags:
- devops
- logging
- monitoring
- reference
status: note
visibility: public
reviewed_at: '2026-10-07'
publication_reviewed_at: '2026-10-07'
applies_to: 일반적인 로그 분석 절차와 Cloudflare의 2018년 공개 사례
---

# 로그 분석과 Cloudflare 사례

로그는 사건의 상세 기록, 메트릭은 집계된 상태, trace는 요청이 여러 구간을 통과한 흐름을 살펴보는 데 쓴다. 지연 경보로 이상을 찾고 같은 시간·요청 ID의 로그와 trace로 원인 후보를 좁히는 식으로 연결한다.

## 분석에 필요한 필드

```json
{"time":"2026-10-07T00:00:00Z","service":"demo-api","request_id":"demo-42","route":"/articles/:id","status":503,"duration_ms":1200,"error_code":"dependency_timeout"}
```

학습용 가상 로그다. 시각, 서비스, 환경, route, 상태와 지연을 구조화하고 요청 ID로 연결한다. URL 전체나 사용자 ID를 메트릭 label로 넣으면 cardinality가 크게 늘 수 있다. 토큰·쿠키·비밀번호와 불필요한 개인정보는 수집 전에 제거한다.

## 느린 요청을 조사하는 순서

1. 발생 시간과 기능·사용자 영향 범위를 정하고 오류율·p95·p99를 확인한다.
2. 같은 구간의 로그를 route·상태·오류 종류로 나눠 특정 작업에 몰리는지 본다.
3. 대표 요청 ID의 trace에서 DB, 외부 호출과 queue 대기를 비교한다.
4. 최근 배포·설정·입력량 변화와 대조해 가설을 세운다.
5. 가설을 확인할 관측이나 작은 재현을 하고 완화 후 같은 지표를 비교한다.

한 줄의 timeout만으로 DB가 원인이라고 확정하지 않는다. 로그 유실·수집 지연·sampling과 시계 차이가 있으면 관찰도 편향될 수 있다.

## Cloudflare의 공개 사례에서 배울 점

[2018-03-06의 원문](https://blog.cloudflare.com/http-analytics-for-6m-requests-per-second-using-clickhouse/)은 대규모 HTTP 분석 파이프라인을 ClickHouse 중심으로 바꾼 사례다. 이전 파이프라인의 집계·저장 구성에는 단일 장애 지점과 유지보수 복잡성이 있었고, 새 구조에서는 분석 저장소의 기능에 맞춰 집계와 처리 책임을 재배치했다.

핵심은 특정 제품을 사용하면 같은 처리량이 나온다는 주장이 아니다. 분석 질의, 데이터량·보존 기간, 집계 시점과 장애 복구 조건을 기준으로 구조를 선택했다는 점이다. 원문의 수치는 당시 Cloudflare 환경의 결과이며 현재 제품 기능이나 이 위키의 검증 수치로 취급하지 않는다.

## 자신의 설계에 적용하기

먼저 자주 묻는 질문을 정한다. “최근 10분 동안 어떤 route의 오류가 늘었는가?”에 필요한 필드와 집계를 정의하고, 원본 로그가 필요한 조사와 미리 집계할 통계를 구분한다. 보관 기간, 압축, 삭제, 접근 권한과 재처리 비용도 결정한다.

초당 100개의 로그가 평균 1KiB라는 학습 가정이면 하루 원본량은 약 8.24GiB다. 복제·인덱스·압축·peak와 보존 기간을 추가해 용량을 추정한다. 로그 수집 장애가 애플리케이션까지 멈추게 할지, 일부 유실을 허용할지도 요구사항으로 정한다.

[통합 로그 설계](integration.md) · [SRE](../sre/sre.md) · [성능 진단](../troubleshooting.md)

## 참고 자료와 확인

사례는 공개 원문을 요약했고 나머지는 학습용 분석 절차다. 실제 로그나 고객 데이터를 수집하지 않았으며 ClickHouse의 처리량을 측정하지 않았다.

- [Cloudflare HTTP Analytics 사례](https://blog.cloudflare.com/http-analytics-for-6m-requests-per-second-using-clickhouse/)
- [OpenTelemetry: 관측 신호](https://opentelemetry.io/docs/concepts/signals/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#devops](../../tags.md#devops) · [#logging](../../tags.md#logging) · [#monitoring](../../tags.md#monitoring) · [#reference](../../tags.md#reference)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
