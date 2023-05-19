import sqlite3
import customtkinter as ct
import pandas as pd

janela_principal = ct.CTk()
janela_principal.title("Cadastro de Clientes")
janela_principal.geometry("330x350")

def cadastrar_cliente():
    conexao = sqlite3.connect('clientes.db')
    cursor_server = conexao.cursor()

    cursor_server.execute('INSERT INTO clientes VALUES (:nome, :sobrenome, :email, :telefone)',
                          {
                            'nome': entry_nome.get(),
                            'sobrenome': entry_sobrenome.get(),
                            'email': entry_email.get(),
                            'telefone': entry_telefone.get() 
    })

    conexao.commit()
    conexao.close()

    entry_nome.delete(0,"end")
    entry_sobrenome.delete(0,"end")
    entry_email.delete(0,"end")
    entry_telefone.delete(0,"end")

def exporta_clientes():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    # Inserir dados na tabela:
    c.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados = c.fetchall()
    
    # print(clientes_cadastrados)
    clientes_cadastrados=pd.DataFrame(clientes_cadastrados,columns=['nome','sobrenome','email','telefone','Id_banco'])
    clientes_cadastrados.to_excel('clientes.xlsx')

    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

rotulo_nome = ct.CTkLabel(janela_principal, text="Nome:")
rotulo_nome.grid(row=0, column=0, padx=10, pady=10)

entry_nome = ct.CTkEntry(janela_principal, width=200)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

rotulo_sobrenome = ct.CTkLabel(janela_principal, text="Sobrenome: ")
rotulo_sobrenome.grid(row=1, column=0, padx=10, pady=10)

entry_sobrenome = ct.CTkEntry(janela_principal, width=200)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

rotulo_email = ct.CTkLabel(janela_principal, text="Email: ")
rotulo_email.grid(row=2, column=0, padx=10, pady=10)

entry_email = ct.CTkEntry(janela_principal, width=200)
entry_email.grid(row=2, column=1, padx=10, pady=10)

rotulo_telefone = ct.CTkLabel(janela_principal, text="Telefone: ")
rotulo_telefone.grid(row=3, column=0, padx=10, pady=10)

entry_telefone = ct.CTkEntry(janela_principal, width=200)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

botao_cadastrar = ct.CTkButton(janela_principal,text="Cadastrar Cliente", command=cadastrar_cliente)
botao_cadastrar.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipadx=80)

botao_exportar = ct.CTkButton(janela_principal,text="exportar para excel", command=exporta_clientes)
botao_exportar.grid(row=5, column=0, columnspan=2, padx=10, pady=10, ipadx=80)

janela_principal.mainloop()