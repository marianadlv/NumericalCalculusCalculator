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