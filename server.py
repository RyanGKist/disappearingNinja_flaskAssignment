from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template ("index.html")

@app.route("/ninja")
def all_ninja():
	return render_template ("all_ninjas.html")

@app.route("/ninja/<color>")
def specific_ninja(color):
	color = color
	if color == "blue":
		return render_template ("leonardo.html")
	if color == "orange":
		return render_template ("michelangelo.html")
	if color == "red":
		return render_template ("raphael.html")
	if color == "purple":
		return render_template ("donatello.html")
	else:
		return render_template("not_april.html")



app.run(debug=True)
