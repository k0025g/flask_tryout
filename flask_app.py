from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return "<p>test flask huiswerk les 11</p>"
