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

1. Instalamos un cliente VNC (Ej. RealVNC) desde el repositorio de apliciones Play Store.
   
2. Iniacimos RealVNC y añadimos una nueva conexión. Clic en el icono **+**.

3. Añadimos la IP de nuestro servidor VNC y el puerto de escucha (normalmente 5900). Además añadimos el nombre del equipo. Pulsar **Create**.
4. Nos saldra una pantalla con el resumen de la conexión. Pulsar **Connect**.
5. En la siguiente pantalla nos muestra una advertencia de conexión no encriptada **Unencrypted connection**. Si quieres desactiva la advertencia para conexiones sucesivas con **Warn me every time**.
6. Introduce la contraseña configurada anteriormente para el servidor. Pulsar **Continue**.
7. Ya estamos conectados a nuestro equipo Educaandos. Ahora se podrá ver en la pizarra todo lo que hagamos en nuestro PC. Incluso es posible manejar el equipo desde la pizarra.
