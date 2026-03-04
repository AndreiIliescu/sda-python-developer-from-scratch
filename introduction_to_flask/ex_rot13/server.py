from flask import Flask, render_template
from flask import request
import codecs

app = Flask(__name__)


@app.route("/")
def home():
  return render_template("rot13.html")


@app.route("/do_it")
def do_it():
  return codecs.encode(request.args.get('text'), 'rot_13')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5047, debug=True)