# Bienvenido a PrimaryGPT

PrimaryGPT es un chatbot que contiene información acerca de Primary para que le puedas preguntar y te responda.

Usa LongChain para generar respuestas, la API de OpenAI para FineTunning y la API de Slack para la interfaz.

## Instalación

Primero, instalar todas las dependencias de LangChain:

```bash
pip install langchain[all]
```

Luego, instalar las dependencias del proyecto.

```bash
pip install -r requirements.txt
```

## Credenciales de Google

Para usar la API de Google, es necesario tener un archivo JSON con las credenciales de Google Cloud Platform. Para obtenerlo, sigue los siguientes pasos:

1. Ve a la [consola de Google Cloud Platform](https://console.cloud.google.com/). 
> Deberás ingresar con una cuenta que no sea la de Primary, ya que no posee permisos.
2. Crea un nuevo proyecto.
3. Crea una nueva cuenta de servicio.
4. Crea credenciales OAUTH para la cuenta de servicio.
5. Descarga el archivo JSON con las credenciales.
6. Copia el archivo JSON en la carpeta `credentials` del proyecto y renombra el archivo a `credentials.json`. 

## Configuración del proyecto

Para configurar el proyecto, es necesario crear un archivo `.env` en la raíz del proyecto con las siguientes variables:

```bash
OPENAI_API_KEY= 
Clave de la API de OPEN AI

GOOGLE_APPLICATION_CREDENTIALS=
Con el path donde se encuentra el archivo credentiasl.json 
Por defecto: `./credentials/credentials.json`

```

## Carpeta de documentos
Para setear el ID de la carpeta de GDrive se debe obtener desde el browser y copiarla en la variable `folder_id = "ief98ujsk9a5eysy90kytd-t"` del archivo `main.py`

![image](https://www.haihai.ai/content/images/2023/05/Screenshot-2023-05-26-at-9.32.33-AM.png)