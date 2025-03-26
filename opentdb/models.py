from typing import List, Optional
from pydantic import BaseModel
from enums import Categories, Difficulties, QuestionTypes, Encodings


class Question(BaseModel):
    type: str
    difficulty: str
    category: str
    question: str
    correct_answer: str
    incorrect_answers: List[str]


class Results(BaseModel):
    response_code: int
    results: List[Question]


class QuestionParameters(BaseModel):
    amount: int
    category: Optional[Categories] = None
    difficulty: Optional[Difficulties] = None
    type: Optional[QuestionTypes] = None
    encode: Optional[Encodings] = None
