# Usa un'immagine base di Python 3.9 slim per mantenere il container leggero
FROM python:3.9-slim

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Copia il file requirements.txt e installa le dipendenze
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copia tutto il contenuto dell'app nel container
COPY . /app

# Espone la porta su cui Flask funzionerà (5000)
EXPOSE 5000

# Comando per eseguire l'applicazione Flask
CMD ["python", "app/app.py"]
