---
title: Docker 개요
category: containers
tags:
- containers
- docker
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
reviewed_at: '2026-10-06'
applies_to: Linux 컨테이너 중심의 일반 Docker 개념
content_origin: original-summary
---

# Docker 개요

Docker Engine은 CLI·API·daemon을 통해 이미지, 컨테이너, 네트워크와 볼륨을 관리한다. 이미지는 실행에 필요한 파일과 메타데이터를 담으며 컨테이너는 이미지에서 생성된 실행 인스턴스다. 이미지 태그는 변경될 수 있으므로 재현 가능한 배포에서는 digest도 확인한다.

일반적인 Linux 컨테이너는 호스트 커널을 공유하고 namespace로 리소스의 보이는 범위를 나누며 cgroup으로 사용량 등을 관리한다. 별도 게스트 커널을 사용하는 VM과 구분한다. 커널 공유에 따른 보안 경계와 호스트 호환성을 고려한다.

## 기본 흐름

Dockerfile 작성 → 이미지 빌드 → registry에 저장 → 이미지를 선택해 컨테이너 실행 순서로 진행한다. `docker build`의 마지막 경로는 build context이며 Dockerfile 위치를 별도로 지정하려면 `-f`를 사용한다.

컨테이너의 쓰기 계층과 볼륨의 수명을 구분한다. 애플리케이션 데이터가 필요한 경우 컨테이너 재생성 시에도 사용할 저장소와 백업 방식을 정한다. 볼륨을 쓴다는 사실만으로 백업이 생기는 것은 아니다.

## 관찰과 오케스트레이션

`docker stats`로 리소스 사용량을, `docker logs`로 지원되는 로그를 확인한다. 다중 컨테이너 애플리케이션에는 Compose를 사용할 수 있다. Kubernetes는 클러스터의 원하는 상태와 배치 등을 관리하는 오케스트레이션 시스템이다.

[Dockerfile](dockerfile.md) · [이미지 경량화](lightweight-image.md) · [로그 확인](troubleshooting.md)

## 참고 자료

- [Docker Engine](https://docs.docker.com/engine/)
- [Docker 개념](https://docs.docker.com/get-started/docker-concepts/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#containers](../../tags.md#containers) · [#docker](../../tags.md#docker)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
