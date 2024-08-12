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
