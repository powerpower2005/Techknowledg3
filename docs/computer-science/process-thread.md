---
title: 프로세스와 스레드
category: computer-science
tags:
- computer-science
- process
- thread
status: note
reviewed_at: '2026-10-06'
applies_to: 프로세스·스레드 기초 및 Java 21 ThreadLocal
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# 프로세스
실행 중인 모든 프로그램은 필요한 정보를 기록할 수 있는 구조체를 가짐
즉, 실행 중인 프로그램을 프로세스라고 함
프로세스는 만들어질 때, OS에게 리소스를 받아 생성되고 OS에 의해 스케쥴링 되고 OS에 의해 소멸됨

프로세스가 가지는 리소스
- code : 컴파일된 명령어
- data : 전역 변수 등
- heap : C의 malloc 처럼 개발자가 임의로 메모리를 받아서 사용함
- stack : 함수의 실행시간 스택


다중 프로세스로 작업을 진행할 수 있음
-> 프로세스 생성 시, 오버헤드가 큼
-> 프로세스마다 *독립적인 메모리 주소 공간*을 갖고 있어서 프로세스 간 통신하기 복잡함


# 스레드
다중 프로세스는 복잡하기 때문에
프로세스 내에서 여러 스택(함수 흐름)을 갖게 하자.
-> 스레드 탄생
오히려 메모리 주소를 공유하기 떄문에 생기는 동기화 문제가 일어남

또한 스레드를 많이 만든다고 능사는 아니기 때문에
-> 스레드 풀을 활용해서 스레드 생성 오버헤드를 줄임
-> best practice는 application 마다 다름

일반적으로  성능테스트 도구로 WT, CT를 이용해서 CPU연산 시간을 평가함


## ** 스레드 전용 저장소
thread local storage
- 같은 변수 이름이나 키를 사용해도 저장된 값은 스레드별로 독립적이다. 다른 스레드의 값을 공유하는 영역이라는 뜻은 아니다.
- 모든 스레드가 동일한 변수에 접근하는 것처럼 보이지만, 사실 변수의 인스턴스는 각각의 스레드에 속함


# thread safe?
어떤 코드가 주어졌을 때, 몇개의 스레드가 호출하든 스레드들이 어떤 순서로 호출하든 상관없이 올바른 결과가 나온다면 thread safe한 것.

어떻게 해야 작성할 수 있는가?
즉, 스레드 전용 리소스를 언제 사용하고, 공유 리소스를 언제 사용하는지에 대한 것부터 파악 해야함


# 스레드 전용 리소스, 공유 리소스

함수의 지역 변수, 스레드 스택 영역, 스레드 전용 저장소 -> 스레드 전용 리소스

heap, data, code -> 공유 리소스

특히 구현 시, call by value가 아닌 call by reference 또는 전역 변수 등과 사용될 때, 복잡해짐

- 스레드 전용 저장소
- read-only
- atomic operation
- mutex, semaphore, spin lock 등 공유 리소스 제어



# 멀티 스레드의 문제

1.  공유 데이터에 대한 상호 배타적인 작업

2. 스레드간 동기화 문제


acquire-release semantics

대부분 lock을 걸고 공유 변수를 보호하면서 사용함

## 적용 범위와 확인

프로세스·스레드 기초 및 Java 21 ThreadLocal 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [ThreadLocal API](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ThreadLocal.html)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#computer-science](../tags.md#computer-science) · [#process](../tags.md#process) · [#thread](../tags.md#thread)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
