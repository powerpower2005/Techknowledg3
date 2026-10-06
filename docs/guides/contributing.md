---
title: 문서 작성 규칙
category: wiki
tags:
- wiki
status: note
visibility: public
---

# 문서 작성 규칙

`docs/<주제>/` 아래 소문자 영문·하이픈 파일명으로 문서를 만듭니다. 한 문서는 한 곳에 두고 태그로 관련 주제를 연결합니다. 문서의 공개 범위와 출처를 확인한 뒤 추가합니다.

## 메타데이터

```yaml
---
title: Redis 캐싱 전략
category: databases
tags:
  - redis
  - caching
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
---
```

`category`는 첫 번째 주제 디렉터리이며 `tags`는 소문자 kebab-case 목록입니다. `status`는 `note`, `draft`, `review` 중 하나입니다. `note`는 모든 내용과 실행 결과가 검증되었다는 뜻이 아닙니다. 공개 문서는 `visibility: public`을 사용하며 검사는 이 표시를 요구합니다. 이 메타데이터는 접근 통제가 아니고 새 파일을 추가할 때 공개 여부를 명시하는 규칙입니다.

설명·예시·참고 출처를 쓰고 버전에 따라 달라지는 내용에는 `applies_to`, `reviewed_at`을 기록합니다. 문서 검토와 실제 실행 결과를 구분합니다. 실제 연락처·운영 주소·인증 정보 대신 `example.com`, `example.test`와 loopback을 사용합니다. 외부 이미지·도서 발췌·코드를 재배포할 때는 허가와 고지 조건을 확인합니다.

## 링크와 갱신

상대 경로의 `.md` 링크는 GitHub와 웹 위키에서 함께 사용할 수 있습니다. 새 글은 `templates/article.md`로 시작합니다. 사용 가능한 주제명은 `scripts/wiki.py`의 CATEGORIES에 정의돼 있으며 실제 문서가 있는 주제만 목차에 표시됩니다.

```bash
python scripts/wiki.py update
python scripts/wiki.py check
python -m mkdocs build --strict
```

`update`는 주제 목차·태그·문서 하단·웹 메뉴를 생성합니다. 생성 영역은 직접 수정하지 않습니다. `check`는 메타데이터·로컬 링크·자동 목록을 검사합니다.
