
# A very simple Flask Hello World app for you to get started with...
from VP_candidate import main, get_url_list
from flask import Flask
from datetime import datetime

present = datetime.now()
app = Flask(__name__)

@app.route('/')
def hello_world():

    url_list = get_url_list()
    statement = main(url_list, present)
    return statement

if __name__ == "__main__":
    hello_world()