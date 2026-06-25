import os
import json
import re
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get Gemini API key from .env
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)


def extract_json_from_response(text):
    """
    Gemini may return JSON inside markdown like ```json ... ```
    This function extracts clean JSON text.
    """
    text = text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()
    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    match = re.search(r"\[.*\]", text, re.DOTALL)
    if match:
        return match.group(0)

    return text


def generate_quiz(subject, topic, difficulty, num_questions):
    prompt = f"""
    Generate {num_questions} multiple-choice quiz questions for the subject "{subject}" on the topic "{topic}".
    Difficulty level should be "{difficulty}".

    Return ONLY a valid JSON array.
    Each question must follow exactly this format:

    [
      {{
        "question": "Question text",
        "options": ["option1", "option2", "option3", "option4"],
        "answer": "correct option",
        "topic": "{topic}"
      }}
    ]

    Rules:
    - Return exactly {num_questions} questions
    - Each question must have 4 options
    - answer must exactly match one option
    - Do not write explanation
    - Do not write any text before or after JSON
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        raw_text = response.text.strip()
        cleaned_json = extract_json_from_response(raw_text)
        quiz_data = json.loads(cleaned_json)

        valid_questions = []
        for q in quiz_data:
            if (
                "question" in q and
                "options" in q and
                "answer" in q and
                "topic" in q and
                isinstance(q["options"], list) and
                len(q["options"]) == 4 and
                q["answer"] in q["options"]
            ):
                valid_questions.append(q)

        return valid_questions

    except Exception as e:
        print("Error while generating quiz:", e)
        return []