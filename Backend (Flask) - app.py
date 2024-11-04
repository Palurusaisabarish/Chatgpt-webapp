# app.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

# Set your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_input,
        max_tokens=100
    )
    
    reply = response.choices[0].text.strip()
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
