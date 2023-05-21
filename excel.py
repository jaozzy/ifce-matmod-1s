import os
import pandas as pd

planilhas = []
Db = os.getcwd()
d = os.path.join(Db, "ia_data")

for i, arquivo in enumerate(os.listdir(d), start=1):
    if arquivo.endswith('.xlsx'):
        caminho_arquivo = os.path.join(d, arquivo)
        print(f"Lendo planilha {i}: {arquivo}")
        try:
            planilha = pd.read_excel(caminho_arquivo, engine='openpyxl', dtype={'CÓDIGO': str})
            planilhas.append(planilha)
        except Exception as e:
            print(f"Erro ao ler a planilha {i}: {e}")

dados_completos = pd.concat(planilhas, ignore_index=True)

dados_completos.to_excel('dados_completos.xlsx', index=False)
