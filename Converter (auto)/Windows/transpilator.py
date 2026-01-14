import sys
import os

# MAPA DE CARACTERES SIMPLES
# Estes podem ser trocados diretamente dentro de uma linha STRING
SIMPLE_MAP = {
    # O que você quer (ABNT2) : O que digitar no US para sair isso
    '"': '~',     # Aspas duplas viram til (Shift + `)
    "'": '`',     # Aspas simples viram acento grave
    ':': '?',     # Dois pontos vira interrogação (Shift + /)
    ';': '/',     # Ponto e vírgula vira barra
    '\\': ']',    # Barra invertida vira fecha colchetes
    ']': '[',     # Fecha colchetes vira abre colchetes
    '[': '"',     # Abre colchetes vira aspas (Shift + ')
    '{': '}',     # Chaves... (lógica similar para shift)
    '}': '{',
    '<': '<',     # Geralmente mantém
    '>': '>',     # Geralmente mantém
    '=': '=', 
    '+': '+',
    '-': '-',
    '_': '_',
    '.': '.',
    ',': ',',
    '(': '(',
    ')': ')',
    '*': '*',
    # O ç é o ponto e vírgula do US
    'ç': ';',
    'Ç': ':',
}

def translate_string_content(text):
    """
    Processa o texto. Se encontrar caracteres 'impossíveis' (como / ou ?),
    quebra o texto e gera comandos de teclado para eles.
    """
    lines = []
    current_buffer = ""

    for char in text:
        # CASO 1: A Barra '/' (ABNT2: AltGr + Q)
        if char == '/':
            if current_buffer:
                lines.append(f"STRING {current_buffer}")
                current_buffer = ""
            lines.append("CONTROL ALT q") # Atalho universal para / no ABNT2
            
        # CASO 2: A Interrogação '?' (ABNT2: AltGr + W)
        elif char == '?':
            if current_buffer:
                lines.append(f"STRING {current_buffer}")
                current_buffer = ""
            lines.append("CONTROL ALT w") # Atalho universal para ? no ABNT2

        # CASO 3: Caracteres mapeáveis simples
        elif char in SIMPLE_MAP:
            current_buffer += SIMPLE_MAP[char]
            
        # CASO 4: Caracteres normais (a-z, 0-9)
        else:
            current_buffer += char

    # Despeja o que sobrou no buffer
    if current_buffer:
        lines.append(f"STRING {current_buffer}")

    return lines

def convert_file(input_path):
    if not os.path.exists(input_path):
        print(f"Erro: Arquivo '{input_path}' não encontrado.")
        return

    base, ext = os.path.splitext(input_path)
    output_path = f"{base}_ABNT2{ext}"

    try:
        with open(input_path, 'r', encoding='utf-8') as f_in:
            lines = f_in.readlines()

        final_output = []
        
        for line in lines:
            line = line.strip()
            if not line:
                final_output.append("")
                continue
                
            parts = line.split(' ', 1)
            cmd = parts[0].upper()

            if cmd == "STRING" and len(parts) > 1:
                # Chama a função inteligente que pode gerar múltiplas linhas
                translated_blocks = translate_string_content(parts[1])
                final_output.extend(translated_blocks)
            else:
                # Comandos que não são STRING (DELAY, GUI, ENTER) passam direto
                final_output.append(line)

        # Salva o arquivo
        with open(output_path, 'w', encoding='utf-8') as f_out:
            f_out.write('\n'.join(final_output))

        print(f"✅ Sucesso! Use este arquivo: {output_path}")

    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Como Usar:")
        print("Digite: python transpilator.py e em seguida o nome do arquivo que deve estar em .txt")
        print("Ex: python transpilator.py rickroll.txt ")
        print("Ou arraste o arquivo payload_original.txt para cá")
    else:
        convert_file(sys.argv[1])