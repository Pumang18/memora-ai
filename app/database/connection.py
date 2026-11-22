from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import settings

if settings.database_url.startswith("sqlite:///"):

    db_path = settings.database_url.replace(
        "sqlite:///",
        "",
        1
    )

    Path(db_path).parent.mkdir(
        parents=True,
        exist_ok=True
    )

class Base(DeclarativeBase):
    pass

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False}
    if settings.database_url.startswith("sqlite")
    else {}
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False
)

def initialize_database():

    Base.metadata.create_all(bind=engine)