# Conexión Inalámbrica desde una pizarra SmartBoard MX V5 a Educaandos 20.04

## Prerequisitos
1. Instalar el servidor x11vnc desde el repositorio de Educaandos.
![Instalar servidor x11VNC](pantallazos/servidorVNC/servidorVNC_0.png)

## Instalación del servidor VNC

1. Descargar el archivo **Conexion_remota_SmartBoard.zip**.

2. Descomprimir el archivo.

Desde la línea de comandos
~~~
unzip conexion_smartboard.zip
~~~

3. Muevete a la carpeta descomprimida.


Desde la línea de comandos.
~~~
cd conexion_smartboard
~~~

4. Concede permisos de ejecución al archivo **install.sh**
~~~
chmod u+x install.sh
~~~
5. Ejecuta el script de instalación
~~~
./install.sh
~~~
También con
~~~
bash install.sh
~~~


## Ejecución y configuración del Servidor VNC
Esto lo hacemos en nuestro portátil o PC con Educaandos.

1. En el icono del escritorio **Conexión SmartBoard** mostrar el menú contextual y seleccionar la opción **Permitir Lanzar**.

2. Iniciar la aplicación **Conexión SmartBoard**. En la pantalla se muestra la dirección IP actual del equipo y cuatro botones:

- Ver/Actualizar IP
- Configurar/Cambiar Contraseña VNC
- Iniciar Servidor VNC
- Parar Servidor VNC

![Iniciar la aplicación](pantallazos/servidorVNC/servidorVNC_1.png)

3. (Opcional) Actualizar la dirección IP si es que hubiera cambiado desde que se inicio el programa.

![Ver/Actualizar IP](pantallazos/servidorVNC/servidorVNC_2.png)

4. Configurar la contraseña del servidor VNC. Esto lo hacemos por seguridad para que no pueda conectarse cualquiera a nuestro PC o portátil Educaandos.

![Configurar contraseña](pantallazos/servidorVNC/servidorVNC_3.png)

3. Iniciar el servidor VNC.

![Iniciar servidor VNC](pantallazos/servidorVNC/servidorVNC_4.png)

4. Conectase desde el cliente VNC.

Ir al apartado [Instalación y Configuración del Cliente VNC.](#instalación-y-configuración-del-cliente-vnc)


5. Parar el servidor VNC cuando hayamos terminado.

![alt text](pantallazos/servidorVNC/servidorVNC_5.png)

## Instalación y configuración del cliente VNC
Esto lo hacemos en nuestra pizarra SmartBoard MX V5

1. Instalamos un cliente VNC (Ej. RealVNC Viewer) desde el repositorio de apliciones Play Store.

![Instalar RealVNC](<pantallazos/clienteVNC/Pantallazo_RVNC Viewer_0.jpg>)

   
2. Iniciamos RealVNC.
<!--<img src="https://github.com/crea-soft/conexion-smartboard-educaandos/blob/main/pantallazos/clienteVNC/Pantallazo_RVNC%20Viewer_1.jpg" alt="Instalación Cliente VNC" style="width:25%; height:auto;">-->

![Iniciar RealVNC](<pantallazos/clienteVNC/Pantallazo_RVNC Viewer_1.jpg>)

4. Añadimos una nueva conexión.     Clicar en el icono **+**.

5. Añadimos la IP de nuestro servidor VNC y el puerto de escucha (normalmente 5900). Además añadimos el nombre del equipo. Pulsar **Create**.


![Añadir Conexión](<pantallazos/clienteVNC/Pantallazo_RVNC Viewer_2.jpg>)


6. Nos saldra una pantalla con el resumen de la conexión. Pulsar **Connect**.

![Configurar Conexión](<pantallazos/clienteVNC/Pantallazo_RVNC Viewer_3.jpg>)

7. En la siguiente pantalla nos muestra una advertencia de conexión no encriptada **Unencrypted connection**. Si quieres desactiva la advertencia para conexiones sucesivas con **Warn me every time**.

![Advertencia](<pantallazos/clienteVNC/Pantallazo_RVNC Viewer_4.jpg>)

8. Introduce la contraseña configurada anteriormente para el servidor. Pulsar **Continue**.

![Introducir Contraseña](<pantallazos/clienteVNC/Pantallazo_RVNC Viewer_5.jpg>)

9. Ya estamos conectados a nuestro equipo Educaandos. Ahora se podrá ver en la pizarra todo lo que hagamos en nuestro PC. Incluso es posible manejar el equipo desde la pizarra.

![Conectado Orientación Vertical](<pantallazos/clienteVNC/Pantallazo_RVNC Viewer_6.jpg> )

![Conectado Orientación Horizontal](<pantallazos/clienteVNC/Pantallazo_RVNC Viewer_7.jpg>)