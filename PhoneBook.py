import sqlite3
import sys

def all_contacts():
        print("\n")
        c.execute("SELECT rowid,* FROM contacts")
        items = c.fetchall()
        count = 0
        if items:
            for item in items:
                count += 1
                print("\t Id: " + str(count))
                print("\t Name: " + item[1])
                print("\t Ph_No: " + item[2])
                print("\t Email_Id: " + item[3])
                print("\n")
        else:
            print("\t Contact list Empty....!")
            print("\n")
        return
def delete_contacts():
        print("\t Name of the contact you want to DELETE")
        name = input("\t >>> ")
        c.execute("DELETE FROM contacts WHERE Name=(?)",(name,))
        con.commit()
        print("\n")
        print("\t contact Deleted.....")
        print("\n")
        return

def delete_all():
    print("\t !! ALL THE DATA IN THE CONTACTS WILL BE DELETED !!")
    print("\n")
    print("\t type 'yes' to Delete, 'no' to Cancel")
    print("\n")
    choice = input("\t >>>")
    if choice == "yes":
        c.execute("DELETE FROM contacts")
        con.commit()
        print("\n \t ALL THE DATA DELETED...")
        print("\n")
    if choice == "no":
        print("\t Quitting....")

def add_contacts():
        print("\n")
        name = input("\t Enter the name: ")
        ph_no = input("\t Enter the Ph_N0: ")
        email = input("\t Enter the Email: ")
        c.execute("INSERT INTO contacts VALUES (?,?,?)",(name,ph_no,email)) 
        con.commit()
        print("\n")
        print("\t New contact is adedd......") 
        print("\n")
        return 

def search_contacts():
        print("\n")
        print("\t Name of the contact")
        name = input("\t >>> ")
        print("\n")
        c.execute("SELECT rowid,* FROM contacts WHERE Name=?",(name,))
        items = c.fetchall()
        count = 0
        if items:
            for item in items:
                count += 1
                print("\t Id: " + str(count))
                print("\t Name: " + item[1])
                print("\t Ph_no: " + item[2])
                print("\t Email_Id: " + item[3])
                print("\n")
        else:
            print("\t  Contact not found...!")
            print("\n")
        return

def Greetings():
    print("\n")
    print(" <<<!!! HELLO user, welcome to python PhoneBook !!!>>>")
    print("\n")
    print("\t Enter all the inputs in Lower_case letters")
    print("\n")

def Farewell():
    print("\n")
    print("\t <<<< THANK YOU FOR USING PHONEBOOK >>>>")
    print("\n")
    print("\t      <<<< COME AGAIN......... >>>>     ")
    print("\n")
    sys.exit()

def under_line():
    print("_____#" * 20)
    print("\n")


def mainmenu():
        print(" !!! please select one of the below actions. !!!")
        print("\n")
        print("""
        >>> 1 - View contacts in the list. \n 
        >>> 2 - Search contact. \n 
        >>> 3 - Add new contacts. \n 
        >>> 4 - Delete contacts. \n 
        >>> 5 - Delete all the contacts \n 
        >>> 6 - Exit \n
        """)
        choice = input(" >>> ")

        if choice == '1':
            all_contacts()
            under_line()
        
        if choice == '2':
            search_contacts()
            under_line()

        if choice == '3':
            add_contacts()
            under_line()

        if choice == '4':
            delete_contacts()
            under_line()

        if choice == '5':
            delete_all()
            under_line()

        if choice == '6':
            Farewell()
            

Greetings()
con = sqlite3.connect("database.db")
c = con.cursor()
try:
    c.execute("CREATE TABLE contacts (Name text, Ph_No text, Email text)")
except:
    pass
con.commit()
while True:
    mainmenu()
    con.commit()
con.close()