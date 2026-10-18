import random
import time
import urllib.error
import urllib.request

BASE_URL = "http://localhost:8000"

# Rutas con ponderación probabilística (endpoint, peso)
ENDPOINTS = [
    ("/", 0.50),  # 50% de las peticiones a la raíz (200 OK)
    ("/health", 0.30),  # 30% a /health (200 OK)
    ("/docs", 0.10),  # 10% a la documentación Swagger (200 OK)
    (
        "/route-not-found",
        0.10,
    ),  # 10% a ruta inexistente para generar errores 404 (Golden Signal)
]

print("🚀 Iniciando generador de tráfico hacia la API FastAPI...")
print("Pulsá Ctrl + C en cualquier momento para detener la simulación.\n")

count = 0
try:
    while True:
        # Seleccionar endpoint y peso correctamente descomprimiendo la tupla
        paths, weights = zip(*ENDPOINTS)
        endpoint = random.choices(paths, weights=weights)[0]
        url = f"{BASE_URL}{endpoint}"

        start_time = time.time()
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "DevOpsTrafficSim/1.0"}
            )
            with urllib.request.urlopen(req) as response:
                status_code = response.status
        except urllib.error.HTTPError as e:
            status_code = e.code
        except Exception as e:
            status_code = f"ERR ({e})"

        elapsed_ms = (time.time() - start_time) * 1000
        count += 1

        print(
            f"[{count:04d}] GET {endpoint:<20} -> Status: {status_code} | Latencia: {elapsed_ms:.2f} ms"
        )

        # Ráfagas aleatorias entre 100ms y 500ms
        time.sleep(random.uniform(0.1, 0.5))

except KeyboardInterrupt:
    print(f"\n🛑 Simulación de tráfico finalizada. Total de peticiones: {count}")