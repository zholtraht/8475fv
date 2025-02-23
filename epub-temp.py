import os
import re

# Função para remover números sobrescritos/subscritos isolados
def remover_numeros_isolados(texto):
    # Expressão regular para encontrar caracteres sobrescritos e subscritos
    regex = re.compile(r'[\u00B2-\u00B3\u2070-\u2079\u2080-\u2089]')
    
    # Função para verificar se o caractere deve ser removido
    def verificar_caractere(match):
        caractere = match.group()
        posicao = match.start()
        
        # Verificar se o caractere é um número sobrescrito/subscrito
        if caractere in '¹²³⁰⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉':
            # Verificar o contexto do caractere
            anterior = texto[posicao - 1] if posicao > 0 else ''
            posterior = texto[posicao + 1] if posicao < len(texto) - 1 else ''
            
            # Caso 1: Manter se for um expoente de número (ex: 2², 4³)
            if anterior.isdigit():
                return caractere  # Manter
            
            # Caso 2: Manter se fizer parte de uma fórmula química (ex: H₂O, CO₂)
            if anterior.isalpha() and posterior.isalpha():
                return caractere  # Manter
            
            # Caso 3: Remover se estiver isolado ou não for parte de um expoente/fórmula
            return ''  # Remover
        
        return caractere  # Manter outros caracteres
    
    # Aplicar a função de verificação a todos os caracteres encontrados
    return regex.sub(verificar_caractere, texto)

# Perguntar ao usuário o nome do arquivo
nome_arquivo = input("Digite o nome do arquivo de texto (com extensão): ")

# Carregar o texto do arquivo especificado pelo usuário
with open(nome_arquivo, 'r', encoding='utf-8') as file:
    texto = file.read()

# Remover números sobrescritos/subscritos isolados
texto = remover_numeros_isolados(texto)

# Separar o texto em parágrafos (utilizando a linha vazia como separador)
paragrafos = texto.split('\n\n')

# Encapsular cada parágrafo com as tags <p></p> e adicionar uma linha vazia após cada parágrafo
html_paragrafos = ['<p>{}</p>\n'.format(paragrafo) for paragrafo in paragrafos]

# Juntar os parágrafos formatados em uma string única
html_texto = '\n'.join(html_paragrafos)

# Obter o nome do arquivo sem a extensão
nome_base = os.path.splitext(nome_arquivo)[0]

# Criar o nome do arquivo de saída
nome_arquivo_saida = f"{nome_base}.html"

# Salvar o texto HTML formatado em um novo arquivo
with open(nome_arquivo_saida, 'w', encoding='utf-8') as file:
    file.write(html_texto)

print(f"Texto convertido para HTML com sucesso! Arquivo salvo como {nome_arquivo_saida}")