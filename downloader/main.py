from download import download
from time import sleep
from util import get_hashes


if __name__ == "__main__":
    hashes = get_hashes("./data/dump-1748.txt")

    for hash in hashes:
        download(f"https://cses.fi/file/{hash}/1/1/", f"./codes/1748/{hash}.cpp")
        print("Downloaded", hash)
        sleep(0.01)