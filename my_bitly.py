import argparse
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
    parsed_url = urlparse(url)
    bitlink_without_protocol = f"{parsed_url.netloc}{parsed_url.path}"

    response = requests.get(
        f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink_without_protocol}/clicks/summary",
        headers=headers
    )
    response.raise_for_status()

    return response.json()["total_clicks"]


def is_bitlink(token, url):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    parsed_url = urlparse(url)
    bitlink = f"{parsed_url.netloc}{parsed_url.path}"

    response = requests.get(
        f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}",
        headers=headers
    )

    return response.ok


def get_arguments():
    parser = argparse.ArgumentParser(description="Manage bitlinks and preview basic stats for it")
    parser.add_argument("url", help="URL to shorten or Bitly link to review stats")
    return parser.parse_args()


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("BITLY_TOKEN")
    args = get_arguments()
    try:
        if is_bitlink(token, args.url):
            print(f"Clicks count = {count_clicks(token, args.url)}")
        else:
            print(f"Shortened url - {shorten_link(token, args.url)}")
    except requests.exceptions.HTTPError:
        print("Something goes wrong")
