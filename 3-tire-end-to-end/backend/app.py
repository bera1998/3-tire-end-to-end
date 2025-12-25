from flask import Flask, jsonify
import os
import mysql.connector

app = Flask(__name__)

# ==========================
# Database Configuration
# ==========================
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppassword")
DB_NAME = os.getenv("DB_NAME", "appdb")

# Function to get DB connection
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
        return None

# ==========================
# Sample API endpoint
# ==========================
@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from backend!"})

# ==========================
# API endpoint to fetch users from DB
# ==========================
@app.route("/api/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

# ==========================
# Main
# ==========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)