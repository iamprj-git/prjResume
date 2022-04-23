
from sqlite3 import Cursor
import mysql.connector

class db():
    def __init__(self):
        self.s=mysql.connector.connect(
                   host='localhost',
                    port='3306',
                    user='prajwal',
                    password='prajwal@2580',
                    database='prajwal'
        )
        query=('create table if not exists user (user_id int primary key, user_name varchar(20),phone_number varchar(10))')
        l=self.s.cursor()
        l.execute(query)
        print("created")
    def insert_user(self):
        userid=input("Enter the user id : ")
        username=input("Enter the Username: ")
        phone=input("Enter the phone: ")
        query="insert into user(user_id,user_name,phone_number)values({},'{}','{}')".format(userid,username,phone)
        l=self.s.cursor()
        l.execute(query)
        self.s.commit()
        print("user insert sucessfully!!")
    def fetch(self):
        x=input("Enter the id to fetch the data:")
        query="select * from user where user_id = {}".format(x)
        l=self.s.cursor()
        l.execute(query)
        for row in l:
            print("user id: ",row[0])
            print("user name: ",row[1])
            print("user phone: ",row[2])  
p= db()
#for i in range(0,10):
    #p.insert_user(i+1,"Prajwal{}".format(i+1),"981697142{}".format(i+1))
my={"fetching_data":'f',"Inserting data":'i',"quit":'q'}
key_press=False
while not(key_press=="q"):
    for key,values in my.items():
        print("press",key,"to","value")
    key_press=input("Press keys(F,I,Q)").lower()
    if key_press=='f':
        print("you are in fetching ")
        print("\n")
        p.fetch()
    elif key_press=='i':
        print("you are in Inserting ")
        print("\n")
        p.insert_user()
    elif key_press=='q':
        break
    else:
        print("something went wrong!")