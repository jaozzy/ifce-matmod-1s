# SES - Suavização Exponencial Simples

import pandas as pd
import os
import colorama
from colorama import Fore, Style
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

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
    '001': 'Coca-Cola 2L',
    '002': 'Leite',
    '003': 'Pão',
    '004': 'Detergente',
    '005': 'Papel Higiênico',
    '006': 'Café',
    '007': 'Miojo',
    '008': 'Macarrão',
    '009': 'Carne',
    '010': 'Frango',
    '011': 'Farinha',
    '012': 'Queijo',
    '013': 'Presunto',
    '014': 'Arroz',
    '015': 'Feijão',
    '016': 'Chocolate',
    '017': 'Ruffles',
    '018': 'Dúzia de Ovos',
    '019': 'Sabão Líquido 2L',
    '020': 'Garrafa De Água 250ml',
}

print (Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"definindo diretório"{Style.RESET_ALL} {Fore.GREEN}inciando... ⏰{Style.RESET_ALL}')

Db  = os.getcwd()

d = os.path.join(Db, "planilhas")

print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"definindo diretório"{Style.RESET_ALL} {Fore.GREEN}concluído com sucesso! ✅\n' + Style.RESET_ALL)

print (Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"leitura das planilhas"{Style.RESET_ALL} {Fore.GREEN}inciando... ⏰' + Style.RESET_ALL)

for arquivo in os.listdir(d):
    if arquivo.endswith('.xlsx') or arquivo.endswith('.xls'):
        caminho_arquivo = os.path.join(d, arquivo)
        planilha = pd.read_excel(caminho_arquivo)
        planilha['CÓDIGO'] = ['001', '002', '003', '004', '005', '006', '007', '008',
                              '009', '010', '011', '012', '013', '014', '015', '016',
                              '017', '018', '019', '020']

        print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"leitura das planilhas"{Style.RESET_ALL} {Fore.GREEN}concluído com sucesso! ✅\n' + Style.RESET_ALL)

        print (Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"separando os dados"{Style.RESET_ALL} {Fore.GREEN}inciando... ⏰' + Style.RESET_ALL)
        
        X = planilha[['CÓDIGO', 'QTD. COMP.']]
        y = planilha['RESULTADO'].map({'lucro': 1, 'prejuízo': 0})

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"separando os dados"{Style.RESET_ALL} {Fore.GREEN}concluído com sucesso! ✅\n' + Style.RESET_ALL)

        print (Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"treinando ia"{Style.RESET_ALL} {Fore.GREEN}inciando... ⏰' + Style.RESET_ALL)
        
        model = SimpleExpSmoothing(y_train)
        model_fit = model.fit()

        y_pred = model_fit.forecast(len(y_test))

        accuracy = accuracy_score(y_test, y_pred.round())
        print(f"==========\nAcurácia: {accuracy}\n==========")
        
        print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"treinando ia"{Style.RESET_ALL} {Fore.GREEN}concluído com sucesso! ✅\n' + Style.RESET_ALL)
        
        print (Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"criando log"{Style.RESET_ALL} {Fore.GREEN}inciando... ⏰' + Style.RESET_ALL)
        
        output_file = f"resultado_{arquivo}.txt"
        
        with open(output_file, 'w') as log_file:
            log_file.write(f"Acurácia: {accuracy}\n")

        print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"criando log"{Style.RESET_ALL} {Fore.GREEN}concluído com sucesso! ✅\n' + Style.RESET_ALL)

