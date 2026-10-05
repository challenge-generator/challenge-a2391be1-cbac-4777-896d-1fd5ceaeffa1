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