from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/questions")
def generate_form():
    """generate the form"""  
    return render_template("questions.html", mad_lib_words = silly_story.prompts)


@app.post("/results")
def print_story():
    #print the story
    story = silly_story.generate(request.form)
    print(request.form)
    return render_template("story.html", jinja_story = story)


# @app.get("/questions") --> postrequest

#form 
# there are inputs we need to collect
# based on those inputs you 
#get request -> request.args 
#post request -> request.forms