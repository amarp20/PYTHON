import tkinter as tk

def calcular_presupuesto():
    ingreso = float(entry_kilometros.get())
    total = ingreso*0.1
    label_resultado.config(text=f"El total asciende a: {total} Euros")

ventana = tk.Tk()
ventana.title("Calculadora de Impuestos")

tk.Label(ventana, text="Sus ingresos anuales:").grid(row=0, column=0)
entry_kilometros = tk.Entry(ventana)
entry_kilometros.grid(row=0, column=1)

boton_calcular = tk.Button(ventana, text="Calcular Impuestos", command=calcular_presupuesto)
boton_calcular.grid(row=5, column=0, columnspan=2)

label_resultado = tk.Label(ventana, text="")
label_resultado.grid(row=6, column=0, columnspan=2)

ventana.mainloop()
