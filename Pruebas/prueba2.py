'''Crea una aplicación que calcule el impuesto sobre la renta de una persona. 
La aplicación debe pedir al usuario su ingreso anual y calcular el impuesto basado en las siguientes tasas:
Hasta 10,000€: 10%
De 10,001€ a 20,000€: 15%
De 20,001€ a 30,000€: 20%
Más de 30,000€: 25%
La aplicación puede manejar excepciones para validar la entrada del usuario.
Debe mostrar el impuesto total a pagar.'''

import tkinter as tk

def calcular_presupuesto():
    
    ingreso = float(entry_kilometros.get())
    
    if ingreso <= 10000:
            total = ingreso*0.1
    elif ingreso > 10000 and ingreso <= 20000:
            total = ingreso*0.15
    elif ingreso > 20000 and ingreso <= 30000:
            total = ingreso*0.20
    else:
            total = ingreso*0.25
            
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
        
   




      
        
        