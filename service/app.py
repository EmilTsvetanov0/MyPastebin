from flask import Flask, request,render_template, redirect, url_for
import random
import string
app = Flask(__name__)
codes = {}
reserved = {}
langs = {}
import logging
import requests
import bd_work
from bd_work import *


# Проверка словаря
for key, value in language_mapping.items():
    print(f"{key}: {value}")


url = 'http://language-detecting-model:80/predict'

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Отправка POST запроса

language_mapping_reverse = {
    "language-cpp": "C++",
    "language-python": "Python",
    "language-javascript": "JavaScript",
    "language-csharp": "C#",
    "language-c": "C",
    "language-go": "Go",
    "language-applescript": "AppleScript",
    "language-kotlin": "Kotlin",
    "language-pascal": "Pascal",
    "language-java": "Java",
    "language-jq": "jq",
    "language-r": "R",
    "language-wolfram": "Mathematica/Wolfram Language",
    "language-rust": "Rust",
    "language-lua": "Lua",
    "language-vbnet": "Visual Basic .NET",
    "language-swift": "Swift",
    "language-scala": "Scala",
    "language-ruby": "Ruby",
    "language-php": "PHP",
    "language-powershell": "PowerShell",
    "language-perl": "Perl",
    "language-cobol": "COBOL",
    "language-armasm": "ARM Assembly",
    "language-fortran": "Fortran",
    "language-erlang": "Erlang"
}

def generate_random_word():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))


def make_string_without_tags(txt):
    txt.replace('<', '&lt')
    txt.replace('>', '&gt')
    txt.replace('&', '&amp')
    txt.replace('“', '&quot')
    txt.replace('‘', '&apos')
    return txt

@app.route('/')
def home():
    return redirect(f'/new')

@app.route('/new', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        code = make_string_without_tags(request.form['code'])

        language = request.form['coding_language']
        if(language == "" or language == "0"):
            data = {"text": code}
            response = requests.post(url, json=data)
            language = language_mapping [response.json()['prediction']]



        link = generate_random_word()
        while (exist(link)):
            link = generate_random_word()

        add_data(link, code, language)
        print (f'added new page {link} in {language}')
        return redirect(f'/text_view/{link}')
    else:
        return render_template('main.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.route('/text_view/<id>')
def showcode(id):
    if (exist(id)):
        lang = get_lang(id)
        lang = [lang, language_mapping_reverse[lang]]
        return render_template('text_view.html', text_id=id, code_text=get_text(id), prefered_language=lang)
    else:
        return render_template('404.html')

if __name__ == '__main__':
    create_table()
    app.run(host='0.0.0.0',port=1333)
