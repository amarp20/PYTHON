import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class JuegoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Piedra, Papel o Tijera")

        self.jugadas = ["piedra", "papel", "tijera"]

        self.imagenes = {
            "piedra": ImageTk.PhotoImage(Image.open("recursos/piedra.png").resize((100, 100))),
            "papel": ImageTk.PhotoImage(Image.open("recursos/papel.png").resize((100, 100))),
            "tijera": ImageTk.PhotoImage(Image.open("recursos/tijeras.png").resize((100, 100)))
        }

        tk.Label(root, text="Elige tu jugada:").pack()

        self.persona = None

        # Botones para elegir jugada
        for jugada in self.jugadas:
            button = tk.Button(root, image=self.imagenes[jugada], command=lambda j=jugada: self.elegir_jugada(j))
            button.pack(side="left", padx=10, pady=10)

        self.resultado_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.resultado_label.pack(pady=20)

    def elegir_jugada(self, jugada):
        self.persona = jugada
        maquina = random.choice(self.jugadas)
        self.mostrar_resultado(maquina)

    def mostrar_resultado(self, maquina):
        if self.persona == maquina:
            resultado = f"Empate: ambos eligieron {self.persona}."
        elif (self.persona == "piedra" and maquina == "tijera") or \
             (self.persona == "papel" and maquina == "piedra") or \
             (self.persona == "tijera" and maquina == "papel"):
            resultado = f"Tú ganas: {self.persona} vence a {maquina}."
        else:
            resultado = f"Yo gano: {maquina} vence a {self.persona}."

        self.resultado_label.config(text=resultado)

        # Mostrar un cuadro de diálogo con el resultado
        messagebox.showinfo("Resultado", resultado)

# Configuración de la ventana principal de Tkinter
root = tk.Tk()
juego = JuegoGUI(root)
root.mainloop()