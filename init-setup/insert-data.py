import pymysql as pm

con = pm.connect(host="localhost",
                user="root",
                passwd="root",
                db="hotel_db",
                cursorclass=pm.cursors.DictCursor)

cur = con.cursor()

# Your connection code here...

with open('insert-data.sql', 'r') as sql_file:
    result_iterator = cur.execute(sql_file.read(), multi=True)
    for res in result_iterator:
        print("Running query: ", res)  # Will print out a short representation of the query
        print(f"Affected {res.rowcount} rows" )

    con.commit()  
