import os
import requests

from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_link(token, url):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "long_url": url
    }
    response = requests.post(
        "https://api-ssl.bitly.com/v4/bitlinks",
        headers=headers,
        json=payload
    )
    response.raise_for_status()

    return response.json()["link"]


def count_clicks(token, url):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "units": -1
    }
    bitlink_without_protocol = "".join(urlparse(url)[1:])

    response = requests.get(
        f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink_without_protocol}/clicks/summary",
        headers=headers,
        params=params
    )
    response.raise_for_status()

    return response.json()["total_clicks"]


def is_bitlink(token, url):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    parsed = urlparse(url)
    bitlink = f"{parsed.netloc}{parsed.path}"

    response = requests.get(
        f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}",
        headers=headers
    )

    return response.ok


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("BITLY_TOKEN")
    url = input("Please enter URL for shortener or bit.ly url to get clicks count: ")

    try:
        if is_bitlink(token, url):
            print(f"Clicks count = {count_clicks(token, url)}")
        else:
            print(f"Shortened url - {shorten_link(token, url)}")
    except requests.exceptions.HTTPError:
        print("Something goes wrong")
