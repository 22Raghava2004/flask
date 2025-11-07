from flask import Flask,render_template,request,redirect,url_for
import os
web=Flask(__name__)

pick=os.path.join('static')
web.config['UPLOAD_FOLDER']=pick
@web.route('/')
def home():
    pic=os.path.join(web.config['UPLOAD_FOLDER'],'samurai.jpg')
    return render_template('home.html',user_img=pic)
@web.route('/two')
def two():
    pic=os.path.join(web.config['UPLOAD_FOLDER'],'samurai.jpg')
    return render_template('two.html',user_img=pic)

if __name__=='__main__':
    web.run(debug=True)