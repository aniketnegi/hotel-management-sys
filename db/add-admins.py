# Python script to add entries in a database
import pymysql as pm
import shutil

db = pm.connect(host="localhost", user="root", passwd="root", db="hotel_db")
cur = db.cursor()

#=================================TODO - Adding an admin seems to mess up the id increments=============================================
#=================================TODO - Handle Entry of duplicate username and password.=============================================


def addAdmin(name: str, user: str, password: str, usr_type: str = 2):
    cur.execute(
        f"INSERT INTO users (name, username, password, type) VALUES ('{name}', '{user}', '{password}', {usr_type})"
    )
    db.commit()


def reviewAdmins(columns='*'):
    cur.execute("DESC users")
    title = tuple(x[0] for x in cur.fetchall())

    cur.execute(f"SELECT {columns} FROM users")

    print('--------------------------------------------------------')
    print("{:<8} {:<20} {:<10} {:<10} {:<10}".format(title[0], title[1],
                                                     title[2], title[3],
                                                     title[4]))
    for data in cur.fetchall():
        print("{:<8} {:<20} {:<10} {:<10} {:<10}".format(
            data[0], data[1], data[2], data[3], data[4]))
    print('--------------------------------------------------------')


#=================================TODO - Function does not seem to work (pymysql.err.OperationalError: (1054, "Unknown column 'user' in 'field list'"))=============================================
#=================================TODO - Handle Entry of duplicate username and password.=============================================


def editAdmin():
    reviewAdmins('id, name')
    command = ''

    id_to_edit = input(
        "\nEnter the id of the admin you want to edit from the above table: ")
    print("\nEnter the new details of the admin (Press Enter if no change):\n")
    new_username = input("Enter the new username: ")
    new_password = input("Enter the new password: ")

    if new_username != '' and new_password != '':
        command = f'SET username = "{new_username}" AND password = "{new_password}"'
    elif new_username != '':
        command = f'SET username = "{new_username}"'
    elif new_password != '':
        command = f'SET password = "{new_password}"'
    else:
        print("\nNo changes made to the admin!")
        return

    cur.execute(f"UPDATE users {command} WHERE id = {id_to_edit}")
    db.commit()


def delAdmin():
    reviewAdmins()

    id_to_delete = input(
        "\nEnter the id of the admin you want to delete from the above table: "
    )

    cur.execute(f"SELECT id, name FROM users WHERE id = {id_to_delete}")

    choice = input(
        "\nAre you sure you want to delete this admin?\nEnter 'y' to continue or 'n' to exit: "
    ).lower()

    if choice == 'y':
        cur.execute(f"DELETE FROM users WHERE id = {id_to_delete}")
        db.commit()
        print(
            "\nAdmin deleted successfully!\nTaking you back to the Main Menu!\n"
        )
    elif choice == 'n':
        print(
            "\nAlright, Last minute change of mind!\nTaking you back to the Main Menu!\n"
        )
    else:
        print(
            f"\nI'm sorry, I don't understand '{choice}'.\nTaking you back to the Main Menu!\n"
        )


#=================================TODO - Add general func to all final "exit this utility or return to main menu calls" that pressing Enter will take back to main  menu=============================================
def main():
    print('\n\n\n')
    columns = shutil.get_terminal_size().columns
    print('Welcome to the Admin Utility!'.center(columns))
    print('\n\n')
    state = True
    while state:
        choice_Master = input(
            "Would you like to -\n1. Add an ADMIN\n2. Review ADMINS\n3. Edit Existing ADMINS\n4. Delete and existing ADMIN\n5. Exit\n"
        )
        if choice_Master == "1":
            print(
                '\nDo you really want to go ahead and add an administrator?\nAdministrators have access to the entire system and make changes at any point.\n'
            )
            choice_addAdmin = input(
                "Enter 'y' to continue or 'n' to exit: ").lower()
            if choice_addAdmin == "y":
                print("\nEnter the details of the admin:")
                name = input("Name: ")
                user = input("Username: ")
                password = input("Password: ")
                usr_type = input("User Type (1 for admin, 2 for employee): ")

                addAdmin(name, user, password, usr_type)
                print("\nUser added successfully!\n\n")

            elif choice_addAdmin == "n":
                print(
                    "\nAlright, Last minute change of mind!\nTaking you back to the Main Menu!\n"
                )
            else:
                print(
                    f"I'm sorry, I don't understand '{choice_addAdmin}'.\nTaking you back to the Main Menu!\n"
                )

        elif choice_Master == "2":
            ask_reviewAdmin = input(
                "\nDo you really want to review all admin user data?\nThis contains all the usernames & passwords in plaintext format!\n\nEnter 'y' to continue or 'n' to exit: "
            )
            print("\n")

            if ask_reviewAdmin == 'y':
                reviewAdmins()
                action_exitCode = input(
                    "\nEnter 'y' to exit this utility or 'n' to continue to the Main Menu: "
                ).lower()
                if action_exitCode == 'y':
                    state = False
                    print(
                        "\nThank you for using this utility!\nExiting the program...\n"
                    )

            elif ask_reviewAdmin == 'n':
                print(
                    "\nAlright, Looks like you weren't in a safe environment!\nTaking you back to the Main Menu!\n"
                )

            else:
                print(
                    f"I'm sorry, I don't understand '{ask_reviewAdmin}'.\nTaking you back to the Main Menu!\n"
                )

        elif choice_Master == "3":
            editAdmin()
            action_exitCode = input(
                "\nEnter 'y' to exit this utility or 'n' to continue to the Main Menu: "
            ).lower()
            if action_exitCode == 'y':
                state = False
                print(
                    "\nThank you for using this utility!\nExiting the program...\n"
                )
            else:
                continue

        elif choice_Master == "4":
            delAdmin()
            action_exitCode = input(
                "\nEnter 'y' to exit this utility or 'n' to continue to the Main Menu: "
            ).lower()
            if action_exitCode == 'y':
                state = False
                print(
                    "\nThank you for using this utility!\nExiting the program...\n"
                )
            else:
                continue

        elif choice_Master == "5":
            state = False
            print(
                "\nThank you for using this utility!\nExiting the program...\n"
            )

        else:
            print("\nMisinput! Please try again.\n")


if __name__ == "__main__":
    main()
    cur.close()
    db.close()