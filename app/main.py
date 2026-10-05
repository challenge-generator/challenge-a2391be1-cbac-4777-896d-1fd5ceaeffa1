import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import Settings
from app.api.v1.endpoints import router as api_router

# Configuración de la aplicación FastAPI
app = FastAPI(
    title="Sensor Analytics API",
    description="API para consultar datos de sensores almacenados en DynamoDB",
    version="0.1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carga de configuración
settings = Settings()

# Montaje de routers
app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    """Inicializa recursos al arrancar la aplicación"""
    from app.config.dynamodb import init_dynamodb
    await init_dynamodb()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=settings.app_host,
        port=settings.app_port,
        log_level=settings.log_level.lower()
    )