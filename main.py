import time
import redis
from flask import Flask

app = Flask(__name__)


@app.route("/<x>")
def hello_world(x):

    r = redis.Redis(host='localhost', port=6379, db=0)

    if r.exists(x) == 1:
        return r.get(x)
    else:
        result = int(x) + 1
        time.sleep(5)
        r.set(x, result, ex=30)
        return f"{result}"



    #
    #
    # #TODO: Ask Redis, does x exist?
    # r = redis.Redis(host='localhost', port=6379, db=0)
    #
    # #TODO: If exist, return stored value
    #
    # #TODO: If not exist, calculate
    # for i in range(100000000):
    #     result = x + 1
    #
    # #TODO: Save result to redis
    #
    # return result
