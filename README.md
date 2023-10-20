# code-comedian
You think you have a funny developer joke? Let AI be the judge.

## Getting Started

### Prerequisites
- Python 3.11
- Poetry
### Setup
1. Copy the .env.example file into a new file named .env in the same directory:
`cp .env.example .env`
2. Open the .env file and replace the empty string with your OpenAI key:
`OPENAI_API_KEY="your-openai-key"`
### Installation
1. Install the project dependencies using Poetry:
`poetry install`
### Running the Server
1. Run the server using the following command:
`poetry run python -m src.code_comedian.api.main`
This should start a server at
`http://0.0.0.0:8000/code-comedian`
### Making Requests to the API Server
You can make requests to the API server using the routes defined in `src/code_comedian/api/main.py`

To get your joke judged, you can send a POST request to /joke with the joke content in the request body.
```
curl -X POST "http://localhost:8000/code-comedian/joke" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"content\":\"Your joke here\"}"
```

## About the Project

We’re usually familiar with design-patterns with conventional software architectures. There are also design patterns emerging for LLM apps.

The `code-comedian` project, where an AI judges if your developer joke is funny or not, was created to demonstrate practical patterns for integrating large language models (LLMs) into systems & products.

**There are 7 key design patterns.**

- [**Evaluations](https://eugeneyan.com/writing/llm-patterns/#evals-to-measure-performance):** To measure performance of an LLM

- [**RAG](https://eugeneyan.com/writing/llm-patterns/#retrieval-augmented-generation-to-add-knowledge):** To add recent, external knowledge

- [**Fine-tuning](https://eugeneyan.com/writing/llm-patterns/#fine-tuning-to-get-better-at-specific-tasks):** To get better at specific tasks

- [**Caching](https://eugeneyan.com/writing/llm-patterns/#caching-to-reduce-latency-and-cost):** To reduce latency & cost

- [**Guardrails](https://eugeneyan.com/writing/llm-patterns/#guardrails-to-ensure-output-quality):** To ensure output quality

- [**Defensive UX](https://eugeneyan.com/writing/llm-patterns/#defensive-ux-to-anticipate--handle-errors-gracefully):** To anticipate & manage errors gracefully

- [**Collect user feedback](https://eugeneyan.com/writing/llm-patterns/#collect-user-feedback-to-build-our-data-flywheel):** To build our data flywheel

