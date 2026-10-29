from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app.routers import clientes, productos, pedidos

# Inicializar la aplicación
app = FastAPI(
    title="Taller 3 ADSO - Tienda",
    version="3.0",
    description="API relacional: clientes, productos, pedidos y detalles",
)

# Obtener la ubicación de la carpeta app
BASE_DIR = Path(__file__).resolve().parent

# Habilitar los archivos HTML y CSS
app.mount("/app", StaticFiles(directory=BASE_DIR / "static", html=True), name="static")

# Registrar los routers
app.include_router(clientes.router)
app.include_router(productos.router)
app.include_router(pedidos.router)


# Ruta principal
@app.get("/", tags=["Inicio"])
def inicio():
    return {"mensaje": "API tienda ADSO", "documentacion": "/docs"}
