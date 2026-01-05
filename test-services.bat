@echo off
chcp 65001 >nul
echo ========================================
echo Testing Services
echo ========================================
echo.
echo Checking Backend Service...
curl -s http://127.0.0.1:8000/health
echo.
echo.
echo Checking Frontend Service...
curl -s http://localhost:5173 | findstr /C:"html" >nul
if %errorlevel% equ 0 (
    echo Frontend is running at http://localhost:5173
) else (
    echo Frontend is not responding
)
echo.
echo ========================================
echo Test Complete
echo ========================================
pause
