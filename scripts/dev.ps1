# Start local Hugo preview server from the repository root.
$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

$hugo = $null
$hugoCmd = Get-Command hugo -ErrorAction SilentlyContinue
if ($hugoCmd) { $hugo = $hugoCmd.Source }

if (-not $hugo) {
    $fallback = "D:\Claude code\tools\hugo\hugo.exe"
    if (Test-Path $fallback) { $hugo = $fallback }
}

if (-not $hugo -or -not (Test-Path $hugo)) {
    Write-Host "Hugo not found" -ForegroundColor Red
    exit 1
}

$dartSass = "D:\Claude code\tools\dart-sass"
if (Test-Path $dartSass) {
    $env:PATH = "$dartSass;$env:PATH"
}

Write-Host "Starting site at http://127.0.0.1:1313/ ..." -ForegroundColor Green
& $hugo server -D --bind 127.0.0.1 --baseURL "http://127.0.0.1:1313/" --port 1313
