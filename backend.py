from dotenv import load_dotenv
import os
import requests

load_dotenv()

api = os.getenv("API")


def get_data(place, days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api}"
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    get_data(place="Tokyo")

