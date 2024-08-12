from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route("/images")
def serve_image(filename):
    return send_from_directory('my_images', filename)

if __name__ == '__main__':
    app.run(debug=True)

# Quiz questions
QUESTIONS = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin"], "answer": "Paris"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"}
    {"question": "Which element on the periodic table has the chemical symbol O?", "options": ["Oxygen", "Gold", "Hydrogen"], "answer": "Oxygen"}
    {"question": "Which planet in our solar system is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter"], "answer": "Mars"}
    {"question": "What is the smallest prime number?", "options": ["0", "1", "2"], "answer": "2"}
    {"question": "Who wrote the novel 1984?", "options": ["George Orwell", "Ronan Berry", "Ray Bradbury"], "answer": "George Orwell"}
    {"question": "In which year did the Titanic sink?", "options": ["1910", "1911", "1912"], "answer": "1912"}
    {"question": "Which element has the atomic number 79", "options": ["Gold", "Silver", "Mercury"], "answer": "Gold"}
    {"question": "Which mathematician is credited with the invention of the modern binary system?", "options": ["Blaise Pascal", "Gottfried Wilhelm Leibniz", "René Descartes"], "answer": "Gottfried Wilhelm Leibniz"}
]

@app.route('/')
def index():
    questions_with_index = [{"index": i, **question} for i, question in enumerate(QUESTIONS)]
    return render_template('index.html', questions=questions_with_index)

@app.route('/submit', methods=['POST'])
def submit():
    user_answers = request.json
    score = 0
    for i, question in enumerate(QUESTIONS):
        if user_answers.get(str(i)) == question["answer"]:
            score += 1
    return jsonify({"score": score, "total": len(QUESTIONS)})

if __name__ == '__main__':
    app.run(debug=True)
