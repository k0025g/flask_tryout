from flask import Flask


@app.route('/')
def home():
    return "<p>Hello world!</p>"
