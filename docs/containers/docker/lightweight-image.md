---
title: 경량 컨테이너 이미지
category: containers
tags:
- containers
- docker
- performance
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
reviewed_at: '2026-10-06'
applies_to: Docker multi-stage build 개념; 실행 의존성은 애플리케이션별 확인
content_origin: original-summary
---

# 경량 컨테이너 이미지

multi-stage build로 빌드 도구가 있는 단계와 실행에 필요한 파일만 담는 단계를 나눈다. 최종 단계에 무엇을 복사했는지가 실제 이미지 내용에 영향을 준다.

## 줄일 항목

- `.dockerignore`로 불필요한 build context를 제외한다.
- 최종 단계에 소스 전체와 빌드 캐시를 복사하지 않는다.
- 런타임 라이브러리, CA 인증서와 사용자·권한 설정은 필요한 만큼 포함한다.
- 패키지 설치와 임시 파일 정리를 같은 RUN에서 처리하면 이전 레이어에 불필요한 파일이 남는 일을 줄일 수 있다.
- 비밀을 COPY하거나 ARG로 넣지 않고 해당 빌드 도구의 secret 기능을 사용한다.

작은 베이스 이미지가 모든 애플리케이션에 적합한 것은 아니다. 예를 들어 libc 차이 또는 동적 링크 의존성 때문에 빌드된 바이너리가 실행되지 않을 수 있다. 크기 외에도 지원 버전, 보안 업데이트, 실행·디버깅 요건을 확인한다.

캐시 활용은 빌드 시간을 줄이는 방법이며 이미지 크기 감소와 같은 지표는 아니다. 최종 파일·레이어·실행 결과를 각각 검사한다.

## 참고 자료

- [Docker multi-stage build](https://docs.docker.com/build/building/multi-stage/)
- [Docker 빌드 권장 사항](https://docs.docker.com/build/building/best-practices/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#containers](../../tags.md#containers) · [#docker](../../tags.md#docker) · [#performance](../../tags.md#performance)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
