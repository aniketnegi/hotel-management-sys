<<<<<<< Updated upstream
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
=======
'''
1. Add Customer - Done
2. Add Room
3. Add Booking - Done
4. View Customer - Done
5. View Room
6. View Booking - Done
7. Update Customer
8. Update Room
9. Update Booking
10. Delete Customer
11. Delete Room
12. Delete Booking
13. Exit
'''
from flask import Flask, redirect, render_template, url_for, flash
from webforms import reservationForm, loginForm, confirmReservation, searchReservation
import pymysql as pm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

#Connect to the database
db = pm.connect(host="localhost",
                user="root",
                passwd="root",
                db="hotel_db",
                cursorclass=pm.cursors.DictCursor)
cursor = db.cursor()

# in
logged_in = False


def checkLoggedIn():
    global logged_in
    return bool(logged_in)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = reservationForm()

    if form.validate_on_submit():
        data = form.data
        current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        data['comments'] = 'NULL' if data['comments'] == '' else data[
            'comments']  # Just a Default Value

        cursor.execute(
            "INSERT INTO booked (name, contact_no, address, email, id_proof_type, id_proof_no, date_in, date_out, no_children, no_adults, room_preference, comments, time_booked) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (data['name'], data['phone'], data['address'], data['email'],
             data['id_type'], data['id_number'], data['arrival_date'],
             data['departure_date'], data['no_children'], data['no_adults'],
             data['room_preference'], data['comments'], current_time))

        db.commit()

        flash(f'Reservation for {form.name.data} has been made!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


@app.route('/admin', methods=['GET', 'POST'])
def login():
    form = loginForm()

    global logged_in

    if form.validate_on_submit():
        login_data = form.data

        username = cursor.execute(
            f'SELECT username FROM users WHERE username = "{login_data["username"]}"'
        )

        if bool(username):
            username = cursor.fetchone()['username']
            print(username)
            password = cursor.execute(
                f'SELECT password FROM users WHERE username = "{login_data["username"]}"'
            )
            if bool(password):
                password = cursor.fetchone()['password']
                print(password)
                if login_data["password"] == password:
                    logged_in = True
                    return redirect(url_for('admin'))
                else:

                    flash('Incorrect password!')
                    return redirect(url_for('login'))
            else:
                flash('Invalid username or password!')
                return redirect(url_for('login'))
        else:
            flash('Incorrect username!')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)


# =================================Logged in Logic is working!========================


@app.route('/admin/dashboard')
def admin():
    if checkLoggedIn():
        return render_template('admin.html')
    else:
        return redirect('unauthorized')


@app.route('/unauthorized')
def unauthorized():
    return render_template('unauthorized.html')


# =================================Separate These Functions========================
@app.route('/admin/confirm', methods=['GET', 'POST'])
def confirm():
    form = searchReservation()

    if form.validate_on_submit():

        search_data = form.data
        cursor.execute(
            f"SELECT * FROM booked WHERE {search_data['search_by']} = '{search_data['search_value']}'"
        )
        customer_data = cursor.fetchall()

        if form.submit.data:
            if len(customer_data) == 0:
                flash('No results found!')
                return redirect(url_for('confirm'))
            else:
                return redirect(
                    url_for('reservation_found',
                            id=customer_data[0]['booking_id']))
    return render_template('confirm.html', form=form)


# ============================================================


@app.route('/admin/found/<int:id>', methods=['GET', 'POST'])
def reservation_found(id):
    form = confirmReservation()

    cursor.execute(f"SELECT * FROM booked WHERE booking_id = {id}")
    customer_data = cursor.fetchone()

    if form.validate_on_submit():
        if form.delete.data:
            cursor.execute(f"DELETE FROM booked WHERE booking_id = {id}")
            db.commit()
            flash('Reservation has been deleted!')
            return redirect(url_for('confirm'))
        elif form.edit.data:
            return redirect(url_for('edit_reservation', id=id))
        elif form.confirm.data:
            cursor.execute(
                f"UPDATE booked SET status = 1 WHERE booking_id = {id}")
            cursor.execute(
                f"INSERT INTO checked_in(name, contact_no, address, email, id_proof_type, id_proof_no, date_in, date_out, no_children, no_adults) SELECT name, contact_no, address, email, id_proof_type, id_proof_no, date_in, date_out, no_children, no_adults FROM booked WHERE booking_id = {id}"
            )
            # ===== Add booking id etc. ========
            db.commit()
            flash('Reservation has been confirmed!')
            return redirect(url_for('confirm'))
    return render_template('reservation_found.html',
                           customer_data=customer_data,
                           form=form)


@app.route('/admin/edit/<int:id>', methods=['GET', 'POST'])
def edit_reservation(id):
    return render_template('edit.html')


# ============================================================


@app.route('/admin/bookings')
def bookings():
    form = reservationForm()

    if form.validate_on_submit():
        data = form.data
        current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        data['comments'] = 'NULL' if data['comments'] == '' else data[
            'comments']  # Just a Default Value

        cursor.execute(
            "INSERT INTO checked_in (name, contact_no, address, email, id_proof_type, id_proof_no, date_in, date_out, no_children, no_adults, room_preference, comments, time_booked) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (data['name'], data['phone'], data['address'], data['email'],
             data['id_type'], data['id_number'], data['arrival_date'],
             data['departure_date'], data['no_children'], data['no_adults'],
             data['room_preference'], data['comments'], current_time))

        db.commit()

        flash(f'Reservation for {form.name.data} has been made!')
        return redirect(url_for('bookings'))
    return render_template('bookings.html', form=form)


@app.route('/admin/details')
def details():
    cursor.execute("SELECT * FROM checked_in")
    user = cursor.fetchall()
    data = len(user) != 0
    return render_template('customer_deets.html', users=user, data=data)


@app.route('/admin/services')
def services():
    return render_template('services.html')


@app.route('/admin/checkout')
def checkout():
    return render_template('checkout.html')


@app.route('/admin/logout')
def logout():
    global logged_in
    logged_in = False
    return redirect(url_for('login'))
>>>>>>> Stashed changes


if __name__ == "__main__":
    app.run(debug=True)