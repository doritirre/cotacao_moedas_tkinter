# cotacao_moedas_tkinter
Projeto de cotação de moedas no python usando a Lib tkinter

import locale
from msilib.schema import ComboBox
import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
from tkcalendar import DateEntry
from tkinter.filedialog import askopenfilename
import pandas as pd
import requests
from datetime import datetime
import numpy as np

requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')
dict_moedas = requisicao.json()
print(requisicao)
dicionario_moedas = requisicao.json()

lista_moedas = list(dicionario_moedas.keys())

lista_moedas = list(dict_moedas.keys())

def pegar_cotacao():
    moeda = comboBox_seleciona_moeda.get()
    data_cotacao = cal_moeda.get()
    moeda = combobox_selecionarmoeda.get()
    data_cotacao = calendario_moeda.get()
    ano = data_cotacao[-4:]
    mes = data_cotacao[3:5]
    dia = data_cotacao[:2]
    link = f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}"
    requisicao_moeda = requests.get(link)
    cotacao = requisicao_moeda.json()
    valor_moeda = cotacao[0]['bid']
    label_texto_cotacao['text'] = f"A cotação da {moeda} no dia {data_cotacao} foi de {valor_moeda}"
    
    
    label_textocotacao['text'] = f"A cotação da {moeda} no dia {data_cotacao} foi de: R${valor_moeda}"


def selecionar_arquivo():
    pass
    caminho_arquivo = askopenfilename(title="Selecione o Arquivo de Moeda")
    var_caminhoarquivo.set(caminho_arquivo)
    if caminho_arquivo:
        label_arquivoselecionado['text'] = f"Arquivo Selecionado: {caminho_arquivo}"


def atualizar_cotacoes():
    pass
    try:
        # ler o dataframe de moedas
        df = pd.read_excel(var_caminhoarquivo.get())
        moedas = df.iloc[:, 0]
        # pegar a data de inicio e data de fim das cotacoes
        data_inicial = calendario_datainicial.get()
        data_final = calendario_datafinal.get()
        ano_inicial = data_inicial[-4:]
        mes_inicial = data_inicial[3:5]
        dia_inicial = data_inicial[:2]

        ano_final = data_final[-4:]
        mes_final = data_final[3:5]
        dia_final = data_final[:2]

        for moeda in moedas:
            link = f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?" \
                   f"start_date={ano_inicial}{mes_inicial}{dia_inicial}&" \
                   f"end_date={ano_final}{mes_final}{dia_final}"

            requisicao_moeda = requests.get(link)
            cotacoes = requisicao_moeda.json()
            for cotacao in cotacoes:
                timestamp = int(cotacao['timestamp'])
                bid = float(cotacao['bid'])
                data = datetime.fromtimestamp(timestamp)
                data = data.strftime('%d/%m/%Y')
                if data not in df:
                    df[data] = np.nan

                df.loc[df.iloc[:, 0] == moeda, data] = bid
        df.to_excel("Teste.xlsx")
        label_atualizarcotacoes['text'] = "Arquivo Atualizado com Sucesso"
    except:
        label_atualizarcotacoes['text'] = "Selecione um arquivo Excel no Formato Correto"



janela = tk.Tk()

janela.title("Ferramenta de Cotação de Moedas")

label_cotacao_moedas = tk.Label(text="Cotação de 1 moeda específica", borderwidth=2, relief='solid')
label_cotacao_moedas.grid(row=0, column=0, padx=10, pady=10, sticky='NSEW', columnspan=3) 
janela.title('Ferramenta de Cotação de Moedas')

label_selecionar_moedas = tk.Label(text="Selecionar Moeda", anchor='e')
label_selecionar_moedas.grid(row=1, column=0, padx=10, pady=10, sticky='NSEW', columnspan=2)
label_cotacaomoeda = tk.Label(text="Cotação de 1 moeda específica", borderwidth=2, relief='solid')
label_cotacaomoeda.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

comboBox_seleciona_moeda = ttk.Combobox(values=lista_moedas)
comboBox_seleciona_moeda.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')
label_selecionarmoeda = tk.Label(text="Selecionar Moeda", anchor='e')
label_selecionarmoeda.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

label_selecionar_dia = tk.Label(text="Selecionar o dia que deseja pegar a cotação", anchor='e')
label_selecionar_dia.grid(row=2, column=0, padx=10, pady=10, sticky='NSEW', columnspan=2)
combobox_selecionarmoeda = ttk.Combobox(values=lista_moedas)
combobox_selecionarmoeda.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')

cal_moeda = DateEntry(year=2022, locale='pt_br')
cal_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')
label_selecionardia = tk.Label(text="Selecione o dia que deseja pegar a cotação", anchor='e')
label_selecionardia.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

