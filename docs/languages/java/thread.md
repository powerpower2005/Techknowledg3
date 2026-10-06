---
title: Java 가상 스레드와 플랫폼 스레드
category: languages
tags:
- java
- languages
status: note
reviewed_at: '2026-10-06'
applies_to: Java 21 가상 스레드 API; JDK 24 pinning 변경
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# Java 가상 스레드와 플랫폼 스레드

플랫폼 스레드는 OS 스레드와 연결되고 가상 스레드는 JVM이 carrier 플랫폼 스레드에 실행을 배치한다. 가상 스레드는 많은 blocking I/O 작업의 동시성을 다루는 데 유용하지만 CPU 연산 자체를 빠르게 만들지는 않는다.

## Java 21 예시

```java
try (var executor = java.util.concurrent.Executors.newVirtualThreadPerTaskExecutor()) {
    var result = executor.submit(() -> "completed");
    System.out.println(result.get());
}
```

이 코드는 완료와 executor 정리를 보여주는 최소 예시다. 실제 외부 요청에서는 timeout·취소와 downstream 동시 접속 한도를 별도로 정한다. 가상 스레드 수가 많아도 DB 연결 수와 외부 서비스 용량은 유한하다.

## ThreadLocal과 pinning

ThreadLocal 값은 스레드마다 독립적이며 모든 스레드가 같은 지역 값을 공유한다는 뜻이 아니다. 많은 가상 스레드에 큰 값을 넣으면 메모리 비용이 커질 수 있다. ThreadLocal이 있다는 사실만으로 pinning을 단정하지 않는다.

Java 21의 synchronized 내부 blocking은 pinning을 일으킬 수 있다. JDK 24는 JEP 491로 이 제한을 개선했으므로 버전을 구분한다. native 호출 등 다른 원인과 DB 대기를 측정 증거로 나누어 확인한다.

## 적용 범위와 확인

Java 21 가상 스레드 API; JDK 24 pinning 변경 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [Java 21 가상 스레드](https://docs.oracle.com/en/java/javase/21/core/virtual-threads.html)
- [ThreadLocal](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ThreadLocal.html)
- [JEP 491](https://openjdk.org/jeps/491)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#java](../../tags.md#java) · [#languages](../../tags.md#languages)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
