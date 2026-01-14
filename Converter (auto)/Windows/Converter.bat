@echo off
:: Verifica se o usuário arrastou um arquivo
if "%~1"=="" (
    echo [ERRO] Por favor, arraste um arquivo de texto para cima deste icone.
    echo.
    pause
    exit /b
)

:: Executa o script Python passando o arquivo arrastado (%1) como argumento
python transpilator.py "%~1"

:: Pausa para o usuário ver o resultado (Sucesso ou Erro)
echo.
pause