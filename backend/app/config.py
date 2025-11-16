from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./dushime.db"
    SMTP_HOST: str = "localhost"
    SMTP_PORT: int = 25
    SMTP_USER: str | None = None
    SMTP_PASS: str | None = None
    FROM_EMAIL: str = "no-reply@dushime-school.rw"
    ADMIN_EMAIL: str = "info@dushime-school.rw"

    class Config:
        env_file = ".env"

settings = Settings()
