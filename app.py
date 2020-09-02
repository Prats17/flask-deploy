# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 11:25:35 2020

@author: Dell
"""




from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('main.html')

@app.route('/click', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return render_template('main.html',p_text='Entered symbol'+processed_text)


if __name__ == "__main__":
    app.run(debug=True)
