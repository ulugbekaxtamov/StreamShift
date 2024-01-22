from core.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class APILog(Base):
    rtsp_url: Mapped[str] = mapped_column(String(500), index=True)
    hls_url: Mapped[str] = mapped_column(String(500), index=True, nullable=True)

    def get_hls_url(self, base_url: str):
        return f"{base_url}{self.hls_url}"

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, url={self.rtsp_url!r}, timestamp={self.hls_url})"
