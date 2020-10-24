from tkinter import *
from tkinter import scrolledtext
from Biseccion import *
from PuntoFijo import *
from Secante import *
from PosFalsa import *
from Funcion import *
from Muller import *
from Horner import *
from NewtonR import *
from Lagrange import *
from difDivididas import *
from Hermit import *
from Diferenciacion import *
from Integracion import *
from IntegracionCompuesta import *
from Romberg import *
from TaylorNew import *
from PuntoMedio import *
from EulerModificado import *
from Heun import *
from RungeKutta import *
from GaussJordan import *
from PIL import Image, ImageTk

import numpy as np
import matplotlib.pyplot as plt
import math

def solverRoots(opcion):
    if opcion == "Posición Falsa": PosFalsa()
    elif opcion == "Bisección": Bis()
    elif opcion == "Punto Fijo": PF()
    elif opcion == "Newton Raphson": Newton()
    elif opcion == "Secante": Sec()
    elif opcion == "Müller": Mull()
    elif opcion == "Horner": Horn()

def solverInter(opcion):
    if opcion == "Hermit": Herm()
    elif opcion == "Lagrange": Lag()
    elif opcion == "Diferencias Divididas": Div()

def solverDif(opcion):
    if opcion == "Extremo de 3 puntos": ExtremoTres()
    elif opcion == "Intermedio de 3 puntos": IntermedioTres()
    elif opcion == "Extremo de 5 puntos": ExtremoCinco()
    elif opcion == "Intermedio de 5 puntos": IntermedioCinco()
    elif opcion == "Integración abierta": IntAbierta()
    elif opcion == "Integración cerrada": IntCerrada()
    elif opcion == "Integración compuesta abierta": IntCompAbierta()
    elif opcion == "Trapecio Compuesto": TrapecioComp()
    elif opcion == "Simpson Compuesto": SimpsonComp()
    elif opcion == "Romberg": Romb()

def solverEcDif(opcion):
    if opcion == "Taylor": newTaylor()
    elif opcion == "Punto Medio": puntoM()
    elif opcion == "Euler Modificado": eulerMod()
    elif opcion == "Heun": heun()
    elif opcion == "Runge Kutta": runge()

def solverMatrix(opcion):
    if opcion == "Gauss Jordan": gauss()

def ayudaFunction():
    newwin = Toplevel(window)
    newwin.geometry('600x500')
    newwin.title("Ayuda")
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    txt = scrolledtext.ScrolledText(frame, width=85, height=40)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)
    text = "Existen 5 secciones de la calculadora. Cuando encuentres la que necesites,\npresiona las flechas para que aparezcan todas las opciones. \nDespués de seleccionar, aprieta el botón de 'Resolver' de la sección elegida.\n\n\n"
    text += "A continuación se explican algunos principios de la calculadora:\n\n"
    text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
    text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(x) + sin(3*x) - tan(x/7) \n\n"
    text += "Exponenciales: exp()\nEjemplo: e^(3x) se escribiría así: exp(3*x) \n\n"
    text += "Logarítmicas: log()\nEjemplo: log((2*x)^3)\n\n"
    text += "Cuando se piden puntos o coeficientes, escribir los datos separados\npor comas, sin espacios --> ejemplo: 1,2,3,4\n\n"
    text += "Para escribir una matriz:\nSeparar números con espacios y renglones con saltos de línea\nEjemplo:\n1 2 3 4\n5 6 7 8"
    txt.insert(INSERT, text)

