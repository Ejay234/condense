from flask import Flask, render_template, request, flash, redirect, url_for
from condense import condenser

app = Flask(__name__)


condense_sentences = []


@app.route('/index')
def index():
    return render_template('index.html', answers=condense_sentences)


@app.route("/", methods=['GET', 'POST'])
def condense():
    if(request.method == 'POST'):
        prompt = request.form['prompt']
        if not prompt:
            flash('Input is required!')
        else:
            item = condenser(prompt)
            condense_sentences.append(item)
            return redirect(url_for('index'))
    else:
        return render_template('condense.html')
