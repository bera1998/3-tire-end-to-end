from flask import Flask, jsonify

app = Flask(__name__)

# Sample API endpoint
@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from backend!"})

# You can add more API endpoints as needed
# Example: /api/data, /api/users etc.

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)