from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def load_questions():
    questions = []
    with open('questions.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append(row)
    return questions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    questions = load_questions()
    return render_template('quiz.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    questions = load_questions()
    score = 0

    for q in questions:
        user_answer = request.form.get(q['id'])
        if user_answer == q['answer']:
            score += 1

    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)