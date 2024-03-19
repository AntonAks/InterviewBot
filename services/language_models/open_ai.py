from openai import OpenAI
from openai.types.chat import ChatCompletion
from settings import settings


class OpenAIService:
    def __init__(self, role: str = "user"):
        self.client = OpenAI(api_key=settings.open_ai_key)
        self.model = settings.open_ai_model
        self.max_tokens = settings.open_ai_max_tokens
        self.role = role

    def completions_create(self, prompt: str) -> ChatCompletion:
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": self.role,
                        "content": prompt,
                    }
                ],
                model=self.model,
                max_tokens=self.max_tokens
            )
            return response
        # TODO: Change exception type to some internal exception (after creation)
        except Exception as e:
            print(f"An error occurred: {e}")

