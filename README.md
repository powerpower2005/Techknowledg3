# Techknowledg3

공개 기술 학습 위키입니다. **90개 주제 문서**를 같은 Markdown 원본으로 GitHub와 로컬 웹에서 읽습니다. 주제별 목차, 문서 태그와 검색을 제공합니다.

- [위키 홈](docs/index.md)
- [태그로 찾기](docs/tags.md)
- [로컬 실행](docs/guides/wiki.md)
- [문서 작성 규칙](docs/guides/contributing.md)
- [나중에 GitHub Pages로 게시](docs/guides/github-pages.md)

## 로컬 실행

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m mkdocs serve
```

`http://127.0.0.1:8001/Techknowledg3/`에서 읽습니다. Python 3.12 환경을 권장합니다.

## 문서 관리

```bash
python scripts/wiki.py update
python scripts/wiki.py check
python -m mkdocs build --strict
```

문서는 공개 범위·참고 출처·적용 버전을 확인한 학습 노트입니다. 문서 검토와 실습·실측 결과는 구분합니다. 사이트 배포는 별도의 수동 워크플로로 켭니다.
