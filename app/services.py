import os
import ffmpeg
from fastapi import HTTPException
from urllib.parse import urlparse

from core.config import settings


class RTSPtoHLSConverter:
    """
        A class to convert RTSP video streams to the HLS (HTTP Live Streaming) format.
        Attributes:
            hls_output_dir (str): Directory where HLS files will be stored.
            hls_segment_time (int): Duration of each segment of the HLS stream in seconds.
        Methods:
            convert_rtsp_to_hls(rtsp_url: str) -> str: Converts the given RTSP URL to HLS format.
    """

    def __init__(self, log, hls_output_dir=settings.hls_output_dir, hls_segment_time=settings.hls_segment_time):
        self.hls_output_dir = f"{hls_output_dir}/log_{log.id}"
        self.hls_segment_time = hls_segment_time

    async def convert_rtsp_to_hls(self, rtsp_url):
        """
                Asynchronously converts an RTSP stream to HLS format.
                Parameters:
                    rtsp_url (str): The RTSP URL to be converted.
                Returns:
                    str: The path to the HLS playlist file.
        """

        try:
            os.makedirs(self.hls_output_dir, exist_ok=True)
            parsed_url = urlparse(rtsp_url)
            path = parsed_url.path
            filename = os.path.basename(path)

            hls_playlist_path = os.path.join(self.hls_output_dir, f"{filename}.m3u8")
            ffmpeg.input(rtsp_url, rtsp_transport="tcp").output(
                hls_playlist_path, format="hls", hls_time=self.hls_segment_time
            ).run_async(pipe_stdout=True, pipe_stderr=True)
            return hls_playlist_path

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
