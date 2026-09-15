# 1. Imagen base ligera de Python
FROM python:3.11-slim

# 2. Directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar archivo de dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el código de la aplicación
COPY app.py .

# 5. Puertos y comando para ejecutar la app
EXPOSE 8080
CMD ["python", "app.py"]
