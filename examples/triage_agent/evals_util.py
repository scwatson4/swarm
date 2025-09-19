from swarm.client import create_azure_openai_client
import instructor
from pydantic import BaseModel
from typing import Optional

__client = instructor.from_openai(create_azure_openai_client())


class BoolEvalResult(BaseModel):
    value: bool
    reason: Optional[str]


def evaluate_with_llm_bool(instruction, data) -> BoolEvalResult:
    eval_result, _ = __client.chat.completions.create_with_completion(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": data},
        ],
        response_model=BoolEvalResult,
    )
    return eval_result
