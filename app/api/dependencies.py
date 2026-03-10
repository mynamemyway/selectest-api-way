from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import async_session_maker


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency для получения сессии базы данных.

    Используется в FastAPI endpoints через Depends().
    Гарантированно закрывает сессию после завершения запроса.

    Yields:
        AsyncSession: Асинхронная сессия SQLAlchemy
    """
    async with async_session_maker() as session:
        yield session
