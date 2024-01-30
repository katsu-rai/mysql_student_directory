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

    cnxn = myc.connect(
    host=server,
    port=port,
    database=database,
    user=username,
    password=password
    )
    if cnxn.is_connected():
        cursor =  cnxn.cursor()
        db_Info = cnxn.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        

except myc.Error as e:
    print("Error while connecting to MySQL", e)




# Menu list 
choice = None
while choice != "5":
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
            custom_column_names = ['ID','First name','Last name','email','major_id']
            pf = pd.DataFrame(rows)
            pf.columns = custom_column_names
            print (pf)
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS `test`.`test` (`ID` INT AUTO_INCREMENT,`First_name` VARCHAR(45) NOT NULL,`Last_name` VARCHAR(45) NOT NULL,`Birthday` DATE NOT NULL,PRIMARY KEY (`ID`));")
            print("no data ")
    elif choice == "2" : 
        last_name = input("what is your last name: ")
        first_name = input("What is your first name: ")
        birthday = input("When is your birthday yyyy-mm-dd: ")
        cursor.execute(f"INSERT INTO test (Last_name, First_name, Birthday) VALUES ('{last_name}', '{first_name}','{birthday}');")
        cnxn.commit()
        print ('add actor sucessfully')
    
    elif choice == "3" : 
        user_id = input("Which user ID whats to update: ")
        last_name = input("User new last name: ")
        first_name = input("User new first name: ")
        birthday = input("User new birthday: ")
        cursor.execute(f"UPDATE test SET Last_name = '{last_name}', First_name = '{first_name}', Birthday = '{birthday}' WHERE ID = {user_id};")
        cnxn.commit()
        print (' update actor sucessfully')
    elif choice == "4" : 
        delete_id = input("Which ID you want to delete: ")
        cursor.execute(f"DELETE FROM `test`.`test` WHERE `ID` = {delete_id};")
        cnxn.commit()
        print ('delete sucessfuly')