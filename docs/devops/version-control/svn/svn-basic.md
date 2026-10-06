---
title: SVN 기본
category: devops
tags:
- devops
- svn
- version-control
status: note
reviewed_at: '2026-10-06'
applies_to: SVN의 중앙 저장소·working copy 기본 개념
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# SVN 기본

SVN은 중앙 저장소와 working copy를 사용하는 버전 관리 도구다. update는 저장소 변경을 가져오고 commit은 자신의 변경을 저장소에 반영한다. Git의 로컬 commit과 같은 동작으로 생각하지 않는다.

## 조회부터 실습하기

```sh
svn info
svn status
svn diff
svn log -l 5
```

개인 실습 working copy에서 update → 수정 → diff 검토 → commit의 순서를 연습한다. 변경 추적에 들어가지 않은 새 파일은 add가 필요하다. conflict는 양쪽 의도를 확인해 해결하고 결과를 검사한다.

## 주의할 동작

revert는 로컬 변경을 버릴 수 있고 commit은 중앙 저장소에 변경을 보내므로 조회 명령과 구분한다. credentials나 생성 artifact를 저장하지 않는다. lock과 branch/merge 방식은 팀 운영 규칙과 SVN 버전을 함께 확인한다.

## 적용 범위와 확인

SVN의 중앙 저장소·working copy 기본 개념 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [Apache Subversion 시작 안내](https://subversion.apache.org/quick-start)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#devops](../../../tags.md#devops) · [#svn](../../../tags.md#svn) · [#version-control](../../../tags.md#version-control)

[주제 목차](../../index.md) · [위키 홈](../../../index.md)

<!-- END WIKI NAV -->
