#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
import socket
import subprocess
import os

# ---------------- Definiciones de Rutas ----------------
# Asegúrate de que estas rutas sean correctas para tu sistema Linux.
VNC_EXECUTABLE = "/usr/bin/x11vnc" 
TERMINAL_COMMAND = "gnome-terminal" # <-- ¡Cambia esto si usas otro terminal (ej: "konsole", "xterm")!

# ---------------- Funciones Auxiliares de Sistema ----------------

def obtener_ip_local():
    """Intenta obtener la dirección IP local de la máquina."""
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
    except Exception:
        try:
            ip_address = socket.gethostbyname(socket.gethostname())
        except Exception:
            ip_address = "Error: No se pudo obtener la IP."
    finally:
        if s:
            s.close()
    return ip_address

def mostrar_ip():
    """Obtiene la IP y actualiza la etiqueta en la ventana."""
    ip = obtener_ip_local()
    ip_var.set(ip)

def get_running_vnc_pids():
    """
    Usa 'pgrep' para obtener la lista de PIDs de todos los procesos 'x11vnc'.
    """
    try:
        result = subprocess.run(['pgrep', 'x11vnc'], capture_output=True, text=True, check=False)
        
        if result.returncode == 0:
            pids = [int(p.strip()) for p in result.stdout.split() if p.strip().isdigit()]
            return pids
        return []
    except FileNotFoundError:
        messagebox.showerror("Error de Ejecución", "El comando 'pgrep' no fue encontrado. ¿Está instalado?")
        return []
    except Exception as e:
        messagebox.showerror("Error de Verificación", f"Ocurrió un error al verificar procesos: {e}")
        return []

# ---------------- Función configuracion_contrasena_vnc ----------------

def configurar_contrasena_vnc():
    """
    Ejecuta x11vnc -storepasswd DENTRO de un nuevo terminal para permitir 
    la interacción del usuario (ingreso de contraseña).
    """
    # 1. Avisar al usuario
    messagebox.showinfo(
        "Configuración de Contraseña VNC",
        "Se abrirá una nueva ventana de terminal para que ingreses y confirmes la contraseña de VNC.\n\n"
        "¡Introduce la contraseña y luego cierra la ventana de terminal!"
    )

    # 2. Comando completo para ejecutar en la terminal
    # Esto asegura que el comando se ejecute y luego la terminal permanezca abierta (opcional, pero útil)
    vnc_passwd_command = f'"{VNC_EXECUTABLE}" -storepasswd {os.path.expanduser("~/.vnc/passwd")}'
    
    # Comando para abrir una nueva terminal y ejecutar el comando VNC
    full_terminal_command = [
        TERMINAL_COMMAND,
        '--',
        '/bin/bash',
        '-c',
        # Ejecutamos el comando VNC y luego un 'read' para esperar a que el usuario presione Enter,
        # o simplemente el comando y dejamos que la terminal se cierre.
        # En este caso, solo ejecutamos y la terminal se cerrará o esperará según la configuración por defecto.
        vnc_passwd_command
    ]
    
    try:
        # Usamos Popen (sin esperar) ya que el proceso se ejecutará en una ventana separada
        subprocess.Popen(full_terminal_command, start_new_session=True)
        # No podemos saber si fue exitoso hasta que la terminal termine,
        # por lo que asumimos el éxito si se lanza la terminal.
        messagebox.showinfo("Contraseña VNC", "Ventana de configuración de contraseña lanzada. Por favor, completa los pasos en la nueva terminal.")
        
    except FileNotFoundError:
        messagebox.showerror("Error de Ejecución", f"El comando de terminal ('{TERMINAL_COMMAND}') no fue encontrado. ¿Está instalado?")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")


# ---------------- Funciones de control de VNC (Sin cambios) ----------------

