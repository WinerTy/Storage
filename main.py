import uvicorn

from config import config
from utils.app.create_app import create_application

if __name__ == "__main__":
    app = create_application()
    uvicorn.run(app, host=config.server.host, port=config.server.port)
