from flask import Flask, request, jsonify, render_template
from chatbot import get_response
import sqlite3

app = Flask(__name__)

# 👉 Home page
@app.route("/")
def home():
    return render_template("index.html")

# 👉 Chat API
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    print("User:", user_input)
    response = get_response(user_input)
    print("Bot:", response)   

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS chats (user TEXT, bot TEXT)")
    cursor.execute("INSERT INTO chats VALUES (?, ?)", (user_input, response))

    conn.commit()
    conn.close()

    return jsonify({"response": response})

app.run(debug=True)