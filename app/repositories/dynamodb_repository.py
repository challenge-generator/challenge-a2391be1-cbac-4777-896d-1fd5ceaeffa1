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