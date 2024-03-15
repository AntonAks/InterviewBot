import functools
from openai.types.chat import ChatCompletion, ChatCompletionMessage
from openai.types.completion_usage import CompletionUsage
from openai.types.chat.chat_completion import Choice
from services.language_models.open_ai import OpenAIService
from unittest import mock

QUESTION_TEXT = "First can have unique values, second can't"
ANSWER_TEXT = "'What are the differences between lists and sets in Python?"
HOW_TO_IMPROVE = "The answer is partially correct. While it is true that sets in Python cannot have duplicate values, lists can also contain unique values. To improve the answer, you can mention other differences such as sets being unordered and not having indexing capabilities like lists do."
CHAT_COMPLETION = ChatCompletion(id='chatcmpl-92hKBO6St3Inw46jgTM3frbTfSmx3', choices=[
                    Choice(finish_reason='stop',
                           index=0,
                           logprobs=None,
                           message=ChatCompletionMessage(
                               content='Estimation: 3\nHow to Improve: The answer is partially correct. While it is true that sets in Python cannot have duplicate values, lists can also contain unique values. To improve the answer, you can mention other differences such as sets being unordered and not having indexing capabilities like lists do.',
                               role='assistant', function_call=None, tool_calls=None))], created=1710430223,
                                            model='gpt-3.5-turbo-0125',
                                            object='chat.completion', system_fingerprint='fp_4f2ebda25a',
                                            usage=CompletionUsage(completion_tokens=86,
                                                                  prompt_tokens=80,
                                                                  total_tokens=166,
                                                                  text=""))


def mock_oai_client_answer_check(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with mock.patch.object(
                OpenAIService,
                "completions_create",
                return_value=CHAT_COMPLETION,
                autospec=True,
        ) as _:
            return func(*args, **kwargs)

    return wrapper
