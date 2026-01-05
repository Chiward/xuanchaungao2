@echo off
chcp 65001 >nul
echo ========================================
echo Smart Draft Generator - Frontend Start
echo ========================================
echo.
echo Starting frontend application...
echo Dev server: http://localhost:5173
echo.
echo Press Ctrl+C to stop application
echo ========================================
echo.

cd /d "%~dp0frontend"
npm run dev
