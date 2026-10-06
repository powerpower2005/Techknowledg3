---
title: 메모리와 포인터
category: computer-science
tags:
- computer-science
- memory
status: note
reviewed_at: '2026-10-06'
applies_to: C11 공개 초안의 배열·포인터·scanf; 표준 C 배열 layout
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# 메모리와 포인터

## 값과 주소

```c
int arr[] = {10, 20, 30};
int i = 1;
// arr[i] == *(arr + i) == 20
// *arr + i == 10 + 1 == 11
```

포인터에 정수를 더하면 가리키는 타입 크기에 맞춰 이동한다. 배열의 범위 밖을 역참조하거나 해제한 객체를 접근하면 정의되지 않은 동작이 될 수 있다. `arr`이 대부분의 식에서 첫 원소 포인터로 변환된다고 해서 배열 타입과 포인터 타입이 같은 것은 아니다.

```c
#include <stdio.h>
int main(void) {
    int a;
    if (scanf("%d", &a) != 1) return 1;
    printf("%d\n", a);
    return 0;
}
```

`scanf("%d", a)`처럼 정수 값을 주소 자리에 넘기는 것은 올바르지 않다. 입력 성공 여부를 검사하기 전 초기화되지 않은 값을 사용하지 않는다.

## 배열 순회와 캐시

C의 다차원 배열은 행 우선으로 저장되므로 `matrix[row][col]`의 마지막 인덱스인 col을 내부 루프에서 바꾸면 인접 원소를 순회한다. “열을 먼저 바꾸는 내부 루프”와 “열 우선 저장”을 혼동하지 않는다. 다른 언어·라이브러리의 배열 layout은 다를 수 있으며 실제 성능은 데이터 크기와 접근 패턴으로 측정한다.

스택·힙은 흔한 구현 구분이다. C 언어의 객체 수명과 저장 기간을 설명할 때 모든 지역 변수가 반드시 특정 물리 스택 주소에 있다고 단정하지 않는다.

## 적용 범위와 확인

C11 공개 초안의 배열·포인터·scanf; 표준 C 배열 layout 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [C11 공개 초안 §6.5.2.1, §6.5.6](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf)
- [C11 공개 초안 §6.5.2.1](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#computer-science](../tags.md#computer-science) · [#memory](../tags.md#memory)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
