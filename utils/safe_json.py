import json


def safe_json_parse(text):
    """
    Safely converts Gemini output into a Python dictionary.

    Handles:
    - ```json ... ```
    - ``` ... ```
    - Empty responses
    - Invalid JSON
    """

    if not text:
        return {}

    text = text.strip()

    # Remove markdown code block
    if text.startswith("```json"):
        text = text.replace("```json", "", 1)

    if text.startswith("```"):
        text = text.replace("```", "", 1)

    if text.endswith("```"):
        text = text[:-3]

    text = text.strip()

    try:
        return json.loads(text)

    except json.JSONDecodeError:
        return {
            "raw_output": text
        }

    except Exception as e:
        return {
            "error": str(e),
            "raw_output": text
        }