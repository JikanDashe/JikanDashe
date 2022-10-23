from flask import Flask,render_template,request
import sqlite3 as sq

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST','GET'])
def submitNum():
    if (request.method =='POST'):
      name = request.form['name']
      number = request.form['number']
    
    with dbconnect () as dbconn:
     cur = conn.cursor
     query = 'INSERT INTO phone_book (name,number)VALUES(?,?)'
        cur.execute(query,(name,number))
        print('executed')
    return render_template('completed.html')

@app.route('/phonebook')
def displayphonebook():
    with dbconnect () as dbconn:
     cur = conn.cursor()
     cur.execyte(query)

    row = cur.fetchall()

    return render_template('phonebook.html',phonebook=row)

@app.route('/edit{id}')
def edit (id):
    with dbconnect () as dbconn:
     cur = conn.cursor
     query = 'INSERT INTO edit (name,number)VALUES(?,?)'
        cur.execute(query,(name,number))
        print('executed')




if __name__=='__main__':
    app.run(debug=True)
