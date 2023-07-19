

# Introducción
La **esco api fondos** es un complemento de esco fondos para poder realizar integraciones a su negocio y poder enviar o tomar información de esco fondos.

## ¿Qué puedo realizar?
**esco api fondos** cuenta con 3 segmentos que le permitirán realizar diferentes acciones.

### Segmento Inversiones
Con este segmento de inversiones podrán automatizar la operatoria de los fondos que administren dentro de esco fondos.
Podrán enviar inversiones a los fondos, como así tambien consultar las inversiones realizadas.

### Segmento Consultivo
Con el segmento consultiva podrán obtener información sobre las cuentas cuotapartistas como posición, solicitudes y liquidaciones, como así también información de cartera de los fondos.

### Segmento Transaccional
Con el segmento transaccional podrán realizar alta de cuentas y personas como así también ingresar solicitudes de suscripción y rescates en esco fondos.

## ¿Cómo utilizarla?
Para obtener una imágen deberá contar con una cuenta en  [Docker Hub](https://hub.docker.com/), nos deberá informar el usuario de la cuenta y le compartiremos la imágen de **esco api fondos** a través de ese medio.

Luego deberá montarla en un ambiente en su infraestructura con los [requerimientos](https://clientes.primary.com.ar/requerimientos/esco-api/) adecuados.

> Disponemos de un [Sandbox](https://api.sistemasesco.com/swagger/index.html?urls.primaryName=esco%20fondos%20v%205) para que pueda realizar sus integraciones sin necesidad de instalar **esco api fondos** en sus ambientes.


# Instalación y Configuración

## Requerimientos

Para conocer los requerimientos de la **esco api fondos** le recomendamos que revise los requerimientos en el [siguiente link](https://clientes.primary.com.ar/docs/requerimientos/esco-api/).

Es requesito mandatorio tener instalado el aplicativo de **esco fondos**.

## Instalación

### Base de datos

Se deberán ejecutar los scripts provistos por Primary correspondientes a la versión a instalar. Estos scripts deben ser ejecutados en la base de datos de **esco fondos**.

### Esco API

Una vez que le hayamos compatido la imagen a través de DokerHub, se les proporcionará un archivo [docker-compose.yml](https://drive.google.com/file/d/1LJys7L0biY6Fam-Oi8z8ExzwmTtfU935/view?usp=sharing) para parametrizar y levantar la imagen de la API en sus ambientes.

Deberá parametrizar la conexiṕon a la base de datos de **esco fondos**.

`VFDB_CONNECTIONSTRING=Data Source=192.168.22.11;Initial Catalog=vfCli_Cliente;Trusted_Connection=false;user id=UsuarioGenerico;pwd=vesco;Connect Timeout=30000`

### Levantando el ambiente

1. Crear la network de esco dentro de la NAT de docker



```bash
docker network create --gateway 10.18.1.1 --subnet 10.18.1.0/24 esconetwork
```


2. Hacer login contra el docker hub


```bash
	docker login -u <DockerHubId> -p <password de docker hub>
```



**Ejemplo**


```bash
	docker login -u midockerhubid -p midockerhubpass
```



3. Levantar las aplicaciones


```bash
docker-compose up -d
```


4. Posicionarse en la ruta donde se aloja el Compose.yml y correr las siguientes lineas de comando:


```bash
docker-compose -f archivo_compose.yml down  # Baja la API
docker system prune -a -f  # Limpia las imagenes
docker network create --gateway 10.18.1.1 --subnet 10.18.1.0/24 esconetwork  # Crea la red
docker-compose -f archivo_compose.yml up -d	# Sube la API
```


5. Para verificar que **esco api fondos** se encuentra levantada, se deberá conectar a la url de conexión y ejecutar alguno de los métodos.

Para el ejemplo anterior: `http://192.168.22.11:6003/swagger/index.html`

### Aclaraciones
Si ya tiene levantada una esco api fondos y desea actualizarla, antes de hacerlo deberá limpiar el contenedor con los siguientes comandos:


```bash
docker-compose -f compose.yml down
docker system prune -a -f
docker volume prune

```


> Tenga en cuenta que el nombre archivo `compose.yml` deberá ser el mismo que utilizó para levantar la imagen.