import locale
from msilib.schema import ComboBox
import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
from tkcalendar import DateEntry
import requests

requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')
dict_moedas = requisicao.json()
print(requisicao)

lista_moedas = list(dict_moedas.keys())

def pegar_cotacao():
    pass

def selecionar_arquivo():
    pass

def atualizar_cotacoes():
    pass


janela = tk.Tk()

janela.title("Ferramenta de Cotação de Moedas")

label_cotacao_moedas = tk.Label(text="Cotação de 1 moeda específica", borderwidth=2, relief='solid')
label_cotacao_moedas.grid(row=0, column=0, padx=10, pady=10, sticky='NSEW', columnspan=3) 

label_selecionar_moedas = tk.Label(text="Selecionar Moeda", anchor='e')
label_selecionar_moedas.grid(row=1, column=0, padx=10, pady=10, sticky='NSEW', columnspan=2)

comboBox_seleciona_moeda = ttk.Combobox(values=lista_moedas)
comboBox_seleciona_moeda.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

label_selecionar_dia = tk.Label(text="Selecionar o dia que deseja pegar a cotação", anchor='e')
label_selecionar_dia.grid(row=2, column=0, padx=10, pady=10, sticky='NSEW', columnspan=2)

cal_moeda = DateEntry(year=2022, locale='pt_br')
cal_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

label_texto_cotacao = tk.Label(text="")
label_texto_cotacao.grid(row=3, column=0, padx=10, pady=10, sticky='nswe')

btn_pegar_cotacao = ttk.Button(text="Pegar Cotação", command=pegar_cotacao)
btn_pegar_cotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

# Cotação de várias moedas   ####################################################################################

label_cotacao_varias_moedas = tk.Label(text="Cotação de Multiplas Moedas", borderwidth=2, relief='solid')
label_cotacao_varias_moedas.grid(row=4, column=0, padx=10, pady=10, sticky='NSEW', columnspan=3) 

label_selecionar_arquivo = tk.Label(text="Selecionar um arquivo em Excel com as moedas na Coluna", anchor='e')
label_selecionar_arquivo.grid(row=5, column=0, padx=10, pady=10, sticky='NSEW', columnspan=2)

btn_selecionar_arquivo = ttk.Button(text="Clique para selecionar", command=selecionar_arquivo)
btn_selecionar_arquivo.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

label_arquivo_selecionado = tk.Label(text="Nenhum Arquivo Selecionado", anchor='e')
label_arquivo_selecionado.grid(row=6, column=0, padx=10, pady=10, sticky='NSEW', columnspan=3)

label_data_inicial = tk.Label(text="Data Inicial", anchor='e')
label_data_inicial.grid(row=7, column=0, padx=10, pady=10, sticky='NSEW')

cal_data_ini = DateEntry(year=2022, locale='pt_br')
cal_data_ini.grid(row=7, column=1, padx=10, pady=10, sticky='nswe')

label_data_final = tk.Label(text="Data Final", anchor='e')
label_data_final.grid(row=8, column=0, padx=10, pady=10, sticky='NSEW')

cal_data_fim = DateEntry(year=2022, locale='pt_br')
cal_data_fim.grid(row=8, column=1, padx=10, pady=10, sticky='nswe')

btn_atualizar_cotacoes = ttk.Button(text="Atualizar Cotações", command=atualizar_cotacoes)
btn_atualizar_cotacoes.grid(row=9, column=0, padx=10, pady=10, sticky='nswe')

label_atualizar_cotacoes = tk.Label(text="")
label_atualizar_cotacoes.grid(row=9, column=1, padx=10, pady=10, sticky='nswe', columnspan=2)

btn_fechar = ttk.Button(text="Fechar", command=janela.quit)
btn_fechar.grid(row=10, column=2, padx=10, pady=10, sticky='nswe')


janela.mainloop()