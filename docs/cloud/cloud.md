---
title: 클라우드 개요
category: cloud
tags:
- cloud
status: note
reviewed_at: '2026-10-06'
applies_to: IaaS/PaaS/SaaS 공통 개념과 AWS 책임 모델 예시
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# 클라우드 개요

클라우드는 네트워크로 자원을 제공하고 필요한 만큼 할당·회수하는 운영 모델이다. IaaS는 VM·네트워크 등 기반 자원, PaaS는 애플리케이션 실행 기반, SaaS는 완성된 소프트웨어 기능을 제공한다. 경계는 제품별로 달라진다.

## 선택 기준

탄력적인 자원 공급과 관리 서비스로 초기 운영 부담을 줄일 수 있다. 비용은 사용량, 데이터 전송, 저장과 관리 기능으로 나누어 추정한다. 자동 확장만 설정했다고 비용이나 장애 대응이 자동으로 해결되지는 않는다.

보안 책임은 서비스 유형별로 나뉜다. 관리 서비스도 사용자 데이터·접근 권한·애플리케이션 설정의 책임을 없애지 않는다. 가용 영역과 region의 장애 범위, 서비스 quota와 복구 목표를 확인한다.

## 학습 예시

웹 앱을 설계한다면 입구(load balancer), 실행 자원, DB, 객체 저장, 비밀 정보 관리와 관찰 지표를 그려 본다. 최소 권한과 백업·복구 시험을 포함하고 단일 VM 구성과 관리 서비스 구성을 비용·복구 시간으로 비교한다. 실제 계정에 자원을 생성하기 전 예상 비용과 삭제 절차를 정한다.

## 적용 범위와 확인

IaaS/PaaS/SaaS 공통 개념과 AWS 책임 모델 예시 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [AWS 공동 책임 모델](https://aws.amazon.com/compliance/shared-responsibility-model/)
- [재해 복구 개요](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/introduction.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#cloud](../tags.md#cloud)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
