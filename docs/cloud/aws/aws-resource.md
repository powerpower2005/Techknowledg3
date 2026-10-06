---
title: AWS 자원과 로드 밸런서
category: cloud
tags:
- aws
- cloud
- infrastructure
- networking
status: note
reviewed_at: '2026-10-06'
applies_to: EKS AWS Load Balancer Controller 기준; Auto Mode·NGINX는 별도 구현
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# AWS 자원과 로드 밸런서

## 기본 연결

VPC와 subnet, route table, 보안 그룹, 인터넷/NAT 경로를 나누어 본다. public subnet의 경로가 있다고 모든 인스턴스가 public IP나 올바른 보안 정책을 자동으로 갖는 것은 아니다. 가용 영역과 장애 범위도 확인한다.

## EKS와 controller 구분

AWS Load Balancer Controller 기준으로 Ingress는 ALB HTTP(S) 라우팅을 구성하고 `type: LoadBalancer` Service는 NLB 구성에 사용한다. controller 버전, IngressClass/Service의 class와 annotation 위치를 함께 확인한다. EKS Auto Mode 등 다른 구현은 별도 설정을 따른다.

NGINX Ingress Controller는 별도의 controller다. NGINX를 외부에 노출하는 Service와 그 뒤의 Ingress 라우팅은 AWS controller가 Ingress로 ALB를 만드는 흐름과 같지 않다. 서로 다른 controller의 annotation을 섞지 않는다.

## 진단과 검증

DNS → listener/TLS → target group health → Service/endpoint → 앱 순서로 확인한다. IP target과 instance target의 경로·보안 그룹 조건이 다르다. 장애 원인은 controller 이벤트, target health와 앱 응답으로 나눈다. 자원 생성·삭제와 요금은 실제 계정에서 별도 검토한다.

## 적용 범위와 확인

EKS AWS Load Balancer Controller 기준; Auto Mode·NGINX는 별도 구현 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [EKS Load Balancer Controller](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html)
- [EKS ALB Ingress](https://docs.aws.amazon.com/eks/latest/userguide/alb-ingress.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#aws](../../tags.md#aws) · [#cloud](../../tags.md#cloud) · [#infrastructure](../../tags.md#infrastructure) · [#networking](../../tags.md#networking)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
