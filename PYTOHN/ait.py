# import sqlite3

# try:
    
#     connection = sqlite3.connect('school.db')
#     cursor = connection.cursor()

#     print("Connected to the SQLite database successfully!")

# except sqlite3.Error as e:
#     print(f"Error connecting to the SQLite database: {e}")

# finally:

#     if connection:
#         connection.close()


# import sqlite3  


# conn = sqlite3.connect('school.db')  


# cursor = conn.cursor() 
# cursor.execute('''  
#     CREATE TABLE IF NOT EXISTS students (  
#         id INTEGER PRIMARY KEY,  
#         name TEXT,  
#         age INTEGER,  
#         grade REAL  
#     )  
# ''')  

# conn.commit()  
# conn.close()  

# print("Table 'students' created successfully (if it didn't already exist).")

# (id,' name, age, gpa')
# (1, 'Alice', 20, 3.8),
# (2, 'Bob', 21, 3.5),
# (3, 'Charlie', 22, 3.9)



# import sqlite3

# # Connect to your database (replace 'your_database.db' with your database file)
# conn = sqlite3.connect('your_database.db')
# cursor = conn.cursor()

# # Execute the query
# cursor.execute("SELECT * FROM students")

# # Fetch all records
# records = cursor.fetchall()

# # Print the results in a readable format
# print(f"{'ID':<5} {'Name':<10} {'Age':<5} {'GPA':<5}")
# print("-" * 25)
# for record in records:
#     print(f"{record[0]:<5} {record[1]:<10} {record[2]:<5} {record[3]:<5}")

# # Close the connection
# conn.close()

# class Animal:
#     def _init_(self, name, species, sound):
#         self.name = name        
#         self.species = species  
#         self.sound = sound      

#     def make_sound(self):
#         return f'{self.name} says {self.sound}.'
#     def info(self):
#         return f'{self.name} is a {self.species}.'
    
# dog = Animal("Buddy", "dog", "woof")
# cat = Animal("Whiskers", "cat", "meow")
# cow = Animal("MYMY", "cow", "myyy")
# monkey= Animal("MOMO", "monkey", "aaaaa")

# print(dog.info())           
# print(dog.make_sound())    

# print(cat.info())           
# print(cat.make_sound())      

# print(cow.info())           
# print(cow.make_sound())  

# print(monkey.info())           
# print(monkey.make_sound())