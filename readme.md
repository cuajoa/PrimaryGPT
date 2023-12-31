![image](images/logo.png)


# Bienvenido a PrimaryGPT

PrimaryGPT es un repositorio que posee ejemplos de LLM con LangChain.

Los casos de usos actuales son los siguientes:

- Leer documentos de una carpeta de Google Drive para aprender de la info que posee esa carpeta
- Conectarse a Confluence y aprender de un espacio en particular

## Ejemplos
Encontrarán ejemplos de los siguientes casos de uso:

- Cómo utilizar distintos Loader de Langchain para cargar documentos 
- Cómo utilizar los splitter de Langchain para separar documentos en oraciones
- Cómo almacenar los documentos en una base de datos de vectores (ChromaDB)
- Cómo obtener información de la base de datos de vectores (ChromaDB) y como usar compresores

### Casos de Uso
Dentro de la carpeta de `/examples/9-CasosUso` encontrarán ejemplos de los siguientes casos de uso:
- Chatbot que retorna casos de prueba de una funcionalidad que apendió del loader desde Confluence
- Chatbot que retorna Historias de usuario y Criterios de aceptación de una funcionalidad que apendió del loader desde Confluence
- Chatbot que que funciona como knowledge base de una funcionalidad que apendió del loader desde gDrive

> Encontrarán distintos ejemplos usando Davinci o GPT3-Turbo.

## Instalación

Instalar las dependencias del proyecto.

```bash
pip install -r requirements.txt
```

Ejecutar el siguiente comando para levantar la UI de Chainlit, aún está en pruebas experimentales:
```bash
chainlit run main.py -w
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

Para configurar el proyecto, es necesario crear un archivo `.env` en la raíz del proyecto.
Para ello, renombrar el archivo `.env.example` a `.env` y completar los datos.

## Carpeta de documentos
Para setear el ID de la carpeta de GDrive se debe obtener desde el browser y copiarla en la variable `folder_id = "1qVqm6IBs5DWeytuwCQ95b09GVED5DGLU"` del archivo `/examples/9-CasosUso/GdriveKnowledgeBase.py`

![image](images/gdrive.png)


---

# Recursos

[LangChain Official Site](https://python.langchain.com/docs/get_started)

[8 Minutes LangChain OpenAI Beginner Tutorial | ChatGPT with your PDF](https://youtu.be/FuqdVNB_8c0)

[The LangChain Cookbook - Beginner Guide To 7 Essential Concepts](https://youtu.be/2xxziIWmaSA)

[Augmented Language Models (LLM Bootcamp)](https://youtu.be/YdeuQhlHmCA)

[LLMOps (LLM Bootcamp)](https://youtu.be/Fquj2u7ay40)

[Chroma User Guide](https://docs.trychroma.com/usage-guide)

## Cursos

[ChatGPT Prompt Engineering for Developers](https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/1/introduction)

[UDEMY - LangChain- Develop LLM powered applications with LangChain](https://primary.udemy.com/course/langchain/)

## Repositorios útiles

[Awesome LangChain](https://github.com/kyrolabs/awesome-langchain)