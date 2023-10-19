import uvicorn
from fastapi import FastAPI, Request

from ..settings import settings

app = FastAPI(
    title="Joke Judge AI",
    version="1.0.0",
    docs_url=f"{settings.fastapi.prefix}/docs",
    openapi_url=f"{settings.fastapi.prefix}/openapi.json",
)


@app.post("/joke")
def judge_joke():
    """Judges your joke"""
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run(
        "src.joke_judge_ai.api.main:app",
        host=settings.fastapi.host,
        port=settings.fastapi.port,
        log_config=None,
        reload=settings.fastapi.reload,
    )
