from app.llm.gemini_provider import GeminiProvider


class ChatService:

    def __init__(self):

        self.provider = GeminiProvider()

        self.messages = []

    def chat(self, user_message):

        self.messages.append({
            "role": "user",
            "content": user_message
        })

        try:

            result = self.provider.generate_response(
                self.messages
            )

            self.messages.append({
                "role": "assistant",
                "content": result["content"]
            })

            return result

        except Exception:

            self.messages.pop()
            raise

    def clear_history(self):

        self.messages.clear()

    def close(self):

        self.provider.close()