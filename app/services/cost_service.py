from app.core.config import settings


class CostService:

    def calculate_cost(
        self,
        input_tokens,
        output_tokens
    ):

        input_rate = settings.input_price
        output_rate = settings.output_price

        # No pricing configured means unknown cost.
        if input_rate is None or output_rate is None:
            return None

        input_cost = (
            input_tokens * input_rate
        ) / 1_000_000

        output_cost = (
            output_tokens * output_rate
        ) / 1_000_000

        return round(
            input_cost + output_cost,
            10
        )