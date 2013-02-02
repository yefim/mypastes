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
    pastes = redis.lrange(username, 0, -1)
    return json.dumps(pastes)
  else:
    pastes = request.form.getlist('paste')
    paste = request.form.get('paste')
    # handle arrays with *[]
    if pastes is not None:
      return json.dumps(redis.lpush(username, *pastes))
    elif paste is not None:
      return json.dumps(redis.lpush(username, *paste))
    else:
      return ""

if __name__ == "__main__":
  app.run(debug=True)
