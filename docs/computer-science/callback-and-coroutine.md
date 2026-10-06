---
title: 콜백과 코루틴
category: computer-science
tags:
- async
- computer-science
- thread
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
reviewed_at: '2026-10-06'
applies_to: Python 3.12 asyncio 및 일반적인 콜백 개념
content_origin: original-summary
---

# 콜백과 코루틴

콜백은 다른 코드에 전달해 나중에 호출하도록 하는 함수다. 호출 시점과 실행 스레드는 라이브러리의 계약에 달려 있으며, 콜백이라는 이유만으로 새 스레드가 생기지는 않는다.

코루틴은 실행을 중단하고 상태를 유지한 채 재개할 수 있는 루틴이다. Python의 `asyncio`에서는 이벤트 루프가 여러 Task를 협력적으로 실행한다. `async def` 함수를 호출하면 코루틴 객체가 만들어지며, 실행하려면 await하거나 Task로 스케줄링해야 한다.

## 대기와 실행을 구분하기

- 동기·비동기는 결과를 어떤 방식으로 전달하고 기다리는지에 관한 구분이다.
- blocking·nonblocking은 호출이 완료되지 않았을 때 호출 스레드를 기다리게 하는지에 관한 구분이다.
- `await`가 항상 스레드를 바꾸거나 CPU 병렬 실행을 만든다는 뜻은 아니다.
- 이벤트 루프에서 일반 blocking I/O를 직접 호출하면 다른 Task의 진행도 막힌다. 적절한 비동기 API를 사용하거나 `asyncio.to_thread` 등으로 blocking 작업을 분리한다.

## 실습

[로컬 I/O 비교 실험](async-io-case-study.md)에서 같은 요청을 순차·스레드 풀·asyncio로 실행한다. 동시성 제한, timeout, 취소와 오류 처리를 함께 확인한다.

## 참고 자료

- [Python 3.12 코루틴과 Task](https://docs.python.org/3.12/library/asyncio-task.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#async](../tags.md#async) · [#computer-science](../tags.md#computer-science) · [#thread](../tags.md#thread)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
