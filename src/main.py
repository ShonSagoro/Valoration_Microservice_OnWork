from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging, sys, os
import uvicorn
import logging
from loguru import logger
from reviews_management.infraestructure.endpoints import router as valoration_router

logger.remove()
logger.add("file_{time}.log", rotation="1 week", retention="1 month", level="DEBUG")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(valoration_router, prefix="")


def main():
    logging.info(f'API is running')
    try:
        logging.info(f'API is running in http://localhost:3002s')
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    except Exception as e:
        logging.error(f'Error while running API: {str(e)}')
    except KeyboardInterrupt:
        logging.warn('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

if __name__ == "__main__":
  main()