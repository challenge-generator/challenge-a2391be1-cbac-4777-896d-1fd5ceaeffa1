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