import requests


def read_url(url):
    return requests.get(url).text