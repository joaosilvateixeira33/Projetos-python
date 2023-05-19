import tkinter as tk
import pymysql

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciador de Clientes")
        
        # widgets
        lbl_nome = tk.Label(self.master, text="Nome")
        lbl_nome.grid(row=0, column=0, padx=5, pady=5)
        self.ent_nome = tk.Entry(self.master)
        self.ent_nome.grid(row=0, column=1, padx=5, pady=5)
        
        lbl_email = tk.Label(self.master, text="E-mail")
        lbl_email.grid(row=1, column=0, padx=5, pady=5)
        self.ent_email = tk.Entry(self.master)
        self.ent_email.grid(row=1, column=1, padx=5, pady=5)
        
        lbl_telefone = tk.Label(self.master, text="Telefone")
        lbl_telefone.grid(row=2, column=0, padx=5, pady=5)
        self.ent_telefone = tk.Entry(self.master)
        self.ent_telefone.grid(row=2, column=1, padx=5, pady=5)
        
        btn_adicionar = tk.Button(self.master, text="Adicionar", command=self.adicionar_cliente)
        btn_adicionar.grid(row=3, column=0, padx=5, pady=5)
        
        btn_atualizar = tk.Button(self.master, text="Atualizar", command=self.atualizar_cliente)
        btn_atualizar.grid(row=3, column=1, padx=5, pady=5)
        
        btn_excluir = tk.Button(self.master, text="Excluir", command=self.excluir_cliente)
        btn_excluir.grid(row=3, column=2, padx=5, pady=5)
        
        self.lista_clientes = tk.Listbox(self.master, width=50)
        self.lista_clientes.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
        self.lista_clientes.bind("<<ListboxSelect>>", self.selecionar_cliente)
        
        # conectar ao banco de dados
        self.conexao = pymysql.connect(
            host="localhost",
            user="Joao Marcos ",
            password="abc123",
            database="dados"
        )
        
        # carregar clientes
        self.carregar_clientes()