import os
import re
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, url_for, request, redirect, flash, make_response, jsonify
from summariser import nltk_summariser, gensim_summariser

# Initialise Flask
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Custom error handling
@app.errorhandler(404)
def page_not_found_error(error):
    return make_response(jsonify({'Error': str(error)}), 404)  # 404 Not Found

@app.errorhandler(500)
def internal_server_error(error):
    return make_response(jsonify({'Error': str(error)}), 500)  # Internal Server Error

#Home page
@app.route("/")
def index():
    return render_template('index.html')

#Summarised text page
@app.route("/results", methods=('POST',))
def results():
    url = request.form.get('url')

    try:
        # Retrieve page associated with url
        response = requests.get(url)

        if response.status_code != 200:
            raise RuntimeError()

    except:
        # Error message for invalid url
        flash('The url is invalid. Please fix it and resubmit.')
        return redirect(url_for('index'))

    # Parse results with Beauitful Soup
    soup = BeautifulSoup(response.content, "lxml")
    paragraphs = soup.find_all('p')
    article_text = ""
    for p in paragraphs:
        article_text += p.text
    article_text = re.sub("[\(\[].*?[\)\]]", "", article_text)
    article_text = re.sub(r'(?<!\w)([A-Z])\.', r'\1', article_text)
    article_text = re.sub(r'\s([?.!"](?:\s|$))', r'\1', article_text)
    article_text = article_text.replace("e.g.", "eg")
    article_text = article_text.replace("i.e.", "ie")

    # Generate NLTK summary
    nltk_summary = nltk_summariser.get_summary(article_text)

    #Generate Gensim summary
    gensim_summary = gensim_summariser.get_summary(article_text)

    return render_template('results.html', nltk_summary=nltk_summary, gensim_summary=gensim_summary)

if __name__ == "__main__":
    app.run(debug=True)
