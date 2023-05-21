import pandas as pd
import os
import shutil
import colorama
from colorama import Fore, Style
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from itertools import cycle

check = ('✅')

colorama.init()

def ct():
    sys = os.name
    if sys == 'nt':
        os.system('cls')
    else:
        os.system('clear')

ct()

codigos_produtos = {
    '001': 'Coca-Cola (2L)',
    '002': 'Leite (2L)',
    '003': 'Pão de Fatia',
    '004': 'Detergente',
    '005': 'Papel Higiênico',
    '006': 'Café',
    '007': 'Miojo',
    '008': 'Macarrão',
    '009': 'Carne (Kg)',
    '010': 'Frango (Kg)',
    '011': 'Farinha',
    '012': 'Queijo (500g)',
    '013': 'Presunto (500g)',
    '014': 'Arroz (Kg)',
    '015': 'Feijão (Kg)',
    '016': 'Chocolate (90g)',
    '017': 'Ruffles (92g)',
    '018': 'Dúzia de Ovos',
    '019': 'Sabão Líquido (2L)',
    '020': 'Garrafa de Água (250ml)'
}

produtos_precos_compra = {
    'Coca-Cola (2L)': 7.50,
    'Leite (2L)': 3.00,
    'Pão de Fatia': 2.63,
    'Detergente': 1.50,
    'Papel Higiênico': 6.00,
    'Café': 1.88,
    'Miojo': 2.44,
    'Macarrão': 3.60,
    'Carne (Kg)': 37.50,
    'Frango (Kg)': 15.00,
    'Farinha': 4.50,
    'Queijo (500g)': 12.38,
    'Presunto (500g)': 9.38,
    'Arroz (Kg)': 6.00,
    'Feijão (Kg)': 6.00,
    'Chocolate (90g)': 4.31,
    'Ruffles (92g)': 3.68,
    'Dúzia de Ovos': 8.44,
    'Sabão Líquido (2L)': 22.43,
    'Garrafa de Água (250ml)': 1.88
}

produtos_precos_venda = {
    'Coca-Cola (2L)': 10.00,
    'Leite (2L)': 4.00,
    'Pão de Fatia': 3.50,
    'Papel Higiênico': 8.00,
    'Café': 2.50,
    'Miojo': 3.25,
    'Macarrão': 4.8,
    'Carne (Kg)': 50.00,
    'Frango (Kg)': 20.00,
    'Farinha': 6.00,
    'Queijo (500g)': 16.50,
    'Presunto (500g)': 12.50,
    'Arroz (Kg)': 8.00,
    'Feijão (Kg)': 8.50,
    'Chocolate (90g)': 5.75,
    'Ruffles (92g)': 4.90,
    'Dúzia de Ovos': 11.25,
    'Sabão Líquido (2L)': 29.90,
    'Garrafa de Água (250ml)': 2.50
}

print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"definindo diretório"{Style.RESET_ALL} {Fore.GREEN}inciando... ⏰{Style.RESET_ALL}')

Db = os.getcwd()

caminho_arquivo_original = os.path.join(Db, "dados_completos.xlsx")
caminho_arquivo_copia = os.path.join(Db, "dados_analise.xlsx")

# Copiar o arquivo para criar a cópia
shutil.copyfile(caminho_arquivo_original, caminho_arquivo_copia)

# Ler a planilha de análise
planilha = pd.read_excel(caminho_arquivo_copia)

print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"definindo diretório"{Style.RESET_ALL} {Fore.GREEN}concluído com sucesso! ✅\n' + Style.RESET_ALL)

codigo_iterator = cycle(['001', '002', '003', '004', '005', '006', '007', '008',
                         '009', '010', '011', '012', '013', '014', '015', '016',
                         '017', '018', '019', '020'])
planilha['CÓDIGO'] = [next(codigo_iterator) for _ in range(len(planilha))]

print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"leitura das planilhas"{Style.RESET_ALL} {Fore.GREEN}concluído com sucesso! ✅\n' + Style.RESET_ALL)

print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"separando os dados"{Style.RESET_ALL} {Fore.GREEN}inciando... ⏰' + Style.RESET_ALL)

X = planilha[['PRODUTO', 'QTD. COMP.']]
y = planilha['RESULTADO'].replace({'lucro': 1, 'prejuízo': 0})

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=40)

print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"separando os dados"{Style.RESET_ALL} {Fore.GREEN}concluído com sucesso! ✅\n' + Style.RESET_ALL)

print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"treinando o modelo"{Style.RESET_ALL} {Fore.GREEN}inciando... ⏰' + Style.RESET_ALL)

model = ExponentialSmoothing(  # tipo de algoritmo utilizado
    endog=y_train,
    trend='add',
    seasonal='add',
    seasonal_periods=4).fit()

y_pred = model.predict(start=len(y_train), end=len(y_train) + len(y_test) - 1)

y_pred = [round(value) for value in y_pred]

accuracy = accuracy_score(y_test, y_pred)

print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"treinando o modelo"{Style.RESET_ALL} {Fore.GREEN}concluído com sucesso! ✅\n' + Style.RESET_ALL)

print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"classificando"{Style.RESET_ALL} {Fore.GREEN}inciando... ⏰' + Style.RESET_ALL)

classificacoes = ['lucro', 'prejuízo']

for i in range(len(X_test)):
    if y_pred[i] == 1:
        classificacao = 'lucro'
    else:
        classificacao = 'prejuízo'

    planilha.at[X_test.index[i], 'RESULTADO'] = classificacao

print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"classificando"{Style.RESET_ALL} {Fore.GREEN}concluído com sucesso! ✅\n' + Style.RESET_ALL)

print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"atualizando planilha final"{Style.RESET_ALL} {Fore.GREEN}inciando... ⏰' + Style.RESET_ALL)

planilha_final = pd.read_excel(caminho_arquivo_original)
planilha_final = planilha_final.append(planilha)

print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"atualizando planilha final"{Style.RESET_ALL} {Fore.GREEN}concluído com sucesso! ✅\n' + Style.RESET_ALL)

print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"salvando planilha final"{Style.RESET_ALL} {Fore.GREEN}inciando... ⏰' + Style.RESET_ALL)

planilha_final.to_excel(caminho_arquivo_original, index=False)

print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"salvando planilha final"{Style.RESET_ALL} {Fore.GREEN}concluído com sucesso! ✅\n' + Style.RESET_ALL)

print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"análise completa"{Style.RESET_ALL} {Fore.GREEN}concluída com sucesso! ✅' + Style.RESET_ALL)

print("\n")

print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"execução do programa"{Style.RESET_ALL} {Fore.GREEN}concluída com sucesso! ✅' + Style.RESET_ALL)
