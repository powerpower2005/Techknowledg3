---
title: CS 면접 질문과 학습 순서
category: interview
tags:
- interview
- computer-science
status: note
visibility: public
publication_reviewed_at: '2026-10-07'
---

# CS 면접 질문과 학습 순서

기본 개념을 질문으로 확인하고, 관련 지식 문서에서 원리와 예시를 찾아 자신의 답변을 만드는 시작 페이지입니다. 아래 질문은 학습용이며 특정 기업의 실제 기출 문제를 뜻하지 않습니다.

## 공부하는 순서

1. 운영체제와 메모리: 프로그램이 실행되고 자원을 공유하는 방법을 이해합니다.
2. 네트워크: 요청이 서버에 도착하고 응답이 돌아오는 과정을 설명합니다.
3. 데이터베이스: 데이터 모델, 인덱스와 분산 시스템의 조건을 비교합니다.
4. 보안과 시스템 설계: 인증, 캐시, 가용성과 운영 비용을 연결합니다.

질문마다 **정의 → 동작 원리 → 구체적인 예시 → 한계와 대안** 순서로 설명해 보세요. 읽은 내용을 외우는 데서 끝내지 않고 작은 실습과 관찰 결과를 답변에 추가합니다.

## 운영체제와 컴퓨터 과학

| 질문 | 답변에 포함할 내용 | 관련 지식 |
| --- | --- | --- |
| 프로세스와 스레드는 어떻게 다른가? | 주소 공간, 공유 자원, 독립적인 실행 흐름과 동기화 | [프로세스와 스레드](../computer-science/process-thread.md) |
| 동시성과 병렬성은 어떻게 다른가? | 작업 진행의 겹침, 동시에 실행되는 작업, I/O와 CPU 작업의 예 | [비동기 I/O 사례](../computer-science/async-io-case-study.md) |
| 비동기와 논블로킹은 같은 말인가? | 호출의 반환 조건과 완료 통지 방식을 나누어 설명 | [비동기 I/O 사례](../computer-science/async-io-case-study.md) |
| 포인터와 메모리 주소를 어떻게 설명할 것인가? | 값과 주소의 구분, 유효 기간과 잘못된 접근 | [메모리와 포인터](../computer-science/memory-and-pointers.md) |
| 컴파일과 링킹은 각각 무엇을 하는가? | 소스 변환, 심볼과 라이브러리 연결, 정적·동적 링킹 | [컴파일과 링킹](../computer-science/compilation.md) |
| 코루틴은 스레드와 어떤 관계가 있는가? | 중단·재개, 스케줄링과 실행 스레드의 관계 | [콜백과 코루틴](../computer-science/callback-and-coroutine.md) |

## 네트워크

| 질문 | 답변에 포함할 내용 | 관련 지식 |
| --- | --- | --- |
| 웹 주소를 입력하면 어떤 일이 일어나는가? | DNS, 연결, TLS, HTTP 요청과 응답, 캐시 조건 | [DNS와 HTTP 요청 관찰](../networking/dns-process.md) |
| TCP와 UDP는 어떤 기준으로 선택하는가? | 전송 보장, 순서, 지연과 애플리케이션의 요구 | [네트워크 개요](../networking/network.md) |
| 리버스 프록시를 왜 사용하는가? | 요청 전달, 부하 분산, TLS 종료와 장애 지점 | [리버스 프록시와 HAProxy](../networking/reverse-proxy.md) |
| CORS는 어떤 문제를 다루는가? | Origin, 브라우저의 응답 접근, preflight와 서버 인증의 역할 | [CORS](../security/cors/cors.md) |

## 데이터베이스

| 질문 | 답변에 포함할 내용 | 관련 지식 |
| --- | --- | --- |
| SQL과 NoSQL은 어떻게 선택하는가? | 데이터 모델, 질의, 제약과 일관성 요구 | [SQL과 NoSQL 비교](../databases/sql.md) |
| 인덱스는 왜 조회를 빠르게 하고 언제 비용이 되는가? | 탐색, 선택도, 쓰기와 저장 공간, 실행 계획 | [인덱스와 실행 계획](../databases/index-tuning.md) |
| CAP 정리는 어떤 상황의 선택을 설명하는가? | 네트워크 분할 시 일관성과 가용성, PACELC와의 연결 | [CAP와 PACELC](../databases/cap-theorem.md) |
| 캐시를 도입하면 어떤 문제가 추가되는가? | 적중률, 만료, 무효화, 장애와 원본 저장소 부하 | [Redis 활용 패턴](../databases/redis/redis-usecase.md) |

## 보안과 시스템 설계

| 질문 | 답변에 포함할 내용 | 관련 지식 |
| --- | --- | --- |
| 세션과 JWT 기반 인증은 무엇이 다른가? | 상태 저장, 검증, 만료·취소와 토큰 보관 | [세션과 인증 토큰](../security/session-token/session-token.md) |
| TLS 인증서는 어떤 역할을 하는가? | 인증서 체인, 호스트 이름, 서명과 신뢰 | [X.509 인증서](../security/x509-certificates.md) |
| 컨테이너와 가상머신은 어떻게 다른가? | 격리 경계, 커널 공유, 이미지와 자원 비용 | [Docker 개요](../containers/docker/docker.md) · [가상화](../computer-science/virtualization.md) |
| CDN은 언제 효과적이고 무엇을 주의해야 하는가? | 캐시 키, TTL, 무효화와 원본 부하 | [CloudFront와 CDN](../cloud/aws/cloudfront.md) |
| 서비스가 느려졌다면 어디부터 확인하는가? | 영향 범위, 지표, 가설, 병목과 검증 | [성능과 장애 진단](../devops/troubleshooting.md) |
| 서비스의 신뢰성을 어떤 지표로 설명하는가? | 사용자 관점의 SLI, SLO와 오류 예산 | [SRE](../devops/sre/sre.md) |

## 질문을 계속 모으기

질문별 답변은 `docs/interview/`에 문서를 추가해 정리합니다. 질문의 핵심 개념을 자세히 다루는 글은 운영체제·네트워크·데이터베이스 같은 주제에 저장하고 답변에서 연결하세요. 작성 방법은 [문서 작성 규칙](../guides/contributing.md)을 참고합니다.

아직 별도 문서가 없는 자료구조·알고리즘, 트랜잭션 격리 수준, 교착 상태 등도 질문과 지식을 함께 추가해 확장할 수 있습니다.

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#interview](../tags.md#interview) · [#computer-science](../tags.md#computer-science)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
