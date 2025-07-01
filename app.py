from flask import Flask, render_template, request, jsonify
from process_query import process_query

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["query"]
        response = process_query(query)
        return jsonify({"response": response})
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(debug=True)
