---
title: 위키 사용법
category: wiki
tags:
- wiki
status: note
visibility: public
---

# 위키 사용법

`docs/`의 같은 Markdown 원본을 GitHub와 로컬 웹 위키에서 읽습니다. [홈](../index.md)에서 주제를 고르거나 [태그 목록](../tags.md)을 사용합니다. 웹에서는 검색과 밝은·어두운 화면 전환도 제공합니다.

## 로컬에서 읽기

Python 3.12 환경을 권장합니다. 저장소 루트에서 실행합니다.

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m mkdocs serve
```

macOS/Linux:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m mkdocs serve
```

주소는 `http://127.0.0.1:8001/Techknowledg3/`입니다. 문서 추가·태그 변경 후 가상환경 Python으로 `scripts/wiki.py update`를 실행합니다.

| 위치 | 용도 |
| --- | --- |
| `docs/<주제>/` | 태그와 제목을 가진 주제 문서 |
| `docs/<주제>/index.md` | 자동 생성한 주제 목차 |
| `docs/tags.md`, `docs/tags/index.md` | Markdown·웹 태그 탐색 |
| `docs/guides/` | 사용·작성·배포 안내 |
| `templates/article.md` | 새 문서 양식 |
| `scripts/wiki.py` | 목차 생성과 검사 |
| `site/` | Git에 넣지 않는 빌드 결과 |

[문서 작성 규칙](contributing.md) · [GitHub Pages](github-pages.md)
