# Techknowledg3

CS 면접 질문과 기술 지식을 모으는 공개 학습 위키입니다. 같은 Markdown 원본으로 GitHub, GitHub Pages와 로컬 웹에서 읽습니다. 주제별 목차, 문서 태그와 검색을 제공합니다.

- [위키 홈](docs/index.md)
- [CS 면접 질문과 학습 순서](docs/interview/cs-interview.md)
- [CS 면접 답변과 꼬리 질문 26개](docs/interview/cs-answers.md)
- [태그로 찾기](docs/tags.md)
- [로컬 실행](docs/guides/wiki.md)
- [문서 작성 규칙](docs/guides/contributing.md)
- [GitHub Pages 게시와 갱신](docs/guides/github-pages.md)

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

문서는 공개 범위·참고 출처·적용 버전을 확인한 학습 노트입니다. 문서 검토와 실습·실측 결과는 구분합니다. GitHub Pages를 활성화하면 `main`에 올린 변경은 검사와 빌드 후 자동 게시됩니다. 최초 설정과 배포 중지 방법은 [배포 안내](docs/guides/github-pages.md)를 참고하세요.

면접 질문을 추가할 때는 [질문 양식](templates/interview.md)을 복사해 `docs/interview/`에 저장합니다. 개념을 자세히 설명하는 문서는 해당 주제 디렉터리에 두고 면접 답변에서 연결합니다.
