import requests


def download(url: str, file: str) -> str:
    result = requests.get(url)

    with open(file, "wb") as f:
        f.write(result.content)
