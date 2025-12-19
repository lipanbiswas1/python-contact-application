import json
import os
import csv

file="contact.json"

def createcontact():
    if not os.path.exists(file):
        with open(file,"w") as a:
            json.dump([],a) 
    print("contact from enter 0 to exit")

    while True :
        name=input("Enter name and 0 to exit : ")
        if name == "0":
            print("exit")
            break
        else:
            age=int(input("enter age : "))
            subject=input("enter subject : ")
            mark=float(input("enter mark : "))
            contect={"name": name, "age": age , "subject": subject , "mark" : mark}
            with open (file,"r") as r:
                data = json.load(r)
            data.append(contect)
            with open (file,"w") as w:
                json.dump(data,w,indent=4)
            print("save successfully")

def view_contact():
    with open (file,"r") as t:
        data=json.load(t)
    if not data :
        print("no contact found")
        return
    else:
        print("====contact list====")
        for i,c in enumerate(data,start=1):
            print(f"{i}. name : {c['name']}, \n age : {c['age']} \n subject : {c['subject']} \n mark {c['mark']}")

def searchContact (name):
    with open (file,"r") as r:
        data=json.load(r)
    found=[c for c in data if c['name'].lower()== name.lower()]
    # print(found)
    if found :
        print("contact found")
        for c in found:
            print(f" name : {c['name']}, \n age : {c['age']} \n subject : {c['subject']} \n mark {c['mark']}")
    else:
        print('contact no found')


def updatecontact (name):
    with open (file,"r") as f:
        data=json.load(f)
    for c in data : 
        if c["name"].lower() == name.lower() :
            print("Contact found , enter new detail")
            newage=int(input("Enter New Age : "))
            newsubject=input("Enter New Subject :")
            newmark=input("Enter Merks : ")
            if newage : c["age"] = newage 
            if newsubject : c["subject"] = newsubject
            if newmark : c["mark"] = float(newmark)
            
            with open (file,"w") as f :
                json.dump(data,f,indent=4)
            print("Contact updated")
            return
    print("contact no found")
# name1 = input("Enter Contact Name : ")
# updatecontact(name1)


def delete (name):
    with open (file,"r") as f:
        data=json.load(f)
    newdata=[c for c in data if c["name"].lower() != name.lower() ]
    if len(newdata) == len(data):
        print("contact not found")
        return
    with open (file,"w") as f:
        json.dump(newdata,f,indent=4)
    print("Contact deleted successfully")

def jsoncsv ():
    with open (file,"r") as f:
        data=json.load(f)
    with open ("contact.csv","w") as f:
        writer=csv.writer(f)
        writer.writerow(["name","age","subject","mark"])
        for c in data :
            writer.writerow([c["name"],c["age"],c["subject"],c["mark"]])
    print("====CSV File Created ===")


        



def main ():
    print("====>  wellcom contact app <====")
    print("option 1 , create contact")
    print("option 2 , find contact ")
    print("option 3 , update contact ")
    print("option 4 , view all contact ")
    print("option 5 , Delete Contact ")
    print("option 6 , CSV file Download  ")

    option=int(input("Enter your option  : "))
    if option == 1 :
        print("Create new contact select")
        createcontact()
        return
    elif option == 2 :
        print("Find contact select")
        name=input("enter name :")
        searchContact(name)
    elif option == 3 :
        print("update contact select ")
        name=input("Enter name : ")
        updatecontact(name)
    elif option == 4 :
        print("view all contact select ")
        view_contact()
    elif option == 5:
        print("Delete contact")
        name=input("Enter name : ")
        delete(name)
    elif option == 6 :
        print("CSV File Selected")
        jsoncsv()
    else :
        print("select correct option ")

main()



# delete contact ,,,,,,,,,,,,

