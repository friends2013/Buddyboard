from flask import Flask, render_template, request, redirect, url_for
from markupsafe import Markup, escape
import txt
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def render_form():
    post = open("./abfm.txt", "r").read().split('\n')
    return render_template('abfm.html', posts=post)

@app.route('/', methods=['POST'])
def add_data():
    data = request.form.get('data')
    if data:
        try:
            with open('./abfm.txt', 'a') as file:
                file.write(request.remote_addr + ";" + escape(data) + '\n')
            return redirect(url_for('render_form'))
        except Exception as e:
            return "Error: " + str(e)
    else:
        return "No data provided in the request."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)