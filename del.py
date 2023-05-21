import os

os.system('cls')

diretorio = os.getcwd()
d2 = os.path.join(diretorio, "planilhas")
d3 = os.path.join(diretorio, "txt")
extensoes = ['.txt', '.xlsx']

for arquivo in os.listdir(diretorio):
    nome, extensao = os.path.splitext(arquivo)
    if extensao in extensoes:
        os.remove(os.path.join(diretorio, arquivo))

for arquivo in os.listdir(d2):
    nome, extensao = os.path.splitext(arquivo)
    if extensao in extensoes:
        os.remove(os.path.join(d2, arquivo))
        
for arquivo in os.listdir(d3):
    nome, extensao = os.path.splitext(arquivo)
    if extensao in extensoes:
        os.remove(os.path.join(d3, arquivo))

os.system('cls')
