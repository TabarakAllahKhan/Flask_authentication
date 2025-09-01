from flask import Flask, render_template, redirect,request


app=Flask(__name__)


@app.route('/')
def index():
    return 'app is running'


if __name__=='main':
    app.run(debug=True)