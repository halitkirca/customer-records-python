import csv

def viewRecords():
    try:
        with open("customerRecords.csv", "r", newline='', encoding="utf-8") as file:
            read = csv.reader(file, delimiter=",")
            for row in read:
                print(row)  
    except Exception as e:
        print(e)
    finally:
        menu()

def addCustomer():
    try: 
        exist = False
        customerId = (input("Customer id ..:"))
        
        with open("customerRecords.csv", "r", newline='', encoding="utf-8") as file:
            read = csv.reader(file, delimiter=",")
            for row in read:
                if row[0] == customerId:
                    exist = True
                    print("This customer already exists.")
        
        if exist == False:
            firstName = input("First name ..:").title().strip()
            lastName = input("Last name ..:").title().strip()
            product = input("Product name ..:").strip()
            
            with open("customerRecords.csv", "a", newline='', encoding="utf-8") as file:
                record = csv.writer(file)
                record.writerow([customerId, firstName, lastName, product])
            print("New customer added.")

    except Exception as e:
        print("Couldn't process..:", e)
    finally:
        menu()

def deleteCustomer():
    try:
        newrows = []
        customerId = input("Enter customer id to delete a customer ..:")
        deleted = False

        with open("customerRecords.csv", "r", newline="", encoding="utf-8") as readerfile:
            reader = csv.reader(readerfile, delimiter=",")
            for row in reader:
                if row[2] != customerId:
                    newrows.append(row)
                else:
                    deleted = True

        with open("customerRecords.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(newrows)

        if deleted == True:
            print("Customer deleted.")
        else:
            print("Customer was not found.")

    except Exception as e:
        print("Couldn't process..:", e)
    finally:
        menu()

def infoCustomer():
    try:
        info = False
        customerId = input("Enter customer id to show info of a customer ..:")
        with open("customerRecords.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if customerId in row:
                    info = True
                    print(row)
                    break

        if info == False:
            print("Customer was not found.")

    except Exception as e:
        print("Couldn't process..:", e)
    finally:
        menu()

def updateCustomer():
    try:
        newrows = []
        customerId = input("Enter customer id to update ..:")
        updated = False

        with open("customerRecords.csv", "r", newline="", encoding="utf-8") as readerfile:
            reader = csv.reader(readerfile, delimiter=",")
            for row in reader:
                if row[0] != customerId:
                    newrows.append(row)
                else:
                    updated = True
                    firstName = input("First name ..:").title().strip()
                    lastName = input("Last name ..:").title().strip()
                    product = input("Product name ..:").strip()
                    newrows.append([customerId, firstName, lastName, product])

        with open("customerRecords.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(newrows)

        if updated == True:
            print("Customer updated succesfully.")
        else:
            print("Customer was not found.")

    except Exception as e:
        print("Couldn't process..:", e)
    finally:
        menu()
    

def menu():
    print("-----Welcome to menu-----")
    print("[1]: View customer records")
    print("[2]: Add new customer")
    print("[3]: Delete customer")
    print("[4]: View certain customer")
    print("[5]: Update a customer")
    print("[6]: Exit menu")
    num = input("Choose an option from 1 to 6:\n")
    if num == "1":
        viewRecords()
    elif num == "2":
        addCustomer()
    elif num == "3":
        deleteCustomer()
    elif num == "4":
        infoCustomer()
    elif num == "5":
        updateCustomer()
    elif num == "6":
        return print("Exited from menu.")
    else:
        print("Enter a number from 1 to 6 please.")
        menu()
    
menu()
    





