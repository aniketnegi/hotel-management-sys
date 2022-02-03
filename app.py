'''
2. Add Room
5. View Room
8. Update Room
11. Delete Room
1. Add Customer - Done
3. Add Booking - Done
4. View Customer - Done
6. View Booking - Done
7. Update Customer - Done | Partially Done | How to put default value in the dropdown field?
9. Update Booking - Done
10. Delete Customer - Done
12. Delete Booking - Done
13. Exit - Done
'''

from flask import Flask, redirect, render_template, url_for, flash
from webforms import reservationForm, loginForm, confirmReservation, roomDetails, searchReservation, servicesForm, userServicesForm, checkoutForm
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

# Global Variables
base_charge = 1000

# Login
logged_in = False

# ============================== TODO: Add random customer_id whatever(as required only. check db to confirm the auto_increment and all that are alr there.) =====
# ============================== TODO: ADMIN DASH ================================================================================================================
# ============================== TODO: CHECK FOR DESIGN INCONSISTENCIES (The alerts sometimes pop on the full page instead of small part) ========================


def checkLoggedIn():
    global logged_in
    return bool(logged_in)


def generateRandomID():
    global cursor
    cursor.execute("SELECT COUNT(*) FROM customer")
    count = cursor.fetchone()
    count = count['COUNT(*)']
    count += 1
    return count


