# Usa una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo
WORKDIR /usr/src/app

# Copia los archivos de requerimientos y realiza la instalación
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Instala el controlador de MongoDB para Django
RUN pip install djongo

# Copia el código fuente del proyecto al contenedor
COPY . .

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
