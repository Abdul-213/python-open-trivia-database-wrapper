import requests
from typing import Optional
from enums import Categories, Difficulties, QuestionTypes, Encodings
from models import Question, Results, QuestionParameters

base_url = "https://opentdb.com/"
api_url = "api.php"
category_url = "api_category.php"
category_question_count = "api_count.php"
global_question_count = "api_count_global.php"


class openTriviaDB:

    def __init__(self):
        self._params = {}
        pass

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

    def get_questions(self, category: Categories | None = None,
                      difficulty: Difficulties | None = None,
                      question_type: QuestionTypes | None = None,
                      encodings: Encodings | None = None,
                      number_of_questions: int | None = 10) -> Results:

        params = self.set_parameters(QuestionParameters(amount=number_of_questions,
                                                        category=category,
                                                        difficulty=difficulty,
                                                        type=question_type,
                                                        encode=encodings))

        response = requests.get(f"{base_url}{api_url}", params=params).json()

        return Results(**response)