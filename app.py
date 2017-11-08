from flask import Flask, render_template
import numpy as np
from content_manager import Content

TOPIC_DICT = Content()

app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template("index.html", TOPIC_DICT = TOPIC_DICT )

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/posting/<post_url>")
def posting(post_url):
    return render_template("post.html",post_url = post_url)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)