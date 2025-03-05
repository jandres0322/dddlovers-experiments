FROM python:3.9-slim

WORKDIR /app

# Copia el archivo de dependencias y lo instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación
COPY . .

# El comando por defecto se sobrescribe en docker-compose
CMD ["python", "consumer.py"]
