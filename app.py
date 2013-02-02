import json
from redis import Redis
from flask import Flask, request, render_template
app = Flask(__name__)

redis = Redis()


@app.route("/")
def index():
  return "hello"


@app.route("/<username>", methods=['GET', 'POST'])
def pastes(username):
  if request.method == 'GET':
    pastes = redis.lrange(username, 0, -1)
    if request.headers['Accept'] == 'application/json':
      return json.dumps(pastes)
    else:
      return render_template('paste.html', pastes=pastes)
  else:
    pastes = request.form.getlist('paste')
    # should check validity of pastes
    redis.lpush(username, *pastes)
    pastes = redis.lrange(username, 0, -1)
    if request.headers['Accept'] == 'application/json':
      return json.dumps(pastes)
    else:
      return render_template('paste.html', pastes=pastes)

if __name__ == "__main__":
  app.run(debug=True)
