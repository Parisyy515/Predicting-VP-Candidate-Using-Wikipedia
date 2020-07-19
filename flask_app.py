
# A very simple Flask Hello World app for you to get started with...
from VP_candidate import main, get_url_list
from flask import Flask
from datetime import *

present = datetime.now()
app = Flask(__name__)


@app.route('/')
def hello_world():
    # return 'Hello from Flask!'
    url_list = get_url_list()
    main(url_list, present)

if __name__ == "__main__":
    hello_world()