from pydantic_settings import BaseSettings, SettingsConfigDict

from .database import DataBaseConfig
from .server import ServerConfig


class AppConfig(BaseSettings):
    db: DataBaseConfig
    server: ServerConfig = ServerConfig()

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )


config = AppConfig()
