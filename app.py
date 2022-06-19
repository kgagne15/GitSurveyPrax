from crypt import methods
from flask import Flask, request, render_template, redirect
from surveys import Survey, Question, satisfaction_survey

app = Flask(__name__)

responses = []

@app.route('/')
def home_page():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html', instructions=instructions, title=title)

# @app.route('/questions/<int:id>')
# def question_zero(id):
#     questions = []
#     for question in satisfaction_survey.questions:
#         questions.append(question)
#     return render_template('questions.html', questions=questions)

@app.route('/questions/<int:id>', methods=["POST"])
def questions_page(id):
    question = satisfaction_survey.questions[id]
    return render_template('questions.html', question=question, id=id)
