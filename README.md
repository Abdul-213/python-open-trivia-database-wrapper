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

Example response:

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

