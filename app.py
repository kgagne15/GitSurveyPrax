from crypt import methods
from flask import Flask, request, render_template, redirect, flash, session
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

@app.route('/session-set', methods=['POST'])
def set_session():
    session['responses'] = []
    return redirect('/questions/0')

@app.route('/questions/<int:id>')
def questions_page(id):
    length = len(list(session['responses']))
    if length == len(satisfaction_survey.questions):
        return render_template('thanks.html')
    elif id == length:
        question = satisfaction_survey.questions[id]
        answer_choices = satisfaction_survey.questions[id].choices
        return render_template('questions.html', question=question, id=id, answer_choices=answer_choices)
    else: 
        # question = satisfaction_survey.questions[len(responses)]
        # answer_choices = satisfaction_survey.questions[len(responses)].choices
        flash("You must answer the questions in order.")
        return redirect(f'/questions/{length}')

@app.route('/answer', methods=["POST"])
def answer_page():
    answer = request.form['answer']
    responses = session['responses']
    responses.append(answer)
    session['responses'] = responses
    length = len(list(session['responses']))
    if length < len(satisfaction_survey.questions):
        return redirect(f'questions/{length}')
    else: 
        #print(session['responses'])
        return render_template('thanks.html')
