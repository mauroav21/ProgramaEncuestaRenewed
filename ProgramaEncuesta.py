#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select

import tkinter as tk
from tkinter import ttk, messagebox

# Función al presionar el botón
def iniciar_automatizacion():
    matricula = entry_matricula.get()
    contrasena = entry_contrasena.get()

    if not matricula or not contrasena:
        messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")
        return

    # Aquí iría la lógica con Selenium
    messagebox.showinfo("Éxito", "La automatización ha comenzado.")

# Configuración de ventana
ventana = tk.Tk()
ventana.title("ProgramaEncuestaRenew")
ventana.geometry("400x250")
ventana.configure(bg="#f0f4f7")

# Estilo moderno con ttk
style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 11), background="#f0f4f7")
style.configure("TEntry", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 11), padding=6)

# Frame contenedor
frame = ttk.Frame(ventana, padding=20)
frame.pack(expand=True)

# Título
ttk.Label(frame, text="Inicio de Sesión", font=("Segoe UI", 14, "bold")).grid(column=0, row=0, columnspan=2, pady=10)

# Campo matrícula
ttk.Label(frame, text="Matrícula:").grid(column=0, row=1, sticky="e", pady=5, padx=5)
entry_matricula = ttk.Entry(frame, width=25)
entry_matricula.grid(column=1, row=1)

# Campo contraseña
ttk.Label(frame, text="Contraseña:").grid(column=0, row=2, sticky="e", pady=5, padx=5)
entry_contrasena = ttk.Entry(frame, width=25, show="*")
entry_contrasena.grid(column=1, row=2)

# Botón iniciar
ttk.Button(frame, text="Iniciar Evaluación", command=iniciar_automatizacion).grid(column=0, row=3, columnspan=2, pady=20)

ventana.mainloop()
