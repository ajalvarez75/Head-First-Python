from flask import Flask, render_template
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4', methods=['POST'])
#if you wanted to add GET support to the /search4 URL, you need only change the
#@app.route line of code to look like this: @app.route('/search4', methods=['GET', 'POST']).
#For more on this, see the Flask docs, which are available here http://flask.pocoo.org.
def do_search() -> str:
    return str(search4letters('life, the universe, and everything','eiru,!'))

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')

app.run(debug=True)