label_texto_cotacao = tk.Label(text="")
label_texto_cotacao.grid(row=3, column=0, padx=10, pady=10, sticky='nswe')
calendario_moeda = DateEntry(year=2021, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')

btn_pegar_cotacao = ttk.Button(text="Pegar Cotação", command=pegar_cotacao)
btn_pegar_cotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')
label_textocotacao = tk.Label(text="")
label_textocotacao.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

# Cotação de várias moedas   ####################################################################################
botao_pegarcotacao = tk.Button(text="Pegar Cotação", command=pegar_cotacao)
botao_pegarcotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')

label_cotacao_varias_moedas = tk.Label(text="Cotação de Multiplas Moedas", borderwidth=2, relief='solid')
label_cotacao_varias_moedas.grid(row=4, column=0, padx=10, pady=10, sticky='NSEW', columnspan=3) 

label_selecionar_arquivo = tk.Label(text="Selecionar um arquivo em Excel com as moedas na Coluna", anchor='e')
label_selecionar_arquivo.grid(row=5, column=0, padx=10, pady=10, sticky='NSEW', columnspan=2)
# cotação de várias moedas

btn_selecionar_arquivo = ttk.Button(text="Clique para selecionar", command=selecionar_arquivo)
btn_selecionar_arquivo.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')
label_cotacavariasmoedas = tk.Label(text="Cotação de Múltiplas Moedas", borderwidth=2, relief='solid')
label_cotacavariasmoedas.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_arquivo_selecionado = tk.Label(text="Nenhum Arquivo Selecionado", anchor='e')
label_arquivo_selecionado.grid(row=6, column=0, padx=10, pady=10, sticky='NSEW', columnspan=3)
label_selecionararquivo = tk.Label(text='Selecione um arquivo em Excel com as Moedas na Coluna A')
label_selecionararquivo.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

label_data_inicial = tk.Label(text="Data Inicial", anchor='e')
label_data_inicial.grid(row=7, column=0, padx=10, pady=10, sticky='NSEW')
var_caminhoarquivo = tk.StringVar()

cal_data_ini = DateEntry(year=2022, locale='pt_br')
cal_data_ini.grid(row=7, column=1, padx=10, pady=10, sticky='nswe')
botao_selecionararquivo = tk.Button(text="Clique para Selecionar", command=selecionar_arquivo)
botao_selecionararquivo.grid(row=5, column=2, padx=10, pady=10, sticky='nsew')

label_data_final = tk.Label(text="Data Final", anchor='e')
label_data_final.grid(row=8, column=0, padx=10, pady=10, sticky='NSEW')
label_arquivoselecionado = tk.Label(text='Nenhum Arquivo Selecionado', anchor='e')
label_arquivoselecionado.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

cal_data_fim = DateEntry(year=2022, locale='pt_br')
cal_data_fim.grid(row=8, column=1, padx=10, pady=10, sticky='nswe')
label_datainicial = tk.Label(text="Data Inicial", anchor='e')
label_datafinal = tk.Label(text="Data Final", anchor='e')
label_datainicial.grid(row=7, column=0, padx=10, pady=10, sticky='nsew')
label_datafinal.grid(row=8, column=0, padx=10, pady=10, sticky='nsew')

btn_atualizar_cotacoes = ttk.Button(text="Atualizar Cotações", command=atualizar_cotacoes)
btn_atualizar_cotacoes.grid(row=9, column=0, padx=10, pady=10, sticky='nswe')
calendario_datainicial = DateEntry(year=2021, locale='pt_br')
calendario_datafinal = DateEntry(year=2021, locale='pt_br')
calendario_datainicial.grid(row=7, column=1, padx=10, pady=10,  sticky='nsew')
calendario_datafinal.grid(row=8, column=1, padx=10, pady=10, sticky='nsew')

label_atualizar_cotacoes = tk.Label(text="")
label_atualizar_cotacoes.grid(row=9, column=1, padx=10, pady=10, sticky='nswe', columnspan=2)
botao_atualizarcotacoes = tk.Button(text='Atualizar Cotações', command=atualizar_cotacoes)
botao_atualizarcotacoes.grid(row=9, column=0, padx=10, pady=10, sticky='nsew')

btn_fechar = ttk.Button(text="Fechar", command=janela.quit)
btn_fechar.grid(row=10, column=2, padx=10, pady=10, sticky='nswe')
label_atualizarcotacoes = tk.Label(text="")
label_atualizarcotacoes.grid(row=9, column=1, columnspan=2, padx=10, pady=10, sticky='nsew')

botao_fechar = tk.Button(text='Fechar', command=janela.quit)
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky='nsew')

janela.mainloop()
