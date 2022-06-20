from crypt import methods
from flask import Flask, request, render_template, redirect
from surveys import Survey, Question, satisfaction_survey
from flask_debugtoolbar import DebugToolbarExtension



app = Flask(__name__)
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def home_page():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html', instructions=instructions, title=title)

@app.route('/questions/<int:id>')
def questions_page(id):

    question = satisfaction_survey.questions[id]
    answer_choices = satisfaction_survey.questions[id].choices
    
    return render_template('questions.html', question=question, id=id, answer_choices=answer_choices)

@app.route('/answer', methods=["POST"])
def answer_page():
    answer = request.form['answer']
    responses.append(answer)
    id = (len(responses))

    if id < len(satisfaction_survey.questions):
        return redirect(f'questions/{id}')
    else: 
        return render_template('thanks.html')
