import os
import json

def menu():
        
        os.system('clear')
        print("Welcome to PasswordManger. This is a lightweight application dedicated to storing passwords with a associated website login by using key-value pairs. At the moment, data is stored locally within a file. Enter Help to console to see list of available actions.\n")

        print("Known Clients: \n")

        with open('data.json') as outfile:
                clients = json.load(outfile)

        for client in clients['data_entries']:

                for names in client.values():

                        print(names['client'])

        print("\n")


def help():
        
        os.system('clear')
        
        print("menu - returns to main menu")
        print("display - displays all currently listed client-password pair contained in dictionary")
        print("fetch - returns a specified key within contained in dictionary")
        print("add - adds a client-password pair to dictionary")
        print("remove - removes a specified cient password pair from dictionary")
        print("edit - DNW - change a pre-existing password with an associated client")
        print("clear - deletes all currently existing client-password pairs held within data file")
        print("exit - ends program\n\n")
        print("IMPORTANT: DO NOT MODIFY FILE DIRECTLY UNLESS FORMATTED AS SPECIFIED. EDITING THE DATA FILE COULD POTENTIALLY CREATE FAULTY INFORMATION THAT MUST BE RECONCILED MANUALLY.\n")
        

def showClients():

        os.system('clear')
        
        print("Known Clients: \n")

        with open('data.json') as outfile:
                clients = json.load(outfile)

        for client in clients['data_entries']:

                for names in client.values():

                        print(names['client'])

        print("\n")


def display():

        os.system('clear')
        print("Known Information of Clients: \n")
        
        with open('data.json') as outfile:
                curr_data = json.load(outfile)

        for entry in curr_data['data_entries']:

                for dict_entries in entry.values():

                        print("Client Name: " + dict_entries['client'])
                        print("Username: " + dict_entries['username'])
                        print("Password: " + dict_entries['password'])

                        print("\n")
        

                      
        outfile.close()


def fetch():

        showClients()
        
        user_input = input("Enter Client to Fetch: ")
        cleaned_input = user_input.replace(' ','')

        with open('data.json') as outfile:
                curr_data = json.load(outfile)
                
        flag = False
        
        for local_dicts in curr_data['data_entries']:

                for keys in local_dicts.values():

                        if cleaned_input == keys['client']:

                                os.system('clear')
                                print("Client Information: \n")
                                print("Client Name: " + keys['client'])
                                print("Username: " + keys['username'])
                                print("Password: " + keys['password'])
                                print("Login URL: " + keys['url'])
                                flag = True

        if flag == False:
                os.system('clear')
                print("error: could not locate client\n")
                
        print("\n")


def add():
        
        os.system('clear')

        new_client = input("Enter New Client: ")
        new_username = input("Enter Username: ")
        new_password = input("Enter Password: ")
        new_url = input("Enter Login URL: ")
        
        cleaned_client = new_client.replace(' ','')
        cleaned_username = new_username.replace(' ','')
        cleaned_password = new_password.replace(' ','')
        
        new_entry = {"client" : cleaned_client, "username" : cleaned_username, "password" : cleaned_password, "url" : new_url}
        new_dict = {cleaned_client : new_entry}
        
        with open('data.json', 'r+') as outfile:
                outfile_data = json.load(outfile)
                outfile_data['data_entries'].append(new_dict)
                outfile.seek(0)
                json.dump(outfile_data, outfile, indent=4)

        display()
        

def remove():

        showClients()
        
        user_input = input("Enter Client to Delete: ")
        cleaned_input = user_input.replace(' ','')

        with open('data.json') as outfile:
                curr_data = json.load(outfile)
                
        flag = False

        
        for entry in curr_data['data_entries']:
                
                for i in entry.values():
                        
                        if cleaned_input == i['client']:
                                
                                curr_data['data_entries'].remove(entry)
                                flag = True
                                break

        with open('data.json', 'w') as json_file:
                json.dump(curr_data, json_file, indent=4)

        os.system('clear')
                
       
        
        if flag == False:
                print("error: could not locate client\n")

        else:
                print("Deleted Entry: \n")

        print("\n")

        display()

       
        
def change():

        showClients()


def clear():

        os.system('clear')

        user_input = input("Are you sure you want to delete all entries? (y/n)\n")

        cleaned_input = user_input.replace(' ', '')

        with open('data.json') as outfile:

                data = json.load(outfile)

        if cleaned_input == 'y':

                for entry in data['data_entries']:

                        for i in entry.values():
                                data['data_entries'].clear()
                                break
                        
        with open('data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

        os.system('clear')
        print("All Data was Sucessfully Deleted\n")
                        

def invalid_argument():
        
        os.system('clear')
        print("erorr: command not found. For a list of supported comamnds enter 'Help' to console.\n")


os.system("clear")
print("<STARTING> PasswordManager v.0.0.1\n")

infofile = open(r"userInfo.txt", "r")
username = infofile.readline()
infofile.close()

menu()

while True:

        user_input = input("(" + username + ")" + " > ")
        cleaned_input = user_input.replace(' ', '')

        match cleaned_input:

                case "menu":
                        menu()
                        
                case "help":
                        help()
                        
                case "display":
                        display()
                        
                case "fetch":
                        fetch()
                        
                case "add":
                        add()
                        
                case "remove":
                        remove()

                case "edit":
                        change()
                        
                case "clear":
                        clear()

                case "exit":
                        break
                case "quit":
                        break
                case "q":
                        break

                case _:
                        invalid_argument()
                
                
os.system('clear')
print("Fibonacci Yeah! (>_<)\n")
