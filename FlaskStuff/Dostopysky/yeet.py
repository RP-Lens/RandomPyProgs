from ast import dump
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

def popAns(ans):
        for i in range(4):
            for j in range(4):
                q = i + 97
                w = j + 97
                s = request.files.get(chr(q) + chr(w))

                if s is not None:
                    ans[i][j] = 1
                else:
                    ans[i][j] = 0


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        name = request.form['name']
        age = request.form['age'] 
        ans = [[0 for i in range(4)] for j in range(4)]
        popAns(ans)

        return redirect(url_for("answer", name=name, ans=ans))
    else:
        return render_template("index.html")


@app.route("/yeetusspugeetus/<name>")
def answer(name, ans):
    return render_template('ans.html', info="yoinkus", nm=name)


if __name__ == "__main__":
    app.run(debug=True)