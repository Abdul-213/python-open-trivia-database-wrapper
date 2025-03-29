import requests
from typing import Optional
from enums import QuestionCategories, QuestionDifficulties, QuestionTypes, QuestionEncodings
from models import Question, Results, QuestionParameters

base_url = "https://opentdb.com/"
api_url = "api.php"
category_url = "api_category.php"
category_question_count = "api_count.php"
global_question_count = "api_count_global.php"


class Parameters:
    Category = QuestionCategories
    Difficulty = QuestionDifficulties
    Type = QuestionTypes
    Encode = QuestionEncodings


class openTriviaDB:

    def __init__(self, generate_token: bool = False):
        self._params = {}
        self.token = None

        if generate_token:
            self.token = requests.get(f"{base_url}api_token.php?command=request").json()["token"]

    def set_parameters(self, question_parameters: QuestionParameters) -> dict:

        if question_parameters.amount:
            self._params["amount"] = question_parameters.amount
        if question_parameters.category:
            self._params["category"] = question_parameters.category.value
        if question_parameters.difficulty:
            self._params["difficulty"] = question_parameters.difficulty.value
        if question_parameters.type:
            self._params["type"] = question_parameters.type.value
        if question_parameters.encode:
            self._params["encode"] = question_parameters.encode.value

        return self._params

    def get_questions(self, category: QuestionCategories | None = None,
                      difficulty: QuestionDifficulties | None = None,
                      question_type: QuestionTypes | None = None,
                      encodings: QuestionEncodings | None = None,
                      number_of_questions: int | None = 10) -> Results:

        params = self.set_parameters(QuestionParameters(amount=number_of_questions,
                                                        category=category,
                                                        difficulty=difficulty,
                                                        type=question_type,
                                                        encode=encodings))

        response = requests.get(f"{base_url}{api_url}", params=params).json()

        return Results(**response)