from flask import Flask
from app.src.controllers import HOME

app = Flask(__name__)

@app.route("/")
def homepage():
    return HOME.show()

if __name__ == "__main__":
    app.run()