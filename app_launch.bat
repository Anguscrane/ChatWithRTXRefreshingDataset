@echo off
setlocal enabledelayedexpansion
set "env_path_found="

for /f "tokens=1,* delims= " %%a in ('"%programdata%\MiniConda\Scripts\conda.exe" env list') do (
    set "env_name=%%a"
    set "env_path=%%b"
    if "!env_path!"=="" (
        set "env_path=!env_name!"
    )
    echo !env_path! | findstr /C:"env_nvd_rag" > nul
    if !errorlevel! equ 0 (
        set "env_path_found=!env_path!"
        goto :endfor
    )
)

:endfor
if not "%env_path_found%"=="" (
    echo Environment path found: %env_path_found%
    call "%programdata%\MiniConda\Scripts\activate.bat" %env_path_found%
    python verify_install.py
    python run.py
    pause
) else (
    echo Environment with 'env_nvd_rag' not found.
    pause
)

endlocal