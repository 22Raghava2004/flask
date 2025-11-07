from flask import Flask, render_template, request, redirect, url_for
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='#Ragha2005',
    host='localhost',
    port='5432'
)
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS register (
    name VARCHAR(20),
    city VARCHAR(20),
    phoneno VARCHAR(15)
)
''')
conn.commit()

web = Flask(__name__)

@web.route('/')
@web.route('/register')
def reg():
    return render_template('register.html')

@web.route('/hello', methods=['POST', 'GET'])
def hello():
    name = request.form.get('name')
    city = request.form.get('city')
    phoneno = request.form.get('phoneno')

    if name and city and phoneno:
        try:
            # Check if user already exists
            cursor.execute('SELECT * FROM register WHERE name=%s AND phoneno=%s', (name, phoneno))
            row = cursor.fetchone()

            if row:
                return redirect(url_for('login'))
            else:
                cursor.execute('INSERT INTO register (name, city, phoneno) VALUES (%s, %s, %s)', (name, city, phoneno))
                conn.commit()
        except Exception as e:
            print("Database Error:", e)
            conn.rollback()

    return render_template('index.html', name=name, city=city, ph_no=phoneno)

@web.route('/login')
def login():
    return render_template('login.html')

@web.route('/login_verify', methods=['POST'])
def login_verify():
    name = request.form.get('name')
    phoneno = request.form.get('phoneno')

    cursor.execute('SELECT * FROM register WHERE name = %s AND phoneno = %s', (name, phoneno))
    user = cursor.fetchone()

    if user:
        return render_template('index.html', name=user[0], city=user[1], ph_no=user[2])
    else:
        return "❌ Invalid login. Please register first!"

if __name__ == '__main__':
    web.run(debug=True)
