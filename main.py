from flask import Flask, render_template


app = Flask('app')


@app.route('/')
def index_page():
  return render_template('index.html')
