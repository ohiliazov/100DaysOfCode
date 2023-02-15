import requests


def get_question_data():
    response = requests.get(
        "https://opentdb.com/api.php",
        params={"amount": "10", "type": "boolean"},
    )
    assert response.status_code == 200

    return response.json()["results"]
