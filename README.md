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
2. Iniacimos RealVNC y añadimos una nueva conexión.
