import re, sys, os

def menu():
    os.system("CLS")
    print("------------------------------------------------------------------------------------")
    print(" Regex Search Tester")
    print("------------------------------------------------------------------------------------")
    print("  1. Search using Regex to test your regex skills")
    print("  2. Add line to the DB")
    print("  3. Remove line from the DB")
    print("  4. List")
    print("  5. Exit")
    print("------------------------------------------------------------------------------------")
    print(" Q=BACK")
    print("------------------------------------------------------------------------------------")
    #print("  q to go back")
    
    user_menu_choice = input("").lower()

    #print("menu choice is = " + str(user_menu_choice))
    if user_menu_choice in ("5", "e", "q"):
        print("OK Quitting!")
        sys.exit()
    if user_menu_choice in ("1", "s"):
        search()
    if user_menu_choice in ("2", "a"):
        add()
    if user_menu_choice in ("3", "r"):
        remove()
    if user_menu_choice in ("4", "l"):
        listDB()
    if user_menu_choice in ("6", "c"):
        os.system("CLS")
        menu()
    else:
        menu()

def add():
    os.system("CLS")
    print("------------------------------------------------------------------------------------")
    print(" Regex Search Tester  -  Add to the DataBase")
    print("------------------------------------------------------------------------------------")
    listWNumbers()
    new_line_to_DB = input("What line do you want to add?\n")
    new_line_to_DB = new_line_to_DB+"\n"
    if new_line_to_DB in ("n", "no", "q", "b", "back", "Q", "B", ""):
        menu()
    else:
        adding_to_DB(new_line_to_DB)


def listWNumbers():
    file_content = readFromFile()
    #print("List:\n-------------------------\n")
    for index, line in enumerate(file_content):
        print(str(index+1)+" "+line)
    print("-------------------------\n")
    #print(str(type(file_content)))


def listDB():
    os.system("CLS")
    print("------------------------------------------------------------------------------------")
    print(" Regex Search Tester  -  List")
    print("------------------------------------------------------------------------------------")
    listWNumbers()
    input("")
    menu()


    
def remove():
    os.system("CLS")
    print("------------------------------------------------------------------------------------")
    print(" Regex Search Tester  -  Remove from the DataBase")
    print("------------------------------------------------------------------------------------")
    file_DB = open("regex_tester_DB.txt", "r")
    file_content = file_DB.readlines()
    sec_content = ""
    for lines in file_DB:
        print(type(lines))
        sec_content = file_DB.readlines(lines)
    file_DB.close()
    listWNumbers()
    del_this_line = input("Which Line do you want to delete?   q to quit\n")
    if del_this_line == "q":
        menu()
    del_this_line = int(del_this_line)
    del file_content[del_this_line-1]
    #print(file_content)
    saveToFile(file_content)
    input("")
    menu()



def search():
    os.system("CLS")
    print("------------------------------------------------------------------------------------")
    print(" Regex Search Tester  -  Search the DataBase")
    print("------------------------------------------------------------------------------------")
    file_content = readFromFile()
    listWNumbers()
    user_search = input("Insert your regex search\nsearch: ")
    #if user_search == "l":
    #    listWNumbers()
    #    user_search = input("Insert your regex search\nsearch: ")
    #if user_search == "q":
    #    menu()
    print("Result:\n")
    matches = 0
    for line in file_content:
        result = re.search(user_search, line)
        #print(result)
        if str(result) != "None":
            print("(MATCH) - " + str(line.strip("\n")))
            print("(INFO)  -  " + str(result)+"\n")
            matches = matches+1
        #print(result)
    print("Matches: "+str(matches))
        
    #print("end of module result:  " + str(result))
    input("")
    menu()






def readFromFile():
    file_DB = open("regex_tester_DB.txt", "r")
    file_content = file_DB.readlines()
    file_DB.close()
    return file_content


def saveToFile(newContent):
    file = open("regex_tester_DB.txt", "w")
    for line in newContent:
        #line = line.strip("\n")
        file.write(line)
    file.close()
    
    

  
def adding_to_DB(new_line_to_DB):
    file = open("regex_tester_DB.txt", "a")
    file.write(new_line_to_DB)
    file.close()
    menu()


if not os.path.exists("regex_tester_DB.txt"):
    file = open("regex_tester_DB.txt", "w")
    file.close()
menu()
