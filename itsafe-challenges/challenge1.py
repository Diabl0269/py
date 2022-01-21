# Solves math exercises on a remote site

import requests
from bs4 import BeautifulSoup

session = requests.session()

# Initial get
r = session.get("https://challenges.itsafe.co.il/PYTHON/stage1.php").text

while "You did it!, go to stage2.php" not in r:
    # Post returns redirect.
    soup = BeautifulSoup(r, 'html.parser')
    print(soup.h3.text)
    try:
        res = eval(soup.h3.text)
    except:
        res = 0

    r = session.post("https://challenges.itsafe.co.il/PYTHON/api.php", data={"solution": res, "chal": "stage1"}).text

print(r)
