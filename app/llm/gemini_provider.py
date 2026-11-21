from google import genai
from google.genai import types

from app.core.config import settings


class GeminiProvider:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.api_key
        )

        self.model = settings.model

    def generate_response(self, messages):

        contents = []

        for message in messages:

            role = (
                "model"
                if message["role"] == "assistant"
                else "user"
            )

            contents.append(
                types.Content(
                    role=role,
                    parts=[
                        types.Part.from_text(
                            text=message["content"]
                        )
                    ]
                )
            )

        response = self.client.models.generate_content(
            model=self.model,
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=(
                    "You are Memora AI, a helpful "
                    "personal AI assistant. "
                    "Answer accurately and clearly."
                ),
                temperature=0.7,
                max_output_tokens=2048
            )
        )

        usage = response.usage_metadata

        return {
            "content": response.text or "",
            "input_tokens": (
                usage.prompt_token_count if usage else 0
            ),
            "output_tokens": (
                usage.candidates_token_count if usage else 0
            ),
            "total_tokens": (
                usage.total_token_count if usage else 0
            ),
            "model": self.model
        }

    def close(self):

        self.client.close()