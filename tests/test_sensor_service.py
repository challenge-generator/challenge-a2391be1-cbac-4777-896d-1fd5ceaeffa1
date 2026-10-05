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