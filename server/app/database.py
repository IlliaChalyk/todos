from os import environ
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

connection_url = URL.create(
    'postgresql',
    environ.get('DB_USER'),
    environ.get('DB_PASSWORD'),
    environ.get('DB_HOST'),
    environ.get('DB_PORT'),
    environ.get('DB_NAME'),
)

engine = create_engine(connection_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Base(DeclarativeBase):
    pass
