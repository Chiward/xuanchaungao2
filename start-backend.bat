@echo off
chcp 65001 >nul
echo ========================================
echo Smart Draft Generator - Backend Start
echo ========================================
echo.
echo Starting backend service...
echo Service address: http://127.0.0.1:8000
echo.
echo Press Ctrl+C to stop service
echo ========================================
echo.

cd /d "%~dp0backend"
python main.py
