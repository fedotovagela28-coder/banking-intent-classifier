from pydantic_settings import BaseSettings, SettingsConfigDict

class AppConfig(BaseSettings):
    app_name: str = "ml-priject-template"
    app_version: str = "0.1.0" 
    log_level: str = "INFO"
    model_path: str = "models/model.pkl"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

config = AppConfig()