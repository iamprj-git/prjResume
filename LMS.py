import datetime
from logging import exception


class LMS:
    def __init__(self,book_lists,l_name):
        self.book_lists="books.txt"
        self.l_name=l_name
        self.books_dict={}
        ID=100
        with open(self.book_lists) as st:
            content=st.readlines()
        for lines in content:
            self.books_dict.update({str(ID):{"books_title":lines.replace("\n",""),
            "lender_name":"","issue_date":"","status":"Available"}})
            ID+=1
        self.lines=lines
    def display(self):
        print("--------------------------Lists of books---------------------------")
        print("Books Id","\t","Books Title")  
        print("-------------------------------------------------------------------")     
        for key,value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"),"\t\t","[",value.get("status"),"]")
    
    def issued_books(self):
        books_id=input("Enter the ID of the books:")
        current_date= datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["status"]!="Available":
                 print("This book is issued to {} on {}".format(self.books_dict[books_id]["lender_name"],self.books_dict[books_id]["issue_date"]))
                 return self.issued_books()
            elif self.books_dict[books_id]["status"]=="Available":
                name= input("What is your name? ")
                self.books_dict[books_id]["lender_name"]=name
                self.books_dict[books_id]["issue_date"]=current_date
                self.books_dict[books_id]["status"]="Already issued"
                print("Books issued sucessfully!!!!!")
        else:
            print("Not found such a directory books!!")  
            return self.issued_books   
    
    def add_books(self):
        new_books=input("Enter the titles of the book:")
        if len(new_books)>25:
            print("the title of the books is so long:")
        else:
            with open(self.book_lists,"a") as t:
                t.writelines("{}\n".format(new_books))
                self.books_dict.update({str(int(max(self.books_dict))+1):{"books_title":new_books , "lender_name":" " , "issue_date":" " , "status":"Available" }})
            print("Books was added sucessfully!!")

    def return_books(self):
        books_id=input("Enter the books ID=")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["ststus"]=="Available":
                print("This book is already in this library..so,please check your ID!!")
            elif self.books_dict[books_id]["status"]!="Available":
                self.books_dict[books_id]["lender_name"]=""
                self.books_dict[books_id]["issue_date"]=" "
                self.books_dict[books_id]["status"]="Available"
try:
    l=LMS("books.txt","python library name")
    press_key_list={"D":"dispaly","I":"Issued books","A":"Add Books","R":"return books","Q":"Quit"}
    key_press=False
    while not(key_press=="q"):
        print(f"------------------welcome to {l.l_name}------------------------------")
        print("If you want to skip any criteria please tap [G]")
        for key,value in press_key_list.items():
            print("press",key,"to",value)
        key_press=input("Press key:").lower()
        if key_press =="d":
            print("-----you are in Display directory-------")
            print("\n")
            l.display()
        elif key_press =="i":
            print("-----you are in Issued directory-------")
            print("\n")
            l.issued_books()
        elif key_press =="a":
            print("-----you are in Add directory-------")
            print("\n")
            l.add_books()
        elif key_press =="r":
            print("-----you are in Return directory-------")
            print("\n")
            l.return_books()
        elif key_press =="q":
            break
        else:
            continue
except exception as e:
    print("something went wrong!!")
