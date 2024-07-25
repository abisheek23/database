import sqlite3

con = sqlite3.connect("sample.db")#db connection

try:
    con.execute("create table student(age int,name text,mark real)")#create table
except:
    pass

con.execute("insert into student(age,name,mark)values(25,'anu',14)") 
con.commit()   
con.execute("insert into student(age,name,mark)values(20,'athul',10)") 
con.commit()   
con.execute("insert into student(age,name,mark)values(25,'adith',16)") 
con.commit()   
con.execute("insert into student(age,name,mark)values(25,'abi',19)") 
con.commit()   

con.execute("delete from student where name='anu'")
con.commit
data=con.execute("select * from student")
print("{:<15}{:<15}{:<15}".format("age","name","mark"))
print('_'*45)
for i in data:
    print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2])) 
print()