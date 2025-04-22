from typing import Annotated

import uvicorn
from fastapi import File, UploadFile

from storage.config import config
from storage.utils.app import create_application

app = create_application()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=config.server.host,
        port=config.server.port,
        reload=config.server.debug,
    )
