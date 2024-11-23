import tkinter as tk
from tkinter import messagebox
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#calcular resistencia equivalente en serie
def JDRC_calcular_resistencia_serie(JDRC_resistencias):
    return np.sum(JDRC_resistencias)

#calcular resistencia equivalente en paralelo
def JDRC_calcular_resistencia_paralelo(JDRC_resistencias):
    if 0 in JDRC_resistencias:
        return 0  # Si alguna resistencia es 0 en paralelo, la resistencia total es 0
    return 1 / np.sum(1 / JDRC_resistencias)

#calcular y mostrar la resistencia equivalente
def JDRC_calcular_resistencia():
    JDRC_resistencias_str = JDRC_entrada_resistencias.get()
    JDRC_resistencias = list(map(float, JDRC_resistencias_str.split(",")))  # Convertimos los valores ingresados a flotantes
    
    JDRC_tipo_conexion = JDRC_seleccion_tipo.get()  # Obtenemos el tipo de conexión (serie o paralelo)
    
    if JDRC_tipo_conexion == "serie":
        JDRC_resistencia_eq = JDRC_calcular_resistencia_serie(JDRC_resistencias)
    elif JDRC_tipo_conexion == "paralelo":
        JDRC_resistencia_eq = JDRC_calcular_resistencia_paralelo(JDRC_resistencias)
    else:
        messagebox.showerror("Error", "Seleccione un tipo de conexión válido.")
        return
    
    JDRC_resultado.set(f"Resistencia equivalente: {JDRC_resistencia_eq:.2f} Ohms")
    JDRC_graficar_resistencia(JDRC_resistencias, JDRC_tipo_conexion)

#graficar la relación entre resistencia total y número de resistencias
def JDRC_graficar_resistencia(JDRC_resistencias, JDRC_tipo_conexion):
    JDRC_resistencias_totales = []
    
    for i in range(1, len(JDRC_resistencias) + 1):
        if JDRC_tipo_conexion == "serie":
            JDRC_resistencia_eq = JDRC_calcular_resistencia_serie(JDRC_resistencias[:i])
        else:
            JDRC_resistencia_eq = JDRC_calcular_resistencia_paralelo(JDRC_resistencias[:i])
        JDRC_resistencias_totales.append(JDRC_resistencia_eq)
    
    plt.plot(range(1, len(JDRC_resistencias) + 1), JDRC_resistencias_totales, marker='o')
    plt.title(f"Resistencia Total vs Número de Resistencias ({JDRC_tipo_conexion.capitalize()})")
    plt.xlabel("Número de Resistencias")
    plt.ylabel("Resistencia Total (Ohms)")
    plt.grid(True)
    plt.show()

#  interfaz gráfica con Tkinter
JDRC_ventana = tk.Tk()
JDRC_ventana.title("Calculadora de Resistencia Equivalente")

# Variables de entrada y resultado
JDRC_entrada_resistencias = tk.StringVar()
JDRC_resultado = tk.StringVar()
JDRC_seleccion_tipo = tk.StringVar()

# Etiquetas y cuadros de entrada
tk.Label(JDRC_ventana, text="Ingrese los valores de resistencias separados por coma:").pack(pady=5)
tk.Entry(JDRC_ventana, textvariable=JDRC_entrada_resistencias, width=40).pack(pady=5)

# Botones de selección para el tipo de conexión
tk.Radiobutton(JDRC_ventana, text="Serie", variable=JDRC_seleccion_tipo, value="serie").pack(anchor=tk.W)
tk.Radiobutton(JDRC_ventana, text="Paralelo", variable=JDRC_seleccion_tipo, value="paralelo").pack(anchor=tk.W)

# Botón para calcular la resistencia equivalente
tk.Button(JDRC_ventana, text="Calcular Resistencia Equivalente", command=JDRC_calcular_resistencia).pack(pady=10)

# Etiqueta para mostrar el resultado
tk.Label(JDRC_ventana, textvariable=JDRC_resultado).pack(pady=5)

# Iniciamos la ventana principal
JDRC_ventana.mainloop()
