---
title: Docker 로그 확인
category: containers
tags:
- containers
- docker
- logging
- troubleshooting
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
---

Docker 컨테이너에서 로그를 확인
단일 컨테이너 로그 확인:
docker logs <컨테이너 ID>

실시간 로그 스트리밍:
docker logs -f <컨테이너 ID>

다중 컨테이너 로그 관리:
로깅 드라이버 사용. 예: json-file, syslog, fluentd.

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#containers](../../tags.md#containers) · [#docker](../../tags.md#docker) · [#logging](../../tags.md#logging) · [#troubleshooting](../../tags.md#troubleshooting)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
