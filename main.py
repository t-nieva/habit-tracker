import requests
from dotenv import load_dotenv
import os
import datetime as dt

# Load credentials
load_dotenv()
TOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = os.getenv("PIXELA_USERNAME")
GRAPH_ID = os.getenv("GRAPH_ID")

# Constants
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
HEADERS = {"X-USER-TOKEN":TOKEN}

def create_user():
    user_params = {
        "token":TOKEN,
        "username":USERNAME,
        "agreeTermsOfService":"yes",
        "notMinor": "yes"
    }
    response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print(response.text)
    return response

def create_graph():
    graph_params = {
        "id":GRAPH_ID,
        "name":"My Running Log",
        "unit":"km",
        "type":"float",
        "color": "shibafu"
    }
    response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=HEADERS)
    print(response.text)
    return response

# Post value to the graph
now = dt.datetime.now()
pixela_date = now.strftime("%Y%m%d")
def post_pixel(date: str, quantity: str):
    payload = {"date": date, "quantity": quantity}
    response = requests.post(url=PIXEL_ENDPOINT, json=payload, headers=HEADERS)
    print(response.text)
    return response

update_date = "20250610"
def update_pixel(date: str, quantity: str):
    update_endpoint = f"{PIXEL_ENDPOINT}/{date}"
    payload = {"quantity": quantity}
    response = requests.put(url=update_endpoint, json=payload, headers=HEADERS)
    print(response.text)
    return response

delete_date = "20250610"
def delete_pixel(date: str):
    delete_endpoint = f"{PIXEL_ENDPOINT}/{date}"
    response = requests.delete(url=delete_endpoint, headers=HEADERS)
    print(response.text)
