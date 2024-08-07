import sqlite3

conn=sqlite3.connect("student.db")
# conn.execute("create table std (name text ,age int ,place text)")
# conn.execute("insert into std values('arun' ,20,'ekm'),('akhil',25,'ekm'),('anu',22,'ekm')")
# conn.commit()
# conn.execute("insert into std values('sree' ,24,'ekm')")
# conn.commit()
"""manuel update"""
# conn.execute("update std set place='thr' where name='arun'")
# conn.commit()
"""update """
# name=input("enter the name")
# place=input ("enter the place")
# conn.execute("update std  set place=? where name=?",(place,name))
# conn.commit()

"""delete"""
"""1"""
conn.execute("delete from std where name='akhil'")
conn.commit()
# """2"""
# name=input("enter the name")
# conn.execute("delete from std where name=?",(name,))
# # conn.commit()
# data=conn.execute("select * from std where name like '_n%'")
# for i in data:
#     print(i)
""" order"""

# data=conn.execute("select * from std order by name")
# for i in data:
#     print(i)

"""group by"""
# sum 
# max
# min
# avg
# count
# sum
# data=conn.execute("select max(age)from std group by name")

# for i in data:
#     print(i)

# conn.execute("create table mark (name text , mark1 int,mark2 int)")
# conn.execute("insert into mark values('akhil',50,40),('anu',50,35),('arjun',30,50)")
# conn.commit()
"""joinin two tables"""
# data=conn.execute("select std.name,std.age,std.place,mark.mark1,mark.mark2 from std join mark on std.name=mark.name")
# for i in data :
#     print(i)
"""left join"""

data=conn.execute("select std.name,std.age,std.place,mark.mark1,mark.mark2 from mark left join std on std.name=mark.name")
for i in data :
    print(i)
