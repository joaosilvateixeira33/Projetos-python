import tkinter as tk
import random

# Função para gerar um CPF aleatório
def gerar_cpf():
    cpf = ''
    for i in range(9):
        cpf += str(random.randint(0, 9))
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0
    cpf += str(digito1)
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0
    cpf += str(digito2)
    return cpf

# Função para validar um CPF
def validar_cpf(cpf):
    if not cpf.isdigit() or len(cpf) != 11:
        return False
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0
    if int(cpf[9]) != digito1:
        return False
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0
    if int(cpf[10]) != digito2:
        return False
    return True

# Função para lidar com o botão "Gerar CPF"
def gerar_cpf_handler():
    cpf = gerar_cpf()
    cpf_var.set(cpf)

# Função para lidar com o botão "Validar CPF"
def validar_cpf_handler():
    cpf = cpf_var.get()
    if validar_cpf(cpf):
        resultado_var.set('CPF válido')
    else:
        resultado_var.set('CPF inválido')

# Cria a janela principal
root = tk.Tk()
root.title('Gerador de cpf')
root.geometry("600x400+500+200")

# Cria a variável que vai guardar o CPF gerado
cpf_var = tk.StringVar()

# Cria a entrada de texto para o CPF
cpf_entry = tk.Entry(root, textvariable=cpf_var)

# Cria o botão "Gerar CPF"
gerar_cpf_button = tk.Button(root, text='Gerar CPF', command=gerar_cpf_handler)

# Cria o botão "Validar CPF"
validar_cpf_button = tk.Button(root, text='Validar CPF', command=validar_cpf_handler)

# Cria a variável que vai mostrar o resultado da validação do CPF
resultado_var = tk.StringVar()

# Cria o rótulo para mostrar o resultado da validação do CPF
resultado_label = tk.Label(root, textvariable=resultado_var)

# Organiza os widgets na janela principal
cpf_entry.pack()
gerar_cpf_button.pack()
validar_cpf_button.pack()
resultado_label.pack()

# Inicia o loop da interface gráfica
root.mainloop()