@app.route('/', methods=['GET', 'POST'])
def index():
    form = reservationForm()

    cursor.execute("SELECT * FROM rooms where status = 0")
    avail_rooms = cursor.fetchall()

    if len(avail_rooms) == 0:
        flash("No rooms available at the moment. Please try again later.")
        return render_template('index.html', form=form)
    else:

        if form.validate_on_submit():
            data = form.data

            if data['arrival_date'] > data['departure_date']:
                flash(
                    'Arrival date cannot be after departure date! Please try again.'
                )
                return redirect(url_for('index'))
            else:
                current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

                data['comments'] = 'NULL' if data['comments'] == '' else data[
                    'comments']  # Just a Default Value

                cursor.execute(
                    "INSERT INTO booked (name, contact_no, address, email, id_proof_type, id_proof_no, date_in, date_out, no_children, no_adults, room_preference, comments, time_booked) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (data['name'], data['phone'], data['address'],
                     data['email'], data['id_type'], data['id_number'],
                     data['arrival_date'], data['departure_date'],
                     data['no_children'], data['no_adults'],
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

                    cursor.execute(
                        f"SELECT name FROM users WHERE username = '{login_data['username']}'"
                    )

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


@app.route('/admin/dashboard', methods=['GET', 'POST'])
def admin():
    if checkLoggedIn():
        form = roomDetails()
        # Calculate the number of online bookings -
        cursor.execute("SELECT COUNT(*) FROM booked WHERE status = 0")
        online_bookings = cursor.fetchone()['COUNT(*)']

        # Calculate the number of guests -
        cursor.execute("SELECT COUNT(*) FROM checked_in")
        guests = cursor.fetchone()['COUNT(*)']

        # Calculate the number of vacant rooms -
        cursor.execute("SELECT COUNT(*) FROM rooms WHERE status = 0")
        vacant_rooms = cursor.fetchone()['COUNT(*)']

        if form.validate_on_submit() and form.submit.data:
            cursor.execute("SELECT * FROM rooms")
            rooms = cursor.fetchall()
            for i in rooms:
                i['status'] = bool(i['status'])
            return render_template('room_table.html', room_data=rooms)

        return render_template('admin.html',
                               online_bookings=online_bookings,
                               guests=guests,
                               vacant_rooms=vacant_rooms,
                               form=form)
    else:
        return redirect('unauthorized')


@app.route('/admin/unauthorized')
def unauthorized():
    return render_template('unauthorized.html')


@app.route('/admin/confirm', methods=['GET', 'POST'])
def confirm():  # sourcery skip: remove-unnecessary-else, swap-if-else-branches
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
            # Change status in booked table
            cursor.execute(
                f"UPDATE booked SET status = 1 WHERE booking_id = {id}")

            # Generate a unique id for the customer and insert into checked_in table first, followed by the check_in info.
            customer_id = generateRandomID()
            cursor.execute(
                "INSERT INTO checked_in (customer_id, booking_cid) VALUES (%s, %s)",
                (customer_id, id))
            cursor.execute(
                f"INSERT INTO checked_in(name, contact_no, address, email, id_proof_type, id_proof_no, date_in, date_out, no_children, no_adults) where customer_id = {customer_id} SELECT name, contact_no, address, email, id_proof_type, id_proof_no, date_in, date_out, no_children, no_adults FROM booked WHERE booking_id = {id}"
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
    form = reservationForm()
    cursor.execute(f"SELECT * FROM booked WHERE booking_id = {id}")
    customer_data = cursor.fetchone()

    preference_dict = {
        '1': 'Deluxe Room',
        '2': 'Single Room',
        '3': 'Family Room',
        '4': 'Twin Bed Room',
        "NULL": 'No Preference'
    }
    pref = preference_dict[customer_data['room_preference']]

    if form.validate_on_submit():
        data = form.data
        cursor.execute(
            f"UPDATE booked SET name = '{data['name']}', contact_no = '{data['phone']}', address = '{data['address']}', email = '{data['email']}', id_proof_type = '{data['id_type']}', id_proof_no = '{data['id_number']}', date_in = '{data['arrival_date']}', date_out = '{data['departure_date']}', no_children = '{data['no_children']}', no_adults = '{data['no_adults']}', room_preference = '{data['room_preference']}', comments = '{data['comments']}' WHERE booking_id = {id}"
        )
        return redirect(url_for('reservation_found', id=id))
    return render_template('edit.html',
                           customer_data=customer_data,
                           form=form,
                           pref=pref)


@app.route('/admin/bookings', methods=['GET', 'POST'])
def bookings():
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
        return redirect(url_for('bookings'))
    return render_template('bookings.html', form=form)


@app.route('/admin/details')
def details():
    cursor.execute("SELECT * FROM checked_in")
    user = cursor.fetchall()
    data = len(user) != 0
    return render_template('customer_deets.html', users=user, data=data)


@app.route('/admin/services', methods=['GET', 'POST'])
def userServices():
    form = userServicesForm()

    if form.validate_on_submit() and form.submit.data:
        data = form.data

        cursor.execute(
            f"SELECT * from checked_in where {data['search_by']}={data['search_value']}"
        )
        customer_data = cursor.fetchall()
        if len(customer_data) == 0:
            flash('No results found!')
            return redirect(url_for('userServices'))
        else:
            customer_data = customer_data[0]
            return redirect(
                url_for('services', id=customer_data['customer_id']))
    return render_template('userservices.html', form=form)


@app.route('/admin/services/<int:id>', methods=['GET', 'POST'])
def services(id):
    form = servicesForm()
    cursor.execute(f"SELECT * from checked_in where customer_id={id}")
    customer_data = cursor.fetchone()

    if form.validate_on_submit() and form.submit.data:
        data = form.data
        current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO services(service_id, customer_id, service_date, comments, bill) VALUES (%s, %s, %s, %s, %s)",
            (data['service_id'], id, current_time, data['comments'],
             data['price']))
        db.commit()
        return redirect(url_for('services', id=id))
    return render_template('services.html', user=customer_data, form=form)


@app.route('/admin/checkout', methods=['GET', 'POST'])
def checkout():
    form = checkoutForm()
    if form.validate_on_submit() and form.submit.data:
        data = form.data
        cursor.execute(
            f"SELECT * from checked_in where customer_id={data['cust_id']}")
        customer_data = cursor.fetchone()
        print(customer_data['date_out'])
        current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        if customer_data != None:
            try:
                cursor.execute(
                    "INSERT INTO checkout(customer_id, checkout_time) VALUES (%s, %s)",
                    (data['cust_id'], current_time))
                
                cursor.execute('UPDATE checked_in SET date_out = %s WHERE customer_id = %s', (current_time, data['cust_id']))
            except Exception as e:
                flash(
                    'Customer has already checked out!\nPlease recheck the information.'
                )
                return redirect(url_for('checkout'))
            db.commit()
        else:
            flash('Customer not found!')
            return redirect(url_for('checkout'))

        # ===== DO BILL CALC. ========

        bill = []

        # Calculate the difference between two dates
        def date_diff(date1, date2):
            date1 = datetime.strptime(str(date1).split()[0], "%Y-%m-%d")
            date2 = datetime.strptime(str(date2).split()[0], "%Y-%m-%d")
            return abs((date2 - date1).days)

        date1 = customer_data['date_in']
        #date2 = customer_data['date_out']
        date2 = current_time
        days = date_diff(date1, date2) + 1

        # Calculate the bill for each service
        global base_charge
        base_charges_dict = ({
            'name': 'Base Charges',
            'amount': days * base_charge
        })
        bill += [base_charges_dict]

        cursor.execute(
            f"SELECT * from services where customer_id={data['cust_id']}")
        user_avail_services = cursor.fetchall()
        print(user_avail_services, 'user_avail_services')

        cursor.execute("SELECT * from services_categories")
        id_services_db = cursor.fetchall()
        print(id_services_db, 'id_services_db')

        if len(user_avail_services) != 0:
            for service in user_avail_services:
                for service_db_dict in id_services_db:
                    if int(service_db_dict['id']) == int(
                            service['service_id']):
                        temp_price_dict = ({
                            'name': service_db_dict['name'],
                            'amount': int(service['bill'])
                        })
                        bill += [temp_price_dict]

        else:
            bill += ({'name': 'No Services', 'amount': 0})

        # Calculate the total bill
        total_bill = 0
        for i in bill:
            total_bill += i['amount']

        return render_template('checkout.html',
                               customer_data=customer_data,
                               status=True,
                               bill=bill,
                               total=total_bill)
    return render_template('checkout.html', form=form)


@app.route('/admin/logout')
def logout():
    global logged_in
    logged_in = False
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)