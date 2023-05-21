import os
import shutil as s

def ct():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def move_log():
    
    ct()

    diretorio = os.getcwd()
    pasta_logs = os.path.join(diretorio, 'logs')
    arquivo_origem = 'log.txt'
    arquivo_destino = os.path.join(pasta_logs, arquivo_origem)

    def obter_novo_nome_arquivo():
        count = 1
        while True:
            novo_nome = f'log_{count}.txt'
            if novo_nome in os.listdir(pasta_logs):
                count += 1
            else:
                return novo_nome

    if arquivo_origem in os.listdir(diretorio):
        if arquivo_origem in os.listdir(pasta_logs):
            novo_nome = obter_novo_nome_arquivo()
            s.move(arquivo_origem, os.path.join(pasta_logs, novo_nome))
            print(f'Arquivo de log "{arquivo_origem}" movido para a pasta "logs" e renomeado para "{novo_nome}".')
        else:
            s.move(arquivo_origem, arquivo_destino)
            print(f'Arquivo de log "{arquivo_origem}" movido para a pasta "logs".')

def move_xlsx():
    ct()

    diretorio = os.getcwd()
    pasta_planilhas = os.path.join(diretorio, './planilhas/')
    for i in ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]:
        arquivo_origem = 'Vendas ' + str(i) + '.xlsx'
        if(os.path.exists(arquivo_origem)):
            for j in range(0, 12):
                arquivo_origem = 'Vendas ' + str(i) + str(j) + '.xlsx'

    arquivo_destino = os.path.join(arquivo_origem, pasta_planilhas)

    def obter_novo_nome_arquivo():
        count = 1
        while True:
            novo_nome = f'log_{count}.txt'
            if novo_nome in os.listdir(pasta_planilhas):
                count += 1
            else:
                return novo_nome

    if arquivo_origem in os.listdir(diretorio):
        if arquivo_origem in os.listdir(pasta_planilhas):
            novo_nome = obter_novo_nome_arquivo()
            s.move(arquivo_origem, os.path.join(pasta_planilhas, novo_nome))
            print(f'Arquivo de log "{arquivo_origem}" movido para a pasta "logs" e renomeado para "{novo_nome}".')
        else:
            s.move(arquivo_origem, arquivo_destino)
            print(f'Arquivo de log "{arquivo_origem}" movido para a pasta "logs".')

ct()
move_log()
