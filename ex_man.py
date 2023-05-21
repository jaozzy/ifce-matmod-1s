# Importa as bibliotecas necessárias para o código

import shutil
import os
import random as r
import time as t
import pandas as pd


# Faz com que o programa execute 12 vezes seguidas, gerando 1 resultado
# para cada mês e cria uma lista chamada "results", que irá guardar
# as informações necessárias posteriormente

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
    'Detergente': 2.00,
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

def ct():
    sys = os.name
    if sys == 'nt':
        os.system('cls')
    else:
        os.system('clear')

p = int(input('número de iterações (x*12):     '))

for f in range(0, p+1):
    
    for i in range(1, 13):
        results = []

    # Determina se ouve lucro ou prejuízo na venda de um determinado 
    # produto no mês anterior e define a geração de um arquivo de texto
    # com as informações geradas

        class produto:
            codigos = ['#001', '#002', '#003', '#004', '#005',
                '#006', '#007', '#008', '#009', '#010',
                '#011', '#012', '#013', '#014', '#015',
                '#016', '#017', '#018', '#019', '#020']
            
            def __init__(self, nome, lista_qtd_compra):
                self.nome = nome
                self.lista_qtd_comp = lista_qtd_compra
                self.qtd_compra = r.choice(self.lista_qtd_comp)
                self.preco_compra = produtos_precos_compra[nome]
                self.preco_venda = produtos_precos_venda[nome]
            
            def sorteia_venda(self):
                for w in range(20):
                    codigo = self.codigos.pop(0)
                    self.qtd_venda = r.randint((self.qtd_compra//3), self.qtd_compra)
                    valor_venda = self.qtd_venda * self.preco_venda
                
                    if valor_venda < self.qtd_compra * self.preco_compra:
                        self.resultado = 'prejuízo'
                        percentual = ((valor_venda - self.preco_compra) / self.preco_compra) * 10

                    else:
                        self.resultado = 'lucro'
                        percentual = ((valor_venda - self.preco_compra) / self.preco_compra) * 10

                
                    return f".{codigo}. .{self.nome}. .{self.qtd_compra}. .{self.qtd_venda}. .{self.resultado}. .{percentual}."
            
    # Com base nas informações anteriores, determina a quantidade de  
    # garrafas de 2L de coca-cola que foi comprada pelo vendedor no mês 
    # e adiciona o resultado à lista "results"

        class coca(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Coca-Cola (2L)", lista_qtd_compra)
        
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200]
                else:
                    self.lista_qtd_compra = [150, 160, 170, 180]
                
                return resultado

            
        Coca = coca()
        resultado = Coca.sorteia_venda()

    # Com base nas informações anteriores, determina a quantidade de caixas de 2L de   
    # leite que foi comprada pelo vendedor no mês 
    # e adiciona o resultado à lista "results"

        class leite(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Leite (2L)", lista_qtd_compra)
                
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [160, 170, 180, 190, 200, 210, 220]
                else:
                    self.lista_qtd_compra = [140, 150, 160, 170, 180]
                
                return resultado

            
        Leite = leite()
        resultado = Leite.sorteia_venda()
        
    # Com base nas informações anteriores, determina a quantidade  
    # de pacotes de pães de fatia que foi comprada pelo vendedorno 
    # no mês e adiciona o resultado à lista "results"

        class pao(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Pão de Fatia", lista_qtd_compra)
                
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200]
                else:
                    self.lista_qtd_compra = [150, 160, 170, 180]
                
                return resultado
        
        Pao = pao()
        resultado = Pao.sorteia_venda()

        
    # Com base nas informações anteriores, determina a quantidade de garrafas de 
    # detergente que foi comprada pelo vendedor no mês 
    # e adiciona o resultado à lista "results"

        class detergente(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Detergente", lista_qtd_compra)
                
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [120, 125, 130, 135, 140, 145, 150]
                else:
                    self.lista_qtd_compra = [120, 125, 130, 135, 140]
                
                return resultado

            
        Detergente = detergente()
        resultado = Detergente.sorteia_venda()
        
    # Com base nas informações anteriores, determina a quantidade de 
    # pacotes de papel higiênico 
    # que foi comprada pelo vendedor no mês e adiciona o resultado à lista "results"

        class papel_higienico(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Papel Higiênico", lista_qtd_compra)
                
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [90, 100, 110, 120]
                else:
                    self.lista_qtd_compra = [90, 100, 110]
                
                return resultado

            
        Papel_higienico = papel_higienico()
        resultado = Papel_higienico.sorteia_venda()
        
    # Com base nas informações anteriores, determina a quantidade de 
    # pacotes de café que foi comprada pelo vendedor
    # no mês e adiciona o resultado à lista "results"

        class cafe(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Café", lista_qtd_compra)
                
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [170, 175, 180, 185, 190, 195, 200, 205, 210]
                else:
                    self.lista_qtd_compra = [150, 155, 160, 165, 170]
                
                return resultado

            
        Cafe = cafe()
        resultado = Cafe.sorteia_venda()
        
    # Com base nas informações anteriores, determina a quantidade de 
    # pacotes de miojo que foi comprada pelo vendedor
    # no mês e adiciona o resultado à lista "results"
        
        class miojo(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Miojo", lista_qtd_compra)
                
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [110, 115, 120, 125, 130, 135, 140]
                else:
                    self.lista_qtd_compra = [90, 95, 100, 105]
                
                return resultado

            
        Miojo = miojo()
        resultado = Miojo.sorteia_venda()
        
    # Com base nas informações anteriores, determina a quantidade de macarrão 
    # que foi comprada pelo vendedor
    # no mês e adiciona o resultado à lista "results"
        class macarrao(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Macarrão", lista_qtd_compra)
                
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [95, 100, 105, 110, 115, 120, 125]
                else:
                    self.lista_qtd_compra = [80, 85, 90, 95]
                
                return resultado

            
        Macarrao = macarrao()
        resultado = Macarrao.sorteia_venda()
        
    # Com base nas informações anteriores, determina a quantidade de 
    # peças de 1kg de carne que foi comprada pelo vendedor no mês 
    # e adiciona o resultado à lista "results"

        class carne(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Carne (Kg)", lista_qtd_compra)
                
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [30, 35, 40, 45, 50]
                else:
                    self.lista_qtd_compra = [20, 25, 30, 35, 40]
                
                return resultado

        Carne = carne()
        resultado = Carne.sorteia_venda()

        
    # Com base nas informações anteriores, determina a quantidade de 
    # peças de 1/2kg de frango que foi comprada pelo vendedor no mês 
    # e adiciona o resultado à lista "results"

        class frango(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Frango (Kg)", lista_qtd_compra)
                
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [15, 20, 25, 30, 45, 50]
                else:
                    self.lista_qtd_compra = [10, 15, 20, 25]
                
                return resultado
      
        Frango = frango()
        resultado = Frango.sorteia_venda()
        
    # Com base nas informações anteriores, determina a quantidade de pacotes de 1kg  
    # de farinha que foi comprada pelo vendedor no mês 
    # e adiciona o resultado à lista "results"

        class farinha(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Farinha", lista_qtd_compra)
                
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [90, 100, 110, 120]
                else:
                    self.lista_qtd_compra = [80, 90, 100, 110]
                
                return resultado
            
        Farinha = farinha()
        resultado = Farinha.sorteia_venda()
        
    # Com base nas informações anteriores, determina a quantidade de  
    # pacotes de 500g de queijo que foi comprada pelo vendedor no mês 
    # e adiciona o resultado à lista "results"

        class queijo(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Queijo (500g)", lista_qtd_compra)
        
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195]
                else:
                    self.lista_qtd_compra = [90, 95, 100, 105]
                
                return resultado

        Queijo = queijo()
        resultado = Queijo.sorteia_venda()
        
    # Com base nas informações anteriores, determina a quantidade de 
    # pacotes de 500g de presunto que foi comprada pelo vendedor no mês 
    # e adiciona o resultado à lista "results"

        class presunto(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Presunto (500g)", lista_qtd_compra)
                
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195]
                else:
                    self.lista_qtd_compra = [90, 95, 100, 105]
                
                return resultado

        Presunto = presunto()
        resultado = Presunto.sorteia_venda()  
        
    # Com base nas informações anteriores, determina a quantidade de 
    # pacotes de 1kg de arroz que foi comprada pelo vendedor no mês 
    # e adiciona o resultado à lista "results"

        class arroz(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Arroz (Kg)", lista_qtd_compra)
                
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [95, 100, 105, 110, 115, 120, 125]
                else:
                    self.lista_qtd_compra = [80, 85, 90, 95]
                
                return resultado
            
        Arroz = arroz()
        resultado = Arroz.sorteia_venda()
        
    # Com base nas informações anteriores, determina a quantidade de 
    # pacotes de 1kg de feijão que foi comprada pelo vendedor no mês 
    # e adiciona o resultado à lista "results"

        class feijao(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Feijão (Kg)", lista_qtd_compra)
                
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [90, 95, 100, 105, 110, 115, 120]
                else:
                    self.lista_qtd_compra = [75, 80, 85, 90]
                
                return resultado
            
        Feijao = feijao()
        resultado = Feijao.sorteia_venda()
        
    # Com base nas informações anteriores, determina a quantidade de 
    # barras de chocolate que foi comprada pelo vendedor no mês 
    # e adiciona o resultado à lista "results"

        class chocolate(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Chocolate (90g)", lista_qtd_compra)
                
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [45, 50, 55, 60]
                else:
                    self.lista_qtd_compra = [40, 45, 50, 55]
                
                return resultado
            
        Chocolate = chocolate()
        resultado = Chocolate.sorteia_venda()
        
    # Com base nas informações anteriores, determina a quantidade de 
    # pacotes de ruffles que foi comprada pelo vendedor no mês 
    # e adiciona o resultado à lista "results"

        class ruffles(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Ruffles (92g)", lista_qtd_compra)
                
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [40, 45, 50, 55]
                else:
                    self.lista_qtd_compra = [35, 40, 45, 50]
                
                return resultado
            
        Ruffles = ruffles()
        resultado = Ruffles.sorteia_venda()
        
    # Com base nas informações anteriores, determina a quantidade de  
    # embalagens com uma dúzia de ovos que foi comprada pelo vendedor no mês 
    # e adiciona o resultado à lista "results"

        class duzia_ovo(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Dúzia de Ovos", lista_qtd_compra)
                
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [175, 180, 185, 190, 195, 200, 205]
                else:
                    self.lista_qtd_compra = [160, 175, 180, 185]
                
                return resultado
                
        Duzia_ovo = duzia_ovo()
        resultado = Duzia_ovo.sorteia_venda()
        
    # Com base nas informações anteriores, determina a quantidade de  
    # garrafas de 2L de sabão líquido que foi comprada pelo vendedor no mês 
    # e adiciona o resultado à lista "results"

        class sabao_liquido(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Sabão Líquido (2L)", lista_qtd_compra)
                
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [80, 90, 100, 110, 120]
                else:
                    self.lista_qtd_compra = [90, 100, 110]
                
                return resultado
            
        Sabao_liquido = sabao_liquido()
        resultado = Sabao_liquido.sorteia_venda()
        
    # Com base nas informações anteriores, determina a quantidade de  
    # garrafas de água de 250ml que foi comprada pelo vendedor no mês 
    # e adiciona o resultado à lista "results"

        class agua(produto):
            def __init__(self):
                lista_qtd_compra = [140, 150, 160, 170, 180, 190, 200, 210, 220]
                super().__init__("Garrafa de Água (250ml)", lista_qtd_compra)
                
            def sorteia_venda(self):
                resultado = super().sorteia_venda()
                results.append(resultado)
                
                if self.resultado == 'lucro':
                    self.lista_qtd_compra = [140, 160, 170, 180, 190, 200, 210, 220, 240]
                else:
                    self.lista_qtd_compra = [150, 160, 170, 180, 190, 200]
                
                return resultado
            
        Agua = agua()
        resultado = Agua.sorteia_venda()
        
    # Dá uma pausa de 1 segundo no código

        t.sleep(1)

    # Junta todos os resultados de todos os produtos em um arquivo de texto 
    # que será gerado na mesma pasta em que o código foi executado, verificando 
    # se já há um arquivo com os resultados e, caso houver, cria um novo com outro
    # nome para facilitar a identificação do(s) arquivo(s)

        def save_results(results):
            filename = "resultados_{}.txt".format(i)
            with open(filename, "a") as f:
                for result in results:
                    f.write(str(result) + '\n')
                    
        save_results(results)

    # Converte os textos da pasta ./txt para formato de Dataframe. A linha 513 define o nome dos
    # arquivos como "resultados_{numero_mes}.txt". O loop for roda e, então, o valor do "numero_mes"
    # muda a cada execução do código. No if statement da linha 508, ele chega se os arquivos da
    # pasta ./txt existem. Se elas não existem, a função retorna um valor nulo. Caso contrário, ele
    # Lê cada arquivo da pasta, separa cada linha e cada dado do texto em uma array.

        def txt_to_dataframe():
            filename = "resultados_{}.txt".format(i)
            if not os.path.exists(filename):
                return None
            with open(filename, "r") as file:
                lines = file.readlines()
                dados = ".".join(lines)
                el = dados.split(".")
                data = []
        
    # Esse código é um loop que itera sobre um range de 1 a 19, usando a função enumerate()
    # para criar uma variável j que representa o índice da iteração atual.Dentro do loop,
    # o código define algumas variáveis com base no elemento el e em um valor x que é
    # atualizado em cada iteração. Essas variáveis são: "produto", "resultado" e "qtd_comp".
    # O código cria um objeto DataFrame do Pandas com as informações contidas na lista data,
    # usando a função pd.DataFrame(). O objeto resultante é armazenado na variável df e
    # possui três colunas com os nomes "PRODUTO", "RESULTADO" e "QTD. COMP.".

    # codigo 1 - produto 3 - qtd_comp 5 - qtd_vd 7 - resultado 9

                x = 0
                data = []
                for j, _ in enumerate(range(1, 21)):
                    codigo = el[1 + x].strip()
                    produto = el[3 + x].strip()
                    qtd_comp = el[5 + x].strip()
                    qtd_vd = el[7 + x].strip()
                    resultado = el[9 + x].strip()
                    percentual = float(el[11 + x].strip()) / 10000
                    data.append([codigo, produto, qtd_comp, qtd_vd, resultado, percentual])
                    df = pd.DataFrame(data, columns=["CÓDIGO", "PRODUTO", "QTD. COMP.", "QTD. VENDA", "RESULTADO", "L/P"])
                    df["L/P"] = df["L/P"].apply(lambda x: "{:.2%}".format(x))
                    x = x + 14
                return df



    # Define a array "meses".

        meses = ['Janeiro', 'Fevereiro', 'Março',
            'Abril', 'Maio', 'Junho',
            'Julho', 'Agosto', 'Setembro',
            'Outubro', 'Novembro', 'Dezembro']

    # Este código itera sobre uma lista de meses e cria arquivos Excel contendo dados de vendas para
    # cada mês. Ele também usa as funções save_results() e txt_to_dataframe() pra executar tarefas
    # adicionais durante o loop.

    count = 0
    for i, mes in enumerate(meses, start=1):
        count += 1
        print(f"Executando iteração {count}")
        save_results(results)
        df = txt_to_dataframe()
        if df is not None:
            nome_arquivo = f"Vendas {mes}.xlsx"
            with pd.ExcelWriter(nome_arquivo) as writer:
                df.to_excel(writer, index=False, sheet_name="Vendas")

    # A função cria uma pasta chamada "txt" no diretório atual 
    # (se ela ainda não existir), e move todos os arquivos de texto com 
    # extensão ".txt" encontrados no diretório atual para a
    # pasta "txt". Ele usa as bibliotecas "os" e "shutil" 
    # para isso, verificando se cada item encontrado no diretório atual
    # é um arquivo e se tem a extensão ".txt". Se essas condições
    # forem verdadeiras, o arquivo é movido para a pasta "txt".

        def txt_files():
            diretorio_atual = os.getcwd()
            pasta_txt = os.path.join(diretorio_atual, "txt")
            if not os.path.exists(pasta_txt):
                os.mkdir(pasta_txt)
            for nome_arquivo in os.listdir(diretorio_atual):
                caminho_arquivo = os.path.join(diretorio_atual, nome_arquivo)
            else:
                for nome_arquivo in os.listdir(diretorio_atual):
                    caminho_arquivo = os.path.join(diretorio_atual, nome_arquivo)
                    if os.path.isfile(caminho_arquivo) and nome_arquivo.endswith(".txt"):
                        #shutil.move(caminho_arquivo, pasta_txt)
                        os.remove(caminho_arquivo)

    # A função xlsx_files cria uma pasta chamada "planilhas" no diretório atual 
    # (se ela ainda não existir), # e move todos os arquivos Excel com 
    # extensão ".xlsx" encontrados no diretório atual para a
    # pasta "planilhas". Ele usa as bibliotecas os e shutil 
    # para isso, verificando se cada item encontrado no diretório atual
    # é um arquivo e se tem a extensão ".xlsx". Se essas condições
    # forem verdadeiras, o arquivo é movido para a pasta "planilhas".

        def xlsx_files():
            diretorio_atual = os.getcwd()
            pasta_planilhas = os.path.join(diretorio_atual, "ia_data")
            #pasta_planilhas = os.path.join(diretorio_atual, "planilhas")
            if not os.path.exists(pasta_planilhas):
                os.mkdir(pasta_planilhas)

            for nome_arquivo in os.listdir(diretorio_atual):
                caminho_arquivo = os.path.join(diretorio_atual, nome_arquivo)
                if os.path.isfile(caminho_arquivo) and nome_arquivo.endswith(".xlsx"):
                    novo_nome = nome_arquivo
                    count = 1

                    while novo_nome in os.listdir(pasta_planilhas):
                        nome, extensao = os.path.splitext(nome_arquivo)
                        novo_nome = f'{nome}_{count}{extensao}'
                        count += 1

                    shutil.move(caminho_arquivo, os.path.join(pasta_planilhas, novo_nome))
                    print(f'Arquivo de planilha "{nome_arquivo}" movido para a pasta "ia_data" e renomeado para "{novo_nome}".')
                #else:
                    #print(f'Arquivo "{nome_arquivo}" não é um arquivo .xlsx.')

    # Nessa etapa o código limpa o terminal, cria a pasta
    # "txt" e "planilhas" pra poderem ser armazenados os
    # arquivos de maneira organizada.

    ct()
    txt_files()
    xlsx_files()
