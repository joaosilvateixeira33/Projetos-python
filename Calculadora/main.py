from tkinter import *
from tkinter import ttk

#cores

preto = "#1e1f1e"
branco = "#f0f2f0"
azul_escuro = "#666bff"
ciano = "#66f0ff"
laranja = "#ffab40"

janela = Tk()

janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=preto)
janela.resizable(False, False)
janela.attributes("-topmost", 1)




# criar frames
frame_display = Frame(janela, width=235, height=50, bg=preto)
frame_display.grid(row=0, column=0)

frame_botoes = Frame(janela, width=235, height=268)
frame_botoes.grid(row=1, column=0)

# criando botoes
botao_limpar = Button(frame_botoes, text="C", width=11, height=2, bg=branco, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:limpar_tela())
botao_limpar.place(x=0, y=0)

botao_porcentagem = Button(frame_botoes, text="%", width=5, height=2, bg=branco, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entrar_valor("%"))
botao_porcentagem.place(x=118, y=0)

botao_divisao = Button(frame_botoes, text="/", width=5, height=2, bg=azul_escuro, fg=branco, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:limpar_tela())
botao_divisao.place(x=177, y=0)

botao_7 = Button(frame_botoes, text="7", width=5, height=2, bg=branco, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entrar_valor('7'))
botao_7.place(x=0, y=52)

botao_8 = Button(frame_botoes, text="8", width=5, height=2, bg=branco, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entrar_valor('8'))
botao_8.place(x=59, y=52)

botao_9 = Button(frame_botoes, text="9", width=5, height=2, bg=branco, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entrar_valor('9'))
botao_9.place(x=118, y=52)

botao_Multipicacao = Button(frame_botoes, text="x", width=5, height=2, bg=azul_escuro, fg=branco,font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entrar_valor('*'))
botao_Multipicacao.place(x=177, y=52)

botao_4 = Button(frame_botoes, text="4", width=5, height=2, bg=branco, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao_4.place(x=0, y=104)

botao_5 = Button(frame_botoes, text="5", width=5, height=2, bg=branco, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao_5.place(x=59, y=104)

botao_6 = Button(frame_botoes, text="6", width=5, height=2, bg=branco, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao_6.place(x=118, y=104)

botao_Subtracao = Button(frame_botoes, text="-", width=5, height=2, bg=azul_escuro, fg=branco,font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao_Subtracao.place(x=177, y=104)

botao_1 = Button(frame_botoes, text="1", width=5, height=2, bg=branco, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao_1.place(x=0, y=156)

botao_2 = Button(frame_botoes, text="2", width=5, height=2, bg=branco, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao_2.place(x=59, y=156)

botao_3 = Button(frame_botoes, text="3", width=5, height=2, bg=branco, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao_3.place(x=118, y=156)

botao_Soma = Button(frame_botoes, text="+", width=5, height=2, bg=azul_escuro, fg=branco,font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:entrar_valor('+'))
botao_Soma.place(x=177, y=156)

botao_0 = Button(frame_botoes, text="0", width=5, height=2, bg=branco, font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao_0.place(x=0, y=208)

botao_ponto = Button(frame_botoes, text=".", width=5, height=2, bg=azul_escuro, fg=branco,font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao_ponto.place(x=59, y=208)

botao_igual = Button(frame_botoes, text="=", width=5, height=2, bg=azul_escuro, fg=branco,font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:calcular())
botao_igual.place(x=118, y=208)

botao_historico = Button(frame_botoes, text="HS", width=5, height=2, bg=azul_escuro, fg=branco,font=("ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda:adicionar_ao_historico())
botao_historico.place(x=177, y=208)

historico = []

def adicionar_ao_historico(valor):
        janela_interna = Tk()
        janela_interna.title("Janela Interna")
        janela_interna.geometry("235x318")

        # exibir historico de calculos
        historico_label = Label(janela_interna, text="<Vazio>")
        historico_label.pack()

        historico.configure(state="normal")
        historico.insert("end", valor + "\n")
        historico.see("end")
        historico.configure(state="disabled")
        adicionar_ao_historico(todos_valores + " = " + resultado)



todos_valores = ""
valor_texto = StringVar()
def entrar_valor(event):
    global todos_valores

    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

app_scream = Label(frame_display,textvariable=valor_texto,width=16,height=2, padx=7, relief="flat", anchor="e",bd=0, justify=RIGHT, font=("Ivy 18 "), bg="#37474F", fg=preto)
app_scream.place(x=0, y=0)

operacao_temporaria = " "

def calcular():
    global todos_valores
    global operacao_temporaria
    resultado = str(eval(todos_valores))
    valor_texto.set(resultado)
    todos_valores = ""

    
    
    
    

def limpar_tela(): 
    global todos_valores
    todos_valores = "" 
    valor_texto.set("")


janela.mainloop()