---
title: Git 협업 작업 흐름
category: devops
tags:
- devops
- git
- version-control
status: note
reviewed_at: '2026-10-06'
applies_to: Git fetch/merge/rebase/push와 branch rebase 설정
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# Git 협업 작업 흐름

push는 로컬 commit을 원격 ref에 반영한다. 원격에만 새 commit이 있으면 일반적으로 non-fast-forward로 거부되며 push가 자동 merge commit을 만드는 것은 아니다.

## 원격 변경 통합

개인 작업 branch에서 fetch로 원격을 읽고 diff/log를 확인한 뒤 merge 또는 rebase를 선택한다. rebase는 자신의 commit을 새 기반 위에 다시 만들어 commit ID가 바뀐다. 이미 공유한 branch에서는 협업자와 이력 변경 방식을 합의한다.

```sh
git fetch origin
git log --oneline --graph --decorate --all -20
# 아래는 개인 작업 branch에서만 선택해서 실행할 통합 예시
git rebase origin/main
```

`git pull --rebase`는 fetch와 rebase를 연결한다. `branch.<name>.rebase`는 pull의 동작을 설정하는 항목이며 push 직전 자동 rebase 설정이 아니다. 충돌은 양쪽 의도를 반영해 해결한 뒤 관련 검증을 실행한다.

## 마무리

변경과 파일 상태를 확인하고 합의된 branch에 push한다. 강제 push로 원격 변경을 덮어쓰는 것을 일반 해결책으로 사용하지 않는다. 로컬 수정이 있다면 먼저 보존·분리하여 통합 작업의 영향을 확인한다.

## 적용 범위와 확인

Git fetch/merge/rebase/push와 branch rebase 설정 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [Git 설정](https://git-scm.com/docs/git-config)
- [Git push](https://git-scm.com/docs/git-push)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#devops](../../../tags.md#devops) · [#git](../../../tags.md#git) · [#version-control](../../../tags.md#version-control)

[주제 목차](../../index.md) · [위키 홈](../../../index.md)

<!-- END WIKI NAV -->
