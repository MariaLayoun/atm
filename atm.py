username = "username"
password = "password"
n= 500000000

def login():
    user = input("Username: \n")
    while user != username:
        user = input("Incorrect username, try again. \n Username: \n ")
    attempt = 1
    while user == username:
        pword = ""
        while pword != password:
            pword = input("Password: \n")
            if pword == password:
                print("Login succesful")
                break
            elif pword != password and attempt <= 2:
                print("Incorrect password, try again.\n")
                attempt += 1
            else:
                print("Out of attempts.")
                break  
        break

def return_to_main_menu():
    quest = input("Would you like to return to the main menu? \n (yes or no) \n")
    if quest == "yes":
        main_menu()
    elif quest == "no":
        print("Have a great day!")
    else:
        print("Invalid input")
    return new_bal


def display():
    print(f"Your current balance is ${n}")

def withdraw():
    num1 = int(input("How much would you like to withdraw? \n"))
    n -= num1
    display()
    return_to_main_menu()
    
def deposit():
    num2= int(input("How much would you like to deposit?  \n"))
    n += num2
    display()
    return_to_main_menu()


def main_menu():
    status = True
    while status == True:
        action = input("What would you like to do? \n 1) Display account balance \n 2) Withdraw \n 3) Deposit \n 4) Exit \n (1,2,3,4)\n") 
        if action == "1":
            display()
        elif action == "2":
            withdraw()
        elif action == "3":
            deposit()
        elif action == "4":
            status = False
            print("Thank you, have a nice day!")
        else:
            print("Invalid response, try again")
    
def ATM():
    login()
    main_menu()


