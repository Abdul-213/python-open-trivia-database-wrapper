# python-open-trivia-database-wrapper

A Python wrapper for the[ Open Trivia Database API](https://opentdb.com/).

To intall the package, run the following command:

```bash
pip install python-open-trivia-database-wrapper
```

## Usage

```python
from opentdb.opentdb import openTriviaDB, Parameters

trivia = openTriviaDB()
response = trivia.get_questions(category=Parameters.Category.GENERAL_KNOWLEDGE, number_of_questions=1)
```

The `Parameters` class is a helper class that contains enums for the different parameters that can be passed to the `get_questions` method . The `get_questions` method can take the following parameters:

```python
category: Parameters.Category
difficulty: Parameters.Difficulty
question_type: Parameters.QuestionType
number_of_questions: int
```

Example of all the parameters being used: 
```python
response = get_questions(category=Parameters.Category.GENERAL_KNOWLEDGE,
                         difficulty=Parameters.Difficulty.EASY,
                         question_type=Parameters.QuestionType.MULTIPLE,
                         number_of_questions=15)
```

If no parameters are passed in, then a set of 10 random questions will be returned

## Response

Example json response from API:

```json
{
    "response_code": 0,
    "results": [
        {
            "category": "General Knowledge",
            "type": "multiple",
            "difficulty": "easy",
            "question": "What is the most common surname Wales?",
            "correct_answer": "Jones",
            "incorrect_answers": [
                "Williams",
                "Davies",
                "Evans"
            ]
        }
    ]
}
 ```

In code, the response is modelled by a `Result` object, which has the following attributes:


```python
response_code: int
results: List[Question]
```

The `Question` object has the following attributes:

```python
type: str
difficulty: str
category: str
question: str
correct_answer: str
incorrect_answers: List[str]
```

So when looping over the list of results, you can access the attributes like so:

```python
for result in response.results:
    print(result.question)
    print(result.correct_answer)
    print(result.incorrect_answers)
```