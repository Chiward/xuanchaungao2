@echo off
chcp 65001 >nul
echo ========================================
echo Smart Draft Generator - Full Start
echo ========================================
echo.
echo This script will start backend and frontend
echo.
echo Backend: http://127.0.0.1:8000
echo Frontend: Electron Window
echo.
echo Press any key to continue...
pause >nul
echo.
echo ========================================
echo Starting Backend Service...
echo ========================================
start "Backend Service" cmd /k "cd /d "%~dp0backend" && python main.py"
echo.
echo Waiting for backend to start...
timeout /t 3 /nobreak >nul
echo.
echo ========================================
echo Starting Frontend Application...
echo ========================================
start "Frontend App" cmd /k "cd /d "%~dp0frontend" && npm run dev"
echo.
echo ========================================
echo Startup Complete!
echo ========================================
echo.
echo Backend running at: http://127.0.0.1:8000
echo Frontend will open in Electron window
echo.
echo Close this window will NOT stop services
echo Please close "Backend Service" and "Frontend App" windows to stop
echo.
pause
