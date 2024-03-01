import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import dotenv_values

config = {
    **dotenv_values(".env.local"),
    **dotenv_values(".env"),
    **os.environ,  # override loaded values with environment variables
}


class Settings(BaseSettings):
    # db settings
    db_user: str | None = config.get("POSTGRES_USER")
    db_password: str | None = config.get("POSTGRES_PASSWORD")
    db_name: str | None = config.get("POSTGRES_DB")

    # openai settings
    open_ai_key: str | None = config.get("OPEN_AI_KEY")
    open_ai_model: str | None = config.get("OPEN_AI_MODEL")
    open_ai_max_tokens: int | None = config.get("OPEN_AI_MAX_TOKENS")

    model_config = SettingsConfigDict()


settings = Settings()
