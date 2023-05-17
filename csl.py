import os

resultados = []
contagem = {}

def ct():
    sys = os.name
    if sys == 'nt':
        os.system('cls')
    else:
        os.system('clear')

count = 1
resumo_file = "resumo1.txt"
while os.path.exists(resumo_file):
    count += 1
    resumo_file = f"resumo{count}.txt"

for arquivo in os.listdir():
    if arquivo.startswith('resultado_') and arquivo.endswith('.txt'):
        with open(arquivo, 'r', encoding='utf-8', errors='ignore') as file:
            acuracia = file.readline().split(':')[-1].strip()
            porcentagem = float(acuracia) * 100
            resultados.append(f"{arquivo.split('_')[-1].split('.')[0]} = {porcentagem:.0f}% de precisão")

            contagem[porcentagem] = contagem.get(porcentagem, 0) + 1

with open(resumo_file, 'w', encoding='utf-8') as file:
    file.write("Contagem de precisão:\n")
    for porcentagem, count in sorted(contagem.items(), reverse=True):
        file.write(f"{porcentagem:.0f}% - {count}x\n")

    file.write('\n')

    file.write('\n'.join(resultados))

for arquivo in os.listdir():
    if arquivo.startswith('resultado_') and arquivo.endswith('.txt') and arquivo != resumo_file:
        os.remove(arquivo)

ct()
