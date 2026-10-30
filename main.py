import os
import sys

from dotenv import load_dotenv
from google import genai

load_dotenv()

DEFAULT_MODEL = "gemini-2.5-flash"


def main() -> None:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your-gemini-api-key-here":
        sys.exit("GEMINI_API_KEY is not set. Add it to your .env file (see .env.example).")

    prompt = " ".join(sys.argv[1:]) or "Say hello in one short sentence."
    model = os.getenv("GEMINI_MODEL", DEFAULT_MODEL)

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model=model, contents=prompt)
    print(response.text)


if __name__ == "__main__":
    main()
