# TD - Tree Decision


import pandas as pd
import os
import colorama
from colorama import Fore, Style
import time as t

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

check = ('✅')

colorama.init()

for i in range(1, 11):

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
        '020': 'Garrafa De Água (250ml)'
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

    d = os.path.join(Db, "ia_data")

    print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"definindo diretório"{Style.RESET_ALL} {Fore.GREEN}concluído com sucesso! ✅\n' + Style.RESET_ALL)

    print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"leitura das planilhas"{Style.RESET_ALL} {Fore.GREEN}inciando... ⏰' + Style.RESET_ALL)

    for arquivo in os.listdir(d):
        if arquivo.endswith('.xlsx') or arquivo.endswith('.xls'):
            caminho_arquivo = os.path.join(d, arquivo)
            planilha = pd.read_excel(caminho_arquivo)
            planilha['CÓDIGO'] = ['001', '002', '003', '004', '005', '006', '007', '008',
                                  '009', '010', '011', '012', '013', '014', '015', '016',
                                  '017', '018', '019', '020']

            print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"leitura das planilhas"{Style.RESET_ALL} {Fore.GREEN}concluído com sucesso! ✅\n' + Style.RESET_ALL)

            print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"separando os dados"{Style.RESET_ALL} {Fore.GREEN}inciando... ⏰' + Style.RESET_ALL)

            X = planilha[['CÓDIGO', 'QTD. COMP.']]
            y = planilha['RESULTADO'].map({'lucro': 1, 'prejuízo': 0})

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=80)

            print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"separando os dados"{Style.RESET_ALL} {Fore.GREEN}concluído com sucesso! ✅\n' + Style.RESET_ALL)

            print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"treinando ia"{Style.RESET_ALL} {Fore.GREEN}inciando... ⏰' + Style.RESET_ALL)

            clf = DecisionTreeClassifier(random_state=90)
            clf.fit(X_train, y_train)

            y_pred = clf.predict(X_test)

            accuracy = accuracy_score(y_test, y_pred)
            print(f"==========\nAcurácia: {accuracy}\n==========")

            print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"treinando ia"{Style.RESET_ALL} {Fore.GREEN}concluído com sucesso! ✅\n' + Style.RESET_ALL)

            print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"criando log"{Style.RESET_ALL} {Fore.GREEN}inciando... ⏰' + Style.RESET_ALL)

            output_file = f"resultado_{arquivo}.txt"

            with open(output_file, 'w') as log_file:
                log_file.write(f"Acurácia: {accuracy}\n")

            print(Fore.GREEN + f'DEBUG: Processo{Style.RESET_ALL} {Fore.BLUE}"criando log"{Style.RESET_ALL} {Fore.GREEN}concluído com sucesso! ✅\n' + Style.RESET_ALL)

    os.system('python csl.py')

os.system('python log_gen.py')
os.system('python move.py')