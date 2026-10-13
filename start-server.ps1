# Start local Hugo preview server
$ErrorActionPreference = "Stop"

$tools = "D:\Claude code\tools"
$hugo = Join-Path $tools "hugo\hugo.exe"
$goBin = Join-Path $tools "go\bin"

if (-not (Test-Path $hugo)) {
    Write-Host "Hugo not found: $hugo" -ForegroundColor Red
    exit 1
}

$env:PATH = "$goBin;$($tools)\hugo;$env:PATH"
$env:GOROOT = Join-Path $tools "go"
$env:GOPROXY = "https://goproxy.cn,direct"

Set-Location $PSScriptRoot
Write-Host "Starting site at http://127.0.0.1:1313/ ..." -ForegroundColor Green
& $hugo server -D --bind 127.0.0.1 --baseURL "http://127.0.0.1:1313/" --port 1313
