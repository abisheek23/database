import sqlite3

con = sqlite3.connect("sample.db")#db connection

try:
    con.execute("create table student(age int,name text,mark real)")#create table
except:
    pass

# con.execute("update student set name='m....' where name='anu'")
# con.commit
# name=str(input("enter ur name:"))
# new=str(input("new name:"))
# age=int(input("enter new age"))
# con.execute("update student set name=? where name=?age=?",(new,name,))
# con.execute("update student set age")
# con.commit
# data=con.execute("select * from student")
# print("{:<15}{:<15}{:<15}".format("age","name","mark"))
# print('_'*45)
# for i in data:
#     print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2])) 
# print()
# import sqlite3

# # Connect to the SQLite database
# con = sqlite3.connect("sample.db")

# # Create a table if it doesn't exist
# try:
#     con.execute("CREATE TABLE IF NOT EXISTS student (age INT, name TEXT, mark REAL)")
# except sqlite3.Error as e:
#     print(f"An error occurred: {e}")

# # Get user input for updating a student's name and age
# name = input("Enter the current name: ")
# new_name = input("Enter the new name: ")
# new_age = int(input("Enter the new age: "))

# # Update the student's name and age in the table
# try:
#     con.execute("UPDATE student SET name=?, age=? WHERE name=?", (new_name, new_age, name))
#     con.commit()
#     print("Record updated successfully.")
# except sqlite3.Error as e:
#     print(f"An error occurred: {e}")

# # Retrieve and display all records from the student table
# try:
#     data = con.execute("SELECT * FROM student")
#     print("{:<15}{:<15}{:<15}".format("Age", "Name", "Mark"))
#     print('_' * 45)
#     for row in data:
#         print("{:<15}{:<15}{:<15}".format(row[0], row[1], row[2]))
# except sqlite3.Error as e:
#     print(f"An error occurred: {e}")

# # Close the connection to the database
# con.close()
# data=con.execute("select * from student where name like'_n%'")
# print('age','name','mark')
# for i in data :
#     print(i[0],i[1],i[2])
# data=con.execute("select * from student order by name desc")

data=con.execute("select name,max(mark) from student group by name ")
print('age','name','mark')
for i in data :
    print(i) 