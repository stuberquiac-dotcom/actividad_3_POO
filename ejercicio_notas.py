
import math
import tkinter as tk
from tkinter import messagebox

class Notas:
    def __init__(self, lista_notas):
        if len(lista_notas) != 5:
            raise ValueError("Debe ingresar exactamente cinco notas.")
        if any(n < 0 or n > 5 for n in lista_notas):
            raise ValueError("Cada nota debe estar entre 0 y 5.")
        self.lista_notas = lista_notas

    def calcular_promedio(self):
        return sum(self.lista_notas) / len(self.lista_notas)

    def calcular_desviacion(self):
        promedio = self.calcular_promedio()
        return math.sqrt(sum((n - promedio) ** 2 for n in self.lista_notas) / len(self.lista_notas))

    def calcular_menor(self):
        return min(self.lista_notas)

    def calcular_mayor(self):
        return max(self.lista_notas)

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notas - Estadísticas")
        self.resizable(False, False)
        self.geometry("390x370")
        tk.Label(self, text="Estadísticas de cinco notas", font=("Arial", 14, "bold")).pack(pady=12)
        self.campos = []
        formulario = tk.Frame(self)
        formulario.pack()
        for i in range(5):
            tk.Label(formulario, text=f"Nota {i+1}:").grid(row=i, column=0, sticky="e", padx=8, pady=4)
            campo = tk.Entry(formulario, width=18)
            campo.grid(row=i, column=1, padx=8, pady=4)
            self.campos.append(campo)
        botones = tk.Frame(self)
        botones.pack(pady=10)
        tk.Button(botones, text="Calcular", command=self.calcular, width=12).grid(row=0, column=0, padx=5)
        tk.Button(botones, text="Limpiar", command=self.limpiar, width=12).grid(row=0, column=1, padx=5)
        self.resultados = {}
        for clave, etiqueta in [("promedio","Promedio:"),("desviacion","Desviación estándar:"),("mayor","Nota mayor:"),("menor","Nota menor:")]:
            fila = tk.Frame(self)
            fila.pack(anchor="w", padx=22, pady=3)
            tk.Label(fila, text=etiqueta, width=21, anchor="w").pack(side="left")
            valor = tk.Label(fila, text="—", width=12, anchor="w")
            valor.pack(side="left")
            self.resultados[clave] = valor

    def calcular(self):
        valores = []
        try:
            for i, campo in enumerate(self.campos, 1):
                texto = campo.get().strip().replace(",", ".")
                if not texto:
                    raise ValueError(f"Debe ingresar la nota {i}.")
                valores.append(float(texto))
            notas = Notas(valores)
        except ValueError as error:
            messagebox.showerror("Dato inválido", str(error) if str(error) else "Ingrese solo valores numéricos.")
            return
        self.resultados["promedio"].config(text=f"{notas.calcular_promedio():.2f}")
        self.resultados["desviacion"].config(text=f"{notas.calcular_desviacion():.2f}")
        self.resultados["mayor"].config(text=f"{notas.calcular_mayor():.2f}")
        self.resultados["menor"].config(text=f"{notas.calcular_menor():.2f}")

    def limpiar(self):
        for campo in self.campos:
            campo.delete(0, tk.END)
        for valor in self.resultados.values():
            valor.config(text="—")

if __name__ == "__main__":
    VentanaPrincipal().mainloop()
