from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    tmpl = render_template(
            "index.html", )
    return tmpl
