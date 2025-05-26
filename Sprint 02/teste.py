import pandas as pd

# Nome do arquivo Excel de entrada e do arquivo de saída
arquivo_xlsx = "relatorio.xlsx"  # Substitua pelo nome correto do seu arquivo
arquivo_saida = "dados_convertidos.txt"

# Carregar o arquivo Excel, garantindo que todas as colunas sejam tratadas como strings
df = pd.read_excel(arquivo_xlsx, dtype=str, header=0)

# Remover espaços extras dos nomes das colunas
df.columns = df.columns.str.strip()

# Exibir os nomes das colunas carregadas para depuração
print("Colunas encontradas no arquivo Excel:", df.columns)

# Verificar se todas as colunas obrigatórias estão presentes
colunas_esperadas = [
    "Codigo_UOrg", "Codigo_UG", "Nome", "Sigla", "Endereco", "CEP", "Pais", "Telefone",
    "CPF_Responsavel", "Nome_Responsavel", "SIAPE_Responsavel", "Portaria",
    "Nome_Reduzido", "Data_Criacao", "Estado", "Municipio", "Email",
    "Codigo_Siorg", "Almoxarifado"
]

for coluna in colunas_esperadas:
    if coluna not in df.columns:
        raise ValueError(f"Erro: A coluna obrigatória '{coluna}' não foi encontrada no arquivo Excel.")

# Criar o cabeçalho do arquivo
header = "H¥UO¥1¥25000¥170531¥84480343172¥£"

# Criar as linhas de detalhe convertendo cada linha do DataFrame
linhas = []
for _, row in df.iterrows():
    linha = f"D¥{row['Codigo_UOrg']}¥{row['Codigo_UG']}¥{row['Nome']}¥{row['Sigla']}¥{row['Endereco']}¥{row['CEP']}¥{row['Pais']}¥{row['Telefone']}¥{row['CPF_Responsavel']}¥{row['Nome_Responsavel']}¥{row['SIAPE_Responsavel']}¥{row['Portaria']}¥{row['Nome_Reduzido']}¥{row['Data_Criacao']}¥{row['Estado']}¥{row['Municipio']}¥{row['Email']}¥{row['Codigo_Siorg']}¥{row['Almoxarifado']}¥£"
    linhas.append(linha)

# Criar o trailer (rodapé) do arquivo, informando a quantidade de registros
trailer = f"T¥12042017104732¥{len(df)}¥FIM¥£"

# Escrever o arquivo final no formato correto
with open(arquivo_saida, "w", encoding="utf-8") as f:
    f.write(header + "\n")  # Escreve o cabeçalho
    f.write("\n".join(linhas) + "\n")  # Escreve os dados formatados
    f.write(trailer + "\n")  # Escreve o trailer

print(f"Arquivo convertido e salvo como {arquivo_saida}")
