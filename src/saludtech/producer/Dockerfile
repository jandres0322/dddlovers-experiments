FROM python:3.9-slim

WORKDIR /app

# Copiar el archivo de requerimientos y luego instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Comando para iniciar el productor (ajusta según tu script)
CMD ["python", "producer.py"]
