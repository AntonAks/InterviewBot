import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import dotenv_values

config = {
    **dotenv_values("config/.env.local"),
    **dotenv_values("config/.env"),
    **os.environ,  # override loaded values with environment variables
}


class Settings(BaseSettings):
    # db settings
    db_user: str | None = config.get("POSTGRES_USER")
    db_password: str | None = config.get("POSTGRES_PASSWORD")
    db_name: str | None = config.get("POSTGRES_DB")

    if not os.environ.get('TESTING'):
        DATABASE_URL: str = f"postgresql://{db_user}:{db_password}@db:5432/{db_name}"
    else:
        DATABASE_URL: str = f"sqlite:///./tests/test_db.db"

    # api settings
    api_url: str = config.get("API_URL")

    # openai settings
    open_ai_key: str | None = config.get("OPEN_AI_KEY")
    open_ai_model: str | None = config.get("OPEN_AI_MODEL")
    open_ai_max_tokens: int | None = config.get("OPEN_AI_MAX_TOKENS")

    # config celery
    celery_broker_url: str | None = config.get("CELERY_BROKER_URL")
    celery_result_url: str | None = config.get("CELERY_RESULT_BACKEND")

    model_config = SettingsConfigDict()



settings = Settings()
