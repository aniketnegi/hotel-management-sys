# To-do for hotel-management-system

# file: add-admins.py

### func -> addAdmin
-  Adding an admin seems to mess up the id increments
-  Handle Entry of duplicate username and password.

### func -> editAdmin
- Function does not seem to work for any input (pymysql.err.OperationalError: (1054, "Unknown column 'user' in 'field list'"))
- Handle Entry of duplicate username and password.

### func -> main
- Add general func to all final "exit this utility or return to main menu calls" that pressing Enter will take back to main  menu.

---

# General Tasks:
- Link to notion db - https://aniketnegi.notion.site/HILBERT-HOTEL-7ad46e5797b94f18976db2f968221901

---

- [ ]  A webGUI to serve as the interface for employees to handle inputting/searching data related to the customer.
    - [ ]  A Login Page.
    - [ ]  A page to search for customer data *with filters.* It should also have a function to calculate the bill.
    - [ ]  A page to input the Customer Service Data -
        - [ ]  Hotel Restaurant.
        - [ ]  Room Service.
        - [ ]  Hotel Laundry.
        - [ ]  Hotel Chauffeur Service.
    - [ ]  A page for checkout { can also implement a function to print the bill }. { *The room keys have a QR code also that detects the customer deets when they hand it over to the receptionist when checking out. }*