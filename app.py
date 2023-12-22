# app.py

from flask import Flask, render_template
from fake_data import get_fake_names, get_fake_chats

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', fake_names=get_fake_names(), fake_chats=get_fake_chats())

if __name__ == '__main__':
    app.run(debug=True)
