---
title: GitHub Pages 배포
category: wiki
tags:
- wiki
status: note
visibility: public
---

# GitHub Pages 배포

저장소의 Markdown은 공개되어 있습니다. 웹 사이트 게시는 별도로 켭니다. 현재 배포 워크플로는 수동 실행이며 `WIKI_PUBLISH_ENABLED` 변수가 문자열 `true`일 때만 배포합니다.

## 나중에 게시하기

1. `main`에서 문서와 링크 검사, strict 빌드를 통과시킵니다.
2. **Settings → Pages → Build and deployment → Source**에서 **GitHub Actions**를 선택합니다.
3. **Settings → Secrets and variables → Actions → Variables**에 `WIKI_PUBLISH_ENABLED=true`를 설정합니다.
4. **Actions → Deploy wiki to GitHub Pages → Run workflow**를 `main`에서 실행합니다.
5. 성공한 배포의 주소를 확인합니다. 설정된 예상 주소는 `https://powerpower2005.github.io/Techknowledg3/`입니다.

`main` push와 PR에서는 검사와 빌드만 수행합니다. 사이트 빌드는 `docs/`의 파일을 사용하며 빌드 결과 `site/`는 commit하지 않습니다.

## 설정과 검사

사이트 주소·테마는 `mkdocs.yml`, 검사와 배포는 `.github/workflows/`, 고정된 Python 의존성은 `requirements.txt`에 있습니다.

```bash
python scripts/wiki.py check
python -m mkdocs build --strict
```

[GitHub Pages 워크플로](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) · [Material 배포 안내](https://squidfunk.github.io/mkdocs-material/publishing-your-site/)
