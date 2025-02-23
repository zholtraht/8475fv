import os

# Perguntar ao usuário o nome do arquivo
nome_arquivo = input("Digite o nome do arquivo de texto (com extensão): ")

# Carregar o texto do arquivo especificado pelo usuário
with open(nome_arquivo, 'r', encoding='utf-8') as file:
    texto = file.read()

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
