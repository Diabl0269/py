# Solve captcha
import pytesseract
import cv2
import numpy as np
import requests
from bs4 import BeautifulSoup

base_url = "https://challenges.itsafe.co.il/PYTHON/"
# Change level here 0 | 1 | 2
level = 2

session = requests.session()
r = session.get("{0}stage2.php".format(base_url), params="level={0}".format(level))
headers = {"Content-Type": "application/x-www-form-urlencoded"}

while "You did it" not in str(r.content):
    soup = BeautifulSoup(r.text, 'html.parser')
    img_path = soup.img["src"]
    img_src = "{0}{1}".format(base_url, img_path)
    print(img_src)
    img_content = session.get(img_src, stream=True).raw

    image = np.asarray(bytearray(img_content.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (h, w) = image.shape[:2]
    image = cv2.resize(image, (w * 2, h * 2))
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, None)
    # image = cv2.threshold(image, 0, 255, cv2.THRESH_BINA RY | cv2.THRESH_OTSU)[1]

    # Save image to check preparation
    cv2.imwrite("img.png", image)

    captcha = pytesseract.image_to_string(image, None, "tesseract.config").split("\n")[0]

    print(captcha)
    post_url = "{0}api.php".format(base_url)
    r = session.post(post_url, headers=headers,
                     data="chal=stage2&captcha={0}&level={1}".format(captcha, level))

print("Congratulations!")
