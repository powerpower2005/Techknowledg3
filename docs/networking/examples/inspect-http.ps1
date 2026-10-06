param([string]$Url = 'http://127.0.0.1:8001/Techknowledg3/')
$ErrorActionPreference = 'Stop'
$targetUri = [uri]$Url
if ($targetUri.Scheme -notin @('http', 'https')) { throw 'HTTP(S) URL required' }
if ($targetUri.Host -notin @('localhost', '127.0.0.1', '::1')) {
    throw 'This learning script accepts loopback URLs only.'
}
$parsedAddress = $null
if ([System.Net.IPAddress]::TryParse($targetUri.Host, [ref]$parsedAddress)) {
    $selectedAddress = $parsedAddress.ToString()
} else {
    $selectedAddress = Resolve-DnsName -Name $targetUri.Host -Type A |
        Where-Object { $_.IPAddress } | Select-Object -First 1 -ExpandProperty IPAddress
    if (-not $selectedAddress) { throw 'No IPv4 address returned' }
}
$tcpResult = Test-NetConnection -ComputerName $selectedAddress -Port $targetUri.Port -WarningAction SilentlyContinue
if (-not $tcpResult.TcpTestSucceeded) { throw 'TCP connection failed' }
# Use the original URI so the HTTP Host/TLS server name remains correct.
$response = Invoke-WebRequest -Uri $targetUri -TimeoutSec 10 -UseBasicParsing
$responseText = if ($response.Content -is [byte[]]) {
    [Text.Encoding]::UTF8.GetString($response.Content)
} else {
    [string]$response.Content
}
[pscustomobject]@{
    SelectedAddress = $selectedAddress
    Port = $targetUri.Port
    StatusCode = [int]$response.StatusCode
    Preview = $responseText.Substring(0, [Math]::Min(500, $responseText.Length))
}
