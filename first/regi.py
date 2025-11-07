from flask import Flask,render_template,request


web=Flask(__name__)

@web.route('/')
@web.route('/register')
 
def reg():
    return render_template('register.html')

@web.route('/hello',methods=['post','get'])
def hello():
    name=request.form.get('name')
    city=request.form.get('city')
    phoneno=request.form.get('phoneno')


    return render_template('index.html',name=name,city=city,ph_no=phoneno)

if __name__=='__main__':
    web.run(debug=True)