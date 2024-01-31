import mysql.connector as myc
from config import database_config
from datetime import datetime
import pandas as pd 

server = database_config['server']
port = database_config['port']
database = database_config['database']
username = database_config['username']
password = database_config['password']

try: 

    connection = myc.connect(
    host=server,
    port=port,
    database=database,
    user=username,
    password=password
    )
    if connection.is_connected():
        cursor =  connection.cursor()
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        

except myc.Error as e:
    print("Error while connecting to MySQL", e)

# Menu list 
choice = None
while choice != "5":
    print()
    print ("1. display the user table")
    print ("2. add the user to the table")
    print ("3. update the user information")
    print ("4. delet the user")
    print ("5. Quit")

    choice = input("> ")
    
    if choice == "1" :
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        if rows:
            custom_column_names = ['student_id','first name','last name','email','major_id']
            pf = pd.DataFrame(rows)
            pf.columns = custom_column_names
            print (pf.to_string(index=False))
        else:
            print("There is no student data")

    elif choice == "2" : 
        last_name = input("what is your last name: ")
        first_name = input("What is your first name: ")
        email = input("What is your email?: ")
        cursor.execute(f"INSERT INTO student (student_id, firstName, lastName, email, major_id) VALUES (DEFAULT, '{last_name}', '{first_name}','{email}', 1);")
        connection.commit()
        print ('add actor sucessfully')
    
    elif choice == "3" : 
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        if rows:
            custom_column_names = ['student_id','first name','last name','email','major_id']
            pf = pd.DataFrame(rows)
            pf.columns = custom_column_names
            print (pf.to_string(index=False))
        else:
            print("There is no student data")

        print()

        student_id = input("Which student ID whats to update: ")
        last_name = input("Student's new last name: ")
        first_name = input("Student's new first name: ")
        email = input("Student's new email: ")
        cursor.execute(f"UPDATE student SET lastName = '{last_name}', firstName = '{first_name}', email = '{email}' WHERE student_id = {student_id};")
        connection.commit()
        print (' update actor sucessfully')

    elif choice == "4" : 
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        if rows:
            custom_column_names = ['student_id','first name','last name','email','major_id']
            pf = pd.DataFrame(rows)
            pf.columns = custom_column_names
            print (pf.to_string(index=False))
        else:
            print("There is no student data")

        print()

        delete_id = input("Which ID you want to delete: ")
        cursor.execute(f"DELETE FROM student WHERE student_id = {delete_id};")
        connection.commit()
        print ('delete sucessfuly')