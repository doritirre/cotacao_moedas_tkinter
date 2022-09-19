import locale
from msilib.schema import ComboBox
import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
from tkcalendar import DateEntry

lista_moedas = ['USD', 'EUR']

def pegar_cotacao():
    pass

janela = tk.Tk()

janela.title("Ferramenta de Cotação de Moedas")

label_cotacao_moedas = tk.Label(text="Cotação de 1 moeda específica", borderwidth=2, relief='solid')
label_cotacao_moedas.grid(row=0, column=0, padx=10, pady=10, sticky='NSEW', columnspan=3) 

label_selecionar_moedas = tk.Label(text="Selecionar Moeda")
label_selecionar_moedas.grid(row=1, column=0, padx=10, pady=10, sticky='NSEW', columnspan=2)

comboBox_seleciona_moeda = ttk.Combobox(values=lista_moedas)
comboBox_seleciona_moeda.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

label_selecionar_dia = tk.Label(text="Selecionar o dia que deseja pegar a cotação")
label_selecionar_dia.grid(row=2, column=0, padx=10, pady=10, sticky='NSEW', columnspan=2)

cal_moeda = DateEntry(year=2021, locale='pt_br')
cal_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

label_texto_cotacao = tk.Label(text="")
label_texto_cotacao.grid(row=3, column=0, padx=10, pady=10, sticky='nswe')

btn_pegar_cotacao = tk.Button(text="Pegar Cotação", command=pegar_cotacao)
btn_pegar_cotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

# Cotação de várias moedas
label_cotacao_varias_moedas = tk.Label(text="Cotação de Multiplas Moedas", borderwidth=2, relief='solid')
label_cotacao_varias_moedas.grid(row=4, column=0, padx=10, pady=10, sticky='NSEW', columnspan=3) 

janela.mainloop()