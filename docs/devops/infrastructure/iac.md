---
title: Infrastructure as Code
category: devops
tags:
- devops
- iac
- infrastructure
status: note
reviewed_at: '2026-10-06'
applies_to: Terraform CLI의 plan/state 개념; provider별 동작은 별도 확인
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# Infrastructure as Code

IaC는 자원의 원하는 구성을 코드로 표현하고 실제 상태와 맞추는 방법이다. 선언 파일만 보관하면 끝나는 것이 아니라 state, provider 버전, credentials와 변경 권한을 함께 관리해야 한다.

## Terraform 흐름

```sh
terraform fmt -check
terraform validate
terraform plan
```

init은 provider/backend 준비가 필요하고 위 명령도 작업 디렉터리와 인증 환경에 영향을 받는다. 이 문서의 명령은 실행 순서 설명이며 현재 계정에 apply하는 지시가 아니다. plan을 검토하여 생성·변경·삭제 대상과 예기치 않은 교체를 확인한다.

## 상태와 비밀 정보

state와 저장한 plan 파일에는 sensitive 값이 평문으로 포함될 수 있다. `sensitive` 표시는 출력 일부를 가리는 기능이며 파일 암호화나 비밀 미저장의 보장이 아니다. 접근 제어·암호화된 remote backend, state locking·백업을 검토하고 state와 plan 파일을 Git에 넣지 않는다.

## 검증

재실행 시 불필요한 diff가 없는지, 수동 변경을 탐지하는지, 실패 후 state와 실제 자원의 차이를 복구할 수 있는지 확인한다. 모듈과 provider 버전을 고정하고 환경별 입력을 구분한다.

## 적용 범위와 확인

Terraform CLI의 plan/state 개념; provider별 동작은 별도 확인 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [Terraform plan](https://developer.hashicorp.com/terraform/cli/commands/plan)
- [민감 데이터 관리](https://developer.hashicorp.com/terraform/language/manage-sensitive-data)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#devops](../../tags.md#devops) · [#iac](../../tags.md#iac) · [#infrastructure](../../tags.md#infrastructure)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
