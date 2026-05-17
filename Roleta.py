import random
from tkinter import *

janela = Tk()
janela.title('roleta')
janela.configure(background='#8cf774')
janela.geometry('780x560')


def girar_roleta():
    n1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    random.shuffle(n1)
    random.shuffle(n2)
    random.shuffle(n3)

    v1 = n1[1]
    v2 = n2[1]
    v3 = n3[1]

    resultado.config(text=f'{v1} {v2} {v3}')

    if v1 == 7 and v2 == 7 and v3 == 7:
        mensagem.config(text='JACKPOT', font=("Arial", 50))
    else:
        mensagem.config(text='tente de novo!')


resultado = Label(janela, text='', font=("Arial", 80))
resultado.pack(pady=80)

mensagem = Label(janela, text='')
mensagem.pack(pady=20)

botao = Button(janela, text='Girar Roleta!',
               font=('Arial', 20), command=girar_roleta)
botao.pack(pady=10)

janela.mainloop()