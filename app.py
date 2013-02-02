import json
from redis import Redis
from flask import Flask, request, render_template
app = Flask(__name__)

redis = Redis()


@app.route("/")
def index():
  return "hello"


@app.route("/<username>", methods=['GET', 'POST'], defaults={'number': 0})
@app.route("/<username>/<int:number>", methods=['GET', 'POST'])
def pastes(username, number):
  if request.method == 'GET':
    # -1 gets all the things
    pastes = redis.lrange(username, 0, number - 1)
    if request.headers['Accept'] == 'application/json':
      return json.dumps(pastes)
    else:
      return render_template('paste.html', pastes=pastes)
  else:
    pastes = request.form.getlist('paste')
    # should check validity of pastes
    redis.lpush(username, *pastes)
    pastes = redis.lrange(username, 0, number - 1)
    if request.headers['Accept'] == 'application/json':
      return json.dumps(pastes)
    else:
      return render_template('paste.html', pastes=pastes)

if __name__ == "__main__":
  app.run(debug=True)
