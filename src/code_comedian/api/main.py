import uvicorn
from fastapi import APIRouter, FastAPI
from loguru import logger
import openai

from ..settings import settings

openai.api_key = settings.OPENAI_API_KEY

app = FastAPI(
    title="Joke Judge AI",
    version="1.0.0",
    docs_url=f"{settings.fastapi.prefix}/docs",
    openapi_url=f"{settings.fastapi.prefix}/openapi.json",
)

router = APIRouter(prefix=settings.fastapi.prefix)


@router.get("/joke")
def get_joke():
    """Returns a joke"""
    return {"message": "This is a joke!"}


@router.post("/joke")
def judge_joke():
    """Judges your joke"""
    


app.include_router(router)

if __name__ == "__main__":
    logger.info("Starting server...")
    uvicorn.run(
        "src.joke_judge_ai.api.main:app",
        host=settings.fastapi.host,
        port=settings.fastapi.port,
        reload=settings.fastapi.reload,
    )
