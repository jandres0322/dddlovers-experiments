# dddlovers-experiments

Este repositorio contiene experimentos relacionados con Domain-Driven Design (DDD) y su aplicación en proyectos de software. A continuación, se detalla la estructura del proyecto y las instrucciones para su despliegue.

## Estructura del Proyecto

La estructura principal del proyecto es la siguiente:

```plaintext
dddlovers-experiments/
├── src/
│   └── saludtech/
├── .coveragerc
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── saludtech.Dockerfile
```

- `src/saludtech/`: Directorio principal del código fuente del proyecto, que contiene los módulos y paquetes desarrollados.
- `.coveragerc`: Archivo de configuración para la herramienta de cobertura de código.
- `.gitignore`: Archivo que especifica los archivos y directorios que deben ser ignorados por Git.
- `docker-compose.yml`: Archivo de configuración para Docker Compose, que define los servicios y su configuración para el despliegue del proyecto.
- `requirements.txt`: Archivo que lista las dependencias de Python necesarias para ejecutar el proyecto.
- `saludtech.Dockerfile`: Archivo Dockerfile que contiene las instrucciones para construir la imagen de Docker específica para el servicio `saludtech`.

## Despliegue del Proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/jandres0322/dddlovers-experiments.git
cd dddlovers-experiments
```

### 2. Instalar las dependencias

Se recomienda utilizar un entorno virtual para gestionar las dependencias de Python. Puede crear y activar un entorno virtual utilizando `venv`:

```bash
python3 -m venv venv
source venv/bin/activate  # En sistemas Unix/macOS
# venv\Scripts\activate   # En sistemas Windows
```

Luego, instale las dependencias listadas en `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Ejecutar el proyecto localmente

Para ejecutar el proyecto en su entorno local, puede utilizar el siguiente comando:

```bash
python src/saludtech/main.py
```

Asegúrese de reemplazar `main.py` con el nombre del archivo principal de ejecución si es diferente.

### 4. Despliegue con Docker

Si prefiere desplegar el proyecto utilizando Docker, siga estos pasos:

- **Construir la imagen de Docker**:

  ```bash
  docker build -t saludtech -f saludtech.Dockerfile .
  ```

- **Ejecutar la imagen en un contenedor**:

  ```bash
  docker run -d -p 8000:8000 saludtech
  ```

  Esto ejecutará el contenedor y expondrá el servicio en el puerto 8000. Ajuste el puerto según sea necesario.

Alternativamente, puede utilizar Docker Compose para orquestar el despliegue si el proyecto consta de múltiples servicios:

```bash
docker-compose up -d
```

Este comando levantará todos los servicios definidos en el archivo `docker-compose.yml`.
