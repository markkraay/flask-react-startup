from flask import Flask, render_template

app = Flask("__main__")

@app.route("/")
def my_index():
    return render_template("index.html", token="Hello World")

app.run(debug=True)

