import pymysql as pm

con = pm.connect(host="localhost",
                user="root",
                passwd="root",
                db="hotel_db",
                cursorclass=pm.cursors.DictCursor)

cursor = con.cursor()

# Your connection code here...

with open("insert-data.sql", "r") as f:
    commands = [x.strip("\n") for x in f.readlines() if not x.startswith("--") and x!="\n"]
    
    run = ""
    for command in commands:
        run += command
        if run[-1] == ";":
            cursor.execute(run)
            con.commit()
            print("Executed:", run)
            run = "" 

print("\n\nData inserted successfully!\n\n") 
