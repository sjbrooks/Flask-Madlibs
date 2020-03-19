from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "fluffy"

debug = DebugToolbarExtension(app)

# from stories import Story
from stories import story

@app.route('/')
def word_form():
    """Takes in prompts from story instance and creates a form"""

    prompts_from_instance = story.prompts

    return render_template('form.html', prompts=prompts_from_instance)

@app.route('/story')
def generate_story():
    """Takes in inputs from form and pulls in text variable
    from story class to generate a story on the page"""

    prompts_from_instance = story.prompts
    user_word_input = [request.args.get(prompt) for prompt in prompts_from_instance]

    prompt_and_input = {prompts_from_instance[i]: user_word_input[i] for i in range(len(prompts_from_instance))}

    # simpler way to get prompt_and_input in a dict format is just using request.args() with no arguments

    story_text = story.generate(prompt_and_input)

    return render_template('story.html', story_text=story_text)