def Bis():

    def f(f,x):
        return eval(f)

    def graph(function):
        fig = plt.figure()
        x = np.arange(-10,10,0.1)
        y = f(function,x)
        plt.ylim( [-10,10] )
        plt.xlim( [-10,10] )
        plt.plot(x,y,color="green")
        plt.plot([-10,10],[0,0],color="black")
        plt.plot([0,0],[-10,10],color="black")

        plt.show()

    def getGraph():
        function = fx.get()
        replacements = {
            'sin' : 'np.sin',
            'log' : 'np.log',
            'cos' : 'np.cos',
            'exp': 'np.exp',
            'sqrt': 'np.sqrt',
            '^': '**',
        }

        for old, new in replacements.items():
            function = function.replace(old, new)
        return graph(function)

    def ayudaFuncion():
        newWin = Toplevel(newwin)
        newWin.geometry('400x250')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir función\n\n"
        text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
        text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(x) + sin(3*x) - tan(x/7) \n\n"
        text += "Exponenciales: exp()\nEjemplo: e^(3x) se escribiría así: exp(3*x) \n\n"
        text += "Logarítmicas: log()\nEjemplo: log((2*x)^3)\n\n"
        txt.insert(INSERT, text)

    def ayudaIntervalo(extremo):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        if extremo == "a":
            text = "Escribir extremo izquierdo del intervalo"
        elif extremo == "b":
            text = "Escribir extremo derecho del intervalo"
        else:
            text = "Escribir tolerancia --> ejemplo: 1e-5"
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        bis = Biseccion(fx.get(), tol.get(), a.get(), b.get())
        bis = bis.solution()
        txt.insert(INSERT, bis)
    newwin = Toplevel(window)
    #newwin.geometry('600x500')
    newwin.title("Bisección")
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    lbl = Label(panel, text="f(x):")
    lbl.grid(column=1, row=1)
    lbl = Label(panel, text="a:")
    lbl.grid(column=1, row=2)
    lbl = Label(panel, text="b:")
    lbl.grid(column=1, row=3)
    lbl = Label(panel, text="Tolerancia:")
    lbl.grid(column=1, row=4)
    fx = Entry(panel, width=20)
    fx.grid(column=2, row=1)

    btnfx = Button(panel,text="?",command=ayudaFuncion)
    btnfx.grid(column=3,row=1)
    btna = Button(panel,text="?",command=lambda: ayudaIntervalo("a"))
    btna.grid(column=3,row=2)
    btnb = Button(panel, text="?", command=lambda: ayudaIntervalo("b"))
    btnb.grid(column=3, row=3)
    btntol = Button(panel, text="?", command=lambda: ayudaIntervalo("tol"))
    btntol.grid(column=3, row=4)

    a = Entry(panel, width=20)
    a.grid(column=2, row=2)
    b = Entry(panel, width=20)
    b.grid(column=2, row=3)
    tol = Entry(panel, width=20)
    tol.grid(column=2, row=4)
    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=2, row=7)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=1, row=7)
    txt = scrolledtext.ScrolledText(frame, width=120, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def PF():
    def f(f,x):
        return eval(f)

    def graph(function):
        fig = plt.figure()
        x = np.arange(-10,10,0.1)
        y = f(function,x)
        plt.ylim( [-10,10] )
        plt.xlim( [-10,10] )
        plt.plot(x,y,color="green")
        plt.plot([-10,10],[0,0],color="black")
        plt.plot([0,0],[-10,10],color="black")

        plt.show()

    def getGraph():
        function = gx.get()
        replacements = {
            'sin' : 'np.sin',
            'log': 'np.log',
            'cos' : 'np.cos',
            'exp': 'np.exp',
            'sqrt': 'np.sqrt',
            '^': '**',
        }

        for old, new in replacements.items():
            function = function.replace(old, new)
        return graph(function)

    def ayudaFuncion():
        newWin = Toplevel(newwin)
        newWin.geometry('400x250')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir función\n\n"
        text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
        text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(x) + sin(3*x) - tan(x/7) \n\n"
        text += "Exponenciales: exp()\nEjemplo: e^(3x) se escribiría así: exp(3*x) \n\n"
        text += "Logarítmicas: log()\nEjemplo: log((2*x)^3)\n\n"
        txt.insert(INSERT, text)

    def ayudaIntervalo(extremo):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""
        if extremo == "a":
            text = "Escribir extremo izquierdo del intervalo"
        elif extremo == "b":
            text = "Escribir extremo derecho del intervalo"
        elif extremo == "tol":
            text = "Escribir tolerancia --> ejemplo: 1e-5"
        elif extremo == "punto":
            text = "Escribir punto inicial"
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        pf = PuntoFijo(gx.get(), tol.get(), p0.get(), a.get(), b.get())
        pf = pf.solution()
        txt.insert(INSERT, pf)
    newwin = Toplevel(window)
    newwin.geometry('600x500')
    newwin.title("Punto Fijo")
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    lbl = Label(panel, text="g(x):")
    lbl.grid(column=1, row=1)
    lbl = Label(panel, text="Punto inicial:")
    lbl.grid(column=1, row=2)
    lbl = Label(panel, text="Tolerancia:")
    lbl.grid(column=1, row=3)
    lbl = Label(panel, text="a:")
    lbl.grid(column=1, row=4)
    lbl = Label(panel, text="b:")
    lbl.grid(column=1, row=5)
    gx = Entry(panel, width=20)
    gx.grid(column=2, row=1)
    p0 = Entry(panel, width=20)
    p0.grid(column=2, row=2)
    tol = Entry(panel, width=20)
    tol.grid(column=2, row=3)
    a = Entry(panel, width=20)
    a.grid(column=2, row=4)
    b = Entry(panel, width=20)
    b.grid(column=2, row=5)

    btnfx = Button(panel, text="?", command=ayudaFuncion)
    btnfx.grid(column=3, row=1)
    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("a"))
    btna.grid(column=3, row=4)
    btnb = Button(panel, text="?", command=lambda: ayudaIntervalo("b"))
    btnb.grid(column=3, row=5)
    btntol = Button(panel, text="?", command=lambda: ayudaIntervalo("tol"))
    btntol.grid(column=3, row=3)
    btntol = Button(panel, text="?", command=lambda: ayudaIntervalo("punto"))
    btntol.grid(column=3, row=2)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=2, row=7)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=1, row=7)
    txt = scrolledtext.ScrolledText(frame, width=83, height=21)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def Newton():

    def f(f,x):
        return eval(f)

    def graph(function):
        fig = plt.figure()
        x = np.arange(-10,10,0.1)
        y = f(function,x)
        plt.ylim( [-10,10] )
        plt.xlim( [-10,10] )
        plt.plot(x,y,color="green")
        plt.plot([-10,10],[0,0],color="black")
        plt.plot([0,0],[-10,10],color="black")

        plt.show()

    def ayudaFuncion():
        newWin = Toplevel(newwin)
        newWin.geometry('400x250')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir función\n\n"
        text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
        text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(x) + sin(3*x) - tan(x/7) \n\n"
        text += "Exponenciales: exp()\nEjemplo: e^(3x) se escribiría así: exp(3*x) \n\n"
        text += "Logarítmicas: log()\nEjemplo: log((2*x)^3)\n\n"
        txt.insert(INSERT, text)

    def ayudaIntervalo(extremo):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""
        if extremo == "a":
            text = "Escribir extremo izquierdo del intervalo"
        elif extremo == "b":
            text = "Escribir extremo derecho del intervalo"
        elif extremo == "tol":
            text = "Escribir tolerancia --> ejemplo: 1e-5"
        elif extremo == "punto":
            text = "Escribir punto inicial"
        txt.insert(INSERT, text)

    def getGraph():
        function = fxn.get()
        replacements = {
            'sin' : 'np.sin',
            'cos' : 'np.cos',
            'log': 'np.log',
            'exp': 'np.exp',
            'sqrt': 'np.sqrt',
            '^': '**',
        }

        for old, new in replacements.items():
            function = function.replace(old, new)
        return graph(function)

    def clicked():
        txt.delete(1.0, END)
        print("fxn",fxn.get(),"p0",p0.get(),"tol",toln.get())
        n = NewtonR(fxn.get(),p0.get(),toln.get())
        n = n.solution()
        txt.insert(INSERT, n)
    newwin = Toplevel(window)
    newwin.geometry('600x500')
    newwin.title("Newton Raphson")
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    fxLabel = Label(panel, text="f(x):")
    fxLabel.grid(column=0,row=0)
    p0Label = Label(panel, text="Punto inicial:")
    p0Label.grid(column=0, row=1)
    tolLabel = Label(panel, text="Tolerancia:")
    tolLabel.grid(column=0, row=2)
    fxn = Entry(panel, width=20)
    fxn.grid(column=1, row=0)
    p0 = Entry(panel, width=20)
    p0.grid(column=1, row=1)
    toln = Entry(panel, width=20)
    toln.grid(column=1, row=2)

    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("punto"))
    btna.grid(column=3, row=1)
    btnb = Button(panel, text="?", command=lambda: ayudaFuncion())
    btnb.grid(column=3, row=0)
    btntol = Button(panel, text="?", command=lambda: ayudaIntervalo("tol"))
    btntol.grid(column=3, row=2)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=7)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=0, row=7)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def Sec():

    def f(f,x):
        return eval(f)

    def graph(function):
        fig = plt.figure()
        x = np.arange(-1000,1000,0.1)
        y = f(function,x)
        plt.ylim( [-1000,1000] )
        plt.xlim( [-1000,1000] )
        plt.plot(x,y,color="green")
        plt.plot([-1000,1000],[0,0],color="black")
        plt.plot([0,0],[-1000,1000],color="black")

        plt.show()

    def getGraph():
        function = fx.get()
        if function=="": return
        replacements = {
            'sin' : 'np.sin',
            'cos' : 'np.cos',
            'log': 'np.log',
            'exp': 'np.exp',
            'sqrt': 'np.sqrt',
            '^': '**',
        }

        for old, new in replacements.items():
            function = function.replace(old, new)
        return graph(function)

    def ayudaFuncion():
        newWin = Toplevel(newwin)
        newWin.geometry('400x250')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir función\n\n"
        text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
        text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(x) + sin(3*x) - tan(x/7) \n\n"
        text += "Exponenciales: exp()\nEjemplo: e^(3x) se escribiría así: exp(3*x) \n\n"
        text += "Logarítmicas: log()\nEjemplo: log((2*x)^3)\n\n"
        txt.insert(INSERT, text)

    def ayudaIntervalo(extremo):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""
        if extremo == "a":
            text = "Escribir extremo izquierdo del intervalo"
        elif extremo == "b":
            text = "Escribir extremo derecho del intervalo"
        elif extremo == "tol":
            text = "Escribir tolerancia --> ejemplo: 1e-5"
        elif extremo == "punto0":
            text = "Escribir punto 0"
        elif extremo == "punto1":
            text = "Escribir punto 1"
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        s = Secante(fx.get(), p0.get(), p1.get(), tol.get())
        s = s.solution()
        txt.insert(INSERT, s)
    newwin = Toplevel(window)
    newwin.geometry('600x500')
    newwin.title("Secante")
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    ft = Label(panel, text="f(x):")
    ft.grid(column=0, row=0)
    p0 = Label(panel, text="Punto 0:")
    p0.grid(column=0, row=1)
    P1 = Label(panel, text="Punto 1:")
    P1.grid(column=0, row=2)
    tol = Label(panel, text="Tolerancia:")
    tol.grid(column=0, row=3)
    fx = Entry(panel, width=20)
    fx.grid(column=1, row=0)
    p0 = Entry(panel, width=20)
    p0.grid(column=1, row=1)
    p1 = Entry(panel, width=20)
    p1.grid(column=1, row=2)
    tol = Entry(panel, width=20)
    tol.grid(column=1, row=3)

    btnfx = Button(panel, text="?", command=ayudaFuncion)
    btnfx.grid(column=3, row=0)
    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("punto0"))
    btna.grid(column=3, row=1)
    btnb = Button(panel, text="?", command=lambda: ayudaIntervalo("punto1"))
    btnb.grid(column=3, row=2)
    btntol = Button(panel, text="?", command=lambda: ayudaIntervalo("tol"))
    btntol.grid(column=3, row=3)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=7)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=0, row=7)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def PosFalsa():

    def f(f,x):
        return eval(f)

    def graph(function):

        fig = plt.figure()
        x = np.arange(-10,10,0.1)
        y = f(function,x)
        plt.ylim( [-10,10] )
        plt.xlim( [-10,10] )
        plt.plot(x,y,color="green")
        plt.plot([-10,10],[0,0],color="black")
        plt.plot([0,0],[-10,10],color="black")

        plt.show()

    def getGraph():
        function = fx.get()
        replacements = {
            'sin' : 'np.sin',
            'cos' : 'np.cos',
            'log': 'np.log',
            'exp': 'np.exp',
            'sqrt': 'np.sqrt',
            '^': '**',
        }

        for old, new in replacements.items():
            function = function.replace(old, new)
        return graph(function)

    def ayudaFuncion():
        newWin = Toplevel(newwin)
        newWin.geometry('400x250')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir función\n\n"
        text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
        text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(x) + sin(3*x) - tan(x/7) \n\n"
        text += "Exponenciales: exp()\nEjemplo: e^(3x) se escribiría así: exp(3*x) \n\n"
        text += "Logarítmicas: log()\nEjemplo: log((2*x)^3)\n\n"
        txt.insert(INSERT, text)

    def ayudaIntervalo(extremo):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""
        if extremo == "a":
            text = "Escribir extremo izquierdo del intervalo"
        elif extremo == "b":
            text = "Escribir extremo derecho del intervalo"
        elif extremo == "tol":
            text = "Escribir tolerancia --> ejemplo: 1e-5"
        elif extremo == "punto0":
            text = "Escribir punto 0"
        elif extremo == "punto1":
            text = "Escribir punto 1"
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        p = PosicionFalsa(fx.get(), p0.get(), p1.get(), tol.get())
        p = p.solution()
        txt.insert(INSERT, p)
    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    ff = Label(panel, text="f(x):")
    ff.grid(column=0, row=0)
    p0 = Label(panel, text="Punto 0:")
    p0.grid(column=0, row=1)
    P1 = Label(panel, text="Punto 1:")
    P1.grid(column=0, row=2)
    tol = Label(panel, text="Tolerancia:")
    tol.grid(column=0, row=3)
    fx = Entry(panel, width=20)
    fx.grid(column=1, row=0)
    p0 = Entry(panel, width=20)
    p0.grid(column=1, row=1)
    p1 = Entry(panel, width=20)
    p1.grid(column=1, row=2)
    tol = Entry(panel, width=20)
    tol.grid(column=1, row=3)

    btnfx = Button(panel, text="?", command=ayudaFuncion)
    btnfx.grid(column=3, row=0)
    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("punto0"))
    btna.grid(column=3, row=1)
    btnb = Button(panel, text="?", command=lambda: ayudaIntervalo("punto1"))
    btnb.grid(column=3, row=2)
    btntol = Button(panel, text="?", command=lambda: ayudaIntervalo("tol"))
    btntol.grid(column=3, row=3)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=4)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=0, row=4)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def Mull():
    def f(f, x):
        return eval(f)

    def graph(function):
        fig = plt.figure()
        x = np.arange(-20, 20, 0.1)
        y = f(function, x)
        plt.ylim([-20, 20])
        plt.xlim([-20, 20])
        plt.plot(x, y, color="green")
        plt.plot([-20, 20], [0, 0], color="black")
        plt.plot([0, 0], [-20, 20], color="black")

        plt.show()

    def getGraph():
        if coef.get() == "" or g.get() == "": txt.insert(INSERT, "Escriba coeficientes y grado para graficar")
        m = Muller(g.get(), (coef.get()).split(','))
        poli = ""
        for i in range(0, m.grado+1):
            if poli == "": poli = poli + "(" + str(m.coef[i]) + ")*x**" + str(i)
            else: poli = poli + "+" + "(" + str(m.coef[i]) + ")*x**" + str(i)
        function = poli
        replacements = {
            'sin': 'np.sin',
            'cos': 'np.cos',
            'log': 'np.log',
            'exp': 'np.exp',
            'sqrt': 'np.sqrt',
            '^': '**',
        }

        for old, new in replacements.items():
            function = function.replace(old, new)
        return graph(function)

    def ayudaIntervalo(extremo):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""
        if extremo == "coef":
            newWin.geometry('600x150')
            text = "Escribir coeficientes del polinomio empezando por la variable de menor grado.\n\nEscritos separados por comas, sin espacios.\n\nDebe de escribir n+1 coeficientes, siendo n el grado del polinomio.\n\nEjemplo: 2*x^2+3*x-1 --> -1,3,2"
        elif extremo == "grado":
            text = "Escribir grado del polinomio"
        elif extremo == "b":
            text = "Escribir extremo derecho del intervalo"
        elif extremo == "tol":
            text = "Escribir tolerancia --> ejemplo: 1e-5"
        elif extremo == "punto1":
            text = "Escribir punto 1"
        elif extremo == "punto2":
            text = "Escribir punto 2"
        elif extremo == "punto3":
            text = "Escribir punto 3"
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        m = Muller(g.get(), (coef.get()).split(','), x0.get(), x1.get(), x2.get(), tol.get())
        m = m.solution()
        txt.insert(INSERT, m)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    g = Label(panel, text="Grado del polinomio:")
    g.grid(column=0, row=0)
    coef = Label(panel, text="Coeficientes:")
    coef.grid(column=0, row=1)
    x0 = Label(panel, text="Punto 1:")
    x0.grid(column=0, row=2)
    x1 = Label(panel, text="Punto 2:")
    x1.grid(column=0, row=3)
    x2 = Label(panel, text="Punto 3:")
    x2.grid(column=0, row=4)
    tol = Label(panel, text="Tolerancia:")
    tol.grid(column=0, row=5)
    g = Entry(panel, width=20)
    g.grid(column=1, row=0)
    coef = Entry(panel, width=20)
    coef.grid(column=1, row=1)
    x0 = Entry(panel, width=20)
    x0.grid(column=1, row=2)
    x1 = Entry(panel, width=20)
    x1.grid(column=1, row=3)
    x2 = Entry(panel, width=20)
    x2.grid(column=1, row=4)
    tol = Entry(panel, width=20)
    tol.grid(column=1, row=5)

    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("coef"))
    btna.grid(column=3, row=1)
    btnb = Button(panel, text="?", command=lambda: ayudaIntervalo("grado"))
    btnb.grid(column=3, row=0)
    btntol = Button(panel, text="?", command=lambda: ayudaIntervalo("tol"))
    btntol.grid(column=3, row=5)
    btntol = Button(panel, text="?", command=lambda: ayudaIntervalo("punto1"))
    btntol.grid(column=3, row=2)
    btntol = Button(panel, text="?", command=lambda: ayudaIntervalo("punto2"))
    btntol.grid(column=3, row=3)
    btntol = Button(panel, text="?", command=lambda: ayudaIntervalo("punto3"))
    btntol.grid(column=3, row=4)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=6)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=0, row=6)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def Horn():

    def f(f, x):
        return eval(f)

    def graph(function):
        fig = plt.figure()
        x = np.arange(-10, 10, 0.1)
        y = f(function, x)
        plt.ylim([-10, 10])
        plt.xlim([-10, 10])
        plt.plot(x, y, color="green")
        plt.plot([-10, 10], [0, 0], color="black")
        plt.plot([0, 0], [-10, 10], color="black")

        plt.show()

    def getGraph():
        if coef.get() == "" or g.get() == "": txt.insert(INSERT, "Escriba coeficientes y grado para graficar")
        horner = Horner(g.get(), (coef.get()).split(','))
        poli = ""
        for i in range(0, horner.grado+1):
            if poli == "": poli = poli + "(" + str(horner.coef[i]) + ")*x**" + str(i)
            else: poli = poli + "+" + "(" + str(horner.coef[i]) + ")*x**" + str(i)
        function = poli
        replacements = {
            'sin': 'np.sin',
            'cos': 'np.cos',
            'log': 'np.log',
            'exp': 'np.exp',
            'sqrt': 'np.sqrt',
            '^': '**',
        }

        for old, new in replacements.items():
            function = function.replace(old, new)
        return graph(function)

    def ayudaIntervalo(extremo):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""
        if extremo == "coef":
            newWin.geometry('600x150')
            text = "Escribir coeficientes del polinomio empezando por la variable de menor grado.\n\nEscritos separados por comas, sin espacios.\n\nDebe de escribir n+1 coeficientes, siendo n el grado del polinomio.\n\nEjemplo: 2*x^2+3*x-1 --> -1,3,2"
        elif extremo == "grado":
            text = "Escribir grado del polinomio"
        elif extremo == "b":
            text = "Escribir extremo derecho del intervalo"
        elif extremo == "tol":
            text = "Escribir tolerancia --> ejemplo: 1e-5"
        elif extremo == "punto1":
            text = "Escribir punto 1"
        elif extremo == "punto2":
            text = "Escribir punto 2"
        elif extremo == "punto3":
            text = "Escribir punto 3"
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        horner = Horner(g.get(), (coef.get()).split(','), pInit.get(), tol.get())
        horner = horner.solution()
        txt.insert(INSERT, horner)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    g = Label(panel, text="Grado del polinomio:")
    g.grid(column=0, row=0)
    coef = Label(panel, text="Coeficientes:")
    coef.grid(column=0, row=1)
    pInit = Label(panel, text="Punto 1:")
    pInit.grid(column=0, row=2)
    tol = Label(panel, text="Tolerancia:")
    tol.grid(column=0, row=3)
    g = Entry(panel, width=20)
    g.grid(column=1, row=0)
    coef = Entry(panel, width=20)
    coef.grid(column=1, row=1)
    pInit = Entry(panel, width=20)
    pInit.grid(column=1, row=2)
    tol = Entry(panel, width=20)
    tol.grid(column=1, row=3)

    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("coef"))
    btna.grid(column=3, row=1)
    btnb = Button(panel, text="?", command=lambda: ayudaIntervalo("grado"))
    btnb.grid(column=3, row=0)
    btntol = Button(panel, text="?", command=lambda: ayudaIntervalo("tol"))
    btntol.grid(column=3, row=3)
    btntol = Button(panel, text="?", command=lambda: ayudaIntervalo("punto1"))
    btntol.grid(column=3, row=2)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=4)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=0, row=4)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def Lag():

    def f(f, x):
        return eval(f)

    def graph(function):
        fig = plt.figure()
        x = np.arange(-10, 10, 0.1)
        y = f(function, x)
        plt.ylim([-10, 10])
        plt.xlim([-10, 10])
        plt.plot(x, y, color="green")
        plt.plot([-10, 10], [0, 0], color="black")
        plt.plot([0, 0], [-10, 10], color="black")

        plt.show()

    def getGraph():
        function = fx.get()
        replacements = {
            'sin': 'np.sin',
            'cos': 'np.cos',
            'log': 'np.log',
            'exp': 'np.exp',
            'sqrt': 'np.sqrt',
            '^': '**',
        }

        for old, new in replacements.items():
            function = function.replace(old, new)
        return graph(function)

    def ayudaIntervalo(extremo):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""
        if extremo == "coef":
            newWin.geometry('600x150')
            text = "Escribir valores de x que se utilizarán para formar el polinomio.\n\nEscritos separados por comas, sin espacios.\n\nDebe de escribir n+1 coeficientes, siendo n el grado del polinomio.\n\nEjemplo: -1,3,2"
        elif extremo == "grado":
            text = "Escribir grado del polinomio"
        elif extremo == "b":
            text = "Escribir extremo derecho del intervalo"
        elif extremo == "tol":
            text = "Escribir tolerancia --> ejemplo: 1e-5"
        elif extremo == "punto1":
            text = "Escribir punto 1"
        elif extremo == "punto2":
            text = "Escribir punto 2"
        elif extremo == "punto3":
            text = "Escribir punto 3"
        elif extremo == "punto":
            newWin.geometry('500x80')
            text = "Escribir punto a evaluar. Es opcional. \nSólo si se quiere la evaluación del polinomio en ese punto."
        txt.insert(INSERT, text)

    def ayudaFuncion():
        newWin = Toplevel(newwin)
        newWin.geometry('400x250')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir función\n\n"
        text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
        text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(x) + sin(3*x) - tan(x/7) \n\n"
        text += "Exponenciales: exp()\nEjemplo: e^(3x) se escribiría así: exp(3*x) \n\n"
        text += "Logarítmicas: log()\nEjemplo: log((2*x)^3)\n\n"
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        lagrange = Lagrange(fx.get(), g.get(), (coef.get()).split(","), punto.get())
        lagrange = lagrange.solution()
        txt.insert(INSERT, lagrange)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    fx = Label(panel, text="f(x):")
    fx.grid(column=0, row=0)
    g = Label(panel, text="Grado:")
    g.grid(column=0, row=1)
    coef = Label(panel, text="Coeficientes:")
    coef.grid(column=0, row=2)
    punto = Label(panel, text="Punto a evaluar:")
    punto.grid(column=0, row=3)
    fx = Entry(panel, width=20)
    fx.grid(column=1, row=0)
    g = Entry(panel, width=20)
    g.grid(column=1, row=1)
    coef = Entry(panel, width=20)
    coef.grid(column=1, row=2)
    punto = Entry(panel, width=20)
    punto.grid(column=1, row=3)

    btnfx = Button(panel, text="?", command=lambda: ayudaFuncion())
    btnfx.grid(column=3, row=0)
    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("coef"))
    btna.grid(column=3, row=2)
    btnb = Button(panel, text="?", command=lambda: ayudaIntervalo("grado"))
    btnb.grid(column=3, row=1)
    btntol = Button(panel, text="?", command=lambda: ayudaIntervalo("punto"))
    btntol.grid(column=3, row=3)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=4)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=0, row=4)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def Div():

    def f(f, x):
        return eval(f)

    def graph(x, y):
        fig = plt.figure()
        x = np.array(x)
        y = np.array(y)
        plt.ylim([-100, 100])
        plt.xlim([-100, 100])
        plt.scatter(x, y)
        plt.plot([-100, 100], [0, 0], color="black")
        plt.plot([0, 0], [-100, 100], color="black")

        plt.show()

    def getGraph():
        dif = difDivididas(num.get(), (X.get()).split(","), (fX.get()).split(","), punto.get())

        return graph(dif.X,dif.fX)

    def ayudaIntervalo(extremo):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""
        if extremo == "X":
            newWin.geometry('600x150')
            text = "Escribir valores de x.\n\nEscritos separados por comas, sin espacios.\n\nDebe de escribir n+1 coeficientes, siendo n el número de puntos.\n\nEjemplo: -1,3,2"
        elif extremo == "numPuntos":
            text = "Escribir número de puntos"
        elif extremo == "fX":
            newWin.geometry('600x150')
            text = "Escribir los valores f(x), es decir, los valores de x evaluados en la función.\n\nEscritos separados por comas, sin espacios.\n\nDebe de escribir n+1 coeficientes, siendo n el número de puntos.\n\nEjemplo: -1,3,2"
        elif extremo == "tol":
            text = "Escribir tolerancia --> ejemplo: 1e-5"
        elif extremo == "punto1":
            text = "Escribir punto 1"
        elif extremo == "punto2":
            text = "Escribir punto 2"
        elif extremo == "punto3":
            text = "Escribir punto 3"
        elif extremo == "punto":
            newWin.geometry('500x80')
            text = "Escribir punto a evaluar. Es opcional. \nSólo si se quiere la evaluación del polinomio en ese punto."
        txt.insert(INSERT, text)

    def ayudaFuncion():
        newWin = Toplevel(newwin)
        newWin.geometry('400x250')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir función\n\n"
        text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
        text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(x) + sin(3*x) - tan(x/7) \n\n"
        text += "Exponenciales: exp()\nEjemplo: e^(3x) se escribiría así: exp(3*x) \n\n"
        text += "Logarítmicas: log()\nEjemplo: log((2*x)^3)\n\n"
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        dif = difDivididas(num.get(), (X.get()).split(","), (fX.get()).split(","), punto.get())
        dif = dif.solution()
        txt.insert(INSERT, dif)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    num = Label(panel, text="Número de puntos:")
    num.grid(column=0, row=0)
    X = Label(panel, text="X:")
    X.grid(column=0, row=1)
    fX = Label(panel, text="f(X):")
    fX.grid(column=0, row=2)
    punto = Label(panel, text="Punto a evaluar:")
    punto.grid(column=0, row=3)
    num = Entry(panel, width=20)
    num.grid(column=1, row=0)
    X = Entry(panel, width=20)
    X.grid(column=1, row=1)
    fX = Entry(panel, width=20)
    fX.grid(column=1, row=2)
    punto = Entry(panel, width=20)
    punto.grid(column=1, row=3)

    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("numPuntos"))
    btna.grid(column=3, row=0)
    btnb = Button(panel, text="?", command=lambda: ayudaIntervalo("X"))
    btnb.grid(column=3, row=1)
    btntol = Button(panel, text="?", command=lambda: ayudaIntervalo("fX"))
    btntol.grid(column=3, row=2)
    btntol = Button(panel, text="?", command=lambda: ayudaIntervalo("punto"))
    btntol.grid(column=3, row=3)


    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=4)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=0, row=4)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def Herm():

    def f(f, x):
        return eval(f)

    def graph(x, y):
        fig = plt.figure()
        x = np.array(x)
        y = np.array(y)
        plt.ylim([-100, 100])
        plt.xlim([-100, 100])
        plt.scatter(x, y)
        plt.plot([-100, 100], [0, 0], color="black")
        plt.plot([0, 0], [-100, 100], color="black")

        plt.show()

    def getGraph():

        hermit = Hermit(num.get(), (X.get()).split(","), (fX.get()).split(","),(fX1.get()).split(","), punto.get())

        return graph(hermit.xi,hermit.fi)

    def ayudaIntervalo(extremo):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""
        if extremo == "X":
            newWin.geometry('600x150')
            text = "Escribir valores de x.\n\nEscritos separados por comas, sin espacios.\n\nDebe de escribir n+1 coeficientes, siendo n el número de puntos.\n\nEjemplo: -1,3,2"
        elif extremo == "numPuntos":
            text = "Escribir número de puntos"
        elif extremo == "fX":
            newWin.geometry('600x150')
            text = "Escribir los valores f(x), es decir, los valores de x evaluados en la función.\n\nEscritos separados por comas, sin espacios.\n\nDebe de escribir n+1 coeficientes, siendo n el número de puntos.\n\nEjemplo: -1,3,2"
        elif extremo == "f'":
            newWin.geometry('600x150')
            text = "Escribir los valores f'(x), es decir, los valores de x evaluados en la derivada de la función.\n\nEscritos separados por comas, sin espacios.\n\nDebe de escribir n+1 coeficientes, siendo n el número de puntos.\n\nEjemplo: -1,3,2"
        elif extremo == "tol":
            text = "Escribir tolerancia --> ejemplo: 1e-5"
        elif extremo == "punto1":
            text = "Escribir punto 1"
        elif extremo == "punto2":
            text = "Escribir punto 2"
        elif extremo == "punto3":
            text = "Escribir punto 3"
        elif extremo == "punto":
            newWin.geometry('500x80')
            text = "Escribir punto a evaluar. Es opcional. \nSólo si se quiere la evaluación del polinomio en ese punto."
        txt.insert(INSERT, text)

    def ayudaFuncion():
        newWin = Toplevel(newwin)
        newWin.geometry('400x250')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir función\n\n"
        text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
        text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(x) + sin(3*x) - tan(x/7) \n\n"
        text += "Exponenciales: exp()\nEjemplo: e^(3x) se escribiría así: exp(3*x) \n\n"
        text += "Logarítmicas: log()\nEjemplo: log((2*x)^3)\n\n"
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        hermit = Hermit(num.get(), (X.get()).split(","), (fX.get()).split(","),(fX1.get()).split(","), punto.get())
        hermit = hermit.solution()
        txt.insert(INSERT, hermit)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    num = Label(panel, text="Número de puntos:")
    num.grid(column=0, row=0)
    X = Label(panel, text="X:")
    X.grid(column=0, row=1)
    fX = Label(panel, text="f(X):")
    fX.grid(column=0, row=2)
    fX1 = Label(panel, text="f'(X):")
    fX1.grid(column=0, row=3)
    punto = Label(panel, text="Punto a evaluar:")
    punto.grid(column=0, row=4)
    num = Entry(panel, width=20)
    num.grid(column=1, row=0)
    X = Entry(panel, width=20)
    X.grid(column=1, row=1)
    fX = Entry(panel, width=20)
    fX.grid(column=1, row=2)
    fX1 = Entry(panel, width=20)
    fX1.grid(column=1, row=3)
    punto = Entry(panel, width=20)
    punto.grid(column=1, row=4)

    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("numPuntos"))
    btna.grid(column=3, row=0)
    btnb = Button(panel, text="?", command=lambda: ayudaIntervalo("X"))
    btnb.grid(column=3, row=1)
    btntol = Button(panel, text="?", command=lambda: ayudaIntervalo("fX"))
    btntol.grid(column=3, row=2)
    btntol = Button(panel, text="?", command=lambda: ayudaIntervalo("f'"))
    btntol.grid(column=3, row=3)
    btntol = Button(panel, text="?", command=lambda: ayudaIntervalo("punto"))
    btntol.grid(column=3, row=4)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=5)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=0, row=5)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def ExtremoTres():

    def f(f, x):
        return eval(f)

    def graph(x,y):
        fig = plt.figure()
        x = np.array(x)
        y = np.array(y)
        plt.ylim([-100, 100])
        plt.xlim([-100, 100])
        plt.scatter(x, y)
        plt.plot([-100, 100], [0, 0], color="black")
        plt.plot([0, 0], [-100, 100], color="black")

        plt.show()

    def getGraph():

        dif = Diferenciacion("1",[X.get(),X1.get(),X2.get()],[fX.get(),fX1.get(),fX2.get()])

        return graph(dif.X,dif.fX)

    def ayudaIntervalo():
        newWin = Toplevel(newwin)
        newWin.geometry('600x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""
        text += "Se especifica qué X y en el renglón siguiente se escribe la f(X) correspondiente."
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        dif = Diferenciacion("1",[X.get(),X1.get(),X2.get()],[fX.get(),fX1.get(),fX2.get()])
        dif = dif.solution()
        txt.insert(INSERT, dif)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    X = Label(panel, text="X_0:")
    X.grid(column=0, row=0)
    fX = Label(panel, text="f(X_0):")
    fX.grid(column=0, row=1)
    X1 = Label(panel, text="X_0+h:")
    X1.grid(column=0, row=2)
    fX1 = Label(panel, text="f(X_0+h):")
    fX1.grid(column=0, row=3)
    X2 = Label(panel, text="X_0+2h:")
    X2.grid(column=0, row=4)
    fX2 = Label(panel, text="f(X_0+2h):")
    fX2.grid(column=0, row=5)

    X = Entry(panel, width=20)
    X.grid(column=1, row=0)
    fX = Entry(panel, width=20)
    fX.grid(column=1, row=1)
    X1 = Entry(panel, width=20)
    X1.grid(column=1, row=2)
    fX1 = Entry(panel, width=20)
    fX1.grid(column=1, row=3)
    X2 = Entry(panel, width=20)
    X2.grid(column=1, row=4)
    fX2 = Entry(panel, width=20)
    fX2.grid(column=1, row=5)

    btnb = Button(panel, text="?", command=lambda: ayudaIntervalo())
    btnb.grid(column=3, row=0)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=6)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=0, row=6)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def IntermedioTres():

    def f(f, x):
        return eval(f)

    def graph(x, y):
        fig = plt.figure()
        x = np.array(x)
        y = np.array(y)
        plt.ylim([-100, 100])
        plt.xlim([-100, 100])
        plt.scatter(x, y)
        plt.plot([-100, 100], [0, 0], color="black")
        plt.plot([0, 0], [-100, 100], color="black")

        plt.show()

    def getGraph():

        dif = Diferenciacion("2",[X.get(),X1.get(),X2.get()],[fX.get(),fX1.get(),fX2.get()])

        return graph(dif.X,dif.fX)

    def ayudaIntervalo():
        newWin = Toplevel(newwin)
        newWin.geometry('600x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""
        text += "Se especifica qué X y en el renglón siguiente se escribe la f(X) correspondiente."
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        dif = Diferenciacion("2",[X.get(),X1.get(),X2.get()],[fX.get(),fX1.get(),fX2.get()])
        dif = dif.solution()
        txt.insert(INSERT, dif)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    X = Label(panel, text="X_0-h:")
    X.grid(column=0, row=0)
    fX = Label(panel, text="f(X_0-h):")
    fX.grid(column=0, row=1)
    X1 = Label(panel, text="X_0:")
    X1.grid(column=0, row=2)
    fX1 = Label(panel, text="f(X_0):")
    fX1.grid(column=0, row=3)
    X2 = Label(panel, text="X_0+h:")
    X2.grid(column=0, row=4)
    fX2 = Label(panel, text="f(X_0+h):")
    fX2.grid(column=0, row=5)

    X = Entry(panel, width=20)
    X.grid(column=1, row=0)
    fX = Entry(panel, width=20)
    fX.grid(column=1, row=1)
    X1 = Entry(panel, width=20)
    X1.grid(column=1, row=2)
    fX1 = Entry(panel, width=20)
    fX1.grid(column=1, row=3)
    X2 = Entry(panel, width=20)
    X2.grid(column=1, row=4)
    fX2 = Entry(panel, width=20)
    fX2.grid(column=1, row=5)

    btnb = Button(panel, text="?", command=lambda: ayudaIntervalo())
    btnb.grid(column=3, row=0)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=6)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=0, row=6)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def ExtremoCinco():

    def f(f, x):
        return eval(f)

    def graph(x, y):
        fig = plt.figure()
        x = np.array(x)
        y = np.array(y)
        plt.ylim([-100, 100])
        plt.xlim([-100, 100])
        plt.scatter(x, y)
        plt.plot([-100, 100], [0, 0], color="black")
        plt.plot([0, 0], [-100, 100], color="black")

        plt.show()

    def getGraph():

        dif = Diferenciacion("3",[X.get(),X1.get(),X2.get(),X3.get(),X4.get()],[fX.get(),fX1.get(),fX2.get(),fX3.get(),fX4.get()])

        return graph(dif.X,dif.fX)

    def ayudaIntervalo():
        newWin = Toplevel(newwin)
        newWin.geometry('600x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""
        text += "Se especifica qué X y en el renglón siguiente se escribe la f(X) correspondiente."
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        dif = Diferenciacion("3",[X.get(),X1.get(),X2.get(),X3.get(),X4.get()],[fX.get(),fX1.get(),fX2.get(),fX3.get(),fX4.get()])
        dif = dif.solution()
        txt.insert(INSERT, dif)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    X = Label(panel, text="X_0:")
    X.grid(column=0, row=0)
    fX = Label(panel, text="f(X_0):")
    fX.grid(column=0, row=1)
    X1 = Label(panel, text="X_0+h:")
    X1.grid(column=0, row=2)
    fX1 = Label(panel, text="f(X_0+h):")
    fX1.grid(column=0, row=3)
    X2 = Label(panel, text="X_0+2h:")
    X2.grid(column=0, row=4)
    fX2 = Label(panel, text="f(X_0+2h):")
    fX2.grid(column=0, row=5)
    X3 = Label(panel, text="X_0+3h:")
    X3.grid(column=0, row=6)
    fX3 = Label(panel, text="f(X_0+3h):")
    fX3.grid(column=0, row=7)
    X4 = Label(panel, text="X_0+4h:")
    X4.grid(column=0, row=8)
    fX4 = Label(panel, text="f(X_0+4h):")
    fX4.grid(column=0, row=9)

    X = Entry(panel, width=20)
    X.grid(column=1, row=0)
    fX = Entry(panel, width=20)
    fX.grid(column=1, row=1)
    X1 = Entry(panel, width=20)
    X1.grid(column=1, row=2)
    fX1 = Entry(panel, width=20)
    fX1.grid(column=1, row=3)
    X2 = Entry(panel, width=20)
    X2.grid(column=1, row=4)
    fX2 = Entry(panel, width=20)
    fX2.grid(column=1, row=5)
    X3 = Entry(panel, width=20)
    X3.grid(column=1, row=6)
    fX3 = Entry(panel, width=20)
    fX3.grid(column=1, row=7)
    X4 = Entry(panel, width=20)
    X4.grid(column=1, row=8)
    fX4 = Entry(panel, width=20)
    fX4.grid(column=1, row=9)

    btnb = Button(panel, text="?", command=lambda: ayudaIntervalo())
    btnb.grid(column=3, row=0)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=10)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=0, row=10)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def IntermedioCinco():

    def f(f, x):
        return eval(f)

    def graph(x, y):
        fig = plt.figure()
        x = np.array(x)
        y = np.array(y)
        plt.ylim([-100, 100])
        plt.xlim([-100, 100])
        plt.scatter(x, y)
        plt.plot([-100, 100], [0, 0], color="black")
        plt.plot([0, 0], [-100, 100], color="black")

        plt.show()

    def getGraph():
        dif = Diferenciacion("4", [X.get(), X1.get(), X2.get(), X3.get(), X4.get()],
                             [fX.get(), fX1.get(), fX2.get(), fX3.get(), fX4.get()])

        return graph(dif.X, dif.fX)

    def ayudaIntervalo():
        newWin = Toplevel(newwin)
        newWin.geometry('600x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""
        text += "Se especifica qué X y en el renglón siguiente se escribe la f(X) correspondiente."
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        dif = Diferenciacion("4", [X.get(), X1.get(), X2.get(), X3.get(), X4.get()],
                             [fX.get(), fX1.get(), fX2.get(), fX3.get(), fX4.get()])
        dif = dif.solution()
        txt.insert(INSERT, dif)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    X = Label(panel, text="X_0:")
    X.grid(column=0, row=0)
    fX = Label(panel, text="f(X_0):")
    fX.grid(column=0, row=1)
    X1 = Label(panel, text="X_0-h:")
    X1.grid(column=0, row=2)
    fX1 = Label(panel, text="f(X_0-h):")
    fX1.grid(column=0, row=3)
    X2 = Label(panel, text="X_0-2h:")
    X2.grid(column=0, row=4)
    fX2 = Label(panel, text="f(X_0-2h):")
    fX2.grid(column=0, row=5)
    X3 = Label(panel, text="X_0+h:")
    X3.grid(column=0, row=6)
    fX3 = Label(panel, text="f(X_0+h):")
    fX3.grid(column=0, row=7)
    X4 = Label(panel, text="X_0+2h:")
    X4.grid(column=0, row=8)
    fX4 = Label(panel, text="f(X_0+2h):")
    fX4.grid(column=0, row=9)

    X = Entry(panel, width=20)
    X.grid(column=1, row=0)
    fX = Entry(panel, width=20)
    fX.grid(column=1, row=1)
    X1 = Entry(panel, width=20)
    X1.grid(column=1, row=2)
    fX1 = Entry(panel, width=20)
    fX1.grid(column=1, row=3)
    X2 = Entry(panel, width=20)
    X2.grid(column=1, row=4)
    fX2 = Entry(panel, width=20)
    fX2.grid(column=1, row=5)
    X3 = Entry(panel, width=20)
    X3.grid(column=1, row=6)
    fX3 = Entry(panel, width=20)
    fX3.grid(column=1, row=7)
    X4 = Entry(panel, width=20)
    X4.grid(column=1, row=8)
    fX4 = Entry(panel, width=20)
    fX4.grid(column=1, row=9)

    btnb = Button(panel, text="?", command=lambda: ayudaIntervalo())
    btnb.grid(column=3, row=0)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=10)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=0, row=10)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def IntAbierta():

    def f(f, x):
        return eval(f)

    def graph2(function):
        fig = plt.figure()
        x = np.arange(-10, 10, 0.1)
        y = f(function, x)
        plt.ylim([-10, 10])
        plt.xlim([-10, 10])
        plt.plot(x, y, color="green")
        plt.plot([-10, 10], [0, 0], color="black")
        plt.plot([0, 0], [-10, 10], color="black")

        plt.show()

    def graph(x, y):
        fig = plt.figure()
        x = np.array(x)
        y = np.array(y)
        plt.ylim([-10, 10])
        plt.xlim([-10, 10])
        plt.scatter(x, y)
        plt.plot([-10, 10], [0, 0], color="black")
        plt.plot([0, 0], [-10, 10], color="black")

        plt.show()

    def getGraph():
        dif = Integracion("2",fx.get(),"0",(X.get()).split(','),(fX.get()).split(','),"0","0")

        if dif.f == "": return graph(dif.X, dif.fX)
        else:

            function = fx.get()
            replacements = {
                'sin': 'np.sin',
                'log': 'np.log',
                'cos': 'np.cos',
                'exp': 'np.exp',
                'sqrt': 'np.sqrt',
                '^': '**',
            }

            for old, new in replacements.items():
                function = function.replace(old, new)

            return graph2(function)

    def ayudaFuncion():
        newWin = Toplevel(newwin)
        newWin.geometry('600x250')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir función. Si se escribe la función, ya no se escribe en X y en f(X).\n\n"
        text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
        text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(x) + sin(3*x) - tan(x/7) \n\n"
        text += "Exponenciales: exp()\nEjemplo: e^(3x) se escribiría así: exp(3*x) \n\n"
        text += "Logarítmicas: log()\nEjemplo: log((2*x)^3)\n\n"
        txt.insert(INSERT, text)

    def ayudaIntervalo(op):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""

        if op == "funcion":
            ayudaFuncion()
        elif op == "X":
            newWin.geometry('600x150')
            text = "Escribir valores de x (si no se escribió en la función).\n\nEscritos separados por comas, sin espacios.\n\nEjemplo: -1,3,2"
        elif op == "fX":
            newWin.geometry('600x150')
            text = "Escribir los valores f(x) (si no se escribió en la función), es decir, los valores de x evaluados en la función.\n\nEscritos separados por comas, sin espacios.\n\nEjemplo: -1,3,2"
        elif op == "a":
            text = "Escribir extremo izquierdo del intervalo."
        elif op == "b":
            text = "Escribir extremo derecho del intervalo."
        elif op == "n":
            newWin.geometry('600x150')
            text = "Escribir n.\n\nSi se escribió en X y f(X), n es x-1, siendo x el número de puntos escritos.\n\nSi se escribió la función, n puede ser 0, 1, 2 ó 3."
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        print("X:",(X.get()).split(','))
        print(len((X.get()).split(',')))
        dif = Integracion("2",fx.get(),n.get(),(X.get()).split(','),(fX.get()).split(','),a.get(),b.get())
        dif = dif.solution()
        txt.insert(INSERT, dif)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    fx = Label(panel, text="f(x):")
    fx.grid(column=0, row=0)
    X = Label(panel, text="X:")
    X.grid(column=0, row=1)
    fX = Label(panel, text="f(X):")
    fX.grid(column=0, row=2)
    a = Label(panel, text="a:")
    a.grid(column=0, row=3)
    b = Label(panel, text="b:")
    b.grid(column=0, row=4)
    n = Label(panel, text="n:")
    n.grid(column=0, row=5)

    fx = Entry(panel, width=20)
    fx.grid(column=1, row=0)
    X = Entry(panel, width=20)
    X.grid(column=1, row=1)
    fX = Entry(panel, width=20)
    fX.grid(column=1, row=2)
    a = Entry(panel, width=20)
    a.grid(column=1, row=3)
    b = Entry(panel, width=20)
    b.grid(column=1, row=4)
    n = Entry(panel, width=20)
    n.grid(column=1, row=5)

    btnf = Button(panel, text="?", command=lambda: ayudaFuncion())
    btnf.grid(column=3, row=0)
    btng = Button(panel, text="?", command=lambda: ayudaIntervalo("X"))
    btng.grid(column=3, row=1)
    btnb = Button(panel, text="?", command=lambda: ayudaIntervalo("fX"))
    btnb.grid(column=3, row=2)
    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("a"))
    btna.grid(column=3, row=3)
    btnc = Button(panel, text="?", command=lambda: ayudaIntervalo("b"))
    btnc.grid(column=3, row=4)
    btnd = Button(panel, text="?", command=lambda: ayudaIntervalo("n"))
    btnd.grid(column=3, row=5)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=6)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=0, row=6)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def IntCerrada():

    def f(f, x):
        return eval(f)

    def graph2(function):
        fig = plt.figure()
        x = np.arange(-10, 10, 0.1)
        y = f(function, x)
        plt.ylim([-10, 10])
        plt.xlim([-10, 10])
        plt.plot(x, y, color="green")
        plt.plot([-10, 10], [0, 0], color="black")
        plt.plot([0, 0], [-10, 10], color="black")

        plt.show()

    def graph(x, y):
        fig = plt.figure()
        x = np.array(x)
        y = np.array(y)
        plt.ylim([-10, 10])
        plt.xlim([-10, 10])
        plt.scatter(x, y)
        plt.plot([-10, 10], [0, 0], color="black")
        plt.plot([0, 0], [-10, 10], color="black")

        plt.show()

    def getGraph():
        dif = Integracion("1",fx.get(),"0",(X.get()).split(','),(fX.get()).split(','),"0","0")

        if dif.f == "": return graph(dif.X, dif.fX)
        else:
            function = fx.get()
            replacements = {
                'sin': 'np.sin',
                'log': 'np.log',
                'cos': 'np.cos',
                'exp': 'np.exp',
                'sqrt': 'np.sqrt',
                '^': '**',
            }

            for old, new in replacements.items():
                function = function.replace(old, new)

            return graph2(function)

    def ayudaFuncion():
        newWin = Toplevel(newwin)
        newWin.geometry('600x250')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir función. Si se escribe la función, ya no se escribe en X y en f(X).\n\n"
        text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
        text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(x) + sin(3*x) - tan(x/7) \n\n"
        text += "Exponenciales: exp()\nEjemplo: e^(3x) se escribiría así: exp(3*x) \n\n"
        text += "Logarítmicas: log()\nEjemplo: log((2*x)^3)\n\n"
        txt.insert(INSERT, text)

    def ayudaIntervalo(op):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""

        if op == "funcion":
            ayudaFuncion()
        elif op == "X":
            newWin.geometry('600x150')
            text = "Escribir valores de x (si no se escribió en la función).\n\nEscritos separados por comas, sin espacios.\n\nEjemplo: -1,3,2"
        elif op == "fX":
            newWin.geometry('600x150')
            text = "Escribir los valores f(x) (si no se escribió en la función), es decir, los valores de x evaluados en la función.\n\nEscritos separados por comas, sin espacios.\n\nEjemplo: -1,3,2"
        elif op == "a":
            text = "Escribir extremo izquierdo del intervalo."
        elif op == "b":
            text = "Escribir extremo derecho del intervalo."
        elif op == "n":
            newWin.geometry('600x150')
            text = "Escribir n.\n\nSi se escribió en X y f(X), n es x-1, siendo x el número de puntos escritos.\n\nSi se escribió la función, n puede ser 1, 2, 3 ó 4."
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        print("X:",(X.get()).split(','))
        print(len((X.get()).split(',')))
        dif = Integracion("1",fx.get(),n.get(),(X.get()).split(','),(fX.get()).split(','),a.get(),b.get())
        dif = dif.solution()
        txt.insert(INSERT, dif)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    fx = Label(panel, text="f(x):")
    fx.grid(column=0, row=0)
    X = Label(panel, text="X:")
    X.grid(column=0, row=1)
    fX = Label(panel, text="f(X):")
    fX.grid(column=0, row=2)
    a = Label(panel, text="a:")
    a.grid(column=0, row=3)
    b = Label(panel, text="b:")
    b.grid(column=0, row=4)
    n = Label(panel, text="n:")
    n.grid(column=0, row=5)

    fx = Entry(panel, width=20)
    fx.grid(column=1, row=0)
    X = Entry(panel, width=20)
    X.grid(column=1, row=1)
    fX = Entry(panel, width=20)
    fX.grid(column=1, row=2)
    a = Entry(panel, width=20)
    a.grid(column=1, row=3)
    b = Entry(panel, width=20)
    b.grid(column=1, row=4)
    n = Entry(panel, width=20)
    n.grid(column=1, row=5)

    btnf = Button(panel, text="?", command=lambda: ayudaFuncion())
    btnf.grid(column=3, row=0)
    btng = Button(panel, text="?", command=lambda: ayudaIntervalo("X"))
    btng.grid(column=3, row=1)
    btnb = Button(panel, text="?", command=lambda: ayudaIntervalo("fX"))
    btnb.grid(column=3, row=2)
    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("a"))
    btna.grid(column=3, row=3)
    btnc = Button(panel, text="?", command=lambda: ayudaIntervalo("b"))
    btnc.grid(column=3, row=4)
    btnd = Button(panel, text="?", command=lambda: ayudaIntervalo("n"))
    btnd.grid(column=3, row=5)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=6)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=0, row=6)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def IntCompAbierta():

    def f(f, x):
        return eval(f)

    def graph2(function):
        fig = plt.figure()
        x = np.arange(-10, 10, 0.1)
        y = f(function, x)
        plt.ylim([-10, 10])
        plt.xlim([-10, 10])
        plt.plot(x, y, color="green")
        plt.plot([-10, 10], [0, 0], color="black")
        plt.plot([0, 0], [-10, 10], color="black")

        plt.show()

    def graph(x, y):
        fig = plt.figure()
        x = np.array(x)
        y = np.array(y)
        plt.ylim([-10, 10])
        plt.xlim([-10, 10])
        plt.scatter(x, y)
        plt.plot([-10, 10], [0, 0], color="black")
        plt.plot([0, 0], [-10, 10], color="black")

        plt.show()

    def getGraph():
        dif = IntegracionCompuesta("2",fx.get(),"0",(fX.get()).split(','),"0","0")

        if dif.f != "":

            function = fx.get()
            replacements = {
                'sin': 'np.sin',
                'log': 'np.log',
                'cos': 'np.cos',
                'exp': 'np.exp',
                'sqrt': 'np.sqrt',
                '^': '**',
            }

            for old, new in replacements.items():
                function = function.replace(old, new)

            return graph2(function)

    def ayudaFuncion():
        newWin = Toplevel(newwin)
        newWin.geometry('600x250')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir función. Si se escribe la función, ya no se escribe en f(X).\n\n"
        text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
        text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(x) + sin(3*x) - tan(x/7) \n\n"
        text += "Exponenciales: exp()\nEjemplo: e^(3x) se escribiría así: exp(3*x) \n\n"
        text += "Logarítmicas: log()\nEjemplo: log((2*x)^3)\n\n"
        txt.insert(INSERT, text)

    def ayudaIntervalo(op):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""

        if op == "funcion":
            ayudaFuncion()
        elif op == "X":
            newWin.geometry('600x150')
            text = "Escribir valores de x (si no se escribió en la función).\n\nEscritos separados por comas, sin espacios.\n\nDebe de escribir n+1 coeficientes, siendo n el número de puntos.\n\nEjemplo: -1,3,2"
        elif op == "fX":
            newWin.geometry('600x150')
            text = "Escribir los valores f(x) (si no se escribió en la función), es decir, los valores de x evaluados en la función.\n\nEscritos separados por comas, sin espacios.\n\nEjemplo: -1,3,2"
        elif op == "a":
            text = "Escribir extremo izquierdo del intervalo."
        elif op == "b":
            text = "Escribir extremo derecho del intervalo."
        elif op == "n":
            newWin.geometry('600x150')
            text = "Escribir n.\n\nSi se escribió en f(X), n es x-1, siendo x el número de puntos escritos."
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        dif = IntegracionCompuesta("2",fx.get(),n.get(),(fX.get()).split(','),a.get(),b.get())
        dif = dif.solution()
        txt.insert(INSERT, dif)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    fx = Label(panel, text="f(x):")
    fx.grid(column=0, row=0)
    fX = Label(panel, text="f(X):")
    fX.grid(column=0, row=1)
    a = Label(panel, text="a:")
    a.grid(column=0, row=2)
    b = Label(panel, text="b:")
    b.grid(column=0, row=3)
    n = Label(panel, text="n:")
    n.grid(column=0, row=4)

    fx = Entry(panel, width=20)
    fx.grid(column=1, row=0)
    fX = Entry(panel, width=20)
    fX.grid(column=1, row=1)
    a = Entry(panel, width=20)
    a.grid(column=1, row=2)
    b = Entry(panel, width=20)
    b.grid(column=1, row=3)
    n = Entry(panel, width=20)
    n.grid(column=1, row=4)

    btnf = Button(panel, text="?", command=lambda: ayudaFuncion())
    btnf.grid(column=3, row=0)
    btnb = Button(panel, text="?", command=lambda: ayudaIntervalo("fX"))
    btnb.grid(column=3, row=1)
    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("a"))
    btna.grid(column=3, row=2)
    btnc = Button(panel, text="?", command=lambda: ayudaIntervalo("b"))
    btnc.grid(column=3, row=3)
    btnd = Button(panel, text="?", command=lambda: ayudaIntervalo("n"))
    btnd.grid(column=3, row=4)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=6)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=0, row=6)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def TrapecioComp():

    def f(f, x):
        return eval(f)

    def graph2(function):
        fig = plt.figure()
        x = np.arange(-10, 10, 0.1)
        y = f(function, x)
        plt.ylim([-10, 10])
        plt.xlim([-10, 10])
        plt.plot(x, y, color="green")
        plt.plot([-10, 10], [0, 0], color="black")
        plt.plot([0, 0], [-10, 10], color="black")

        plt.show()

    def graph(x, y):
        fig = plt.figure()
        x = np.array(x)
        y = np.array(y)
        plt.ylim([-10, 10])
        plt.xlim([-10, 10])
        plt.scatter(x, y)
        plt.plot([-10, 10], [0, 0], color="black")
        plt.plot([0, 0], [-10, 10], color="black")

        plt.show()

    def getGraph():
        dif = IntegracionCompuesta("0",fx.get(),"0",(fX.get()).split(','),"0","0")

        if dif.f != "":
            function = fx.get()
            replacements = {
                'sin': 'np.sin',
                'log': 'np.log',
                'cos': 'np.cos',
                'exp': 'np.exp',
                'sqrt': 'np.sqrt',
                '^': '**',
            }

            for old, new in replacements.items():
                function = function.replace(old, new)

            return graph2(function)

    def ayudaFuncion():
        newWin = Toplevel(newwin)
        newWin.geometry('600x250')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir función. Si se escribe la función, ya no se escribe en f(X).\n\n"
        text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
        text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(x) + sin(3*x) - tan(x/7) \n\n"
        text += "Exponenciales: exp()\nEjemplo: e^(3x) se escribiría así: exp(3*x) \n\n"
        text += "Logarítmicas: log()\nEjemplo: log((2*x)^3)\n\n"
        txt.insert(INSERT, text)

    def ayudaIntervalo(op):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""

        if op == "funcion":
            ayudaFuncion()
        elif op == "X":
            newWin.geometry('600x150')
            text = "Escribir valores de x (si no se escribió en la función).\n\nEscritos separados por comas, sin espacios.\n\nDebe de escribir n+1 coeficientes, siendo n el número de puntos.\n\nEjemplo: -1,3,2"
        elif op == "fX":
            newWin.geometry('600x150')
            text = "Escribir los valores f(x) (si no se escribió en la función), es decir, los valores de x evaluados en la función.\n\nEscritos separados por comas, sin espacios.\n\nEjemplo: -1,3,2"
        elif op == "a":
            text = "Escribir extremo izquierdo del intervalo."
        elif op == "b":
            text = "Escribir extremo derecho del intervalo."
        elif op == "n":
            newWin.geometry('600x150')
            text = "Escribir n.\n\nSi se escribió en f(X), n es x-1, siendo x el número de puntos escritos."
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        dif = IntegracionCompuesta("0",fx.get(),n.get(),(fX.get()).split(','),a.get(),b.get())
        dif = dif.solution()
        txt.insert(INSERT, dif)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    fx = Label(panel, text="f(x):")
    fx.grid(column=0, row=0)
    fX = Label(panel, text="f(X):")
    fX.grid(column=0, row=1)
    a = Label(panel, text="a:")
    a.grid(column=0, row=2)
    b = Label(panel, text="b:")
    b.grid(column=0, row=3)
    n = Label(panel, text="n:")
    n.grid(column=0, row=4)

    fx = Entry(panel, width=20)
    fx.grid(column=1, row=0)
    fX = Entry(panel, width=20)
    fX.grid(column=1, row=1)
    a = Entry(panel, width=20)
    a.grid(column=1, row=2)
    b = Entry(panel, width=20)
    b.grid(column=1, row=3)
    n = Entry(panel, width=20)
    n.grid(column=1, row=4)

    btnf = Button(panel, text="?", command=lambda: ayudaFuncion())
    btnf.grid(column=3, row=0)
    btnb = Button(panel, text="?", command=lambda: ayudaIntervalo("fX"))
    btnb.grid(column=3, row=1)
    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("a"))
    btna.grid(column=3, row=2)
    btnc = Button(panel, text="?", command=lambda: ayudaIntervalo("b"))
    btnc.grid(column=3, row=3)
    btnd = Button(panel, text="?", command=lambda: ayudaIntervalo("n"))
    btnd.grid(column=3, row=4)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=6)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=0, row=6)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def SimpsonComp():

    def f(f, x):
        return eval(f)

    def graph2(function):
        fig = plt.figure()
        x = np.arange(-10, 10, 0.1)
        y = f(function, x)
        plt.ylim([-10, 10])
        plt.xlim([-10, 10])
        plt.plot(x, y, color="green")
        plt.plot([-10, 10], [0, 0], color="black")
        plt.plot([0, 0], [-10, 10], color="black")

        plt.show()

    def graph(x, y):
        fig = plt.figure()
        x = np.array(x)
        y = np.array(y)
        plt.ylim([-10, 10])
        plt.xlim([-10, 10])
        plt.scatter(x, y)
        plt.plot([-10, 10], [0, 0], color="black")
        plt.plot([0, 0], [-10, 10], color="black")

        plt.show()

    def getGraph():
        dif = IntegracionCompuesta("1",fx.get(),"0",(fX.get()).split(','),"0","0")

        if dif.f != "":
            function = fx.get()
            replacements = {
                'sin': 'np.sin',
                'log': 'np.log',
                'cos': 'np.cos',
                'exp': 'np.exp',
                'sqrt': 'np.sqrt',
                '^': '**',
            }

            for old, new in replacements.items():
                function = function.replace(old, new)

            return graph2(function)

    def ayudaFuncion():
        newWin = Toplevel(newwin)
        newWin.geometry('600x250')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir función. Si se escribe la función, ya no se escribe en f(X).\n\n"
        text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
        text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(x) + sin(3*x) - tan(x/7) \n\n"
        text += "Exponenciales: exp()\nEjemplo: e^(3x) se escribiría así: exp(3*x) \n\n"
        text += "Logarítmicas: log()\nEjemplo: log((2*x)^3)\n\n"
        txt.insert(INSERT, text)

    def ayudaIntervalo(op):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""

        if op == "funcion":
            ayudaFuncion()
        elif op == "X":
            newWin.geometry('600x150')
            text = "Escribir valores de x (si no se escribió en la función).\n\nEscritos separados por comas, sin espacios.\n\nDebe de escribir n+1 coeficientes, siendo n el número de puntos.\n\nEjemplo: -1,3,2"
        elif op == "fX":
            newWin.geometry('600x150')
            text = "Escribir los valores f(x) (si no se escribió en la función), es decir, los valores de x evaluados en la función.\n\nEscritos separados por comas, sin espacios.\n\nEjemplo: -1,3,2"
        elif op == "a":
            text = "Escribir extremo izquierdo del intervalo."
        elif op == "b":
            text = "Escribir extremo derecho del intervalo."
        elif op == "n":
            newWin.geometry('600x150')
            text = "Escribir n.\n\nSi se escribió en f(X), n es x-1, siendo x el número de puntos escritos."
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        dif = IntegracionCompuesta("1",fx.get(),n.get(),(fX.get()).split(','),a.get(),b.get())
        dif = dif.solution()
        txt.insert(INSERT, dif)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    fx = Label(panel, text="f(x):")
    fx.grid(column=0, row=0)
    fX = Label(panel, text="f(X):")
    fX.grid(column=0, row=1)
    a = Label(panel, text="a:")
    a.grid(column=0, row=2)
    b = Label(panel, text="b:")
    b.grid(column=0, row=3)
    n = Label(panel, text="n:")
    n.grid(column=0, row=4)

    fx = Entry(panel, width=20)
    fx.grid(column=1, row=0)
    fX = Entry(panel, width=20)
    fX.grid(column=1, row=1)
    a = Entry(panel, width=20)
    a.grid(column=1, row=2)
    b = Entry(panel, width=20)
    b.grid(column=1, row=3)
    n = Entry(panel, width=20)
    n.grid(column=1, row=4)

    btnf = Button(panel, text="?", command=lambda: ayudaFuncion())
    btnf.grid(column=3, row=0)
    btnb = Button(panel, text="?", command=lambda: ayudaIntervalo("fX"))
    btnb.grid(column=3, row=1)
    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("a"))
    btna.grid(column=3, row=2)
    btnc = Button(panel, text="?", command=lambda: ayudaIntervalo("b"))
    btnc.grid(column=3, row=3)
    btnd = Button(panel, text="?", command=lambda: ayudaIntervalo("n"))
    btnd.grid(column=3, row=4)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=6)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=0, row=6)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def Romb():
    def f(f, x):
        return eval(f)

    def graph(function):
        fig = plt.figure()
        x = np.arange(-10, 10, 0.1)
        y = f(function, x)
        plt.ylim([-10, 10])
        plt.xlim([-10, 10])
        plt.plot(x, y, color="green")
        plt.plot([-10, 10], [0, 0], color="black")
        plt.plot([0, 0], [-10, 10], color="black")

        plt.show()

    def getGraph():
        function = fx.get()
        replacements = {
            'sin': 'np.sin',
            'cos': 'np.cos',
            'log': 'np.log',
            'exp': 'np.exp',
            'sqrt': 'np.sqrt',
            '^': '**',
        }

        for old, new in replacements.items():
            function = function.replace(old, new)
        return graph(function)

    def ayudaFuncion():
        newWin = Toplevel(newwin)
        newWin.geometry('600x250')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir función.\n\n"
        text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
        text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(x) + sin(3*x) - tan(x/7) \n\n"
        text += "Exponenciales: exp()\nEjemplo: e^(3x) se escribiría así: exp(3*x) \n\n"
        text += "Logarítmicas: log()\nEjemplo: log((2*x)^3)\n\n"
        txt.insert(INSERT, text)

    def ayudaIntervalo(op):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""

        if op == "funcion":
            ayudaFuncion()
        elif op == "X":
            newWin.geometry('600x150')
            text = "Escribir valores de x (si no se escribió en la función).\n\nEscritos separados por comas, sin espacios.\n\nDebe de escribir n+1 coeficientes, siendo n el número de puntos.\n\nEjemplo: -1,3,2"
        elif op == "fX":
            newWin.geometry('600x150')
            text = "Escribir los valores f(x) (si no se escribió en la función), es decir, los valores de x evaluados en la función.\n\nEscritos separados por comas, sin espacios.\n\nEjemplo: -1,3,2"
        elif op == "a":
            text = "Escribir extremo izquierdo del intervalo."
        elif op == "b":
            text = "Escribir extremo derecho del intervalo."
        elif op == "tol":
            text = "Escribir tolerancia --> ejemplo: 1e-5"
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        p = Romberg(fx.get(), p0.get(), p1.get(), tol.get())
        p = p.solution()
        txt.insert(INSERT, p)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    ff = Label(panel, text="f(x):")
    ff.grid(column=0, row=0)
    p0 = Label(panel, text="a:")
    p0.grid(column=0, row=1)
    P1 = Label(panel, text="b:")
    P1.grid(column=0, row=2)
    tol = Label(panel, text="Tolerancia:")
    tol.grid(column=0, row=3)
    fx = Entry(panel, width=20)
    fx.grid(column=1, row=0)
    p0 = Entry(panel, width=20)
    p0.grid(column=1, row=1)
    p1 = Entry(panel, width=20)
    p1.grid(column=1, row=2)
    tol = Entry(panel, width=20)
    tol.grid(column=1, row=3)

    btnf = Button(panel, text="?", command=lambda: ayudaFuncion())
    btnf.grid(column=3, row=0)
    btnb = Button(panel, text="?", command=lambda: ayudaIntervalo("a"))
    btnb.grid(column=3, row=1)
    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("b"))
    btna.grid(column=3, row=2)
    btnc = Button(panel, text="?", command=lambda: ayudaIntervalo("tol"))
    btnc.grid(column=3, row=3)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=4)
    graphBtn = Button(panel, text="Graficar", command=getGraph)
    graphBtn.grid(column=0, row=4)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def newTaylor():

    def f(f, x):
        return eval(f)

    def graph(function):
        fig = plt.figure()
        x = np.arange(-10, 10, 0.1)
        y = f(function, x)
        plt.ylim([-10, 10])
        plt.xlim([-10, 10])
        plt.plot(x, y, color="green")
        plt.plot([-10, 10], [0, 0], color="black")
        plt.plot([0, 0], [-10, 10], color="black")

        plt.show()

    def getGraph():
        function = fx.get()
        replacements = {
            'sin': 'np.sin',
            'cos': 'np.cos',
            'log': 'np.log',
            'exp': 'np.exp',
            'sqrt': 'np.sqrt',
            '^': '**',
            't': 'x'
        }

        for old, new in replacements.items():
            function = function.replace(old, new)
        return graph(function)

    def ayudaFuncion():
        newWin = Toplevel(newwin)
        newWin.geometry('600x250')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir función. Utilizar 't' como variable independiente y 'w' como variable dependiente\n\n"
        text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
        text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(t) + sin(3*t) - tan(t/7) \n\n"
        text += "Exponenciales: exp()\nEjemplo: e^(3t) se escribiría así: exp(3*t) \n\n"
        text += "Logarítmicas: log()\nEjemplo: log((2*t)^3)\n\n"
        txt.insert(INSERT, text)

    def ayudaIntervalo(op):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""

        if op == "a":
            text = "Escribir extremo izquierdo del intervalo."
        elif op == "b":
            text = "Escribir extremo derecho del intervalo."
        elif op == "h":
            text = "Escribir h: tamaño de paso."
        elif op == "cond":
            newWin.geometry('500x100')
            text = "Escribir condición separada por coma.\nEjemplo --> 0,0 significa que en el tiempo 0, la función vale 0"
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        p = TaylorN(fx.get(), p0.get(), p1.get(), tol.get(), (cond.get()).split(','))
        p = p.solution()
        txt.insert(INSERT, p)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    ff = Label(panel, text="Función Taylor:")
    ff.grid(column=0, row=0)
    p0 = Label(panel, text="a:")
    p0.grid(column=0, row=1)
    P1 = Label(panel, text="b:")
    P1.grid(column=0, row=2)
    tol = Label(panel, text="h:")
    tol.grid(column=0, row=3)
    cond = Label(panel, text="Condición:")
    cond.grid(column=0, row=4)
    fx = Entry(panel, width=20)
    fx.grid(column=1, row=0)
    p0 = Entry(panel, width=20)
    p0.grid(column=1, row=1)
    p1 = Entry(panel, width=20)
    p1.grid(column=1, row=2)
    tol = Entry(panel, width=20)
    tol.grid(column=1, row=3)
    cond = Entry(panel, width=20)
    cond.grid(column=1, row=4)

    btnf = Button(panel, text="?", command=lambda: ayudaFuncion())
    btnf.grid(column=3, row=0)
    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("a"))
    btna.grid(column=3, row=1)
    btnc = Button(panel, text="?", command=lambda: ayudaIntervalo("b"))
    btnc.grid(column=3, row=2)
    btnd = Button(panel, text="?", command=lambda: ayudaIntervalo("h"))
    btnd.grid(column=3, row=3)
    btnd = Button(panel, text="?", command=lambda: ayudaIntervalo("cond"))
    btnd.grid(column=3, row=4)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=5)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def puntoM():

    def f(f, x):
        return eval(f)

    def graph(function):
        fig = plt.figure()
        x = np.arange(-10, 10, 0.1)
        y = f(function, x)
        plt.ylim([-10, 10])
        plt.xlim([-10, 10])
        plt.plot(x, y, color="green")
        plt.plot([-10, 10], [0, 0], color="black")
        plt.plot([0, 0], [-10, 10], color="black")

        plt.show()

    def getGraph():
        function = fx.get()
        replacements = {
            'sin': 'np.sin',
            'cos': 'np.cos',
            'log': 'np.log',
            'exp': 'np.exp',
            'sqrt': 'np.sqrt',
            '^': '**',
            't': 'x'
        }

        for old, new in replacements.items():
            function = function.replace(old, new)
        return graph(function)

    def ayudaFuncion():
        newWin = Toplevel(newwin)
        newWin.geometry('600x250')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir función. Utilizar 't' como variable independiente y 'w' como variable dependiente\n\n"
        text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
        text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(t) + sin(3*t) - tan(t/7) \n\n"
        text += "Exponenciales: exp()\nEjemplo: e^(3t) se escribiría así: exp(3*t) \n\n"
        text += "Logarítmicas: log()\nEjemplo: log((2*t)^3)\n\n"
        txt.insert(INSERT, text)

    def ayudaIntervalo(op):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""

        if op == "a":
            text = "Escribir extremo izquierdo del intervalo."
        elif op == "b":
            text = "Escribir extremo derecho del intervalo."
        elif op == "h":
            text = "Escribir h: tamaño de paso."
        elif op == "cond":
            newWin.geometry('500x100')
            text = "Escribir condición separada por coma.\nEjemplo --> 0,0 significa que en el tiempo 0, la función vale 0"
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        p = PuntoMedio(fx.get(), p0.get(), p1.get(), tol.get(), (cond.get()).split(','))
        p = p.solution()
        txt.insert(INSERT, p)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    ff = Label(panel, text="f(x):")
    ff.grid(column=0, row=0)
    p0 = Label(panel, text="a:")
    p0.grid(column=0, row=1)
    P1 = Label(panel, text="b:")
    P1.grid(column=0, row=2)
    tol = Label(panel, text="h:")
    tol.grid(column=0, row=3)
    cond = Label(panel, text="Condición:")
    cond.grid(column=0, row=4)
    fx = Entry(panel, width=20)
    fx.grid(column=1, row=0)
    p0 = Entry(panel, width=20)
    p0.grid(column=1, row=1)
    p1 = Entry(panel, width=20)
    p1.grid(column=1, row=2)
    tol = Entry(panel, width=20)
    tol.grid(column=1, row=3)
    cond = Entry(panel, width=20)
    cond.grid(column=1, row=4)

    btnf = Button(panel, text="?", command=lambda: ayudaFuncion())
    btnf.grid(column=3, row=0)
    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("a"))
    btna.grid(column=3, row=1)
    btnc = Button(panel, text="?", command=lambda: ayudaIntervalo("b"))
    btnc.grid(column=3, row=2)
    btnd = Button(panel, text="?", command=lambda: ayudaIntervalo("h"))
    btnd.grid(column=3, row=3)
    btnd = Button(panel, text="?", command=lambda: ayudaIntervalo("cond"))
    btnd.grid(column=3, row=4)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=5)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def eulerMod():

    def f(f, x):
        return eval(f)

    def graph(function):
        fig = plt.figure()
        x = np.arange(-10, 10, 0.1)
        y = f(function, x)
        plt.ylim([-10, 10])
        plt.xlim([-10, 10])
        plt.plot(x, y, color="green")
        plt.plot([-10, 10], [0, 0], color="black")
        plt.plot([0, 0], [-10, 10], color="black")

        plt.show()

    def getGraph():
        function = fx.get()
        replacements = {
            'sin': 'np.sin',
            'cos': 'np.cos',
            'log': 'np.log',
            'exp': 'np.exp',
            'sqrt': 'np.sqrt',
            '^': '**',
        }

        for old, new in replacements.items():
            function = function.replace(old, new)
        return graph(function)

    def ayudaFuncion():
        newWin = Toplevel(newwin)
        newWin.geometry('600x250')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir función. Utilizar 't' como variable independiente y 'w' como variable dependiente\n\n"
        text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
        text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(t) + sin(3*t) - tan(t/7) \n\n"
        text += "Exponenciales: exp()\nEjemplo: e^(3t) se escribiría así: exp(3*t) \n\n"
        text += "Logarítmicas: log()\nEjemplo: log((2*t)^3)\n\n"
        txt.insert(INSERT, text)

    def ayudaIntervalo(op):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""

        if op == "a":
            text = "Escribir extremo izquierdo del intervalo."
        elif op == "b":
            text = "Escribir extremo derecho del intervalo."
        elif op == "h":
            text = "Escribir h: tamaño de paso."
        elif op == "cond":
            newWin.geometry('500x100')
            text = "Escribir condición separada por coma.\nEjemplo --> 0,0 significa que en el tiempo 0, la función vale 0"
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        p = EulerModificado(fx.get(), p0.get(), p1.get(), tol.get(), (cond.get()).split(','))
        p = p.solution()
        txt.insert(INSERT, p)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    ff = Label(panel, text="f(x):")
    ff.grid(column=0, row=0)
    p0 = Label(panel, text="a:")
    p0.grid(column=0, row=1)
    P1 = Label(panel, text="b:")
    P1.grid(column=0, row=2)
    tol = Label(panel, text="h:")
    tol.grid(column=0, row=3)
    cond = Label(panel, text="Condición:")
    cond.grid(column=0, row=4)
    fx = Entry(panel, width=20)
    fx.grid(column=1, row=0)
    p0 = Entry(panel, width=20)
    p0.grid(column=1, row=1)
    p1 = Entry(panel, width=20)
    p1.grid(column=1, row=2)
    tol = Entry(panel, width=20)
    tol.grid(column=1, row=3)
    cond = Entry(panel, width=20)
    cond.grid(column=1, row=4)

    btnf = Button(panel, text="?", command=lambda: ayudaFuncion())
    btnf.grid(column=3, row=0)
    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("a"))
    btna.grid(column=3, row=1)
    btnc = Button(panel, text="?", command=lambda: ayudaIntervalo("b"))
    btnc.grid(column=3, row=2)
    btnd = Button(panel, text="?", command=lambda: ayudaIntervalo("h"))
    btnd.grid(column=3, row=3)
    btnd = Button(panel, text="?", command=lambda: ayudaIntervalo("cond"))
    btnd.grid(column=3, row=4)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=5)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def heun():

    def f(f, x):
        return eval(f)

    def graph(function):
        fig = plt.figure()
        x = np.arange(-10, 10, 0.1)
        y = f(function, x)
        plt.ylim([-10, 10])
        plt.xlim([-10, 10])
        plt.plot(x, y, color="green")
        plt.plot([-10, 10], [0, 0], color="black")
        plt.plot([0, 0], [-10, 10], color="black")

        plt.show()

    def getGraph():
        function = fx.get()
        replacements = {
            'sin': 'np.sin',
            'cos': 'np.cos',
            'log': 'np.log',
            'exp': 'np.exp',
            'sqrt': 'np.sqrt',
            '^': '**',
        }

        for old, new in replacements.items():
            function = function.replace(old, new)
        return graph(function)

    def ayudaFuncion():
        newWin = Toplevel(newwin)
        newWin.geometry('600x250')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir función. Utilizar 't' como variable independiente y 'w' como variable dependiente\n\n"
        text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
        text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(t) + sin(3*t) - tan(t/7) \n\n"
        text += "Exponenciales: exp()\nEjemplo: e^(3t) se escribiría así: exp(3*t) \n\n"
        text += "Logarítmicas: log()\nEjemplo: log((2*t)^3)\n\n"
        txt.insert(INSERT, text)

    def ayudaIntervalo(op):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""

        if op == "a":
            text = "Escribir extremo izquierdo del intervalo."
        elif op == "b":
            text = "Escribir extremo derecho del intervalo."
        elif op == "h":
            text = "Escribir h: tamaño de paso."
        elif op == "cond":
            newWin.geometry('500x100')
            text = "Escribir condición separada por coma.\nEjemplo --> 0,0 significa que en el tiempo 0, la función vale 0"
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        p = Heun(fx.get(), p0.get(), p1.get(), tol.get(), (cond.get()).split(','))
        p = p.solution()
        txt.insert(INSERT, p)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    ff = Label(panel, text="f(x):")
    ff.grid(column=0, row=0)
    p0 = Label(panel, text="a:")
    p0.grid(column=0, row=1)
    P1 = Label(panel, text="b:")
    P1.grid(column=0, row=2)
    tol = Label(panel, text="h:")
    tol.grid(column=0, row=3)
    cond = Label(panel, text="Condición:")
    cond.grid(column=0, row=4)
    fx = Entry(panel, width=20)
    fx.grid(column=1, row=0)
    p0 = Entry(panel, width=20)
    p0.grid(column=1, row=1)
    p1 = Entry(panel, width=20)
    p1.grid(column=1, row=2)
    tol = Entry(panel, width=20)
    tol.grid(column=1, row=3)
    cond = Entry(panel, width=20)
    cond.grid(column=1, row=4)

    btnf = Button(panel, text="?", command=lambda: ayudaFuncion())
    btnf.grid(column=3, row=0)
    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("a"))
    btna.grid(column=3, row=1)
    btnc = Button(panel, text="?", command=lambda: ayudaIntervalo("b"))
    btnc.grid(column=3, row=2)
    btnd = Button(panel, text="?", command=lambda: ayudaIntervalo("h"))
    btnd.grid(column=3, row=3)
    btnd = Button(panel, text="?", command=lambda: ayudaIntervalo("cond"))
    btnd.grid(column=3, row=4)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=5)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def runge():

    def f(f, x):
        return eval(f)

    def graph(function):
        fig = plt.figure()
        x = np.arange(-10, 10, 0.1)
        y = f(function, x)
        plt.ylim([-10, 10])
        plt.xlim([-10, 10])
        plt.plot(x, y, color="green")
        plt.plot([-10, 10], [0, 0], color="black")
        plt.plot([0, 0], [-10, 10], color="black")

        plt.show()

    def getGraph():
        function = fx.get()
        replacements = {
            'sin': 'np.sin',
            'cos': 'np.cos',
            'log': 'np.log',
            'exp': 'np.exp',
            'sqrt': 'np.sqrt',
            '^': '**',
        }

        for old, new in replacements.items():
            function = function.replace(old, new)
        return graph(function)

    def ayudaFuncion():
        newWin = Toplevel(newwin)
        newWin.geometry('600x250')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir función. Utilizar 't' como variable independiente y 'w' como variable dependiente\n\n"
        text += "Operadores matemáticos: + - / * ^ \nEjemplo: 3 + 4 * (5-1)^2 \n\n"
        text += "Trigonométricas: cos(), sin(), tan() \nEjemplo: cos(t) + sin(3*t) - tan(t/7) \n\n"
        text += "Exponenciales: exp()\nEjemplo: e^(3t) se escribiría así: exp(3*t) \n\n"
        text += "Logarítmicas: log()\nEjemplo: log((2*t)^3)\n\n"
        txt.insert(INSERT, text)

    def ayudaIntervalo(op):
        newWin = Toplevel(newwin)
        newWin.geometry('400x50')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = ""

        if op == "a":
            text = "Escribir extremo izquierdo del intervalo."
        elif op == "b":
            text = "Escribir extremo derecho del intervalo."
        elif op == "h":
            text = "Escribir h: tamaño de paso."
        elif op == "cond":
            newWin.geometry('500x100')
            text = "Escribir condición separada por coma.\nEjemplo --> 0,0 significa que en el tiempo 0, la función vale 0"
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        p = RungeKutta(fx.get(), p0.get(), p1.get(), tol.get(), (cond.get()).split(','))
        p = p.solution()
        txt.insert(INSERT, p)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    ff = Label(panel, text="f(x):")
    ff.grid(column=0, row=0)
    p0 = Label(panel, text="a:")
    p0.grid(column=0, row=1)
    P1 = Label(panel, text="b:")
    P1.grid(column=0, row=2)
    tol = Label(panel, text="h:")
    tol.grid(column=0, row=3)
    cond = Label(panel, text="Condición:")
    cond.grid(column=0, row=4)
    fx = Entry(panel, width=20)
    fx.grid(column=1, row=0)
    p0 = Entry(panel, width=20)
    p0.grid(column=1, row=1)
    p1 = Entry(panel, width=20)
    p1.grid(column=1, row=2)
    tol = Entry(panel, width=20)
    tol.grid(column=1, row=3)
    cond = Entry(panel, width=20)
    cond.grid(column=1, row=4)

    btnf = Button(panel, text="?", command=lambda: ayudaFuncion())
    btnf.grid(column=3, row=0)
    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("a"))
    btna.grid(column=3, row=1)
    btnc = Button(panel, text="?", command=lambda: ayudaIntervalo("b"))
    btnc.grid(column=3, row=2)
    btnd = Button(panel, text="?", command=lambda: ayudaIntervalo("h"))
    btnd.grid(column=3, row=3)
    btnd = Button(panel, text="?", command=lambda: ayudaIntervalo("cond"))
    btnd.grid(column=3, row=4)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=5)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def gauss():
    def ayudaIntervalo(op):
        newWin = Toplevel(newwin)
        newWin.geometry('600x100')
        newWin.title("Ayuda")
        frame = Frame(newWin)
        panel = PanedWindow(frame)
        txt = scrolledtext.ScrolledText(frame, width=85, height=40)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        text = "Escribir un renglón en cada línea, separando números con espacios.\nEjemplo:\n1 2 3 4\n5 6 7 8"
        txt.insert(INSERT, text)

    def clicked():
        txt.delete(1.0, END)
        p = matrix.get("1.0",END).splitlines()
        print(p)
        ma = []
        for arr in p:
            aux = arr.split(' ')
            aux2 = []
            for i in range(len(aux)):
                aux2.append(eval(aux[i]))
            ma.append(aux2)
        p = GaussJordan(ma)
        p = p.solution()
        txt.insert(INSERT, p)

    newwin = Toplevel(window)
    newwin.geometry('600x500')
    frame = Frame(newwin)
    panel = PanedWindow(frame)
    ff = Label(panel, text="Matriz:")
    ff.grid(column=0, row=0)
    matrix = Text(panel, height=8, width=25)
    matrix.grid(column=1, row=0)

    btna = Button(panel, text="?", command=lambda: ayudaIntervalo("a"))
    btna.grid(column=3, row=0)

    btn = Button(panel, text="Calcular", command=clicked)
    btn.grid(column=1, row=5)
    txt = scrolledtext.ScrolledText(frame, width=83, height=20)
    txt.grid(column=0, row=1)
    panel.grid(column=0, row=0)
    frame.grid(column=0, row=0)

