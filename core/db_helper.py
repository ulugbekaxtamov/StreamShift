from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session, AsyncSession
from asyncio import current_task

from core.config import settings


class DatabaseHelper:
    """
    Class for managing SQLAlchemy database in asynchronous mode.

    Attributes:
        engine (AsyncEngine): The SQLAlchemy asynchronous engine used to connect to the database.
        session_factory (async_sessionmaker): The SQLAlchemy session factory for creating asynchronous sessions.
    """

    def __init__(self, url: str, echo: bool = False):
        """
        Initializes an instance of the DatabaseHelper class.

        Args:
            url (str): The database connection string.
            echo (bool, optional): Enables or disables SQLAlchemy debug mode (outputting SQL queries). Default is False.
        """
        self.engine = create_async_engine(
            url=url,
            echo=echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False
        )

    def get_scoped_session(self):
        """
        Creates and returns an asynchronous SQLAlchemy session within the current task's scope (scoped session).

        Returns:
            AsyncSession: An asynchronous SQLAlchemy session.
        """
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        """
        Context manager for an asynchronous SQLAlchemy session.

        Returns:
            AsyncSession: An asynchronous SQLAlchemy session.
        """
        async with self.session_factory() as session:
            yield session
            await session.close()

    async def scoped_session_dependency(self) -> AsyncSession:
        """
        Context manager for an asynchronous scoped SQLAlchemy session.

        Returns:
            AsyncSession: An asynchronous scoped SQLAlchemy session.
        """
        session = self.get_scoped_session()
        yield session
        await session.close()


# Create an instance of DatabaseHelper with settings from the settings.db.url and settings.db.echo
db_helper = DatabaseHelper(
    url=settings.db.url,
    echo=settings.db.echo
)
