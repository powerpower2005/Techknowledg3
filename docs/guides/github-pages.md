---
title: GitHub Pages 배포
category: wiki
tags:
- wiki
status: note
visibility: public
---

# GitHub Pages 배포

공개 학습 위키를 GitHub Actions로 빌드해 GitHub Pages에 게시합니다. `main`에 push하거나 수동으로 워크플로를 실행하면 문서 검사와 strict 빌드를 거쳐 배포됩니다. 배포는 `main` 브랜치에서만 가능하며 `WIKI_PUBLISH_ENABLED` 변수가 문자열 `true`여야 합니다.

## 최초 게시 설정

1. `main`에서 문서와 링크 검사, strict 빌드를 통과시킵니다.
2. **Settings → Pages → Build and deployment → Source**에서 **GitHub Actions**를 선택합니다.
3. **Settings → Secrets and variables → Actions → Variables**에 `WIKI_PUBLISH_ENABLED=true`를 설정합니다.
4. **Actions → Deploy wiki to GitHub Pages → Run workflow**를 `main`에서 실행합니다.
5. 성공한 배포의 주소를 확인합니다. 설정된 예상 주소는 `https://powerpower2005.github.io/Techknowledg3/`입니다.

이 설정은 저장소당 한 번 필요합니다. 설정 후에는 `main` push가 사이트를 갱신하며 PR에서는 검사와 빌드만 수행합니다. 사이트 빌드는 `docs/`의 파일을 사용하며 빌드 결과 `site/`는 commit하지 않습니다.

## 질문과 지식 추가하기

1. 면접 질문은 `docs/interview/`, 기술 설명은 `docs/<주제>/`에 Markdown으로 작성합니다.
2. `python scripts/wiki.py update`로 홈, 태그와 메뉴를 갱신합니다.
3. 문서 검사와 strict 빌드를 실행한 뒤 변경을 `main`에 올립니다.
4. **Actions → Deploy wiki to GitHub Pages**에서 배포 성공을 확인합니다.

배포가 실패하면 해당 실행의 로그를 확인하세요. 자동 게시를 멈추려면 `WIKI_PUBLISH_ENABLED=false`로 변경합니다. 이 변수는 새 배포만 중지하며 이미 게시된 사이트는 유지됩니다.

## 설정과 검사

사이트 주소·테마는 `mkdocs.yml`, 검사와 배포는 `.github/workflows/`, 고정된 Python 의존성은 `requirements.txt`에 있습니다.

```bash
python scripts/wiki.py check
python -m mkdocs build --strict
```

[GitHub Pages 워크플로](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) · [Material 배포 안내](https://squidfunk.github.io/mkdocs-material/publishing-your-site/)
