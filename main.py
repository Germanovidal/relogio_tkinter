import tkinter as tk
from tkinter import *
import os
from time import strftime

root = tk.Tk()
root.title('Relógio siuu')
root.geometry('600x320')
root.maxsize(600, 230)
root.minsize(600, 230)
root.configure(background = '#18230F')

def get_saudacao():
    nome_usuario = os.getlogin()
    saudacao.config(text='Olá, ' + nome_usuario)

def get_data():
    data_atual = strftime(' %a, %d %b %Y')
    data.config(text=data_atual)

def get_horas():
    hora_atual = strftime('%H:%M:%S')
    horas.config(text=hora_atual)
    horas.after(1000, get_horas)

tela = tk.Canvas(root, width=600, height=60, bg='#18230F', bd=0, highlightthickness=0,relief='ridge')
tela.pack()

saudacao = Label(root, bg='#18230F', fg='#1F7D53', font=('Bookman Old Style', 16))
saudacao.pack()

data = Label(root, bg='#18230F', fg='#1F7D53', font=('Bookman Old Style', 14))
data.pack(pady=2)

horas = Label(root, bg='#18230F', fg='#1F7D53', font=('Bookman Old Style', 64, 'bold'))
horas.pack(pady=2)

get_saudacao()
get_data()
get_horas()
root.mainloop()
