import csv
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        userDetails = request.form
        uname = userDetails['username'].strip()
        pwd = userDetails['pwd']
        
        with open('data.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([uname, pwd])
            
        with open('creds.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if uname == row[0] and pwd == row[1]:
                    return redirect('/admin')
                else:
                    return render_template('login.html', msg="Invalid username or password")
        
        
    return render_template('login.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/table')
def table():
    return render_template('table.html')


if __name__ == "__main__":
    app.run(debug=True)