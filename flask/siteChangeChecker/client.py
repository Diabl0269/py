import time
import requests
from config import *

old_site = ""


def check_site():
    return requests.get("http://localhost:{0}/index.html".format(PORT)).text


if __name__ == "__main__":
    while True:
        print("Checking site")
        new_site = check_site()

        if old_site != "" and old_site != new_site:
            print("Site has changed!")

        old_site = new_site
        time.sleep(5)
