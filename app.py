# Importing the libraries
from flask import Flask, flash, render_template, redirect  #Flask is the framework
from forms import loginForm  #Importing forms from forms.py made using wtforms
import pymysql as pm  #Importing pymysql

app = Flask(__name__)
# Configure the database
app.config['SECRET_KEY'] = 'mysecretkey'
db = pm.connect(host='localhost', user='root', passwd='root', db='hotel_mgmt')
cursor = db.cursor()


# Admin route 
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = loginForm()
    status = False
    if form.validate_on_submit(): #form validation

        username = cursor.execute(
            'SELECT username FROM employee_login WHERE username = "{}"'.format(
                form.username.data))
        

        if username:
            username = ''.join(
            cursor.fetchone())  #Convert the fetched tuple into str
            password = form.password.data
            user_pass = cursor.execute(
                'SELECT password FROM employee_login WHERE username = "{}"'.
                format(form.username.data))
            user_pass = ''.join(cursor.fetchone())

            if password == user_pass:
                status = True
                name = cursor.execute(
                    "SELECT name FROM employee_login WHERE username = '{}'".
                    format(form.username.data))
                name = ''.join(cursor.fetchone())
                return render_template('admin.html', name=name, status=status, form=form)
            else:
                flash('Invalid Password!')
                return render_template('admin.html', status=status, form=form)
        else:
            flash('Invalid password or username')
            return render_template('admin.html', form=form)
    return render_template('admin.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)