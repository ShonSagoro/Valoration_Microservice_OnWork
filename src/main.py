from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging, sys, os
import uvicorn
from reviews_management.infraestructure.endpoints.valoration_endpoints import router as valoration_router
from publication_management.infraestructure.endpoints.comment_endpoints import router as comment_router
from publication_management.infraestructure.endpoints.publication_endpoints import router as publication_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(valoration_router, prefix="")
app.include_router(comment_router, prefix="")
app.include_router(publication_router, prefix="")

def main():
    logging.info(f'API is running')
    try:
        logging.info(f'API is running in http://localhost:3002')
        uvicorn.run("main:app", host="0.0.0.0", port=3002, reload=True)
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