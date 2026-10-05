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