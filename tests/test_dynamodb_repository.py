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