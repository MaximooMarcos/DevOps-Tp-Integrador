# --- Etapa 1: Builder (Construcción de dependencias) ---
    FROM python:3.11-slim AS builder

    WORKDIR /app
    
    # Instalar herramientas necesarias para compilar paquetes si hiciera falta
    RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*
    
    # Copiar archivo de requerimientos e instalar dependencias en una carpeta temporal
    COPY requirements.txt .
    RUN pip install --no-cache-dir --prefix=/install -r requirements.txt
    
    # --- Etapa 2: Runner (Imagen final liviana y segura) ---
    FROM python:3.11-slim AS runner
    
    WORKDIR /app
    
    # Copiar las dependencias instaladas desde la etapa builder
    COPY --from=builder /install /usr/local
    
    # Crear usuario sin privilegios root por seguridad
    RUN adduser --disabled-password --gecos "" appuser && chown -R appuser:appuser /app
    USER appuser
    
    # Copiar el código fuente de la aplicación
    COPY app/ ./app/
    
    # Exponer el puerto donde corre FastAPI
    EXPOSE 8000
    
    # Comando para ejecutar la aplicación
    CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]