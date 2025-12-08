#!/bin/bash
# Script de instalación

APP_NAME="Conexión Remota SmartBoard"
SCRIPT_FILE="conexion_smartboard.py"
ICON_FILE="conexion_smartboard.png"
APP_FILE="conexion_smartboard.desktop"

# Directorios de destino
INSTALL_DIR="$HOME/.local/bin" # Directorio para scripts ejecutables
ICON_DIR="$HOME/.local/share/icons" # Directorio para iconos
APP_DIR="$HOME/.local/share/applications" # Directorio para aplicaciones
DESKTOP_DIR="$HOME/Escritorio" # Directorio de Escritorio

echo "Iniciando instalación de $APP_NAME..."

# 1. Crear los directorios si no existen
mkdir -p $INSTALL_DIR
mkdir -p $ICON_DIR
mkdir -p $APP_DIR

# 2. Copiar el script  de Python y otros archivos a los directorios correspondientes
cp "$SCRIPT_FILE" "$INSTALL_DIR"
cp "$ICON_FILE" "$ICON_DIR"
cp "$APP_FILE" "$APP_DIR" 
cp "$APP_FILE" "$DESKTOP_DIR"

# 3. Permitir lanzar la aplicación desde el Escritorio
gio set "$DESKTOP_DIR/$APP_FILE" metadata::trusted true

# 4. Dar permisos de ejecución
chmod +x "$INSTALL_DIR/$SCRIPT_FILE"
chmod +x "$DESKTOP_DIR/$APP_FILE"

# 5. Copiar archivos de configuración de Shell
cp .profile $HOME
cp .bashrc $HOME
cp .bash_logout $HOME

## 6. Cargar los archivos de configuración
#source "$HOME/.profile"
#source "$HOME/.bashrc"
#source "$HOME/.bash_logut"

echo "Instalación completada. Puedes ejecutar el script como: conexion_smartboard.py"

# 6. Notificar al usuario y cerrar la sesión para aplicar cambios
echo "===================================================================="
echo "✅ Instalación de $APP_NAME completada."
echo ""
echo "❗ AVISO IMPORTANTE:"
echo "Se requiere **cerrar la sesión** para que los cambios en .bashrc, .profile, etc., surtan efecto."
echo "La sesión de GNOME se cerrará automáticamente en 10 segundos."
echo "===================================================================="

# Pausa de 10 segundos para dar tiempo a leer el mensaje
sleep 10

# Cerrar la sesión de GNOME
/usr/bin/gnome-session-quit --logout --no-prompt
