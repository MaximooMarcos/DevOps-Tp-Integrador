import time
from fastapi import FastAPI, Request
from app.logger import logger

app = FastAPI(
    title="DevOps TP Integrador API",
    description="API REST básica con FastAPI, logs estructurados en JSON y documentación Swagger.",
    version="1.0.0"
)

# Middleware para interceptar peticiones y registrar logs estructurados en JSON
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = round((time.time() - start_time) * 1000, 2)

    # Log estructurado obligatorio
    logger.info(
        "Request procesada",
        extra={
            "path": request.url.path,
            "status_code": response.status_code,
            "method": request.method,
            "duration_ms": process_time
        }
    )
    return response

@app.get("/", tags=["General"])
def read_root():
    return {"message": "Bienvenido al TP Integrador DevOps API"}

@app.get("/health", tags=["Salud"])
def health_check():
    return {"status": "ok", "service": "devops-api"}