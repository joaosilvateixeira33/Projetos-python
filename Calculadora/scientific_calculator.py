import tkinter as tk
import math

"""class Calculator2:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Científica")

        # Cria a tela da calculadora
        self.screen = tk.Entry(master, width=40, font=("Arial", 16))
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Cria os botões
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+",
            
        ]

        # Cria e posiciona os botões
        for i in range(len(buttons)):
            button = tk.Button(master, text=buttons[i], width=7, height=2, font=("Arial", 12))
            row = i // 4 + 1
            col = i % 4
            button.grid(row=row, column=col, padx=5, pady=5)
            button.bind("<Button-1>", self.button_click)

        # Cria um botão de igual
        equals_button = tk.Button(master, text="=", width=30, height=2, font=("Arial", 12))
        equals_button.grid(row=7, column=0, columnspan=4, padx=5, pady=5)
        equals_button.bind("<Button-1>", self.equals_click)

    # Função para lidar com o clique nos botões
    def button_click(self, event):
        button = event.widget
        text = button["text"]

        # Adiciona o texto do botão à tela
        self.screen.insert(tk.END, text)

    # Função para lidar com o clique no botão de igual
    def equals_click(self, event):
        # Pega a expressão da tela
        expression = self.screen.get()

        # Substitui algumas funções e constantes para usar as da biblioteca math
        expression = expression.replace("sin", "math.sin")
        expression = expression.replace("cos", "math.cos")
        expression = expression.replace("tan", "math.tan")
        expression = expression.replace("log", "math.log10")
        expression = expression.replace("sqrt", "math.sqrt")
        expression = expression.replace("pi", "math.pi")
        expression = expression.replace("e", "math.e")
        expression = expression.replace("^2", "**2")
        expression = expression.replace("abs", "math.fabs")
        expression = expression.replace("ceil", "math.ceil")
        expression = expression.replace("floor", "math.floor")

        # Calcula o resultado da expressão
        try:
            result = eval(expression)
        except Exception as e:
            result = "Erro"
        
        # Exibe o resultado na tela
        self.screen.delete(0, tk.END)
        self.screen.insert(tk.END, result)

# Cria a janela da calculadora e inicia o loop de eventos
root = tk.Tk()
app = Calculator2(root)
root.mainloop()"""

import math
import tkinter as tk

class Calculator2:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Científica")

         # Definir o esquema de cores personalizado
        self.bg_color = '#f2f2f2'
        self.button_bg_color = '#4d4d4d'
        self.button_fg_color = '#ffffff'
        self.entry_bg_color = '#ffffff'
        self.entry_fg_color = '#000000'
        self.button_active_bg_color = '#696969'
        self.button_active_fg_color = '#ffffff'

        # Cria um campo de entrada de texto para a entrada do usuário
        self.entry = tk.Entry(master, width=50)
        self.entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        # Cria os botões para cada dígito e operação
        button_text = [
            "7", "8", "9", "C", "AC",
            "4", "5", "6", "+", "-",
            "1", "2", "3", "*", "/",
            "0", ".", "pi", "(", ")",
            "sin", "cos", "tan", "^", "sqrt"
        ]
        self.buttons = []
        for i, text in enumerate(button_text):
            button = tk.Button(master, text=text, width=7, height=2, command=lambda text=text: self.button_click(text))
            row = i // 5 + 1
            col = i % 5
            button.grid(row=row, column=col, padx=2, pady=2)
            self.buttons.append(button)

    def button_click(self, text):
        if text == "C":
            # Apaga o último caractere do campo de entrada
            self.entry.delete(len(self.entry.get()) - 1)
        elif text == "AC":
            # Apaga todo o conteúdo do campo de entrada
            self.entry.delete(0, tk.END)
        elif text == "sin":
            # Calcula o seno do valor no campo de entrada
            try:
                result = math.sin(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except ValueError:
                pass
        elif text == "cos":
            # Calcula o cosseno do valor no campo de entrada
            try:
                result = math.cos(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except ValueError:
                pass
        elif text == "tan":
            # Calcula a tangente do valor no campo de entrada
            try:
                result = math.tan(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except ValueError:
                pass
        elif text == "sqrt":
            # Calcula a raiz quadrada do valor no campo de entrada
            try:
                result = math.sqrt(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except ValueError:
                pass
        elif text == "^":
            # Eleva o valor no campo de entrada à potência especificada
            try:
                x, y = self.entry.get().split("^")
                result = float(x) ** float(y)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except ValueError:
                pass
        elif text == "pi":
            # Insere o valor de pi no campo de entrada
            self.entry.insert(tk.END, str(math.pi))
        else:
            # Insere o texto do botão no campo de entrada
            self.entry.insert(tk.END, text)

root = tk.Tk()
calculator = Calculator2(root)
root.mainloop()