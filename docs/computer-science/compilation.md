---
title: 컴파일과 링킹
category: computer-science
tags:
- compiler
- computer-science
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
reviewed_at: '2026-10-06'
applies_to: GCC를 사용하는 일반적인 C 빌드 흐름
content_origin: original-summary
---

# 컴파일과 링킹

C 프로그램의 일반적인 빌드 흐름은 전처리 → 컴파일 → 어셈블 → 링크다. 컴파일러 내부에서는 구문·타입 등을 검사하고 중간 표현을 최적화할 수 있다. 구체적인 단계와 출력 형식은 언어와 도구에 따라 다르다.

| GCC 옵션 | 이 예제에서 만드는 결과 |
| --- | --- |
| `gcc -E hello.c` | 전처리 결과를 표준 출력에 표시 |
| `gcc -S hello.c` | 어셈블리 파일 |
| `gcc -c hello.c` | 오브젝트 파일 |
| `gcc hello.o -o hello` | 링크한 실행 파일 |

링커는 외부 심볼을 해석하고 섹션을 배치하며 재배치 정보를 처리한다. 이것이 실행 시의 물리 메모리 주소를 미리 고정한다는 뜻은 아니다. 로더와 가상 메모리, 동적 링크 및 ASLR도 실행 주소에 관여한다.

## 라이브러리

정적 링크는 필요한 라이브러리 코드를 실행 파일에 포함한다. 정적 아카이브의 모든 내용이 무조건 복사되는 것은 아니다. 동적 링크는 공유 라이브러리에 대한 참조를 남기고 로드 시점 또는 이후에 연결한다. 크기, 업데이트 방식, 배포 의존성과 시작 비용을 비교하며 한 방식이 언제나 더 빠르다고 일반화하지 않는다.

## 참고 자료

- [GCC 빌드 단계 옵션](https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html)
- [GCC 링크 옵션](https://gcc.gnu.org/onlinedocs/gcc/Link-Options.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#compiler](../tags.md#compiler) · [#computer-science](../tags.md#computer-science)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
