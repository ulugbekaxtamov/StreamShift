from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from datetime import datetime


class Base(DeclarativeBase):
    """
    Base class for all tables in the database.

    This class provides common fields for all tables, such as id, created_at, and updated_at.

    Attributes:
        id (Mapped[int]): Unique identifier of the record (primary key).
        created_at (Mapped[datetime]): Date and time of record creation. Automatically set when a record is created.
        updated_at (Mapped[datetime]): Date and time of the last record update. Automatically updated when a record is modified.
    """

    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column("id", primary_key=True)
    created_at: Mapped[datetime] = mapped_column("created_at", default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column("updated_at", default=datetime.utcnow, onupdate=datetime.utcnow)
