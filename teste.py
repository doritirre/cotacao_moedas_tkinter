from cgi import test
import tkinter as tk
from tkinter import Button, Tk, ttk
from tkinter import font

janela = Tk()
estilo = ttk.Style()
estilo.configure('TButton', font = ('Arial', 50))

b1 = Button(text='Live de Python')
b2 = ttk.Button(text='Live de Python')
b1.pack()
b2.pack(padx=10, pady=10)

janela.mainloop()