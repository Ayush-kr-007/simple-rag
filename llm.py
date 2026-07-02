import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def answer_question(
        question,
        context,
        history=""
):
    prompt = f"""
You are a document question answering assistant.

Previous Conversation:
{history}

Answer ONLY from the provided context.

If the answer cannot be found,
say:

"The answer is not available in the document."

Context:
{context}

Question:
{question}
"""

    response = model.generate_content(
        prompt
    )

    return response.text