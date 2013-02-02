import json
from redis import Redis
from flask import Flask, request
app = Flask(__name__)

redis = Redis()


@app.route("/")
def index():
  return "hello"


@app.route("/<username>", methods=['GET', 'POST'])
def get_pastes(username):
  if request.method == 'GET':
    return json.dumps(redis.lrange(username, 0, -1))
  else:
    # handle arrays with *[]
    return json.dumps(redis.lpush(username, request.form.get('paste')))

if __name__ == "__main__":
  app.run(debug=True)
