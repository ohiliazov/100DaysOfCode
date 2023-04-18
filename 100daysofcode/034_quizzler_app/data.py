import requests

TRIVIA_URL = "https://opentdb.com/api.php"


def get_question_data(amount: int = 10):
    response = requests.get(
        TRIVIA_URL,
        params={"amount": amount, "type": "boolean"},
    )
    assert response.status_code == 200

    return response.json()["results"]
