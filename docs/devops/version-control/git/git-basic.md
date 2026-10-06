---
title: Git 기초
category: devops
tags:
- devops
- git
- version-control
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
reviewed_at: '2026-10-06'
applies_to: 일반 Git 저장소; unborn HEAD와 공유 이력 작업은 별도 확인
content_origin: original-summary
---

# Git 기본 개념

Git은 분산 버전 관리 도구다. 일반적인 clone에는 이력이 있는 로컬 저장소가 있으며 shallow·partial clone 등의 구성에서는 포함 범위가 다를 수 있다.

| 위치 | 역할 |
| --- | --- |
| 작업 디렉터리 | 현재 수정하는 파일 |
| index | 다음 커밋에 담을 내용 |
| 로컬 저장소 | 커밋과 객체, 참조 |
| 원격 저장소 | fetch·push로 함께 사용하는 저장소 |

## 수정 내용 확인

```bash
git status
git diff
git diff --staged
git add docs/example.md
git commit -m "Update example note"
```

`git diff`는 작업 디렉터리와 index, `git diff --staged`는 index와 HEAD의 차이를 확인한다. 커밋은 저장된 index 내용을 사용한다. 한 파일도 일부 변경만 stage되어 있을 수 있다.

## Stage 해제와 추적 중단

일반적으로 HEAD가 있는 저장소에서 `git restore --staged docs/example.md`는 작업 파일을 유지하면서 index를 HEAD 기준으로 되돌린다. `git rm --cached docs/example.md`는 작업 파일을 남기고 추적을 중단하는 변경을 stage한다. 두 작업은 같은 의미가 아니다.

`.gitignore`는 이미 추적 중인 파일이나 과거 커밋의 내용을 삭제하지 않는다. 변경 전후 diff를 확인하고, 공유 이력을 바꾸는 작업은 협업 절차에 맞게 수행한다.

## 참고 자료

- [git restore](https://git-scm.com/docs/git-restore)
- [git rm](https://git-scm.com/docs/git-rm)
- [Pro Git](https://git-scm.com/book/en/v2)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#devops](../../../tags.md#devops) · [#git](../../../tags.md#git) · [#version-control](../../../tags.md#version-control)

[주제 목차](../../index.md) · [위키 홈](../../../index.md)

<!-- END WIKI NAV -->
