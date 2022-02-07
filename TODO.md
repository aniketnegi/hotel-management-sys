Random data:
https://mockaroo.com/

### Not Working
for i in bill:
                    for j in range(1, len(bill)):
                        if i['name'] == bill[j]['name']:
                            i['amount'] += bill[j]['amount']
                            bill.pop(j)

1. Billing Date of checkout, date of checkin - done
2. Bill Number - done
3. Add a room manually if not available.
4. check updation of rooms/checkin_stat etc. - done

# Done

(04-02-2022)

1. changed table names in add-admins.py
2. added auto_increment to `hotel_db`.`users`.`id`

Working logic for confirm reservation - done
Both the admin and user booking forms need room preference added to db - done
add random room based on pref on check_in -> In case room not available, notify and give option for custom adding. - done