def menu():

    newwin = Toplevel(window)
    newwin.geometry("600x630")
    newwin.resizable(width=False, height=False)
    load = Image.open("math.png")
    width, height = load.size
    load = load.resize((round(230 / height * width), round(230)))
    render = ImageTk.PhotoImage(load)
    img = Label(newwin, image=render)
    img.image = render
    img.place(x=170, y=20)

    frame1 = Frame(newwin)
    var = StringVar(frame1)
    var.set("Búsqueda de raíces")
    opcionesRaices = ["Posición Falsa", "Bisección", "Punto Fijo", "Newton Raphson", "Secante", "Müller", "Horner"]
    raices = OptionMenu(frame1, var, *opcionesRaices)
    raices.config(width=20)
    # raices.pack(side='left',padx=30,pady=30)
    raices.pack(side='left', padx=30)
    var2 = StringVar(newwin)
    var2.set("Interpolación")
    opcionesInter = ["Lagrange", "Diferencias Divididas", "Hermit"]
    inter = OptionMenu(frame1, var2, *opcionesInter)
    inter.config(width=20)
    # inter.pack(side='left',padx=70,pady=30)
    inter.pack(side='left', padx=70)
    labelAux = Label(frame1, textvariable=var)
    labelAux2 = Label(frame1, textvariable=var2)
    labelAux.pack()
    labelAux2.pack()

    # segunda línea

    frame2 = Frame(newwin)

    var3 = StringVar(frame2)
    var3.set("Diferenciación/Integración")
    opcionesDif = ["Extremo de 3 puntos", "Intermedio de 3 puntos", "Extremo de 5 puntos", "Intermedio de 5 puntos",
                   "Integración abierta", "Integración cerrada", "Integración compuesta abierta", "Trapecio Compuesto",
                   "Simpson Compuesto", "Romberg"]
    derivadas = OptionMenu(frame2, var3, *opcionesDif)
    derivadas.config(width=20)
    derivadas.pack(side='left', padx=30, pady=30)
    # derivadas.pack(side='top',pady=100)
    # derivadas.pack(side='bottom')
    var4 = StringVar(frame2)
    var4.set("Ecuaciones Diferenciales")
    opcionesEcDif = ["Taylor", "Punto Medio", "Euler Modificado", "Heun", "Runge Kutta"]
    ecdif = OptionMenu(frame2, var4, *opcionesEcDif)
    ecdif.config(width=20)
    ecdif.pack(side='left', padx=70, pady=30)
    # ecdif.pack(side='top')
    labelAux3 = Label(frame2, textvariable=var3)
    labelAux4 = Label(frame2, textvariable=var4)
    labelAux3.pack()
    labelAux4.pack()

    # tercera línea

    frame3 = Frame(newwin)

    var5 = StringVar(frame3)
    var5.set("Solución de matrices")
    opcionesMatrix = ["Gauss Jordan"]
    matrices = OptionMenu(frame3, var5, *opcionesMatrix)
    matrices.config(width=20)
    matrices.pack(side='left', padx=193, pady=30)
    labelAux5 = Label(frame3, textvariable=var5)
    labelAux5.pack()

    frame1.place(x=0, y=300)
    frame2.place(x=0, y=370)
    frame3.place(x=0, y=460)
    solveRaices = Button(newwin, text="Resolver", command=lambda: solverRoots(var.get()))
    solveInter = Button(newwin, text="Resolver", command=lambda: solverInter(var2.get()))
    solveRaices.place(x=100, y=345)
    solveInter.place(x=415, y=345)
    solveDif = Button(newwin, text="Resolver", command=lambda: solverDif(var3.get()))
    solveEcDif = Button(newwin, text="Resolver", command=lambda: solverEcDif(var4.get()))
    solveDif.place(x=100, y=435)
    solveEcDif.place(x=415, y=435)
    # solveRaices.pack(side='bottom')
    solveMatriz = Button(newwin, text="Resolver", command=lambda: solverMatrix(var5.get()))
    solveMatriz.place(x=265, y=530)
    ayuda = Button(newwin, text="Ayuda", highlightbackground="#eda08e", fg="Black", command=lambda: ayudaFunction())
    ayuda.place(x=273, y=570)

