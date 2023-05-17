import os

def ct():
    sys = os.name
    
    if sys == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def read_resumo_file(resumo_file):
    lines = []
    
    with open(resumo_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()[1:4]

    return lines

resumo_files = [f"resumo{i}.txt" for i in range(1, 11)]
log_file = "log.txt"

with open(log_file, 'w', encoding='utf-8') as file:
    for resumo_file in resumo_files:
        if os.path.exists(resumo_file):
            lines = read_resumo_file(resumo_file)

            file.write(f"{resumo_file} {{\n")
            file.writelines(lines)
            file.write("}\n\n")

for resumo_file in resumo_files + ["resumo.txt"]:
    if os.path.exists(resumo_file):
        os.remove(resumo_file)

ct()