from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        print("Age received:", request.form['age'])
        return redirect('/')
    return render_template("base.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5047, debug=True)
