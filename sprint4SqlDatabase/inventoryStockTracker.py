import sqlite3
con = sqlite3.connect('inventory.db')
print('Connection successful')

cur = con.cursor()

def main():
    print("Welcome to the Inventory Stock Tracker! This program is designed to track stock within your inventory, providing tools to add, delete, and view data.")

    
    user_input = input("What would you like to do? Insert, delete, or view? (select, delete, view):").lower()

    if user_input == "insert":
        insert_data()
    elif user_input == "delete":
        delete_item()
    elif user_input == "view":
        select_item()
    else:
        print("Input not recognized, please type insert, delete, or view, is case sensetive.")
    
    user_while = True

    while user_while == True:
        user = input("Wish to continue or close program? (continue or close) is case sensetive:").lower()

        if user == "continue":
            main()
        elif user == "close":
            user_while = False

#function to create table in database
def create_table():
    #Creates the table to store data in
    cur.execute("CREATE TABLE stock (item, amount, description, date added)")

    #inserts a blank line to make the variable requiring user input more readable
    print()
    user_input = input("do you wish to add data to the new table or no? (y or n)")

    #Conditional that sends the user in the right direction, y for inserting data, or n to just end after creating the table
    if user_input == 'y' or user_input == 'Y':
        insert_data()
    elif user_input == 'n' or user_input == 'N':
        return

#function for inserting data into the table
def insert_data():
    print("Please enter the information as instructed below \n")

    loop_input = 'y'
    
    #loop for entering multiple items
    while loop_input == 'y':
         #input variables for entering the data, collected from the user
        item = input("Please enter the name of the item: ")
        amount = input("Please enter how many of the item: ")
        description = input("Please add in a description for the item, including any brand name:")
        date_added = input("Please enter the date this item is being added in(format - yyyy-mm-dd): ")

        cur.execute("INSERT INTO stock VALUES ('%s', '%s', '%s', '%s')" % (item, amount, description, date_added))

        #commits the new row of data
        con.commit()

        loop_input = input("Would you like add another item? (y or n): ").lower()


#function for deleting items in table
def delete_item():
    #warning statement for the user and a help on what info to enter
    print("When deleting an item please use the name of the item and the date added to presicely remove an item.\n")

    print("Please enter the item and date of the item to be removed from the database below \n")

    loop = 'y'

    #loop for deleting multiple items
    while loop == 'y':
        item = input("Enter item name: ")
        date = input("Enter the dated the item was added (format - yyyy-mm-dd): ")

        cur.execute("DELETE FROM stock WHERE item = '%s', AND date added = '%s'" % (item, date))

        con.commit()

        loop = input("Are you deleting another item? (y or n): ").lower()


#function for printing out the stock
def select_item():
    print("Here you will be able to display items in order of your choosing. please enter the info below:\n")

    user_item = input("Are you looking for a specific item or wish to see the entire item list? (specific or stock): ").lower()

    #conditional on what the user wants to see in the database, specific for one item, stock for multiple
    if user_item == "specific":
        user_input = input("What item are you looking for (enter the item name, is case sensitive): ")

        cur.execute("SELECT item FROM stock WHERE item = '%s'" % (user_input))
        print(cur.fetchone())
    elif user_item == "stock":
        user_input = input("What item are you looking for (enter the item name, is case sensitive): ")

        for row in cur.execute("SELECT item FROM stock WHERE item = '%s'" % (user_input)):
            print(row)

main()
#closes connection to the database
con.close()