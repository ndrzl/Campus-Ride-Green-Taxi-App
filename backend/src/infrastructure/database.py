from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# --- LOCAL MAC CONFIGURATION ---
# Change '123' to your actual pgAdmin/Postgres password
# Change 'campus' to the exact name of the DB you created in pgAdmin
HOST = os.getenv("DB_HOST", "127.0.0.1")
PORT = os.getenv("DB_PORT", "5432")
USER = os.getenv("DB_USER", "nadhirahzulkifli")
PASSWORD = os.getenv("DB_PASSWORD", "123") 
DATABASE = os.getenv("DB_NAME", "campus")

# Using asyncpg for asynchronous database communication
# The f-string builds the connection URL automatically
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL", f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

# Create Async Engine
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True, # Set to True for now so you can see the SQL in your terminal!
    future=True
)

# Async Session Factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()