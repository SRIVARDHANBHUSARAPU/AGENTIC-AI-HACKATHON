from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_KEY")
)

MODEL_NAME = "gemini-2.5-flash"