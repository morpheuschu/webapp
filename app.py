#!/usr/bin/python3
# !python*
# coding = utf-8
# author : morpheus
# date : 2023-1/5/2023-{16:51}
# project : webapp
# file : app

from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World"


@app.route("/test")
def test():
    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
