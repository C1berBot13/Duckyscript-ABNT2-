# DuckyScript ABNT2 Converter

> **Transforme seus payloads DuckyScript (US) para funcionarem perfeitamente em teclados brasileiros (ABNT2).**

Se você já tentou plugar um BadUSB (Lilygo T-Dongle S3, Rubber Ducky, Flipper Zero, ESP32) em um computador no Brasil, conhece o pesadelo: você programa `echo "teste" > log.txt` e sai algo bizarro como `echo ~teste~ . log.txt`.

Isso acontece porque o firmware desses dispositivos "pensa" em Layout US, mas o Windows configurado em ABNT2 interpreta os sinais de forma diferente.

Este script Python resolve isso automaticamente.

## O que ele faz?

Ele não apenas troca caracteres simples. Ele é **inteligente**:

1.  **Tradução Direta:** Converte caracteres que mudaram de lugar (ex: `"` vira `~`, `;` vira `/`).
2.  **Injeção de Atalhos:** O ABNT2 não tem teclas dedicadas para `/` ou `?` na camada primária (elas precisam do AltGr). O script detecta isso e insere automaticamente os comandos `CONTROL ALT q` (para `/`) e `CONTROL ALT w` (para `?`).
3.  **Preservação de Comandos:** Mantém `DELAY`, `GUI`, `ENTER` e outros comandos DuckyScript intactos.

## Como Usar

### Pré-requisitos
* Python 3 instalado.

### Passo a Passo

1.  **Escreva seu Payload:**
    Crie seu arquivo `.txt` ou `.ds` normalmente, como se estivesse usando um teclado americano. Escreva o que você quer que apareça na tela.
    * *Exemplo (`payload.txt`):* `STRING https://www.youtube.com/watch?v=dQw4w9WgXcQ`

2.  **Rode o Conversor:**
    Abra o terminal na pasta do projeto e execute:
    ```bash
    python transpilator.py payload.txt
    ```
    *(Dica: Você também pode arrastar o arquivo de texto para cima do script Python se estiver no Windows/Mac).*

3.  **Pegue o Resultado:**
    O script vai gerar um novo arquivo com o sufixo `_ABNT2` (ex: `payload_ABNT2.txt`).

4.  **Deploy:**
    Copie esse arquivo novo para o seu cartão SD e já estará pronto para uso em seu RubberDucky ou em seu hardware que use os payloads duckyscript
    como o projeto "bad usb army knife" que roda em um lilygo t dongle s3.

## Exemplo Prático

**Entrada (O que você escreve):**
```duckyscript
GUI r
DELAY 500
STRING [https://google.com](https://google.com)
ENTER
```
**Saída (O que o script gera para o ABNT2 entender):**
```
GUI r
DELAY 500
STRING https
CONTROL ALT w  <-- Atalho para fazer o ':'
CONTROL ALT q  <-- Atalho para fazer a '/'
CONTROL ALT q  <-- Atalho para fazer a '/'
STRING google.com
ENTER
```
## Como Usar (Modo Fácil)

### No Windows
Incluímos um script de automação para facilitar sua vida.

1. Escreva seu payload DuckyScript normalmente em um arquivo `.txt` ou `.ds` (considere que está digitando num teclado americano).
2. **Arraste e solte** o seu arquivo de texto para cima do arquivo `converter.bat`.
3. Pronto! Um novo arquivo com o final `_ABNT2.txt` será criado na mesma pasta.

### No Linux ou Mac

1. Dê permissão de execução ao script (apenas na primeira vez):
   ```bash
   chmod +x converter.sh
   ```
2. Execute passando o arquivo:
    ```bash
    ./converter.sh meu_payload.txt
    ```
3. Se preferir fazer manualmente:
    ```bash
    python transpilator.py payload.txt
