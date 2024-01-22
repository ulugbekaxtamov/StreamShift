from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import RTSPRequest, LogUpdatePartial
from .services import RTSPtoHLSConverter
from .crud import create_log, update_log, get_logs
from core import db_helper

router = APIRouter(tags=['Stream'])


@router.get("/logs", description="Get all logs in the database")
async def get_products(request: Request, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    base_url = str(request.base_url)
    return await get_logs(session=session, base_url=base_url)


@router.post("/convert_rtsp_to_hls",
             description="Converts an RTSP video stream to HLS format and returns the URL of the HLS playlist.")
async def convert_rtsp_to_hls(request_data: RTSPRequest, request: Request,
                              session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    try:
        log = await create_log(session=session, log_in=request_data)

        converter = RTSPtoHLSConverter(log=log)
        rtsp_url = request_data.rtsp_url

        hls_playlist_path = await converter.convert_rtsp_to_hls(rtsp_url)
        base_url = str(request.base_url)
        hls_url = f"{base_url}{hls_playlist_path}"

        log_update = LogUpdatePartial(hls_url=hls_playlist_path)
        await update_log(session=session, log=log, log_update=log_update)

        return {"id": log.id, "hls_url": hls_url}


    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
