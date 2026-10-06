---
title: CloudFront와 CDN
category: cloud
tags:
- aws
- caching
- cdn
- cloud
status: note
reviewed_at: '2026-10-06'
applies_to: CloudFront 실시간 access log의 Kinesis 전달 경로
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# CloudFront와 CDN

CloudFront는 edge에서 콘텐츠를 제공하는 CDN이다. cache key의 query·header·cookie와 origin 요청 정책을 구분한다. 개인화된 응답을 잘못 공유 캐시하지 않도록 인증·캐시 경계를 정한다.

## 로그 종류

실시간 access log는 Kinesis Data Streams로 전달된다. 여기서 S3나 분석 저장소로 보내려면 후속 소비·전달 파이프라인이 필요하다. 표준 access log는 별도 기능이며 버전과 설정에 따른 지원 목적지를 확인한다. Lambda@Edge 실행 로그와 CloudFront access log도 같은 데이터가 아니다.

## 진단

요청 ID, cache hit/miss, origin 응답, TTL과 캐시 정책을 확인한다. 변경한 origin 콘텐츠가 즉시 모든 edge에서 바뀐다는 전제를 두지 않는다. invalidation·짧은 TTL·버전 URL은 비용과 최신성 요구로 선택한다. 에러 캐싱과 인증 정보 전달도 별도로 확인한다.

## 적용 범위와 확인

CloudFront 실시간 access log의 Kinesis 전달 경로 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [CloudFront 실시간 로그](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#aws](../../tags.md#aws) · [#caching](../../tags.md#caching) · [#cdn](../../tags.md#cdn) · [#cloud](../../tags.md#cloud)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
