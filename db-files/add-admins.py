# Python script to add entries in a database
import pymysql as pm

db = pm.connect(host="localhost", user="root", passwd="root", db="hotel_mgmt")
cur = db.cursor()

#=================================TODO - Adding an admin seems to mess up the id increments=============================================
#=================================TODO - Handle Entry of duplicate username and password.=============================================

def addAdmin(name, user, password):
    cur.execute(
        "INSERT INTO employee_login(name, username, password) VALUES('{}', '{}', '{}')"
        .format(name, user, password))
    db.commit()


def reviewAdmins(columns='*'):
    cur.execute("DESC employee_login")
    title = tuple([x[0] for x in cur.fetchall()])

    cur.execute("SELECT {} FROM employee_login".format(columns))
    print(title)
    for data in cur.fetchall():
        print(data)

#=================================TODO - Function does not seem to work (pymysql.err.OperationalError: (1054, "Unknown column 'user' in 'field list'"))=============================================
#=================================TODO - Handle Entry of duplicate username and password.=============================================

def editAdmin():
    reviewAdmins('id, name')

    id_to_edit = input("\nEnter the id of the admin you want to edit from the above table: ")
    print("\nEnter the new details of the admin (Press Enter if no change):\n")
    new_username = input("Enter the new username: ")
    new_password = input("Enter the new password: ")
    
    if new_username != '' and new_password != '':
        command = 'SET user = "{}" AND password = "{}'.format(new_username, new_password)
    elif new_username != '':
        command = 'SET user = "{}"'.format(new_username)
    elif new_password != '':
        command = 'SET password = "{}"'.format(new_password)
    else:
        print("\nNo changes made to the admin!")
        return

    cur.execute(
        "UPDATE employee_login {}".format(command))
    db.commit()


def delAdmin():
    reviewAdmins('id, name')

    id_to_delete = input("\nEnter the id of the admin you want to delete from the above table: ")
    
    cur.execute("SELECT id, name FROM employee_login WHERE id = {}".format(id_to_delete))

    choice = input("\nAre you sure you want to delete this admin?\nEnter 'y' to continue or 'n' to exit: ").lower()

    if choice == 'y':
        cur.execute(
            "DELETE FROM employee_login WHERE id = {}".format(id_to_delete))
        db.commit()
        print("\nAdmin deleted successfully!\nTaking you back to the Main Menu!\n")
    elif choice == 'n':
        print("\nAlright, Last minute change of mind!\nTaking you back to the Main Menu!\n")
    else:
        print("\nI'm sorry, I don't understand '{}'.\nTaking you back to the Main Menu!\n".format(choice))



#=================================TODO - Add general func to all final "exit this utility or return to main menu calls" that pressing Enter will take back to main  menu=============================================
def main():
    state = True
    while state:
        choice_Master = input(
            "Would you like to\n1. Add an ADMIN\n2. Review ADMINS\n3. Edit Existing ADMINS\n4. Delete and existing ADMIN\n5. Exit\n")
        if choice_Master == "1":
            print(
                'Do you really want to go ahead and add an administrator?\nAdministrators have access to the entire system and make changes at any point.\n'
            )
            choice_addAdmin = input(
                "Enter 'y' to continue or 'n' to exit: ").lower()
            if choice_addAdmin == "y":
                print("Enter the details of the admin:\n")
                name = input("Name: ")
                user = input("Username: ")
                password = input("Password: ")

                addAdmin(name, user, password)
                print("\nUser added successfully as an ADMIN!")

            else:
                if choice_addAdmin == "n":
                    print(
                        "\nAlright, Last minute change of mind!\nTaking you back to the Main Menu!\n"
                    )
                else:
                    print(
                        "I'm sorry, I don't understand '{}'.\nTaking you back to the Main Menu!\n".format(choice_addAdmin)
                    )

        elif choice_Master == "2":
            ask_reviewAdmin = input(
                "\nDo you really want to review all admin user data?\nThis contains all the usernames & passwords in plaintext format\nEnter 'y' to continue or 'n' to exit: "
            )

            if ask_reviewAdmin == 'y':
                reviewAdmins()
                action_exitCode = input(
                    "\nEnter 'y' to exit this utility or 'n' to continue to the Main Menu: "
                ).lower()
                if action_exitCode == 'y':
                    state = False
                else:
                    continue

            elif ask_reviewAdmin == 'n':
                print(
                    "\nAlright, Looks like you weren't in a safe environment!\nTaking you back to the Main Menu!\n"
                )

            else:
                print(
                    "I'm sorry, I don't understand '{}'.\nTaking you back to the Main Menu!\n".format(ask_reviewAdmin)
                )

        elif choice_Master == "3":
            editAdmin()
            action_exitCode = input(
                "\nEnter 'y' to exit this utility or 'n' to continue to the Main Menu: "
            ).lower()
            if action_exitCode == 'y':
                state = False
            else:
                continue
        
        elif choice_Master == "4":
            delAdmin()
            action_exitCode = input(
                "\nEnter 'y' to exit this utility or 'n' to continue to the Main Menu: "
            ).lower()
            if action_exitCode == 'y':
                state = False
            else:
                continue

        elif choice_Master == "5":
            state = False
            print("\nThank you for using this utility!\nExiting the program...\n")

        else:
            print("\nMisinput! Please try again.\n")


if __name__ == "__main__":
    main()
    cur.close()
    db.close()