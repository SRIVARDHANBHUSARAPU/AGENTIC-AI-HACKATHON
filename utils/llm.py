import time

from google import genai
from google.genai import types, errors

from config import client, MODEL_NAME


def safe_gemini_call(prompt, retries=3, delay=2):
    """
    Calls Gemini safely with retries.
    Always returns text.
    """

    for attempt in range(retries):

        try:

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json"
                ),
            )

            return response.text

        except errors.ServerError:
            print(f"[503] Retry {attempt + 1}/{retries}")
            time.sleep(delay)

        except errors.ClientError as e:
            print(f"[Client Error] {e}")
            return f"ERROR: {e}"

        except Exception as e:
            print(f"[Unexpected Error] {e}")
            return f"ERROR: {e}"

    return "ERROR: Gemini failed after retries."