window = Tk()
window.title("Cálculo Numérico")
window.geometry("500x400")
window.resizable(width=False, height=False)

load = Image.open("calculator.png")
width, height = load.size
load = load.resize((round(130 / height * width), round(130)))
render = ImageTk.PhotoImage(load)
img = Label(window, image=render)
img.image = render
img.place(x=180, y=20)

frame = Frame(window)
panel = PanedWindow(frame)
txt = scrolledtext.ScrolledText(frame, width=70, height=40)
txt.grid(column=0, row=1)
panel.grid(column=0, row=0)
text = "¡Bienvenid@ a la SúperCalculadora Martha5000!\n\n"
text = text.rjust(len(text)+12)
text2 = "Cuando se abra el menú, no olvides apretar el botón de\n"
text2aux = "'Ayuda' para saber cómo manejar el programa.\n\n"
text2 = text2.rjust(len(text2)+7)
text2aux = text2aux.rjust(len(text2aux)+7)
text += text2
text+= text2aux
text3 = "Para comenzar aprieta el botón de abajo."
text3 = text3.rjust(len(text3)+7)
text += text3
txt.insert(INSERT, text)
frame.place(x=0, y=200)

mainMenu = Button(window, text="Comenzar", command=lambda: menu())
mainMenu.place(x=205, y=340)

window.mainloop()
