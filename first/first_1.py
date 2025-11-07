from flask import Flask

web=Flask(__name__)

@web.route('/')
@web.route('/register')

def home():
    return "hello world"

if __name__=='__main__':
    web.run(debug=True)
    