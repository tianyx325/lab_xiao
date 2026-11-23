# Lab local preview — clears Hugo asset cache so SCSS edits always apply.
# Usage (from repo or site/):
#   powershell -File site/scripts/dev.ps1
$ErrorActionPreference = "Stop"
$SiteRoot = Split-Path -Parent $PSScriptRoot
$RepoRoot = Split-Path -Parent $SiteRoot

$dart = Join-Path $RepoRoot "tools\dart-sass\dart-sass"
$goBin = Join-Path $RepoRoot "tools\go\bin"
$env:Path = "$dart;$goBin;" + $env:Path

Set-Location $SiteRoot

if (Test-Path "resources\_gen") {
  Remove-Item -Recurse -Force "resources\_gen"
  Write-Host "cleared resources/_gen"
}

Get-Process hugo -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
Start-Sleep -Seconds 1

Write-Host "Hugo owns CSS: assets/scss/main.scss -> template.scss -> lab/*"
Write-Host "Do NOT put lab styles in assets/css/custom.css"
hugo server -D -p 1314 --bind 127.0.0.1 -b http://127.0.0.1:1314/ --disableFastRender
