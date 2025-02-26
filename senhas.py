# maisculo e minuscula 
# Simbulo e espaço 

"""
Security = chave
5ecur1ty = chave

"""
from tkinter import *

chave = input('Digite a base da sua senha: ')

senha = ""
for letras in chave:
    if letras in 'Aa': 
        senha = senha + '10'
    elif letras in 'Bb': senha = senha + "11"
    elif letras in 'Cc': senha = senha + "12"
    elif letras in 'Dd': senha = senha + "13"
    elif letras in 'Ee': senha = senha + "14"
    elif letras in 'Ff': senha = senha + "15"
    elif letras in 'Rr': senha = senha + "#"
    elif letras in 'Mm': senha = senha + "@"
    elif letras in 'Tt': senha = senha + "!"
    elif letras in 'Pp': senha = senha + "$"
    else: senha = senha + letras
   
print(senha)

janela = Tk()
janela.title('Gerenciador de senhas')

texto_orientacao = Label(janela, text= "Clique")
texto_orientacao.grid(column=0, row=0)

botao = Button(janela, text= "Gerar senhas criptografadas", command= chave)
botao.grid(column=0, row=1)


janela.mainloop()
