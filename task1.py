import sqlite3

detail = sqlite3.connect("sample.db")#db detailnection

try:
    detail.execute("create table student_detail(name text,place text ,ph_no int,address text)")#create table
except:
    pass   
# detail.execute("insert into student_detail(name,place,ph_no,address)values('athul','ernakulam',1236547899,'qwert')") 
# detail.commit()   
# detail.execute("insert into student_detail(name,place,ph_no,address)values('adith','kottaym',9874563210,'asdf')") 
# detail.commit()   
# detail.execute("insert into student_detail(name,place,ph_no,address)values('abi','thrishur',6547891230,'zxcvbn')") 
# detail.commit() 
# detail.execute("delete from student_detail where name='athul'") 
# detail.commit()

data=detail.execute("select student.name,student.age,student.mark,student_detail.place,student_detail.ph_no,student_detail.address from student cross join student_detail on student.name=student_detail.name") 
for i in data:
    print(i)
