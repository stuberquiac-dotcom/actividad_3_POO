
import math
import tkinter as tk
from tkinter import messagebox

class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

    def get_volumen(self):
        return self.volumen

    def get_superficie(self):
        return self.superficie

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        if radio <= 0 or altura <= 0:
            raise ValueError("El radio y la altura deben ser mayores que cero.")
        self.radio = radio
        self.altura = altura
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return math.pi * self.altura * self.radio ** 2

    def calcular_superficie(self):
        return 2 * math.pi * self.radio * self.altura + 2 * math.pi * self.radio ** 2

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que cero.")
        self.radio = radio
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return (4.0 / 3.0) * math.pi * self.radio ** 3

    def calcular_superficie(self):
        return 4 * math.pi * self.radio ** 2

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        if base <= 0 or altura <= 0 or apotema <= 0:
            raise ValueError("La base, altura y apotema deben ser mayores que cero.")
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return (self.base ** 2 * self.altura) / 3.0

    def calcular_superficie(self):
        return self.base ** 2 + 2 * self.base * self.apotema

class VentanaFigura(tk.Toplevel):
    def __init__(self, master, tipo):
        super().__init__(master)
        self.tipo = tipo
        self.title(tipo)
        self.resizable(False, False)
        self.geometry("340x270")
        if tipo == "Cilindro":
            campos = [("Radio (cm):", "radio"), ("Altura (cm):", "altura")]
        elif tipo == "Esfera":
            campos = [("Radio (cm):", "radio")]
        else:
            campos = [("Base (cm):", "base"), ("Altura (cm):", "altura"), ("Apotema (cm):", "apotema")]
        self.entradas = {}
        tk.Label(self, text=f"Cálculo de {tipo.lower()}", font=("Arial", 13, "bold")).pack(pady=12)
        form = tk.Frame(self)
        form.pack(pady=4)
        for i, (etiqueta, clave) in enumerate(campos):
            tk.Label(form, text=etiqueta, width=14, anchor="e").grid(row=i, column=0, padx=5, pady=5)
            entrada = tk.Entry(form, width=18)
            entrada.grid(row=i, column=1, padx=5, pady=5)
            self.entradas[clave] = entrada
        tk.Button(self, text="Calcular", command=self.calcular, width=16).pack(pady=10)
        self.lbl_volumen = tk.Label(self, text="Volumen (cm³): —")
        self.lbl_volumen.pack(pady=3)
        self.lbl_superficie = tk.Label(self, text="Superficie (cm²): —")
        self.lbl_superficie.pack(pady=3)

    def calcular(self):
        try:
            valores = {}
            for clave, campo in self.entradas.items():
                texto = campo.get().strip().replace(",", ".")
                if not texto:
                    raise ValueError(f"El campo {clave} es obligatorio.")
                valores[clave] = float(texto)
            if self.tipo == "Cilindro":
                figura = Cilindro(valores["radio"], valores["altura"])
            elif self.tipo == "Esfera":
                figura = Esfera(valores["radio"])
            else:
                figura = Piramide(valores["base"], valores["altura"], valores["apotema"])
        except ValueError as error:
            messagebox.showerror("Error de entrada", str(error))
            return
        self.lbl_volumen.config(text=f"Volumen (cm³): {figura.get_volumen():.2f}")
        self.lbl_superficie.config(text=f"Superficie (cm²): {figura.get_superficie():.2f}")


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras geométricas")
        self.geometry("390x190")
        self.resizable(False, False)
        tk.Label(self, text="Calculadora de figuras geométricas", font=("Arial", 13, "bold")).pack(pady=20)
        fila = tk.Frame(self)
        fila.pack(pady=12)
        for tipo in ("Cilindro", "Esfera", "Pirámide"):
            tk.Button(fila, text=tipo, width=10, command=lambda t=tipo: VentanaFigura(self, t)).pack(side="left", padx=6)
        tk.Label(self, text="Dimensiones en centímetros", fg="gray").pack(pady=5)

if __name__ == "__main__":
    VentanaPrincipal().mainloop()
