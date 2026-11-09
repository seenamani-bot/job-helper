# ai_extractor.py - asks the AI for skills, work history and education.
# Only the cleaned text is sent, and only after you typed y at the checkpoint.

import json
import os

from dotenv import load_dotenv  # loads the key from the .env file
from openai import OpenAI

# The model to use. gpt-4o-mini is cheap and good enough here.
MODEL = "gpt-4o-mini"

# Instructions that tell the AI exactly what to return.
INSTRUCTIONS = """You read resume text and return JSON only, with exactly these keys:
{
  "skills": ["skill", ...],
  "work_history": [{"company": "", "title": "", "dates": "", "summary": ""}],
  "education": [{"school": "", "degree": "", "dates": ""}]
}
Use only what is in the text. If something is not there, use an empty string
or an empty list. Do not invent anything. Placeholders like [NAME] are
removed personal details; ignore them."""


def get_client():
    # Read the key from the environment (.env is loaded into it first).
    load_dotenv()
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY is missing. Add it to your .env file.")
    return OpenAI(api_key=key)


def extract_resume_info(cleaned_text):
    # Send the cleaned text and get back a Python dictionary.
    client = get_client()
    response = client.chat.completions.create(
        model=MODEL,
        response_format={"type": "json_object"},  # ask for valid JSON
        messages=[
            {"role": "system", "content": INSTRUCTIONS},
            {"role": "user", "content": cleaned_text},
        ],
    )
    return json.loads(response.choices[0].message.content)
