import uvicorn
from fastapi import APIRouter, FastAPI
from loguru import logger
import openai

from ..settings import settings
from ..jokes import JokeJudge, Joke, Judgement

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
async def judge_joke(
    request: Joke,
):
    """Judges your joke"""
    judge = JokeJudge()
    judgement = await judge.judge(request.content)

    return Judgement(**judgement.dict())


app.include_router(router)

if __name__ == "__main__":
    logger.info("Starting server...")
    uvicorn.run(
        "src.code_comedian.api.main:app",
        host=settings.fastapi.host,
        port=settings.fastapi.port,
        reload=settings.fastapi.reload,
    )
