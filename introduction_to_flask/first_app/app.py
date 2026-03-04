from flask import Flask, render_template, request, redirect


# print(__name__)
app = Flask(__name__)


@app.route("/")  # creating "/" endpoint,
def hello():  # after a call, the "hello" method is executed,
    # return "Hello, World!"  # and it returns "Hello, World" string
    # return render_template("index.html", title='Home', user='Matheo')
    return render_template("form.html")

@app.route('/hey')
def hey():
    return "Hey!"

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        name = request.form['name']
        age = request.form['age']
        grade = request.form['score']
        # print(f"name: {name}, age: {age}, grade; {grade}")
        return f"name: {name}, age: {age}, grade; {grade}"

    else:
        return f"Bad request! type:{request.method}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5047, debug=True)
