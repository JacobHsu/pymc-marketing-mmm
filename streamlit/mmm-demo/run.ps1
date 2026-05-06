# 一鍵啟動 mmm-demo（在 repo 根目錄或 streamlit/mmm-demo 下執行皆可）

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

conda activate pymc-marketing-dev
streamlit run app.py
