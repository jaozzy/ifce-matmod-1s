import os

os.system('cls')

diretorio = os.getcwd()
extensoes = ['.txt', '.xlsx']

for arquivo in os.listdir(diretorio):
    nome, extensao = os.path.splitext(arquivo)
    if extensao in extensoes:
        os.remove(os.path.join(diretorio, arquivo))

os.system('cls')