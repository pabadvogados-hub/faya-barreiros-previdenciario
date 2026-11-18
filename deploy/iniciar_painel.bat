@echo off
REM Sobe o painel das demandas externas de calculo na maquina do escritorio.
REM Painel: http://127.0.0.1:8765/painel   (usuario/senha em config\.env)
cd /d "%~dp0.."
if exist venv\Scripts\python.exe (
  venv\Scripts\python.exe automacoes\painel\servidor.py
) else (
  python automacoes\painel\servidor.py
)
pause