def iniciar_servidor_vnc():
    """Verifica si x11vnc ya está corriendo. Si no, lo inicia."""
    running_pids = get_running_vnc_pids()
    
    if running_pids:
        pid_list = ", ".join(map(str, running_pids))
        messagebox.showwarning("Servidor VNC", f"El servidor VNC ya está corriendo con el siguiente PID: {pid_list}")
        return

    # Comando a ejecutar para x11vnc, usando la RUTA ABSOLUTA
    vnc_command = [
        VNC_EXECUTABLE, 
        "-bg", "-reopen", "-forever", "-rfbauth", 
        os.path.expanduser("~/.vnc/passwd"), 
        "-display", ":0"
    ]

    try:
        # Ejecutar el proceso sin esperar a que termine
        subprocess.Popen(vnc_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        messagebox.showinfo("Servidor VNC", "Servidor VNC iniciado con éxito en segundo plano.")
        
    except FileNotFoundError:
        messagebox.showerror("Error de Ejecución", f"El comando '{VNC_EXECUTABLE}' no fue encontrado. ¿Está instalado?")
    except Exception as e:
        messagebox.showerror("Error al Iniciar VNC", f"Ocurrió un error: {e}")

def parar_servidor_vnc():
    """Detiene TODOS los procesos x11vnc del sistema usando pkill."""
    running_pids = get_running_vnc_pids()
    
    if not running_pids:
        messagebox.showwarning("Servidor VNC", "No se encontró ningún proceso 'x11vnc' corriendo.")
        return

    try:
        # pkill NO necesita la ruta absoluta porque es un comando de sistema estándar que está en el PATH
        result = subprocess.run(['pkill', 'x11vnc'], check=False) 
        
        if result.returncode == 0:
            pid_list = ", ".join(map(str, running_pids))
            messagebox.showinfo("Servidor VNC", f"Servidor VNC detenido con éxito. Procesos terminados: {pid_list}")
        else:
            messagebox.showerror("Error al Parar VNC", "pkill falló al detener los procesos. Revise permisos.")
            
    except FileNotFoundError:
        messagebox.showerror("Error de Ejecución", "El comando 'pkill' no fue encontrado. ¿Está instalado?")
    except Exception as e:
        messagebox.showerror("Error al Parar VNC", f"Ocurrió un error: {e}")

# ---------------- Configuración de la Ventana Principal (Tkinter) ----------------

# 1. Crear la ventana principal
root = tk.Tk()
root.title("Conexión a pizarra SmartBoard MX V5") 
root.geometry("450x300") 
root.resizable(False, False)


# 2. Variable para almacenar y mostrar la IP
ip_var = tk.StringVar()
ip_var.set("Calculando IP...") 

# --- Sección de IP ---
titulo_label = tk.Label(root, text="Dirección IP de Red Local (para conexión VNC):", font=("Arial", 10))
titulo_label.pack(pady=(15, 5))

ip_label = tk.Label(root, textvariable=ip_var, fg="darkgreen", font=("Arial", 14, "bold"), padx=10, pady=5, relief=tk.SUNKEN)
ip_label.pack()

mostrar_btn = tk.Button(root, text="Ver/Actualizar IP", command=lambda: (mostrar_ip(), messagebox.showinfo("Dirección IP Local", f"La dirección IP del equipo es:\n{ip_var.get()}")), bg="#3498DB", fg="white", font=("Arial", 9))
mostrar_btn.pack(pady=(5, 10))

# --- Separador ---
separator1 = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
separator1.pack(fill='x', padx=5, pady=5)

# --- Sección de Contraseña VNC ---
contrasena_btn = tk.Button(
    root,
    text="🔑 Configurar/Cambiar Contraseña VNC",
    command=configurar_contrasena_vnc,
    bg="#F39C12", # Naranja
    fg="white", 
    font=("Arial", 10, "bold"),
    width=40 
)
contrasena_btn.pack(pady=10)

# --- Separador ---
separator2 = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
separator2.pack(fill='x', padx=5, pady=5)


# --- Sección de Control VNC ---
vnc_frame = tk.Frame(root)
vnc_frame.pack(pady=10)

# Botón INICIAR VNC
iniciar_btn = tk.Button(vnc_frame, text="Iniciar Servidor VNC", command=iniciar_servidor_vnc, bg="#2ECC71", fg="white", font=("Arial", 10, "bold"), width=20)
iniciar_btn.pack(side=tk.LEFT, padx=10)

# Botón PARAR VNC
parar_btn = tk.Button(vnc_frame, text="Parar Servidor VNC", command=parar_servidor_vnc, bg="#E74C3C", fg="white", font=("Arial", 10, "bold"), width=20)
parar_btn.pack(side=tk.RIGHT, padx=10)


# 3. Llama a la función para obtener y mostrar la IP inmediatamente
mostrar_ip() 

# 4. Iniciar el bucle de eventos de Tkinter
root.mainloop()
