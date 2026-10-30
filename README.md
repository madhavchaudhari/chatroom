# chatroom
WebSocket Chatroom

## Setup

The project uses Python 3.14 and [uv](https://docs.astral.sh/uv/) to manage the environment.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh   # install uv, if you don't have it
uv sync                                           # installs Python 3.14 and all dependencies into .venv
cp .env.example .env                              # then put your key in GEMINI_API_KEY
```

Dependencies: `google-genai`, `langchain-google-genai`, `langgraph`, `pydantic`, `python-dotenv`.
Add more with `uv add <package>`.

## Gemini LLM call

```bash
uv run python main.py "What is a WebSocket?"
```
