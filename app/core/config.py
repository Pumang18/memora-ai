import os

from dotenv import load_dotenv

load_dotenv()


def optional_float(name):

    value = os.getenv(name)

    if not value:
        return None

    return float(value)


class Settings:

    def __init__(self):

        self.api_key = os.getenv("GEMINI_API_KEY")

        self.model = os.getenv("GEMINI_MODEL")

        self.database_url = os.getenv(
            "DATABASE_URL",
            "sqlite:///./data/memora.db"
        )

        self.input_price = optional_float(
            "GEMINI_INPUT_PRICE_PER_MILLION"
        )

        self.output_price = optional_float(
            "GEMINI_OUTPUT_PRICE_PER_MILLION"
        )

        if not self.api_key:
            raise ValueError(
                "GEMINI_API_KEY is missing."
            )

        if not self.model:
            raise ValueError(
                "GEMINI_MODEL is missing."
            )


settings = Settings()