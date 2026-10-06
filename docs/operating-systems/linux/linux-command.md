---
title: Linux 명령어
category: operating-systems
tags:
- linux
- operating-systems
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
reviewed_at: '2026-10-06'
applies_to: 일반적인 GNU 명령과 Bash; 다른 구현의 옵션은 별도 확인
content_origin: original-summary
---

# Linux 명령어

다음은 일반 파일 `sample.txt`를 읽는 예다. 세부 옵션은 설치된 도구의 도움말에서 확인한다.

```bash
wc -l sample.txt       # 줄바꿈 문자 개수
wc -w sample.txt       # 단어 개수
wc -c sample.txt       # 바이트 개수
wc -m sample.txt       # 문자 개수
head -n 5 sample.txt   # 앞의 다섯 줄
cut -f 2 sample.txt    # 탭으로 구분된 두 번째 필드
grep -n 'error' sample.txt
sort sample.txt | uniq -c
find . -type f -name 'abc.*'
```

`uniq`는 인접한 같은 행을 묶으므로 전체 중복을 묶으려면 정렬이 필요한 경우가 많다. 정렬 순서는 locale의 영향을 받을 수 있다. `ls` 출력을 줄 수로 세는 방식은 숨김 파일이나 개행을 포함한 파일명 때문에 정확한 파일 개수 계산에 적합하지 않다.

## 파이프와 리다이렉션

`|`는 한 명령의 표준 출력을 다음 명령의 표준 입력으로 전달한다. `>`는 파일을 덮어쓰고 `>>`는 뒤에 추가한다. `<`는 파일을 표준 입력으로 읽는다. 파이프와 파일 리다이렉션을 구분한다.

셸의 작은따옴표와 큰따옴표는 변수 확장 규칙이 다르다. 파일 경로는 공백을 포함할 수 있으므로 인수를 적절히 인용한다. `type`으로 명령이 실행 파일, alias 또는 셸 함수인지 확인할 수 있다.

## 참고 자료

- [GNU Coreutils](https://www.gnu.org/software/coreutils/manual/coreutils.html)
- [GNU Bash](https://www.gnu.org/software/bash/manual/bash.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#linux](../../tags.md#linux) · [#operating-systems](../../tags.md#operating-systems)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
