from sqlite3 import Cursor

import mysql.connector
class db():
    def __init__(self):
        self.s=mysql.connector.connect(
             host='localhost',
             port='3306',
             user='root',
             password=None,
             database='school'
         )
        query=("create table if not exists student_data(stuent_id int primary key, student_name varchar(20), parents_phone_number varchar(10), Total_fee int, paid_fee int,due_fee int)")
        l=self.s.cursor()
        l.execute(query)
        print("sucessfully created!")
    def insert(self):
        std_id=input("Enter the student id:")
        name=input("Enter the student name:")
        number=input("enter the phone number of parents:")
        total=int(input("Enter the total fee:"))
        paid=int(input("Enter the paid fee:"))
        due=int(total-paid)
        query="insert into student_data(stuent_id,student_name, parents_phone_number,Total_fee,paid_fee,due_fee)values({},'{}','{}',{},{},{})".format(std_id,name,number,total,paid,str(due))
        l=self.s.cursor()
        l.execute(query)
        self.s.commit()
        print("sucessfully inserted!")
    
mydb=db()
mydb.insert()


        


