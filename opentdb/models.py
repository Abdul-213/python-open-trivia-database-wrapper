from typing import List, Optional
from pydantic import BaseModel
from enums import QuestionCategories, QuestionDifficulties, QuestionTypes, QuestionEncodings


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
    category: Optional[QuestionCategories] = None
    difficulty: Optional[QuestionDifficulties] = None
    type: Optional[QuestionTypes] = None
    encode: Optional[QuestionEncodings] = None
