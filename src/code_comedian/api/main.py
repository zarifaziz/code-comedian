"""
This module contains the main application for the Joke Judge AI API.
It sets up the FastAPI application, defines the routes, and runs the server.
"""

import openai
import uvicorn
from fastapi import APIRouter, FastAPI, HTTPException
from loguru import logger

from ..joke_judge import Joke, JokeJudge, Judgement, JokeNotDetectedError
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
async def judge_joke(
    request: Joke,
):
    """Judges your joke"""
    judge = JokeJudge()
    try:
        judgement = await judge.judge(request.content)
        logger.info(f"judgement: {judgement}")

    except JokeNotDetectedError as e:
        raise HTTPException(status_code=422, detail=str(e)) from e

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
