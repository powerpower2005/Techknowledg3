---
title: CKS 학습 가이드
category: containers
tags:
- certification
- containers
- kubernetes
- security
status: note
reviewed_at: '2026-10-06'
applies_to: Kubernetes 자격 학습 안내; 응시 규칙은 응시 시점의 공식 안내 확인
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# CKS 학습 가이드

클러스터·시스템 hardening, 공급망, workload 보안과 runtime 탐지를 학습한다.

## 학습 절차

공식 시험 페이지와 연결된 handbook·curriculum에서 범위와 요구 버전을 확인한다. 시험 시간, 통과 점수, 허용 도구·자료·응시 환경은 바뀔 수 있으므로 과거 개인 메모의 규칙을 그대로 사용하지 않는다.

개인 실습 환경에서 작은 manifest를 작성하고 리소스 상태와 이벤트를 읽는 연습을 한다. 명령을 암기하는 데 그치지 않고 실패 조건과 복구 결과를 설명한다. 시험 문제나 조직의 접근 정보를 학습 자료에 저장하지 않는다.

```sh
kubectl config current-context
kubectl -n demo get pods
kubectl -n demo get events --sort-by=.metadata.creationTimestamp
```

조회 명령도 현재 context와 권한을 확인한 뒤 사용한다. 학습 클러스터 외부에는 실행하지 않는다. CKS의 선행 자격 조건은 공식 안내에서 함께 확인한다.

## 적용 범위와 확인

Kubernetes 자격 학습 안내; 응시 규칙은 응시 시점의 공식 안내 확인 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [공식 자격 안내](https://training.linuxfoundation.org/certification/certified-kubernetes-security-specialist/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#certification](../../../tags.md#certification) · [#containers](../../../tags.md#containers) · [#kubernetes](../../../tags.md#kubernetes) · [#security](../../../tags.md#security)

[주제 목차](../../index.md) · [위키 홈](../../../index.md)

<!-- END WIKI NAV -->
