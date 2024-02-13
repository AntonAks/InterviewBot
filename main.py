from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    questoin:str
    is_offer: Union[bool, None] = None

class Answer(BaseModel):
    answer:str
    is_offer: Union[bool, None] = None

class Result(BaseModel):
    result:str
    is_offer: Union[bool, None] = None

@app.get("/")
async def read_root():
    return {"message": "Please enter url: http://127.0.0.1:8000/docs"}

# create Question
@app.get("/question/{question_id}")
async def read_question(question_id: int, q: Union[str, None] = None):
    return {"question_id": question_id, "q": q}

@app.post("/question/{item_id}")
async def update_question(question_id: int, question: Question):
    return {question_id: int, "question": question}

# Create Answer
@app.post("/answer/{answer_id}")
async def write_answer(answer_id: int, answer: Answer):
    return {"answer_id": answer_id, "answer": answer}

#Create Result
@app.get("/result/{result_id}")
async def show_result(result_id: int, result: Result):
    return {"result_id": result_id, "result": result}