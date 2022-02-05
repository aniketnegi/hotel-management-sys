import pymysql as pm
import random

db = pm.connect(host="localhost", user="root", passwd="root", db="hotel_db")
cursor = db.cursor()

# Insert the categories of rooms into room_categories table
room_data = {1: 'Deluxe Room', 2: 'Single Room', 3: 'Family Room', 4: 'Twin Bed Room'}

def insert_room_categories():
    for keys, values in room_data.items():
            room_price = random.randint(500, 1200)
            cursor.execute("INSERT INTO room_categories (id, name, price) VALUES (%s, %s, %s)", (keys, values, room_price))


# Insert the random rooms into rooms table

def insert_rooms():
    for i in range(9):
        for j in range(101, 111):
            room_no = j + i*100
            category_id = random.randint(1, 4)
            cursor.execute("INSERT INTO rooms (room_no, rooms, category_id) VALUES (%s, %s, %s)", (room_no, room_data[category_id] , category_id))


if __name__ == '__main__':
    insert_room_categories()
    insert_rooms()
    db.commit()
    db.close()