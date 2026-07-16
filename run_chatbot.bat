@echo off
chcp 65001 >nul
title Rule-Based AI Chatbot

echo ================================================
echo    Rule-Based AI Chatbot - Launching...
echo ================================================
echo.

C:\Users\Shaheer\.local\bin\python3.11.exe "%~dp0main.py"

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ================================================
    echo  ERROR: Chatbot crashed. See message above.
    echo ------------------------------------------------
    echo  If you see "No module named customtkinter":
    echo  Run this command:
    echo.
    echo  C:\Users\Shaheer\.local\bin\python3.11.exe -m pip install --break-system-packages customtkinter
    echo ================================================
    pause
)
