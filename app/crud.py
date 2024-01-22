from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from .models import APILog

from .schemas import RTSPRequest, LogUpdatePartial


async def get_logs(session: AsyncSession, base_url: str) -> list[APILog]:
    stmt = select(APILog).order_by(APILog.id)
    result: Result = await session.execute(stmt)
    logs = result.scalars().all()

    for log in logs:
        log.hls_url = log.get_hls_url(base_url)

    return list(logs)


async def create_log(session: AsyncSession, log_in: RTSPRequest) -> APILog:
    log = APILog(**log_in.model_dump())
    session.add(log)
    await session.commit()
    return log


async def update_log(session: AsyncSession, log: APILog, log_update: LogUpdatePartial,
                     partial: bool = False) -> APILog:
    for key, value in log_update.model_dump(exclude_unset=partial).items():
        setattr(log, key, value)
    await session.commit()
    return log
