import tkinter as tk
from cpf_generator import CPF

def generate_person():
    cpf = CPF.generate()
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, f"Nome: {name}\n")
    result_text.insert(tk.END, f"Email: {email}\n")
    result_text.insert(tk.END, f"Senha: {password}\n")
    result_text.insert(tk.END, f"CPF: {cpf}")

root = tk.Tk()
root.title("Gerador de Pessoa")

# Frame para o formulário
form_frame = tk.Frame(root)
form_frame.pack()

# Nome
name_label = tk.Label(form_frame, text="Nome:")
name_label.grid(row=0, column=0, sticky=tk.E)

name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1)

# Email
email_label = tk.Label(form_frame, text="Email:")
email_label.grid(row=1, column=0, sticky=tk.E)

email_entry = tk.Entry(form_frame)
email_entry.grid(row=1, column=1)

# Senha
password_label = tk.Label(form_frame, text="Senha:")
password_label.grid(row=2, column=0, sticky=tk.E)

password_entry = tk.Entry(form_frame, show="*")
password_entry.grid(row=2, column=1)

# Botão de geração de pessoa
generate_button = tk.Button(root, text="Gerar Pessoa", command=generate_person)
generate_button.pack()

# Resultado
result_label = tk.Label(root, text="Resultado:")
result_label.pack()

result_text = tk.Text(root, height=10, width=50)
result_text.pack()

root.mainloop()