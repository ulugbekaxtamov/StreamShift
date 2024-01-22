from pydantic import BaseModel, validator


class RTSPRequest(BaseModel):
    """
    Pydantic model for receiving a valid RTSP URL in requests.
    """
    rtsp_url: str

    @validator("rtsp_url")
    def validate_rtsp_url(cls, value):
        if not value.startswith("rtsp://"):
            raise ValueError("Invalid RTSP URL. It should start with 'rtsp://'.")
        return value


class LogUpdatePartial(BaseModel):
    hls_url: str
