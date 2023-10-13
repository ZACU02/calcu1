from tkinter import *

ventana = Tk()
ventana.title("calculadora")
ventana.configure(bg='black')


#i = 0

#entrada
e_texto = Entry(ventana, font = ("Calibri 20"))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady=5)



i=0
def click_boton(valor):
    global i 
    e_texto.insert(i,valor)
    i += 1

def borrar():
    e_texto.delete(0,END)
    i = 0

def eliminar():
    global i
    i=i-1
    e_texto.delete(i,END)

def raiz():
    ecuacion = e_texto.get()
    try:
        numero = float(ecuacion)
        resultado = numero ** 0.5
        e_texto.delete(0, END)
        e_texto.insert(0, resultado)
    except ValueError:
        e_texto.delete(0, END)
        e_texto.insert(0, "Error")

def potencia_n(n):
    ecuacion = e_texto.get()
    try:
        numero = float(ecuacion)
        resultado = numero ** n
        e_texto.delete(0, END)
        e_texto.insert(0, resultado)
    except ValueError:
        e_texto.delete(0, END)
        e_texto.insert(0, "Error")
    
def opercacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i=0

def cambiar_signo():
    ecuacion = e_texto.get()
    if ecuacion and ecuacion[0] == '-':
        e_texto.delete(0)
    elif ecuacion:
        e_texto.insert(0, '-')

def modulo():
    ecuacion = e_texto.get()
    try:
        resultado = eval(ecuacion)
        resultado = resultado % 1  # Calcula el módulo
        e_texto.delete(0, END)
        e_texto.insert(0, resultado)
    except:
        e_texto.delete(0, END)
        e_texto.insert(0, "Error")

    
boton1 = Button(ventana, text="1", width=5, height=2, command = lambda: click_boton(1), bg="pink")
boton2 = Button(ventana, text="2", width=5, height=2, command = lambda: click_boton(2), bg="pink")
boton3 = Button(ventana, text="3", width=5, height=2, command = lambda: click_boton(3), bg="pink")
boton4 = Button(ventana, text="4", width=5, height=2, command = lambda: click_boton(4), bg="pink")
boton5 = Button(ventana, text="5", width=5, height=2, command = lambda: click_boton(5), bg="pink")
boton6 = Button(ventana, text="6", width=5, height=2, command = lambda: click_boton(6), bg="pink")
boton7 = Button(ventana, text="7", width=5, height=2, command = lambda: click_boton(7), bg="pink")
boton8 = Button(ventana, text="8", width=5, height=2, command = lambda: click_boton(8), bg="pink")
boton9 = Button(ventana, text="9", width=5, height=2, command = lambda: click_boton(9), bg="pink")
boton0 = Button(ventana, text="0", width=5, height=2, command = lambda: click_boton(0), bg="pink")

boton_borrar = Button(ventana, text="AC", width=5, height=2, command=lambda:borrar(), bg="fuchsia")
boton_Parentesis1 = Button(ventana, text="(", width=5, height=2, command=lambda: click_boton("("), bg="purple")
boton_Parentesis2 = Button(ventana, text=")", width=5, height=2, command=lambda: click_boton(")"), bg="purple")
boton_Punto = Button(ventana, text=".", width=5, height=2, command=lambda: click_boton("."))

boton_div = Button(ventana, text="/", width=5, height=2, command=lambda: click_boton("/"), bg="blue")
boton_mult = Button(ventana, text="x", width=5, height=2, command=lambda: click_boton("*"), bg="mistyrose")
boton_suma = Button(ventana, text="+", width=5, height=2, command=lambda: click_boton("+"), bg="aquamarine")
boton_resta = Button(ventana, text="-", width=5, height=2, command=lambda: click_boton("-"), bg="silver")
boton_igual = Button(ventana, text="=", width=5, height=2, command=lambda: opercacion(), bg="navy blue")
boton_eliminar = Button(ventana, text="<", width=5, height=2, command=lambda: eliminar(), bg="fuchsia")
boton_raiz = Button(ventana, text="√", width=5, height=2, command=raiz, bg="yellow")
boton_potencia_n= boton_potencia = Button(ventana, text="^n", width=5, height=2, command=lambda: potencia_n(2), bg="orange")
boton_cambiar_signo = Button(ventana, text="+/-", width=5, height=2, command=cambiar_signo, bg="gray")
boton_modulo = Button(ventana, text="%", width=5, height=2, command=modulo, bg="green")

#asignamos colocacion de elementos en ventana
boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_Parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_Parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_div.grid(row=1, column=3, padx=5, pady=5)
boton_eliminar.grid(row=5, column=0, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_mult.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_suma.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_resta.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=1, padx=5, pady=5)
boton_Punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)
boton_raiz.grid(row=2, column=4, padx=5, pady=5)
boton_potencia_n.grid(row=3, column=4, padx=5, pady=5)
boton_cambiar_signo.grid(row=5, column=4, padx=5, pady=5)
boton_modulo.grid(row=4, column=4, padx=5, pady=5)

ventana.mainloop()