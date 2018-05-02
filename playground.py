from flask import Flask, render_template

app = Flask(__name__)

@app.route("/play")
def play():
    return render_template("index.html",boxes=3)

@app.route("/play/<boxes>")
def boxes(boxes):
    return render_template("index.html", boxes=int(boxes))

@app.route("/play/<boxes>/<color>")
def color_boxes(boxes, color):
    return render_template("index.html", boxes=int(boxes), color=color)
app.run(debug=True)