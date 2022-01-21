from flask import Flask
from config import *

app = Flask("Awesome site", static_url_path="")

if __name__ == "__main__":
    app.run("0.0.0.0", port=PORT, debug=True)
