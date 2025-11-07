from flask import Flask, render_template, request, redirect, url_for
import os

web = Flask(__name__)

# ✅ Correct absolute path to static folder
pick = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
web.config['UPLOAD_FOLDER'] = pick

@web.route('/')
def home():
    pics = os.listdir(web.config['UPLOAD_FOLDER'])
    return render_template('home.html', movie_list=pics)

@web.route('/two')
def two():
    return render_template('two.html')

if __name__ == '__main__':
    web.run(debug=True)
