from flask import Flask, render_template, request, flash, redirect, url_for
from condense import condenser

app = Flask(__name__)
app.config['SECRET_KEY'] = ('94d6d6b1912135d0bfb6a47bde639076e9bf5eefef318d8b')

condense_sentences = []


@app.route('/index')
def index():
    return render_template('index.html', answers=condense_sentences)


@app.route("/condense", methods=('POST', 'GET'))
def condense():
    if request.method == 'POST':
        prompt = request.form['prompt']
        if not prompt:
            flash('Input is required!')
        else:
            item = condenser(prompt)
            condense_sentences.append(item)
            return redirect(url_for('index'))
    return render_template('condense.html')
