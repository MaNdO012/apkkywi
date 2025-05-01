import tkinter as tk
from tkinter import messagebox

# Configuración inicial
BG_COLOR = "#f0f8ff"  # Azul claro
BUTTON_COLOR = "#ff6b6b"  # Rojo coral
GLOBO_COLOR = "#e3f2fd"  # Azul muy claro
FONT = ("Arial", 14)

def calcular():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        op = operacion.get()
        
        operaciones = {
            "+": num1 + num2,
            "-": num1 - num2,
            "×": num1 * num2,
            "÷": num1 / num2 if num2 != 0 else "Error"
        }
        
        resultado = operaciones[op]
        
        if resultado == "Error":
            messagebox.showerror("Error", "¡No se puede dividir entre cero!")
            return
            
        # Formatear resultado (eliminar .0 si es entero)
        resultado_formateado = f"{resultado:.2f}".replace(".00", "") if isinstance(resultado, float) else resultado
        
        globo_resultado.config(
            text=f"🎯 Resultado: {resultado_formateado}",
            bg=GLOBO_COLOR,
            fg="#2c3e50",  # Azul oscuro
            font=("Arial", 16, "bold")
        )
        
    except ValueError:
        messagebox.showerror("Error", "¡Solo se permiten números!")

# Crear ventana principal
root = tk.Tk()
root.title("✨ Calculadora Globo")
root.geometry("380x550")
root.configure(bg=BG_COLOR)
root.resizable(True, True)

# Marco contenedor
frame = tk.Frame(root, bg=BG_COLOR, padx=20, pady=20)
frame.pack(expand=True, fill="both")

# Elementos de la UI
tk.Label(frame, text="Calculadora con Globos", bg=BG_COLOR, font=("Arial", 18, "bold"), fg="#2c3e50").pack(pady=10)

# Campos de entrada
def crear_campo(etiqueta):
    tk.Label(frame, text=etiqueta, bg=BG_COLOR, font=FONT).pack(pady=5)
    entrada = tk.Entry(frame, font=FONT, bd=2, relief="groove", justify="center")
    entrada.pack(fill="x", pady=5, ipady=8)
    return entrada

entrada_num1 = crear_campo("Primer número:")
entrada_num2 = crear_campo("Segundo número:")

# Selector de operación
tk.Label(frame, text="Operación:", bg=BG_COLOR, font=FONT).pack(pady=5)
operacion = tk.StringVar(value="+")
tk.OptionMenu(frame, operacion, "+", "-", "×", "÷").config(
    font=FONT, bg="white", activebackground=BUTTON_COLOR
).pack(fill="x", pady=10)

# Botón de cálculo
tk.Button(
    frame,
    text="🔄 CALCULAR",
    command=calcular,
    bg=BUTTON_COLOR,
    fg="white",
    activebackground="#ff5252",
    font=("Arial", 14, "bold"),
    relief="raised",
    bd=3
).pack(fill="x", pady=20, ipady=12)

# Globo de resultado
globo_resultado = tk.Label(
    frame,
    text="⬇️ El resultado aparecerá aquí ⬇️",
    bg=GLOBO_COLOR,
    fg="#2c3e50",
    font=("Arial", 14),
    relief="solid",
    bd=1,
    padx=20,
    pady=15,
    wraplength=300
)
globo_resultado.pack(fill="x", pady=10)

# Créditos
tk.Label(
    frame,
    text="Hecho con  para ti",
    bg=BG_COLOR,
    fg="#7f8c8d",
    font=("Arial", 10)
).pack(side="bottom", pady=10)

root.mainloop()
