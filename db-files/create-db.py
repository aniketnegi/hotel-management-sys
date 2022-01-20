import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root")

cursor = db.cursor(dictionary=True)

with open('db-init.sql', 'r') as sql_file:
    result_iterator = cursor.execute(sql_file.read(), multi=True)
    for res in result_iterator:
        print("Running query: ", res)  # Prints the query that was executed - for debugging
        print(f"Affected {res.rowcount} rows" )

    db.commit()  