import uvicorn
from fastapi import APIRouter, FastAPI

from util.logger import Logger

app = FastAPI()
router = APIRouter(prefix="/agentic-app/api")

log = Logger("agentic-ai-app")


@router.get("/test")
def read_root():
    log.info("Checking agentic-ai-app Start")
    return {"message": "Hello, World!"}


app.include_router(router)


def main():
    log.info("Starting agentic-ai-app")
    uvicorn.run("agentic_ai_app:app", host="127.0.0.1", port=8443, reload=True, log_config="config/logging.ini")


if __name__ == "__main__":
    main()

