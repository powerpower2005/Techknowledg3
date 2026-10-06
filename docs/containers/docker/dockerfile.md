---
title: Dockerfile과 ENTRYPOINT / CMD
category: containers
tags:
- containers
- docker
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
reviewed_at: '2026-10-06'
applies_to: Dockerfile exec form; 예제 애플리케이션은 별도 준비
content_origin: original-summary
---

# Dockerfile과 ENTRYPOINT / CMD

exec form의 `ENTRYPOINT`는 기본 실행 프로그램을 정하고 `CMD`는 기본 인수를 제공할 수 있다. `docker run`의 이미지 뒤 인수는 이 조합에서 CMD를 대체한다. ENTRYPOINT도 `--entrypoint`로 바꿀 수 있으므로 절대 변경할 수 없는 강제 설정은 아니다.

다음은 실행 동작을 보여주는 예다. `app.py` 파일을 준비해야 빌드할 수 있다. 베이스 이미지의 지원 버전과 digest는 사용 시 확인한다.

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY app.py /app/app.py
ENTRYPOINT ["python", "/app/app.py"]
CMD ["--port", "8080"]
```

기본 실행은 `python /app/app.py --port 8080`이고 `docker run example-app --debug`는 `python /app/app.py --debug`가 된다.

shell form은 셸을 거치며 인수·신호 전달 방식이 exec form과 다르다. 종료 신호를 애플리케이션이 받는지, 기본 인수와 재정의가 기대대로 동작하는지 확인한다.

## 참고 자료

- [Dockerfile ENTRYPOINT와 CMD](https://docs.docker.com/reference/dockerfile/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#containers](../../tags.md#containers) · [#docker](../../tags.md#docker)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
