from os import name
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL


app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'hotel_mgmt'
app.config['SECRET_KEY'] = 'wTcnxeGX7Uj&@5p$bf%L!QBVx2St!rYUEvtKwF#$nNfs&bbZDraFfNQS2Eib6#t@%@EJ*iqsYugNqpCtJ8d48i@djrZDEeh$U@8sKPkhbu5T&S3jDAfpvP7tmqiis7^$'    

mysql = MySQL(app)



@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        userDetails = request.form
        uname = userDetails['username'].strip()
        pwd = userDetails['pwd']
        
        # Fetch user id, pwd from db
        cursor = mysql.connection.cursor()
        cursor.execute(f"SELECT * FROM employee_login WHERE username = '{uname}' AND password = '{pwd}'")
        data = cursor.fetchone()
        
        if data:
            cursor.execute(f"SELECT name FROM employee_login WHERE username = '{uname}' AND password = '{pwd}'")
            
            for i in cursor.fetchone(): name=i
            
            flash(f"Welcome {name}", "success")
            return redirect(url_for('admin'))
            cursor.close()
        else:
            flash("Invalid username and password")
            return redirect(url_for('login'))
    
    return render_template('login.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/table')
def table():
    return render_template('table.html')


if __name__ == "__main__":
    app.run(debug=True)