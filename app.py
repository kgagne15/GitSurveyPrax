from crypt import methods
from flask import Flask, request, render_template, redirect, flash
from surveys import Survey, Question, satisfaction_survey
# from flask_debugtoolbar import DebugToolbarExtension

#used minimal help from solution


app = Flask(__name__)
app.config['SECRET_KEY'] = "chickenzarecool21837"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def home_page():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html', instructions=instructions, title=title)

@app.route('/questions/<int:id>')
def questions_page(id):
    if len(responses) == len(satisfaction_survey.questions):
        return render_template('thanks.html')
    elif id == len(responses):
        question = satisfaction_survey.questions[id]
        answer_choices = satisfaction_survey.questions[id].choices
        return render_template('questions.html', question=question, id=id, answer_choices=answer_choices)
    else: 
        question = satisfaction_survey.questions[len(responses)]
        answer_choices = satisfaction_survey.questions[len(responses)].choices
        flash("You must answer the questions in order.")
        return redirect(f'/questions/{len(responses)}')

@app.route('/answer', methods=["POST"])
def answer_page():
    answer = request.form['answer']
    responses.append(answer)
    id = (len(responses))
    if id < len(satisfaction_survey.questions):
        return redirect(f'questions/{len(responses)}')
    else: 
        return render_template('thanks.html')
