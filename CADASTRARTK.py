import pymysql.cursors
from tkinter import *


conexao = pymysql.connect(

    host='localhost',
    user='root',
    passwd='',
    db='cadastrarelogar',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor




)



existente = []

def logar():

    usuariol = (usuario .get())
    senhal = (senha.get())

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from usuarios')
            resultadol = cursor.fetchall()
    except:
        print('erro ao tentar acessar o banco de dados')

    for dado in resultadol:
        if usuariol == dado['usuario'] and senhal == dado['senha']:

            statuschanged = Label(janela, text='USUARIO LOGADO COM SUCESSO', fg='Green')
            statuschanged.grid(row=7, column=1)
            statusl['text'] = statuschanged


def cadastrar():


    #EXTRAINDO OS DADOS

    nomech = str(nome.get())
    sobrenomech = str(sobrenome.get())
    idadech = int(idade.get())
    cpfch = int(cpf.get())
    usuarioch = str(usuarioc.get())
    senhach = str(senhac.get())


    #validador de Logins
    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from usuarios')
            resultadoc = cursor.fetchall()
    except:
        print('erro ao tentar acessar o banco de dados no validador')

    for dado in resultadoc:
        if usuarioch == dado['usuario'] and senhach == dado['senha']:
            existente.append(1)


    #Cadastrar
    try:
        with conexao.cursor() as cursor:
            cursor.execute('insert into usuarios (nome, sobrenome, idade, cpf, usuario, senha) values (%s, %s, %s, %s, %s, %s)', (nomech, sobrenomech, idadech, cpfch, usuarioch, senhach))
            conexao.commit()
            print('cadastrado')

            statusch = Label(janela, text='CADSATRADO COM SUCESSO', fg='Green')
            statusch.grid(row=28, column=1)
            statusc['text'] = statusch
    except:
        print('Erro ao tentar acessar o banco de dados no cadastro')



#Criando a Janela

janela = Tk()
janela.title('cadastrar e logar')
janela.geometry('700x720')






#LOGAR TKINTER
Label(janela, text='      CADASTRAR E LOGAR', bg='black', fg='white', width=30).grid(row=0, column=0, )
Label(janela, text='USUARIO').grid(row=3, column=0)

usuario = Entry(janela, bg='white', fg='green', width=30)
usuario.grid(row=4, column=0)

Label(janela, text='SENHA').grid(row=5, column=0)



senha = Entry(janela, bg='white', fg='green', width=30, show='*')
senha.grid(row=6, column=0)

#status
statusl = Label(janela, text='AINDA NAO AUTENTICADO', fg='Red')
statusl.grid(row=7, column=1)



blogar = Button(janela, text='LOGAR', fg='Blue', command=logar)
blogar.grid(row=7, column=0)


Label(janela).grid(row=8, column=0)





#CADASTRAR



Label(janela, text='CADASTRAR', bg='black', fg='white', width=30).grid(row=9, column=0,)



Label(janela, text='NOME').grid(row=11, column=0)
nome = Entry(janela, width=30, fg='Green')
nome.grid(row=12, column=0)

Label(janela, text='SOBRENOME').grid(row=13, column=0)
sobrenome = Entry(janela, width=30, fg='Green')
sobrenome.grid(row=14, column=0)

Label(janela, text='IDADE').grid(row=15, column=0)
idade = Entry(janela, width=30, fg='Green')
idade.grid(row=16, column=0)

Label(janela, text='CPF').grid(row=17, column=0)
cpf = Entry(janela, width=30, fg='Green')
cpf.grid(row=18, column=0)

Label(janela, text='USUARIO').grid(row=19, column=0)
usuarioc = Entry(janela, width=30, fg='Green')
usuarioc.grid(row=20, column=0)

Label(janela, text='SENHA').grid(row=21, column=0)
senhac = Entry(janela, width=30, fg='Green')
senhac.grid(row=22, column=0)



#status do cadastro

statusc = Label(janela, text='')
statusc.grid(row=28, column=1)








bcadastrar = Button(janela, text='CADASTRAR', fg='Blue', command=cadastrar)
bcadastrar.grid(row=28, column=0)


janela.mainloop()