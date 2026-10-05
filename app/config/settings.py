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