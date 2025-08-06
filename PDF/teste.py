import csv

# --- Obtenção da lista de nomes ---
# Tenta ler os nomes de um arquivo chamado 'nomes_lista.txt'.
# Este arquivo deve conter um nome por linha.
# Você pode criar este arquivo copiando a lista de nomes que forneci anteriormente.

lista_bruta_nomes = []
nome_arquivo_lista = 'nomes_brasileiros_gerado.csv'

try:
    with open(nome_arquivo_lista, 'r', encoding='utf-8') as f:
        lista_bruta_nomes = [linha.strip() for linha in f if linha.strip()]
    if not lista_bruta_nomes:
        print(f"Aviso: O arquivo '{nome_arquivo_lista}' está vazio ou contém apenas linhas em branco.")
except FileNotFoundError:
    print(f"Aviso: Arquivo '{nome_arquivo_lista}' não encontrado.")

# Se a lista estiver vazia (arquivo não encontrado ou vazio), usa uma lista de exemplo.
if not lista_bruta_nomes:
    print("Usando uma lista de exemplo pequena pois a lista principal não foi carregada.")
    lista_bruta_nomes = ["Maria", "José", "Ana", "João", "Carlos", "Beatriz", "Pedro", "Sofia", "Lucas", "Laura"] # Exemplo

# Remove duplicatas e ordena (opcional, mas bom para consistência)
lista_nomes_unicos = sorted(list(set(lista_bruta_nomes)))

# Para este exemplo, vamos usar todos os nomes únicos encontrados.
# Se você precisar de EXATAMENTE 1000 nomes e sua lista for diferente,
# você pode adicionar lógica para truncar ou preencher a lista_nomes_unicos.
# Exemplo para truncar se for maior que 1000:
# if len(lista_nomes_unicos) > 1000:
#     lista_final_de_nomes = lista_nomes_unicos[:1000]
# else:
#     lista_final_de_nomes = lista_nomes_unicos
lista_final_de_nomes = lista_nomes_unicos
# --- Fim da obtenção da lista de nomes ---


# Define o nome da entidade (o primeiro valor na linha do CSV)
nome_da_entidade = "Nome" # Conforme sua especificação

# Cria a lista que representará a única linha no CSV
# O primeiro item é o nome da entidade, seguido por todos os nomes.
linha_para_csv = [nome_da_entidade] + lista_final_de_nomes

# Nome do arquivo CSV de saída
nome_arquivo_saida = 'nomes_entidade_formato.csv'

# Escreve para o arquivo CSV
with open(nome_arquivo_saida, 'w', newline='', encoding='utf-8') as arquivo_csv:
    csv_writer = csv.writer(arquivo_csv)
    # Escreve a única linha contendo a entidade e todos os nomes
    csv_writer.writerow(linha_para_csv)

print(f"A lista de nomes foi gravada no arquivo '{nome_arquivo_saida}'.")
print(f"O arquivo contém 1 linha e {len(linha_para_csv)} colunas.")
print(f"A primeira coluna contém '{nome_da_entidade}'.")
print(f"As {len(lista_final_de_nomes)} colunas seguintes contêm os nomes.")
print(f"Total de nomes processados: {len(lista_final_de_nomes)}.")