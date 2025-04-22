from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
)

from storage.config import config


class DataBaseHelper:
    def __init__(
        self,
        url: str,
        echo: bool = False,
        echo_pool: bool = False,
        max_overflow: int = 10,
        pool_size: int = 5,
    ):
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            max_overflow=max_overflow,
            pool_size=pool_size,
        )

        self.session_factory: async_sessionmaker[AsyncEngine] = (
            async_sessionmaker(  # noqa
                bind=self.engine,
                expire_on_commit=False,
                autoflush=False,
                autocommit=False,
            )
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


db_helper = DataBaseHelper(
    url=str(config.db.url),
    echo=config.db.echo,
    echo_pool=config.db.echo_pool,
    max_overflow=config.db.max_overflow,
    pool_size=config.db.pool_size,
)
