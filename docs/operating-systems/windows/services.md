---
title: Windows 서비스 진단
category: operating-systems
tags:
- operating-systems
- windows
status: note
reviewed_at: '2026-10-06'
applies_to: Windows의 PowerShell 서비스 조회; 기능·권한은 Windows 버전 의존
content_origin: rewritten-learning-note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# Windows 서비스 진단

Windows 서비스는 Service Control Manager가 관리하는 백그라운드 실행 단위다. 실행 계정, 시작 유형, 의존성, 복구 정책과 서비스가 사용하는 자원을 함께 확인한다.

## 조회 예시

```powershell
Get-Service -Name Spooler | Select-Object Name, Status, StartType
Get-Service -Name Spooler -RequiredServices
Get-WinEvent -FilterHashtable @{
    LogName = 'System'
    ProviderName = 'Service Control Manager'
    StartTime = (Get-Date).AddHours(-1)
} -MaxEvents 20
```

Spooler는 조회 대상 예시다. 설치된 서비스와 로그 접근 권한에 따라 결과가 다르며 관련 이벤트가 없을 수도 있다. 이벤트 메시지의 경로나 계정 정보를 외부에 그대로 공유하지 않는다.

## 실패를 구분하기

시작 실패는 실행 파일 경로·계정 권한·의존 서비스·포트 충돌과 앱 로그를 확인한다. 서비스 Running은 앱 요청 성공을 보장하지 않는다. 정상 endpoint와 관련 자원을 함께 확인한다.

New-Service는 임의의 CLI 프로그램을 서비스 프로토콜에 맞는 프로그램으로 바꾸지 않는다. 서비스 생성·계정 변경·재시작은 운영 변경이며 조회 단계 뒤에 영향과 복구 절차를 정한다.

## 적용 범위와 확인

Windows의 PowerShell 서비스 조회; 기능·권한은 Windows 버전 의존 기준으로 설명했습니다. 기술 내용의 문서 검토일은 2026-10-06입니다. 예제를 실제 제품 환경에서 실행했다는 뜻은 아닙니다.

## 참고 자료

- [Get-Service](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-service?view=powershell-7.5)
- [Get-WinEvent](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent?view=powershell-7.5)
- [New-Service](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/new-service?view=powershell-7)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#operating-systems](../../tags.md#operating-systems) · [#windows](../../tags.md#windows)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
