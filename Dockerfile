# Usa un'immagine base ufficiale Python
FROM python:3.9-slim

# Imposta la directory di lavoro nel contenitore
WORKDIR /app

# Copia i file del progetto nella directory di lavoro
COPY . .

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Esponi la porta su cui Flask gira
EXPOSE 5000

# Comando per eseguire l'app
CMD ["python", "app/app.py"]
