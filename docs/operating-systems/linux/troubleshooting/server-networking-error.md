---
title: Linux 서버 네트워크 장애 진단
category: operating-systems
tags:
- linux
- networking
- operating-systems
- troubleshooting
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# Layer1 
- ip link show
네트워크 인터페이스가 잘 작동하고 있는지 확인
인터페이스 비활성화 시, 활성화

Check Network inferace is running, if it doesn't work activate

비활성화된 인터페이스를 활성화
- ip link set <인터페이스 이름> up


드라이버/하드웨어 문제 확인
- dmesg | grep <인터페이스 이름>


# Layer2
MAC 주소 관련 ARP table 확인
check MAC address table

- ip neighbor show

- ip neighbor delete 
명령어를 통해 ARP를 지우고 다시 broadcasting 해서 ARP table에 등록하게 만듦
with Command, Delete ARP Table, ARP Protocol can broadcast to get mac address

- arp -e


ARP 테이블 초기화
- ip neighbor flush <인터페이스 이름>


# Layer3
자신의 local address 확인
check own local address

- ip address show
eth0 인터페이스에 확인 가능

- ping
다른 호스트에 ICMP echo 패킷을 보냄
실제로 패킷이 도달하는지 확인 가능함
ping test to other server

- traceroute
패킷이 전달되는 경로를 살펴봄
check packet hop path

- ip route show


-  DNS, /etc/resolv.conf , /etc/hosts, nslookup
네임서버 확인
check nameserver



# Layer 4



로컬에서 어떤 포트가 수신 대기하고 있는지 확인함 -> 수신하고 있지 않으니 연결이 성립되지 않는 것
check which port is listening,

use ss - netcat 

열려 있는 포트 확인:

- ss -tunlp4 (TCP/UDP 수신 포트, 특정 소켓을 사용하는 프로세스, IPv4  소켓) 
EX)

```
Netid State Recv-Q Send-Q Local Address:Port Peer Address:Port
udp UNCONN 0 0 *:68 *:* users:(("dhclient",pid=3167,fd=6))
udp UNCONN 0 0 127.0.0.1:323 *:* users:(("chronyd",pid=2821,fd=1))
tcp LISTEN 0 128 *:22 *:* users:(("sshd",pid=3366,fd=3))
tcp LISTEN 0 100 127.0.0.1:25 *:* users:(("master",pid=3600,fd=13))

```

sshd 애플리케이션은 출력에 표시된 모든 IP 주소에서 포트 22에서 수신

- telnet

telnet명령은 지정한 호스트 및 포트와 TCP 연결을 설정하려고 시도 (원격 연결에 대한 테스트)
telnet can try to connect specified host and port

연결되지 않는다면
애플리케이션이 수신 대기하지 않는 것일 수 있음
트래픽을 필터링하는 호스트 또는 중간 방화벽이 방해할 수도 있음
Layer 4를 확인하기 위해선 네트워크 관리자와 소통 필요

check firewall

방화벽 상태 확인
- iptables -L -n
- ufw status



# 추가 분석
추가 도구:
tcpdump, wireshark를 통해 트래픽 분석
journalctl -u <네트워크 서비스>: 서비스 관련 로그 확인.

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#linux](../../../tags.md#linux) · [#networking](../../../tags.md#networking) · [#operating-systems](../../../tags.md#operating-systems) · [#troubleshooting](../../../tags.md#troubleshooting)

[주제 목차](../../index.md) · [위키 홈](../../../index.md)

<!-- END WIKI NAV -->
