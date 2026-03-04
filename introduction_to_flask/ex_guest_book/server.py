from flask import Flask, render_template, request, redirect
import json
import time

COMMENTS_FILE = "comments.json"

app = Flask(__name__)


def read_comments():
    comments = []

    try:
        with open(COMMENTS_FILE, "r") as f:
            comments = json.load(f)
    except:
        print(f'New {COMMENTS_FILE} file will be created')

    return comments


@app.route("/")
def main():
    return render_template("base.html")


@app.route("/get_comments")
def get_comments():
    response = app.response_class(
        response=json.dumps(read_comments()),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/add_comment", methods=["POST"])
def add_comment():
    comments = read_comments()

    data = request.json

    comments.append({
        "name": data["name"],
        "text": data["text"],
        "date": time.ctime()
    })

    with open(COMMENTS_FILE, "w") as f:
        json.dump(comments, f)

    return 'OK'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5047, debug=True)