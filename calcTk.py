import tkinter as tk

janela=tk.Tk()
janela.title("Calculadora")
janela.geometry("346x366")
janela.resizable(False, False)
janela.config(bg='black')
janela.iconphoto(True, tk.PhotoImage(file="foto/calc.png"))

text=''
aux2=False

#logica
def entrada(aux):
    global text, aux2
    if aux2==True and (ord(aux)>=48 and ord(aux)<=57):
        text=aux
    else:
        text+=aux

    aux2=False
    valores.set(text)

def confirma():
    global text, aux2
    valor=eval(text)
    aux2=True
    text=str(valor)
    valores.set(text)

def apagar():
    global text
    text=''
    valores.set(text)

#Frames
frame_tela=tk.Frame(janela, width=346, height=70, bg='#444444')
frame_tela.grid(row=0, column=0)
frame_corpo=tk.Frame(janela, width=346, height=296, bg="black")
frame_corpo.grid(row=1, column=0)

#Texto
valores=tk.StringVar()
texto = tk.Label(frame_tela, textvariable=valores, width=23, height=2, anchor='e', padx=5, bg='#444444', fg='white', font=('Arial', 15))
texto.place(relx=1.0, rely=0.5, anchor="e")


#Botões
clean=tk.Button(frame_corpo, text="C", width=15, height=2, command=lambda:apagar())
clean.place(x=0, y=0)
modulo=tk.Button(frame_corpo, text="%", width=6, height=2, command=lambda:entrada('%'))
modulo.place(x=171, y=0)
div=tk.Button(frame_corpo, text="/", width=6, height=2, bg="orange", command=lambda:entrada('/'))
div.place(x=258, y=0)

button_9=tk.Button(frame_corpo, command=lambda:entrada('9'), text="9", width=6, height=2)
button_9.place(x=171, y=59)
button_8=tk.Button(frame_corpo, text="8", width=6, height=2, command=lambda:entrada('8'))
button_8.place(x=85, y=59)
button_7=tk.Button(frame_corpo, text="7", width=6, height=2, command=lambda:entrada('7'))
button_7.place(x=0, y=59)
mul=tk.Button(frame_corpo, text="*", width=6, height=2, bg="orange", command=lambda:entrada('*'))
mul.place(x=258, y=59)

button_6=tk.Button(frame_corpo, text="6", width=6, height=2, command=lambda:entrada('6'))
button_6.place(x=171, y=118)
button_5=tk.Button(frame_corpo, text="5", width=6, height=2, command=lambda:entrada('5'))
button_5.place(x=85, y=118)
button_4=tk.Button(frame_corpo, text="4", width=6, height=2, command=lambda:entrada('4'))
button_4.place(x=0, y=118)
men=tk.Button(frame_corpo, text="-", width=6, height=2, bg="orange", command=lambda:entrada('-'))
men.place(x=258, y=118)

button_3=tk.Button(frame_corpo, text="3", width=6, height=2, command=lambda:entrada('3'))
button_3.place(x=171, y=177)
button_2=tk.Button(frame_corpo, text="2", width=6, height=2, command=lambda:entrada('2'))
button_2.place(x=85, y=177)
button_1=tk.Button(frame_corpo, text="1", width=6, height=2, command=lambda:entrada('1'))
button_1.place(x=0, y=177)
mais=tk.Button(frame_corpo, text="+", width=6, height=2, bg="orange", command=lambda:entrada('+'))
mais.place(x=258, y=177)

button_0=tk.Button(frame_corpo, text="0", width=15, height=2, command=lambda:entrada('0'))
button_0.place(x=0, y=236)
point=tk.Button(frame_corpo, text=".", width=6, height=2, command=lambda:entrada('.'))
point.place(x=171, y=236)
equal=tk.Button(frame_corpo, text="=", width=6, height=2, bg="orange", command=lambda:confirma())
equal.place(x=258, y=236)


janela.mainloop()