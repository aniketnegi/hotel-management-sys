import pymysql as pm

con = pm.connect(host="localhost",
                user="root",
                passwd="root",
                cursorclass=pm.cursors.DictCursor)

cursor = con.cursor()

commands = []

with open("create-database.sql", "r") as f:
    commands = [x.strip("\n") for x in f.readlines() if not x.startswith("--") and x!="\n"]
    
    run = ""
    for command in commands:
        run += command
        if run[-1] == ";":
            cursor.execute(run)
            con.commit()
            print("Executed:", run)
            print("\n")
            run = ""


print("\n\nDatabase created successfully!\n\n")