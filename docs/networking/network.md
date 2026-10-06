---
title: 네트워크 개요
category: networking
tags:
- dns
- http
- networking
- tls
status: note
reviewed_at: '2026-10-06'
applies_to: 일반 네트워크 개념, TCP와 TLS 1.3; API별 timeout 정의는 별도 확인
content_origin: original-summary
visibility: public
publication_reviewed_at: '2026-10-06'
---

# 네트워크 개요

## 웹 요청의 흐름

`https://www.example.com/` 요청을 처음 보내는 일반적인 흐름은 DNS 확인 → 연결 설정 → TLS 인증과 키 협상 → HTTP 요청·응답 → 브라우저 렌더링이다. DNS·연결 캐시와 재사용이 있으면 일부 단계가 생략된다. HTTP/1.1과 HTTP/2는 보통 TCP를 사용하며 HTTP/3는 QUIC를 사용하므로 모든 HTTP를 TCP handshake 하나로 설명하지 않는다.

HTTPS의 기본 포트는 443이다. TLS는 서버 이름과 공개키를 연결하는 인증서의 서명·신뢰 체인 등을 검증하고 세션 키를 협상한다. TLS 1.3에서 인증서의 RSA 키가 있다고 RSA key exchange를 사용하는 것은 아니다.

## TCP와 UDP

TCP는 연결과 순서 있는 바이트 스트림, 재전송, 흐름·혼잡 제어를 제공한다. UDP는 데이터그램 인터페이스이며 TCP와 같은 연결 설정과 전달 보장을 제공하지 않는다. UDP 위에 신뢰성 기능을 구현하는 상위 프로토콜도 있다. DNS 등 개별 서비스가 사용하는 전송 방식은 해당 프로토콜을 확인한다.

## 주소와 라우팅

IPv4 주소는 32비트, IPv6 주소는 128비트다. CIDR은 주소의 prefix 길이를 나타낸다. IPv4의 ARP는 같은 링크에서 다음 홉의 IP에 대응하는 링크 계층 주소를 찾는 데 사용한다. 다른 서브넷의 목적지에 보낼 때는 일반적으로 게이트웨이의 링크 주소가 필요하다. IPv6는 Neighbor Discovery를 사용한다.

공인 주소가 있다는 사실만으로 외부에서 접근 가능해지는 것은 아니다. 라우팅, 방화벽과 수신 애플리케이션 설정도 필요하다. 사설 주소와 NAT는 주소 운영 방식이며 인증이나 접근 통제를 대신하지 않는다.

## 시간과 성능

connect timeout과 read timeout 등의 의미는 클라이언트 API마다 확인한다. DNS, 연결, TLS, 서버 처리, 응답 읽기 시간을 나눠 관찰한다. 대역폭은 용량, 처리량은 실제 달성한 전송량, 지연은 완료까지 걸린 시간이다. 패킷 손실과 tail 지연도 함께 본다.

L4 부하 분산은 보통 IP·포트와 전송 연결을 기준으로, L7 부하 분산은 HTTP 경로나 헤더 같은 애플리케이션 정보를 기준으로 처리한다. 구현과 설정을 확인하며 성능의 우열을 계층 이름만으로 단정하지 않는다.

## 이어 읽기

[DNS 조회 과정](dns-process.md) · [리버스 프록시](reverse-proxy.md)

## 참고 자료

- [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)
- [TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446)
- [HTTP/3](https://www.rfc-editor.org/rfc/rfc9114)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#dns](../tags.md#dns) · [#http](../tags.md#http) · [#networking](../tags.md#networking) · [#tls](../tags.md#tls)

[주제 목차](index.md) · [위키 홈](../index.md)

<!-- END WIKI NAV -->
