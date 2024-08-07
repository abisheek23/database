import  mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="demo",
    password="demo.2023",
    database="mydatabase"
)
"""adding valuse"""
mycursor =mydb.cursor()
# mycursor.execute("create database mydatabase")
# mycursor.execute("create table student (name text,age int ,mark int )")
# mycursor.execute("insert into student values('anu',20,50),('arun',23,40),('sree',18,55)")
# mydb.commit()
"""adding valuse entering"""
# name=input("enter the name")
# age=int(input("enter the age"))
# mark=int(input("enter the mark"))
# mycursor.execute("insert into student values (%s,%s,%s)",(name,age,mark))
# mydb.commit()
"""to select data"""
# mycursor.execute("select * from student")
# data=mycursor.fetchall()
# for i in data:
#     print(i)

# mycursor.execute("select * from student where name='anu'")
# data=mycursor.fetchall()
# for i in data:
#     print(i)

# mycursor.execute("select * from student where name like'__u%'")
# data=mycursor.fetchall()
# for i in data:
#     print(i)

"""update 1"""
# mycursor.execute("update student set mark=58 where name='anu'")
# mydb.commit()

"""update2"""
# name=input("enter the name")
# mark=int(input("enter the new mark"))
# mycursor.execute("update student set mark=%s where name=%s",(mark,name))
# mydb.commit()
"""delete1"""
# mycursor.execute("delete from student where name='anu'")
# mydb.commit()
"""delete2"""
# name=input("enter the name :")
# mycursor.execute("delete from student where name=%s",(name,))
# mydb.commit()


""""""
# mycursor.execute("select count(age) from student group by mark")
# data=mycursor.fetchall()
# for i in data:
#     print(i)

# mycursor.execute("select count(age) from student order by name desc")
# data=mycursor.fetchall()
# for i in data:

# mycursor.execute("insert into student values('anu',20,50),('arun',23,40),('sree',18,55)")
# mydb.commit()

"""new table"""
# mycursor.execute("create table details (name text,place text ,branch text )")
# mycursor.execute("insert into details values('anu','ekm','vyttil'),('arun','ekm','pal')")
# mydb.commit()

# data=conn.execute("select std.name,std.age,std.place,mark.mark1,mark.mark2 from std join mark on std.name=mark.name")
# for i in data :
#     print(i)
mycursor.execute("select student.name,student.age,student.mark,details.place,details.branch from student left join details on student.name=details.name")
data=mycursor.fetchall()
for i in data :
    print(i)
