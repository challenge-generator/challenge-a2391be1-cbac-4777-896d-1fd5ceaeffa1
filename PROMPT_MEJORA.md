# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener un ZIP con el proyecto completo y arrancable.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Superficie de practica — NO resuelvas

Estos archivos SON el ejercicio de la persona. No los implementes; deja stubs.

- `tests/test_dynamodb_repository.py` — El topic pide TDD/pruebas: este archivo es el ejercicio.
- `tests/test_sensor_service.py` — El topic pide TDD/pruebas: este archivo es el ejercicio.

## Lo que le falta a este proyecto

Esto NO lo tenes que adivinar: salio de comparar el proyecto contra la arquitectura declarada del reto y de un analisis estatico del codigo. Completalo TODO.

### Archivos que la arquitectura del reto declara y no estan

Creálos con implementacion real, en la capa que les corresponde:

- `data/sample_data.json`
- `scripts/setup_dynamodb.py`
- `README.md`

### Referencias colgando en el codigo que si esta

Cada una rompe la compilacion:

- `app/api/v1/endpoints.py` — `Settings.get`: Se invoca `get` sobre `Settings`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.
- `app/api/v1/endpoints.py` — `Settings.post`: Se invoca `post` sobre `Settings`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.
- `app/api/v1/endpoints.py` — `Settings.delete`: Se invoca `delete` sobre `Settings`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.

## Como saber que terminaste

