from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from storage.database.helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()


def create_application() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan,
        default_response_class=ORJSONResponse,
    )

    return app
