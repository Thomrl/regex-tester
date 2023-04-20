import re, sys, os

def menu():
    print(" Regex Search Tester ")
    print("1. Add line to the DB")
    print("2. Remove line from the DB")
    print("3. Search using Regex to test your regex skills")
    print("4. Exit")
    print("5. List")
    print("6. Dev")
    print("7. Clear text")
    
    user_menu_choice = input("Insert a number to pick what you want\n").lower()

    print("menu choice is = " + str(user_menu_choice))
    if user_menu_choice in ("4", "e", "q"):
        print("OK Quitting!")
        sys.exit()
    if user_menu_choice in ("1", "a"):
        add()
    if user_menu_choice in ("2", "r"):
        dev()
    if user_menu_choice in ("3", "s"):
        search()
    if user_menu_choice in ("5", "l"):
        list()
    if user_menu_choice in ("6", "d"):
        dev()
    if user_menu_choice in ("7", "c"):
        os.system("CLS")
        menu()
    else:
        menu()

def add():
    new_line_to_DB = input("What line do you want to add to the DB?\n")
    new_line_to_DB = new_line_to_DB+"\n"
    if new_line_to_DB in ("n", "no", "q", "b", "back", "Q", "B"):
        menu()
    else:
        adding_to_DB(new_line_to_DB)


def listWNumbers():
    file_content = readFromFile()
    print("-------------------------\n")
    print("Content from the DB start:\n")
    print("-------------------------\n\n")
    #print("As a list: " + str(file_content) +"\n")
    for index, line in enumerate(file_content):
        print(str(index+1)+" "+line)
    print("\n-------------------------\n")
    print("Content from the DB end.")
    print("-------------------------\n")
    print(str(type(file_content)))


def list():
    file_content = readFromFile()
    print("List:\n-------------------------\n")
    #print("As a list: " + str(file_content) +"\n")
    for index, line in enumerate(file_content):
        print(str(index+1)+" "+line)
    print("\n-------------------------\n")
    print(str(type(file_content)))
    input("press enter when done reading")
    menu()


    
def dev():
    file_DB = open("db.txt", "r")
    file_content = file_DB.readlines()
    sec_content = ""
    for lines in file_DB:
        print(type(lines))
        sec_content = file_DB.readlines(lines)
    file_DB.close()
    print("Content from the DB start:\n")
    print("-------------------------\n")
    print(file_content)
    print("\n-------------------------\n")
    print("Content from the DB end.")
    print("-------------------------\n")
    print(str(type(file_content)))
    listWNumbers()
    del_this_line = input("Which Line do you want to delete?   q to quit\n")
    if del_this_line == "q":
        menu()
    del_this_line = int(del_this_line)
    del file_content[del_this_line-1]
    print(file_content)
    saveToFile(file_content)
    input("press enter when done reading")
    menu()



def search():
    file_content = readFromFile()
    user_search = input("Insert your regex search\n")
    matches = 0
    for line in file_content:
        result = re.search(user_search, line)
        #print(result)
        if str(result) != "None":
            print(result)
            print(line)
            matches = matches+1
        #print(result)
    print("Matches: "+str(matches))
        
    #print("end of module result:  " + str(result))
    input("enter to go to menu")
    menu()






def readFromFile():
    file_DB = open("db.txt", "r")
    file_content = file_DB.readlines()
    file_DB.close()
    return file_content


def saveToFile(newContent):
    file = open("db.txt", "w")
    for line in newContent:
        #line = line.strip("\n")
        file.write(line)
    file.close()
    
    

  
def adding_to_DB(new_line_to_DB):
    file = open("db.txt", "a")
    file.write(new_line_to_DB)
    file.close()
    menu()


menu()
