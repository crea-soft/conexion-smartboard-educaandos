# Conexión Inalámbrica desde una pizarra SmartBoard MX V5 a Educaandos 20.04

## Instalación y configuración del Servidor VNC
Esto lo hacemos en nuestro portátil o PC con Educaandos.

1. Instalar el servidor VNC desde el repositorio de Educaandos
~~~
apt install x11vnc
~~~
2. Abrir un terminal y configurar la contraseña del servidor VNC. Esto lo hacemos por seguridad para que no pueda conectarse cualquiera a nuestro PC o portátil.
~~~
x11vnc --storepasswd
~~~
La contraseña se guardará por defecto en el fichero _~/.vnc/passwd_ en la carpeta de usuario

3. Iniciar el servidor VNC.
~~~
x11vnc -bg -reopen -forever -rfbauth ~/.vnc/passwd -display :0
~~~

## Instalación y configuración del cliente VNC
Esto lo hacemos en nuestra pizarra SmartBoard MX V5

1. Instalamos un cliente VNC (Ej. RealVNC Viewer) desde el repositorio de apliciones Play Store.

<!-- ![Pantallazo_RVNC Viewer_1](https://github.com/user-attachments/assets/d764a051-edf2-40f7-80f7-200a1997b221) -->

   
3. Iniciamos RealVNC.
<img src="https://github.com/crea-soft/conexion-smartboard-educaandos/blob/main/pantallazos/clienteVNC/Pantallazo_RVNC%20Viewer_1.jpg" alt="Instalación Cliente VNC" style="width:25%; height:auto;">  
4. Añadimos una nueva conexión. Clic en el icono **+**.

5. Añadimos la IP de nuestro servidor VNC y el puerto de escucha (normalmente 5900). Además añadimos el nombre del equipo. Pulsar **Create**.
6. Nos saldra una pantalla con el resumen de la conexión. Pulsar **Connect**.
7. En la siguiente pantalla nos muestra una advertencia de conexión no encriptada **Unencrypted connection**. Si quieres desactiva la advertencia para conexiones sucesivas con **Warn me every time**.
8. Introduce la contraseña configurada anteriormente para el servidor. Pulsar **Continue**.
9. Ya estamos conectados a nuestro equipo Educaandos. Ahora se podrá ver en la pizarra todo lo que hagamos en nuestro PC. Incluso es posible manejar el equipo desde la pizarra.
