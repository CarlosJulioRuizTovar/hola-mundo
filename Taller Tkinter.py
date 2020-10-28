import tkinter as tk
from tkinter import ttk
def init_window():

  window = tk.Tk()
  window.title("Mi primera aplicacion")
  window.geometry("400x250")

  label = tk.Label(window, text = "Calculadora", font = ("Arial bold", 15))
  label.grid(column = 0, row = 0)

  entrada1 = tk.Entry(window, width = 10)
  entrada2 = tk.Entry(window, width = 10)

  entrada1.grid(column = 1, row = 1)
  entrada2.grid(column = 1, row = 2)

  label_entrada1 = tk.Label(window, text = "Ingrese primer numero:", font = ("Arial bold", 10))
  label_entrada1.grid(column = 0, row = 1)

  label_entrada2 = tk.Label(window, text = "Ingrese segundo numero:", font = ("Arial bold", 10))
  label_entrada2.grid(column = 0, row = 2)

  label_operador = tk.Label(window, text = "Escoja un operador", font = ("Arial bold", 10))
  label_operador.grid(column = 0, row = 3)

  combo_operadores = ttk.Combobox(window)
  combo_operadores["values"] = ["+", "-", "*", "/", "pow"]
  combo_operadores.current(0)
  combo_operadores.grid(column = 1, row = 3)

  label_resultado = tk.Label(window, text = "Resultado:", font = ("Arial bold", 15))
  label_resultado.grid(column = 0, row = 5)

  chk_state = tk.BooleanVar()

  chk_state.set(False)

  chk = tk.Checkbutton(window, text ='¿Desea redondear su cifra a un entero?', var = chk_state)

  chk.grid(column = 0, row = 6)

  label_spin = tk.Label(window, text="Agrega un multiplicador al resultado", font=("Arial bold", 10))
  label_spin.grid(column=0, row=7)

  var = tk.IntVar()

  var.set(1)

  spin = tk.Spinbox(window, from_ = -100, to = 100, width = 5, textvariable = var)

  spin.grid(column = 1, row = 7)

  style = ttk.Style()

  style.theme_use('default')

  style.configure("black.Horizontal.TProgressbar", background = 'black')

  bar = ttk.Progressbar(window, length = 200, style = 'black.Horizontal.TProgressbar')

  bar['value'] = 0

  bar.grid(column = 0, row = 8)

  def calculadora(num1, num2, operador, mult):

    if operador == "+":
      resultado = int(mult) * (num1 + num2)
    elif operador == "-":
      resultado = int(mult) * (num1 - num2)
    elif operador == "*":
      resultado = int(mult) * (num1 * num2)
    elif operador == "/":
      resultado = int(mult) * (round(num1 / num2, 2))
    else:
      resultado = int(mult) * (num1 ** num2)

    return resultado

  def click_calcular(label, num1, num2, operador, redondeo, mult, bar):

    valor1 = float(num1)
    valor2 = float(num2)
    res = calculadora(valor1, valor2, operador, mult)
    if redondeo:
      res = round(res)
    bar['value'] = 100
    label.configure(text = "Resultado:" + str(res))

  boton = tk.Button(window,
                  command = lambda: click_calcular(
                          label_resultado,
                          entrada1.get(),
                          entrada2.get(),
                          combo_operadores.get(),
                          chk_state.get(),
                          spin.get(),
                          bar),
                  text = "Calcular",
                  bg = "purple",
                  fg = "white")
  
  boton.grid(column = 1, row = 4)

  window.mainloop()

def main():
  init_window()

main()