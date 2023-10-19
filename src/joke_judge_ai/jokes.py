import openai 
from loguru import logger
from enum import Enum
from pydantic import BaseModel, Field, validator
import json
from copy import deepcopy

from .settings import settings

class Joke(BaseModel):
    """Joke class"""
    content: str = Field(..., title="Content", description="The entire joke content including the punchline")

class FunnyRatingEnum(str, Enum):
    """Funny rating enum"""
    NOT_FUNNY = "not funny"
    KINDA_FUNNY = "kinda funny"
    FUNNY = "funny"
    VERY_FUNNY = "very funny"
    HILARIOUS = "hilarious"

class Judgement(BaseModel):
    """Judgement class"""
    joke: Joke = Field(..., title="Joke", description="The joke that was judged")
    funny_rating: FunnyRatingEnum = Field(..., title="Funny rating", description="How funny is the joke?")
    explanation: str = Field(..., title="Explanation", description="Explanation for the funny_rating")

class JokeJudge:
    """Joke judge class"""
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY
        self.model = "gpt-3.5-turbo-16k"
        self.num_tries = 5
        self.prompt = json.load(open("prompt.json", "r"))
    
    async def judge(
        self,
        content: str,
    ):
        """Judges a joke"""
        messages = deepcopy(self.prompt)
        reply = None

        for try_num in range(self.num_tries):
            try:
                logger.info(f"try {try_num+1}/{self.num_tries} to get a response")
                response = openai.Completion.create(
                    engine=self.model,
                    prompt=content,
                    temperature=0.1,
                    max_tokens=768,
                )
                reply = response["choices"][0]["message"]["content"]

                funny_rating = FunnyRatingEnum(response.choices[0].text)
                return Judgement(joke=Joke(content=content), funny_rating=funny_rating)

            except (ValueError, TypeError) as e:
                logger.error(f"Error: {e}")
                if not reply:
                    reply = "failed response"

                messages.append({"role": "assistant", "content": reply})
                messages.append(
                    {
                        "role": "user",
                        "content": f"""
                Previous response was not valid. Error: {e}.
                Please try again.""",
                    }
                )

        logger.error(f"Could not get a response after {self.num_tries} tries")
        raise ValueError(f"Could not get a response after {self.num_tries} tries")
