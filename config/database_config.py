from envguardian import Env


class DatabaseConfig:
    DATABASE_NAME = Env.get("DATABASE_NAME")
    DATABASE_USER = Env.get("DATABASE_USER")
    DATABASE_PASSWORD = Env.get("DATABASE_PASSWORD")
    DATABASE_HOST = Env.get("DATABASE_HOST")
    DATABASE_PORT = Env.get("DATABASE_PORT")
