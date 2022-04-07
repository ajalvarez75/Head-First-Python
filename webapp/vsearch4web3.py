from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)

@app.route('/search4', methods=['POST'])
#if you wanted to add GET support to the /search4 URL, you need only change the
#@app.route line of code to look like this: @app.route('/search4', methods=['GET', 'POST']).
#For more on this, see the Flask docs, which are available here http://flask.pocoo.org.
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)
#This extra comma looks a little strange, but is perfectly fine
#(though optional) Python syntax
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')

app.run(debug=True)
