
import sqlite3






try:
 connn = sqlite3.connect('Project\SQLite_Python.db')
 sqlite_create_table_query = '''CREATE TABLE SqliteDb_developers (
	                                name TEXT NOT NULL,
                                    password TEXT NOT NULL)'''
	
 cursor = connn.cursor()
 print("Successfully Connected to SQLite")
 cursor.execute(sqlite_create_table_query)
 connn.commit()
 print("SQLite table created")
	
 
	
except sqlite3.Error as error:
 print("Error while creating a sqlite table", error)
finally:
	 if connn:
	  False



print("Welcome to Cyber Cafe! Hope you have a great time!")


def login_account():
    name = input("Enter your username:")
    password = input("Enter your password:")

   
    data = cursor.execute('SELECT * FROM SqliteDb_developers')
    output = data.fetchall()
    print(output, sep='\n')
    length = len(output)
    
    for i in range(length):
        if name == output[i][0] and password == output[i][1]:
            print("Access granted.")
            
            break
        
    else:
        print("Access denied.")
        

    


def register_account():
    print("Welcome to CyberCafe, sign up now")
    name = input("Enter a username (make sure it is between 5-15 letters):")

    if len(name) < 5:
        print("Too small")
        register_account()
    elif len(name) > 15:
        print("Too big")
        register_account()
    
    password = input("Enter a password (make sure it is more than 6:")
    if len(password) < 6:
        print("Too small")
        register_account()

    username_sql_query = f'''insert into SqliteDb_developers(name,password) values("{name}","{password}")'''
    cursor.execute(username_sql_query)
    login = input("Would you like to login now? (y/n): ")
    if login == 'y' or "Y":
        login_account()
    
    elif login == 'n' or "N":
        exit()


    

    

accounts = input("Do you have an account? (y/n): ")

if accounts == "y" or accounts == "Y":
    login_account()

elif accounts == "n" or accounts == "N":
    register_account()

else:
    print("Error, please choose one of the options")


