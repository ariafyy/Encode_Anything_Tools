from typing import Callable
from fastapi import FastAPI
from lib.services.encode_anything_core import EncodeAnythingCore
from lib.config import EnvVars
import os
import logging
logger = logging.getLogger(__name__)

path = os.path.dirname(os.path.realpath(__file__))
dir = path.replace('/lib', '/resources')

def _startup_model(app: FastAPI) -> None:
    model_instance = EncodeAnythingCore()
    app.state.model = model_instance


def _shutdown_model(app: FastAPI) -> None:
    app.state.model = None

def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        logger.info("Running app start handler.")
        _startup_model(app)
    return startup

def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        logger.info("Running app shutdown handler.")
        _shutdown_model(app)
    return shutdown



# @app.on_event("startup")
# async def _startup_model(app: FastAPI) -> None:
#     model_instance = EncodeAnythingCore()
#     app.state.model = model_instance

#
# @app.delete("/cache", status_code=status.HTTP_204_NO_CONTENT)
# def delete_cache():
#     memory.clear()