```bash
pip install -r requirements.txt && pytest -q
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Perfil
Chapter Ciencia de Datos, Especialidad Ingeniero IA, Tecnología NoSQL, Senior

### Brecha de conocimiento
Selecciona la clave partición adecuada para bases de datos NoSQL y extraer información de ellas. Candidato con experiencia en ciencia de datos e ingeniería de IA.

### Reto
- Tema: creación de bases de datos NoSQL
- Seniority: senior-l2
- Tipo: practical
- Título: Diseño y Consulta de Base de Datos NoSQL para Análisis de Datos
- Tiempo estimado: 8 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Selección de Clave de Partición — objetivo: Identificar y justificar la clave de partición óptima para la base de datos NoSQL. — entregable (NO resolver): Documento que describe la clave de partición seleccionada y la justificación.
- Fase 2: Implementación de la Base de Datos — objetivo: Implementar la base de datos NoSQL con la clave de partición seleccionada. — entregable (NO resolver): Base de datos NoSQL implementada con datos de prueba.
- Fase 3: Consulta de Datos — objetivo: Realizar consultas eficientes en la base de datos NoSQL. — entregable (NO resolver): Documento con los resultados de las consultas y sugerencias de mejora.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (ZIP).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: pyproject.toml ===
[tool.poetry]
name = "sensor_analytics"
version = "0.1.0"
description = "API para análisis de datos de sensores en DynamoDB"
authors = ["Ingeniero de IA <ia@example.com>"]
license = "MIT"
readme = "README.md"
packages = [{include = "app"}]

[tool.poetry.dependencies]
python = "^3.13"
fastapi = "0.115.0"
uvicorn = "0.30.1"
boto3 = "1.34.123"
pydantic = "2.8.2"
python-dotenv = "1.0.1"
pandas = "2.2.2"

[tool.poetry.group.test.dependencies]
pytest = "8.2.0"
moto = "5.0.0"

[tool.poetry.group.dev.dependencies]
poetry = "^1.8.2"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
addopts = "-v"

// === ARCHIVO: app/main.py ===
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

// === ARCHIVO: app/config/settings.py ===
import os
from pydantic import BaseSettings, Field, PositiveInt
from typing import Optional

class Settings(BaseSettings):
    """Configuración centralizada de la aplicación"""

    # Configuración de la aplicación
    app_host: str = Field(default="0.0.0.0", env="APP_HOST")
    app_port: PositiveInt = Field(default=8000, env="APP_PORT")
    log_level: str = Field(default="INFO", env="LOG_LEVEL")

    # Configuración de DynamoDB
    dynamodb_table_name: str = Field(..., env="DYNAMODB_TABLE_NAME")
    dynamodb_region: str = Field(default="us-east-1", env="DYNAMODB_REGION")
    dynamodb_endpoint_url: Optional[str] = Field(None, env="DYNAMODB_ENDPOINT_URL")

    # Configuración de rendimiento
    dynamodb_max_retries: PositiveInt = Field(default=3, env="DYNAMODB_MAX_RETRIES")
    query_limit: PositiveInt = Field(default=1000, env="QUERY_LIMIT")
    max_concurrent_queries: PositiveInt = Field(default=10, env="MAX_CONCURRENT_QUERIES")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    def get_dynamodb_config(self):
        """Devuelve la configuración para el cliente DynamoDB"""
        config = {
            "region_name": self.dynamodb_region,
            "max_attempts": self.dynamodb_max_retries
        }
        if self.dynamodb_endpoint_url:
            config["endpoint_url"] = self.dynamodb_endpoint_url
        return config

// === ARCHIVO: app/models/sensor_data.py ===
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class SensorData(BaseModel):
    """
    Modelo Pydantic para representar los datos de un sensor.
    Incluye validación de tipos y formatos para asegurar la integridad de los datos.
    """
    sensor_id: str = Field(..., description="Identificador único del sensor.")
    timestamp: datetime = Field(..., description="Fecha y hora de la medición en UTC.")
    temperature: Optional[float] = Field(None, description="Temperatura medida en grados Celsius.")
    humidity: Optional[float] = Field(None, description="Humedad relativa medida en porcentaje.")
    vibration: Optional[float] = Field(None, description="Vibración medida en Hz.")
    
    class Config:
        json_schema_extra = {
            "example": {
                "sensor_id": "sensor-001",
                "timestamp": "2024-05-20T10:00:00Z",
                "temperature": 23.5,
                "humidity": 45.0,
                "vibration": 0.2
            }
        }

    def partition_key(self) -> str:
        """
        Genera la clave de partición compuesta para DynamoDB.
        Formato: sensor_id#YYYY-MM-DD
        """
        return f"{self.sensor_id}#{self.timestamp.date()}"

    def sort_key(self) -> str:
        """
        Genera la clave de ordenación para DynamoDB.
        Formato: timestamp en ISO format (para ordenación cronológica).
        """
        return self.timestamp.isoformat()


class SensorDataCreate(SensorData):
    """
    Modelo para la creación de registros de sensores.
    Hereda de SensorData pero omite campos calculados.
    """
    pass


class SensorDataResponse(SensorData):
    """
    Modelo para respuestas que incluyen datos de sensores.
    Incluye campos adicionales como el ID generado por DynamoDB.
    """
    id: str = Field(..., description="Identificador único generado por DynamoDB.")
    partition_key: str = Field(..., description="Clave de partición generada.")
    sort_key: str = Field(..., description="Clave de ordenación generada.")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "abc123",
                "sensor_id": "sensor-001",
                "timestamp": "2024-05-20T10:00:00Z",
                "temperature": 23.5,
                "humidity": 45.0,
                "vibration": 0.2,
                "partition_key": "sensor-001#2024-05-20",
                "sort_key": "2024-05-20T10:00:00"
            }
        }

// === ARCHIVO: app/repositories/dynamodb_repository.py ===
from typing import List, Optional, Dict, Any
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
from app.models.sensor_data import SensorData, SensorDataCreate, SensorDataResponse
from app.config.settings import Settings
import logging

logger = logging.getLogger(__name__)


class DynamoDBRepository:
    """
    Capa de acceso a datos para DynamoDB.
    Implementa operaciones CRUD y consultas específicas para datos de sensores.
    """
    
    def __init__(self, settings: Settings):
        """
        Inicializa el cliente de DynamoDB con la configuración proporcionada.
        
        Args:
            settings: Configuración de la aplicación que contiene los parámetros de DynamoDB.
        """
        self.dynamodb = boto3.resource(
            'dynamodb',
            region_name=settings.dynamodb_region,
            endpoint_url=settings.dynamodb_endpoint
        )
        self.table_name = settings.dynamodb_table
        self.table = self.dynamodb.Table(self.table_name)

    def save_sensor_data(self, sensor_data: SensorDataCreate) -> SensorDataResponse:
        """
        Guarda un registro de sensor en DynamoDB.
        
        Args:
            sensor_data: Datos del sensor a guardar.
            
        Returns:
            SensorDataResponse: Datos del sensor guardado, incluyendo el ID generado.
            
        Raises:
            ClientError: Si ocurre un error al guardar en DynamoDB.
        """
        try:
            partition_key = sensor_data.partition_key()
            sort_key = sensor_data.sort_key()
            
            item = {
                'id': str(uuid.uuid4()),
                'partition_key': partition_key,
                'sort_key': sort_key,
                'sensor_id': sensor_data.sensor_id,
                'timestamp': sensor_data.timestamp.isoformat(),
                'temperature': sensor_data.temperature,
                'humidity': sensor_data.humidity,
                'vibration': sensor_data.vibration
            }
            
            self.table.put_item(Item=item)
            
            return SensorDataResponse(**item)
        except ClientError as e:
            logger.error(f"Error al guardar datos del sensor {sensor_data.sensor_id}: {e}")
            raise

    def get_sensor_data_by_id(self, id: str) -> Optional[SensorDataResponse]:
        """
        Obtiene un registro de sensor por su ID único.
        
        Args:
            id: Identificador único del registro.
            
        Returns:
            Optional[SensorDataResponse]: Datos del sensor si existe, None en caso contrario.
            
        Raises:
            ClientError: Si ocurre un error al consultar DynamoDB.
        """
        try:
            response = self.table.get_item(Key={'id': id})
            if 'Item' not in response:
                return None
            
            item = response['Item']
            return SensorDataResponse(
                id=item['id'],
                sensor_id=item['sensor_id'],
                timestamp=item['timestamp'],
                temperature=item.get('temperature'),
                humidity=item.get('humidity'),
                vibration=item.get('vibration'),
                partition_key=item['partition_key'],
                sort_key=item['sort_key']
            )
        except ClientError as e:
            logger.error(f"Error al obtener datos del sensor con ID {id}: {e}")
            raise

    def query_sensor_data_by_partition(
        self,
        sensor_id: str,
        date: str,
        limit: int = 100,
        exclusive_start_key: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Consulta datos de un sensor específico en una fecha dada.
        
        Args:
            sensor_id: Identificador del sensor.
            date: Fecha en formato YYYY-MM-DD.
            limit: Número máximo de registros a retornar.
            exclusive_start_key: Clave de paginación para resultados grandes.
            
        Returns:
            Dict[str, Any]: Respuesta de DynamoDB con los items y metadata de paginación.
            
        Raises:
            ClientError: Si ocurre un error al consultar DynamoDB.
        """
        try:
            partition_key = f"{sensor_id}#{date}"
            
            query_params = {
                'KeyConditionExpression': Key('partition_key').eq(partition_key),
                'Limit': limit,
                'ScanIndexForward': False  # Orden descendente por sort_key (timestamp)
            }
            
            if exclusive_start_key:
                query_params['ExclusiveStartKey'] = exclusive_start_key
            
            response = self.table.query(**query_params)
            return {
                'items': [
                    SensorDataResponse(
                        id=item['id'],
                        sensor_id=item['sensor_id'],
                        timestamp=item['timestamp'],
                        temperature=item.get('temperature'),
                        humidity=item.get('humidity'),
                        vibration=item.get('vibration'),
                        partition_key=item['partition_key'],
                        sort_key=item['sort_key']
                    ) for item in response.get('Items', [])
                ],
                'last_evaluated_key': response.get('LastEvaluatedKey')
            }
        except ClientError as e:
            logger.error(f"Error al consultar datos del sensor {sensor_id} en fecha {date}: {e}")
            raise

    def query_sensor_data_by_time_range(
        self,
        sensor_id: str,
        start_date: str,
        end_date: str,
        limit: int = 100,
        exclusive_start_key: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Consulta datos de un sensor en un rango de fechas.
        
        Args:
            sensor_id: Identificador del sensor.
            start_date: Fecha inicial en formato YYYY-MM-DD.
            end_date: Fecha final en formato YYYY-MM-DD.
            limit: Número máximo de registros a retornar.
            exclusive_start_key: Clave de paginación para resultados grandes.
            
        Returns:
            Dict[str, Any]: Respuesta de DynamoDB con los items y metadata de paginación.
            
        Raises:
            ClientError: Si ocurre un error al consultar DynamoDB.
        """
        try:
            query_params = {
                'KeyConditionExpression': (
                    Key('partition_key').begins_with(f"{sensor_id}#") &
                    Key('sort_key').between(start_date, end_date)
                ),
                'Limit': limit,
                'ScanIndexForward': False
            }
            
            if exclusive_start_key:
                query_params['ExclusiveStartKey'] = exclusive_start_key
            
            response = self.table.query(**query_params)
            return {
                'items': [
                    SensorDataResponse(
                        id=item['id'],
                        sensor_id=item['sensor_id'],
                        timestamp=item['timestamp'],
                        temperature=item.get('temperature'),
                        humidity=item.get('humidity'),
                        vibration=item.get('vibration'),
                        partition_key=item['partition_key'],
                        sort_key=item['sort_key']
                    ) for item in response.get('Items', [])
                ],
                'last_evaluated_key': response.get('LastEvaluatedKey')
            }
        except ClientError as e:
            logger.error(
                f"Error al consultar datos del sensor {sensor_id} entre {start_date} y {end_date}: {e}"
            )
            raise

    def delete_sensor_data(self, id: str) -> bool:
        """
        Elimina un registro de sensor por su ID único.
        
        Args:
            id: Identificador único del registro.
            
        Returns:
            bool: True si el registro fue eliminado, False si no existía.
            
        Raises:
            ClientError: Si ocurre un error al eliminar en DynamoDB.
        """
        try:
            response = self.table.delete_item(
                Key={'id': id},
                ReturnValues='ALL_OLD'
            )
            return 'Attributes' in response
        except ClientError as e:
            logger.error(f"Error al eliminar datos del sensor con ID {id}: {e}")
            raise


import uuid

// === ARCHIVO: tests/test_dynamodb_repository.py ===
import pytest
from moto import mock_dynamodb
from app.repositories.dynamodb_repository import DynamoDBRepository
from app.models.sensor_data import SensorDataCreate
from app.config.settings import Settings
from datetime import datetime
import os


@pytest.fixture
def dynamodb_table():
    """
    Fixture para crear una tabla de DynamoDB mockada.
    """
    with mock_dynamodb():
        settings = Settings()
        settings.dynamodb_table = "sensor_data_test"
        settings.dynamodb_region = "us-east-1"
        settings.dynamodb_endpoint = None
        
        dynamodb = boto3.resource('dynamodb', region_name=settings.dynamodb_region)
        
        table = dynamodb.create_table(
            TableName=settings.dynamodb_table,
            KeySchema=[
                {'AttributeName': 'id', 'KeyType': 'HASH'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'id', 'AttributeType': 'S'},
                {'AttributeName': 'partition_key', 'AttributeType': 'S'},
                {'AttributeName': 'sort_key', 'AttributeType': 'S'}
            ],
            GlobalSecondaryIndexes=[
                {
                    'IndexName': 'partition_key-sort_key-index',
                    'KeySchema': [
                        {'AttributeName': 'partition_key', 'KeyType': 'HASH'},
                        {'AttributeName': 'sort_key', 'KeyType': 'RANGE'}
                    ],
                    'Projection': {'ProjectionType': 'ALL'},
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 5,
                        'WriteCapacityUnits': 5
                    }
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        
        table.meta.client.get_waiter('table_exists').wait(TableName=settings.dynamodb_table)
        yield settings


def test_save_sensor_data(dynamodb_table):
    """
    Prueba que verifica la correcta inserción de datos en DynamoDB.
    
    Superficie de práctica:
    - Implementar el método save_sensor_data para guardar un registro.
    - Validar que el registro guardado contiene los campos esperados.
    """
    repository = DynamoDBRepository(dynamodb_table)
    
    sensor_data = SensorDataCreate(
        sensor_id="sensor-001",
        timestamp=datetime(2024, 5, 20, 10, 0, 0),
        temperature=23.5,
        humidity=45.0,
        vibration=0.2
    )
    
    # TODO: Implementar la lógica para guardar y verificar el registro
    pytest.skip("Implementar el test para guardar datos de sensor")


def test_get_sensor_data_by_id(dynamodb_table):
    """
    Prueba que verifica la obtención de un registro por su ID.
    
    Superficie de práctica:
    - Guardar un registro de prueba.
    - Implementar el método get_sensor_data_by_id para recuperarlo.
    - Validar que los datos recuperados coinciden con los guardados.
    """
    repository = DynamoDBRepository(dynamodb_table)
    
    # TODO: Guardar un registro de prueba y luego implementar la lógica de recuperación
    pytest.skip("Implementar el test para obtener datos por ID")


def test_query_sensor_data_by_partition(dynamodb_table):
    """
    Prueba que verifica la consulta de datos por clave de partición.
    
    Superficie de práctica:
    - Guardar múltiples registros para el mismo sensor y fecha.
    - Implementar el método query_sensor_data_by_partition.
    - Validar que se retornan los registros esperados en orden descendente.
    """
    repository = DynamoDBRepository(dynamodb_table)
    
    # TODO: Guardar registros de prueba y luego implementar la lógica de consulta
    pytest.skip("Implementar el test para consultar por clave de partición")


def test_query_sensor_data_by_time_range(dynamodb_table):
    """
    Prueba que verifica la consulta de datos por rango de tiempo.
    
    Superficie de práctica:
    - Guardar registros en diferentes fechas para el mismo sensor.
    - Implementar el método query_sensor_data_by_time_range.
    - Validar que se retornan solo los registros dentro del rango especificado.
    """
    repository = DynamoDBRepository(dynamodb_table)
    
    # TODO: Guardar registros de prueba y luego implementar la lógica de consulta
    pytest.skip("Implementar el test para consultar por rango de tiempo")


def test_delete_sensor_data(dynamodb_table):
    """
    Prueba que verifica la eliminación de un registro.
    
    Superficie de práctica:
    - Guardar un registro de prueba.
    - Implementar el método delete_sensor_data.
    - Validar que el registro ya no existe.
    """
    repository = DynamoDBRepository(dynamodb_table)
    
    # TODO: Guardar un registro de prueba, eliminarlo y verificar su ausencia
    pytest.skip("Implementar el test para eliminar datos")

// === ARCHIVO: app/services/sensor_service.py ===
package app.services

from typing import List, Optional
from datetime import datetime

from app.models.sensor_data import SensorDataCreate, SensorDataResponse
from app.repositories.dynamodb_repository import DynamoDBRepository


class SensorService:
    """
    Coordina la lógica de negocio para procesar consultas de datos de sensores.
    Transforma datos entre la capa de API y el repositorio.
    """

    def __init__(self, repository: DynamoDBRepository):
        self._repository = repository

    def get_sensor_by_id(self, sensor_id: str) -> Optional[SensorDataResponse]:
        """
        Recupera un registro de sensor por su identificador único.
        Retorna None si no existe el sensor.
        """
        if not sensor_id or not sensor_id.strip():
            raise ValueError("El identificador del sensor no puede estar vacío")

        result = self._repository.get_sensor_data_by_id(sensor_id.strip())
        return result

    def get_sensors_by_partition(self, partition_key: str) -> List[SensorDataResponse]:
        """
        Recupera todos los registros de sensores para una clave de partición dada.
        Útil para consultar datos de un sensor específico.
        """
        if not partition_key or not partition_key.strip():
            raise ValueError("La clave de partición no puede estar vacía")

        results = self._repository.query_sensor_data_by_partition(partition_key.strip())
        return results

    def get_sensors_by_time_range(
        self,
        start_time: datetime,
        end_time: datetime,
        sensor_id: Optional[str] = None
    ) -> List[SensorDataResponse]:
        """
        Recupera registros de sensores dentro de un rango de tiempo.
        Opcionalmente filtra por identificador de sensor.
        """
        if start_time is None or end_time is None:
            raise ValueError("Las fechas de inicio y fin son obligatorias")

        if start_time > end_time:
            raise ValueError("La fecha de inicio no puede ser posterior a la fecha de fin")

        results = self._repository.query_sensor_data_by_time_range(
            start_time=start_time,
            end_time=end_time,
            sensor_id=sensor_id
        )
        return results

    def save_sensor_data(self, sensor_data: SensorDataCreate) -> SensorDataResponse:
        """
        Persiste un nuevo registro de datos de sensor en la base de datos.
        Valida que los datos sean correctos antes de guardar.
        """
        if not sensor_data.sensor_id or not sensor_data.sensor_id.strip():
            raise ValueError("El identificador del sensor es obligatorio")

        if sensor_data.timestamp is None:
            raise ValueError("El timestamp es obligatorio")

        return self._repository.save_sensor_data(sensor_data)

    def delete_sensor_data(self, sensor_id: str) -> bool:
        """
        Elimina un registro de sensor por su identificador.
        Retorna True si la eliminación fue exitosa.
        """
        if not sensor_id or not sensor_id.strip():
            raise ValueError("El identificador del sensor no puede estar vacío")

        return self._repository.delete_sensor_data(sensor_id.strip())

    def get_all_sensors(self) -> List[SensorDataResponse]:
        """
        Recupera todos los registros de sensores disponibles.
        Utiliza la clave de partición por defecto para escanear datos.
        """
        return self._repository.query_sensor_data_by_partition("default")

    def transform_to_dict(self, sensor_data: SensorDataResponse) -> dict:
        """
        Transforma un objeto SensorDataResponse a diccionario para serialización.
        """
        return {
            "id": sensor_data.id,
            "sensor_id": sensor_data.sensor_id,
            "timestamp": sensor_data.timestamp.isoformat() if sensor_data.timestamp else None,
            "temperature": sensor_data.temperature,
            "humidity": sensor_data.humidity,
            "vibration": sensor_data.vibration,
        }

    def transform_to_list(self, sensors: List[SensorDataResponse]) -> List[dict]:
        """
        Transforma una lista de SensorDataResponse a lista de diccionarios.
        """
        return [self.transform_to_dict(sensor) for sensor in sensors]

// === ARCHIVO: app/api/v1/endpoints.py ===
package app.api.v1

from typing import List, Optional
from datetime import datetime

from fastapi import APIRouter, HTTPException, Query, status
from pydantic import BaseModel, Field

from app.services.sensor_service import SensorService
from app.models.sensor_data import SensorDataCreate
from app.repositories.dynamodb_repository import DynamoDBRepository
from app.config.settings import Settings


router = APIRouter(prefix="/v1/sensors", tags=["sensors"])


class SensorResponse(BaseModel):
    id: str
    sensor_id: str
    timestamp: Optional[datetime] = None
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    vibration: Optional[float] = None


class SensorCreateRequest(BaseModel):
    sensor_id: str = Field(..., description="Identificador único del sensor")
    timestamp: datetime = Field(..., description="Fecha y hora de la medición")
    temperature: float = Field(..., description="Temperatura en grados Celsius")
    humidity: float = Field(..., description="Humedad relativa en porcentaje")
    vibration: float = Field(..., description="Vibración en Hz")


class SensorListResponse(BaseModel):
    count: int
    data: List[SensorResponse]


def get_sensor_service() -> SensorService:
    settings = Settings()
    repository = DynamoDBRepository(settings)
    return SensorService(repository)


@router.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    """
    Endpoint de verificación de estado del servicio.
    """
    return {"status": "healthy", "service": "sensor-analytics-api"}


@router.get("/{sensor_id}", response_model=SensorResponse)
def get_sensor_by_id(sensor_id: str):
    """
    Recupera un sensor por su identificador único.
    """
    service = get_sensor_service()
    result = service.get_sensor_by_id(sensor_id)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Sensor con ID '{sensor_id}' no encontrado"
        )

    return SensorResponse(
        id=result.id,
        sensor_id=result.sensor_id,
        timestamp=result.timestamp,
        temperature=result.temperature,
        humidity=result.humidity,
        vibration=result.vibration
    )


@router.get("/", response_model=SensorListResponse)
def query_sensors(
    partition: Optional[str] = Query(None, description="Clave de partición del sensor"),
    start_time: Optional[datetime] = Query(None, description="Fecha de inicio del rango"),
    end_time: Optional[datetime] = Query(None, description="Fecha de fin del rango"),
    sensor_id: Optional[str] = Query(None, description="Filtrar por ID de sensor"),
):
    """
    Consulta sensores por clave de partición o por rango de tiempo.
    Permite filtrado opcional por identificador de sensor.
    """
    service = get_sensor_service()

    if partition:
        results = service.get_sensors_by_partition(partition)
    elif start_time and end_time:
        results = service.get_sensors_by_time_range(
            start_time=start_time,
            end_time=end_time,
            sensor_id=sensor_id
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Debe proporcionar 'partition' o 'start_time' y 'end_time'"
        )

    data = [
        SensorResponse(
            id=r.id,
            sensor_id=r.sensor_id,
            timestamp=r.timestamp,
            temperature=r.temperature,
            humidity=r.humidity,
            vibration=r.vibration
        )
        for r in results
    ]

    return SensorListResponse(count=len(data), data=data)


@router.post("/", response_model=SensorResponse, status_code=status.HTTP_201_CREATED)
def create_sensor(data: SensorCreateRequest):
    """
    Crea un nuevo registro de datos de sensor.
    """
    service = get_sensor_service()

    sensor_data = SensorDataCreate(
        sensor_id=data.sensor_id,
        timestamp=data.timestamp,
        temperature=data.temperature,
        humidity=data.humidity,
        vibration=data.vibration
    )

    try:
        result = service.save_sensor_data(sensor_data)
        return SensorResponse(
            id=result.id,
            sensor_id=result.sensor_id,
            timestamp=result.timestamp,
            temperature=result.temperature,
            humidity=result.humidity,
            vibration=result.vibration
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.delete("/{sensor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sensor(sensor_id: str):
    """
    Elimina un sensor por su identificador.
    """
    service = get_sensor_service()

    try:
        deleted = service.delete_sensor_data(sensor_id)
        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Sensor con ID '{sensor_id}' no encontrado"
            )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

// === ARCHIVO: tests/test_sensor_service.py ===
package tests

import pytest
from unittest.mock import Mock, MagicMock
from datetime import datetime, timedelta

from app.services.sensor_service import SensorService
from app.models.sensor_data import SensorDataCreate, SensorDataResponse


@pytest.fixture
def mock_repository():
    return Mock()


@pytest.fixture
def sensor_service(mock_repository):
    return SensorService(repository=mock_repository)


class TestGetSensorById:
    def test_get_sensor_by_id_existente(self, sensor_service, mock_repository):
        sensor_id = "sensor_001"
        expected_data = SensorDataResponse(
            id="record_001",
            sensor_id=sensor_id,
            timestamp=datetime.now(),
            temperature=25.5,
            humidity=60.0,
            vibration=1.2
        )
        mock_repository.get_sensor_data_by_id.return_value = expected_data

        result = sensor_service.get_sensor_by_id(sensor_id)

        assert result is not None
        assert result.sensor_id == sensor_id
        mock_repository.get_sensor_data_by_id.assert_called_once_with(sensor_id)

    def test_get_sensor_by_id_no_existente(self, sensor_service, mock_repository):
        mock_repository.get_sensor_data_by_id.return_value = None

        result = sensor_service.get_sensor_by_id("sensor_inexistente")

        assert result is None

    def test_get_sensor_by_id_empty_id(self, sensor_service):
        with pytest.raises(ValueError, match="no puede estar vacío"):
            sensor_service.get_sensor_by_id("")


class TestGetSensorsByTimeRange:
    def test_query_time_range_basic(self, sensor_service, mock_repository):
        start = datetime(2024, 1, 1, 0, 0, 0)
        end = datetime(2024, 1, 31, 23, 59, 59)
        mock_repository.query_sensor_data_by_time_range.return_value = []

        result = sensor_service.get_sensors_by_time_range(start, end)

        assert isinstance(result, list)
        mock_repository.query_sensor_data_by_time_range.assert_called_once()

    def test_query_time_range_invalid_dates(self, sensor_service):
        start = datetime(2024, 12, 31)
        end = datetime(2024, 1, 1)

        with pytest.raises(ValueError, match="no puede ser posterior"):
            sensor_service.get_sensors_by_time_range(start, end)

    def test_query_time_range_with_sensor_filter(self, sensor_service, mock_repository):
        start = datetime(2024, 1, 1)
        end = datetime(2024, 1, 31)
        sensor_id = "sensor_001"
        mock_repository.query_sensor_data_by_time_range.return_value = []

        sensor_service.get_sensors_by_time_range(start, end, sensor_id=sensor_id)

        mock_repository.query_sensor_data_by_time_range.assert_called_once_with(
            start_time=start,
            end_time=end,
            sensor_id=sensor_id
        )


class TestSaveSensorData:
    def test_save_valid_sensor_data(self, sensor_service, mock_repository):
        sensor_data = SensorDataCreate(
            sensor_id="sensor_001",
            timestamp=datetime.now(),
            temperature=22.5,
            humidity=55.0,
            vibration=0.8
        )
        mock_repository.save_sensor_data.return_value = SensorDataResponse(
            id="new_record",
            sensor_id=sensor_data.sensor_id,
            timestamp=sensor_data.timestamp,
            temperature=sensor_data.temperature,
            humidity=sensor_data.humidity,
            vibration=sensor_data.vibration
        )

        result = sensor_service.save_sensor_data(sensor_data)

        assert result is not None
        assert result.sensor_id == sensor_data.sensor_id
        mock_repository.save_sensor_data.assert_called_once_with(sensor_data)

    def test_save_sensor_data_missing_timestamp(self, sensor_service):
        sensor_data = SensorDataCreate(
            sensor_id="sensor_001",
            timestamp=None,
            temperature=22.5,
            humidity=55.0,
            vibration=0.8
        )

        with pytest.raises(ValueError, match="timestamp es obligatorio"):
            sensor_service.save_sensor_data(sensor_data)


class TestTransformData:
    def test_transform_to_dict(self, sensor_service):
        sensor = SensorDataResponse(
            id="rec_001",
            sensor_id="sensor_001",
            timestamp=datetime(2024, 1, 15, 10, 30, 0),
            temperature=25.0,
            humidity=65.5,
            vibration=1.5
        )

        result = sensor_service.transform_to_dict(sensor)

        assert result["id"] == "rec_001"
        assert result["sensor_id"] == "sensor_001"
        assert "temperature" in result
        assert "humidity" in result
        assert "vibration" in result

    def test_transform_to_list(self, sensor_service):
        sensors = [
            SensorDataResponse(
                id="rec_001",
                sensor_id="sensor_001",
                timestamp=datetime.now(),
                temperature=25.0,
                humidity=60.0,
                vibration=1.0
            ),
            SensorDataResponse(
                id="rec_002",
                sensor_id="sensor_002",
                timestamp=datetime.now(),
                temperature=26.0,
                humidity=61.0,
                vibration=1.2
            )
        ]

        result = sensor_service.transform_to_list(sensors)

        assert len(result) == 2
        assert all(isinstance(item, dict) for item in result)

// === ARCHIVO: docs/clave_particion_justificacion.md ===
# Justificación de Clave de Partición para DynamoDB

## Análisis del Patrón de Acceso

El sistema de monitoreo de infraestructura genera datos de sensores con un patrón de acceso específico que debe guiar el diseño de la clave de partición. Los datos provienen de múltiples sensores que registran mediciones de temperatura, humedad y vibración de forma continua. Cada registro incluye un identificador único del sensor, un timestamp preciso y los valores de las tres mediciones. La naturaleza de las consultas frecuentes determina directamente qué estrategia de partición maximiza el rendimiento.

Las consultas principales que el sistema debe soportar son dos: primera, la recuperación de todos los datos de un sensor específico dentro de un rango temporal, que representa el caso de uso más común cuando un analista necesita evaluar el comportamiento de un sensor particular durante un período de tiempo definido; segunda, la consulta de datos de múltiples sensores en un momento específico, que permite comparar las mediciones de diferentes sensores en un instante dado para detectar anomalías o correlaciones.

## Evaluación de Estrategias de Partición

### Opción 1: Solo sensor_id como clave de partición

Utilizar exclusivamente el identificador del sensor como clave de partición organizaría todos los registros de un mismo sensor en una única partición física de DynamoDB. Esta estrategia garantiza que las consultas por sensor sean extremadamente eficientes, ya que todos los datos relevantes residen en la misma partición y DynamoDB puede realizar operaciones de lectura secuencial. Sin embargo, esta aproximación presenta un problema crítico cuando un sensor genera datos con alta frecuencia: la partición correspondiente recibiría un volumen masivo de escrituras, creando un hotspot que degradaría el rendimiento y podría superar los límites de capacidad de esa partición específica. Además, las consultas que requieren datos de múltiples sensores en un rango de tiempo específico necesitarían realizar operaciones de escaneo paralelo o múltiples consultas a diferentes particiones, aumentando la latencia y el costo.

### Opción 2: Solo timestamp como clave de partición

Invertir la estrategia y utilizar únicamente el timestamp como clave de partición agruparía todos los registros generados en el mismo instante temporal en una partición. Esta aproximación favorece las consultas de instantáneas multiples sensores, permitiendo recuperar todos los registros de un momento dado con una sola operación de lectura. El problema fundamental es que los datos de un sensor específico quedarían dispersos a través de múltiples particiones, obligando a realizar consultas que abarcan muchas particiones diferentes para reconstruir el historial de un sensor. Esta dispersión elimina prácticamente cualquier beneficio de rendimiento para el caso de uso más frecuente del sistema.

### Opción 3: Clave de partición compuesta sensor_id más timestamp truncado

La tercera opción, y la seleccionada para este sistema, combina ambas dimensiones en una clave de partición compuesta. El identificador del sensor se utiliza como primer componente de la clave de partición, mientras que el timestamp se trunca a una granularidad específica (por ejemplo, a nivel de hora o día) y se utiliza como segundo componente. Esta estrategia híbrida ofrece un equilibrio óptimo entre los dos patrones de consulta principales: todos los datos de un sensor en un período truncado específico residen en la misma partición, permitiendo consultas eficientes por sensor y rango temporal; la dispersión de datos a través de múltiples particiones previene la formación de热点; y las consultas de instantáneas múltiples sensores pueden realizarse leyendo las particiones correspondientes a ese momento temporal.

## Distribución de Datos y Consideraciones de Escalabilidad

La clave de partición composta seleccionada debe evaluarse contra la distribución esperada de datos. El sistema de monitoreo contempla un número finito de sensores, típicamente entre decenas y cientos según el tamaño de la infraestructura. Cada sensor genera mediciones a intervalos regulares, probablemente cada pocos minutos o segundos dependiendo del tipo de medición. Con esta distribución, la clave de partición por sensor más timestamp horario garantiza que cada partición contenga un volumen manejable de datos mientras evita la concentración excesiva en una sola partición.

El truncamiento del timestamp a nivel de hora significa que cada partición contendrá las lecturas de un sensor específico durante una hora completa. Para un sensor que genera datos cada minuto, esto representa aproximadamente 60 registros por partición, un volumen perfectamente manejable para DynamoDB. Si la frecuencia de muestreo aumenta a cada segundo, la partición contendría 3600 registros, todavía dentro de rangos operativos normales. La granularidad del truncamiento puede ajustarse según la frecuencia real de muestreo: mayor granularidad (menos preciso) para muestreos muy frecuentes, menor granularidad (más preciso) para muestreos esporádicos.

## Índices Secundarios para Consultas Alternativas

Aunque la clave de partición compuesta optimiza los patrones de consulta principales, el sistema puede necesitar consultas adicionales que no se benefician de esta estructura. Un índice secundario global inverso, que invierta el orden de los componentes de la clave, permitiría consultas eficientes por rango temporal de todos los sensores sin especificar un identificador particular. Este índice representa una opción futura si los patrones de consulta evolucionan para incluir este caso de uso.

// === ARCHIVO: docs/resultados_consultas.md ===
# Resultados de Consultas y Evaluación de Rendimiento

## Metodología de Evaluación

La evaluación del rendimiento de las consultas se realizó sobre un conjunto de datos de prueba que simula el comportamiento real del sistema de monitoreo de infraestructura. El dataset contiene registros de 50 sensores diferentes, cada uno generando mediciones durante un período de 30 días con una frecuencia de muestreo de 5 minutos por sensor. Este volumen total de aproximadamente 432,000 registros proporciona una muestra estadísticamente significativa para evaluar el comportamiento de las consultas bajo condiciones de producción.

Las métricas evaluadas incluyen la latencia media de respuesta, el consumo de unidades de capacidad tanto de lectura como de escritura, el número de particiones accedidas por consulta y la consistencia de los resultados devueltos. Todas las pruebas se ejecutaron utilizando el modo de provisión de capacidad con 10 unidades de capacidad de lectura y escritura, reflectando una configuración de producción típica para sistemas de monitoreo donde el costo debe balancearse con el rendimiento.

## Resultados de Consultas por Sensor y Rango Temporal

La consulta más frecuente del sistema recupera todos los registros de un sensor específico dentro de un rango de fechas. Esta consulta utiliza la clave de partición compuesta para localizar directamente la partición correspondiente al sensor y el período horario, luego aplica una condición de rango sobre la clave de ordenación para restringir los resultados al intervalo temporal solicitado. Los resultados demuestran que esta consulta presenta una latencia promedio de 12 milisegundos con un consumo de 1.5 unidades de capacidad de lectura para intervalos de una hora, escalando linealmente a aproximadamente 8 milisegundos adicionales por cada hora adicional de rango temporal.

El patrón de acceso observado confirma que la clave de partición compuesta seleccionada optimiza correctamente este caso de uso principal. La consulta accede a exactamente las particiones necesarias para cubrir el rango temporal solicitado, sin realizar operaciones de escaneo ni acceder a particiones innecesarias. El consumo de capacidad de lectura se mantiene proporcional al volumen de datos devueltos, sin overhead significativo por la estructura de la clave.

## Resultados de Consultas de Instante Específico

El segundo patrón de consulta evalúa el rendimiento al recuperar todos los registros generados en un momento temporal específico a través de múltiples sensores. Esta consulta requiere un enfoque diferente: en lugar de utilizar la clave de partición primaria, se ejecuta una consulta que filtra por el componente de timestamp de la clave de ordenación. Los resultados muestran una latencia promedio de 45 milisegundos para consultas de instantáneas hourly, con un consumo de 2.8 unidades de capacidad de lectura.

Esta latencia superior se explica porque la consulta debe acceder a múltiples particiones, una por cada sensor que generó datos en el instante solicitado. Con 50 sensores activos, la operación requiere coordinación entre múltiples particiones físicas, lo cual introduce latencia adicional. Sin embargo, el rendimiento se mantiene dentro de límites aceptables para consultas analíticas que no requieren respuesta en tiempo real.

## Análisis de Rendimiento bajo Carga

Las pruebas de carga evaluaron el comportamiento del sistema bajo condiciones de escritura intensiva, simulando el flujo continuo de datos de sensores hacia la base de datos. El sistema procesó exitosamente hasta 500 escrituras por segundo antes de observar degradación del rendimiento, con una latencia de escritura promedio de 8 milisegundos. Este throughput supera significativamente los requisitos típicos de sistemas de monitoreo de infraestructura, donde la frecuencia de muestreo raramente supera una medición por segundo por sensor.

El análisis de la distribución de escrituras confirma que la clave de partición compuesta previene efectivamente la formación de hotspots. Las escrituras se dispersan a través de múltiples particiones según el sensor y el período horario, evitando que una única partición reciba un volumen desproporcionado de operaciones. Esta distribución es fundamental para mantener la estabilidad del sistema bajo cargas pico o durante eventos de mantenimiento que requieren catch-up de datos.

## Sugerencias de Mejora

### Optimización de Granularidad de Partición

Si la frecuencia de muestreo aumenta significativamente, considerando reducir la granularidad del truncamiento de timestamp de hourly a daily. Esto reduciría el número de particiones que las consultas por sensor deben acceder para rangos temporales extensos, disminuyendo la latencia para consultas históricas. El tradeoff es un incremento en el tamaño promedio de cada partición, que debe evaluarse contra el volumen de datos típico por sensor.

### Implementación de Cacheo para Consultas Frecuentes

Las consultas que recuperan datos de sensores para visualización en dashboards presentan patrones repetitivos donde los mismos rangos temporales se consultan repetidamente. Implementar una capa de cacheo con TTL breve (1-5 minutos) sobre los endpoints de consulta más frecuentes reduciría el consumo de capacidad de lectura y la latencia percibida por los usuarios finales. DynamoDB Accelerator representa la opción más integrada para este caso de uso.

### Consideraciones para Proyección de Crecimiento

Si el sistema escala a miles de sensores o frecuencia de muestreo sub-segundo, la arquitectura de clave de partición actual requerirá reevaluación. La clave de partición compuesta sigue siendo válida, pero podría ser necesario implementar una estrategia de escritura en batch más agresiva y considerar la introducción de índices secundarios globales para distribuir la carga de lectura adicional. La monitorización continua de las métricas de partición hotspot en CloudWatch permitirá detectar cuándo estas optimizaciones se vuelven necesarias.
```
