from dotenv import load_dotenv
import os
import requests

load_dotenv()

api = os.getenv("API")


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    get_data(place="Tokyo", forecast_days=3)

