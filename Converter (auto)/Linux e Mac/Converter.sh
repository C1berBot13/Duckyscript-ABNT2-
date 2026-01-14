#!/bin/bash

# Verifica se foi passado um arquivo
if [ -z "$1" ]; then
    echo "❌ Erro: Por favor, arraste um arquivo de texto para cima deste script ou passe como argumento."
    echo "Uso: ./converter.sh seu_payload.txt"
    exit 1
fi

# Pega o caminho absoluto do script Python (assume que está na mesma pasta)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PYTHON_SCRIPT="$SCRIPT_DIR/transpilator.py"

# Executa
python3 "$PYTHON_SCRIPT" "$1"

echo ""
echo "Pressione ENTER para sair..."
read