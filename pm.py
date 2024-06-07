import os
import json
import datetime

def configure() -> str:

        my_name = "NULL"
        
        with open('data.json') as user_file:

                this_user = json.load(user_file)

                if this_user['user'] == "NULL":

                        os.system('clear')
                        this_user['user'] = input("Enter a Username: ")
                        my_name = this_user['user']
                else:
                        my_name = this_user['user']
                
                with open('data.json', 'w') as user_data:
                        json.dump(this_user, user_data, indent=4)
                        
        return my_name


def menu():
        
        os.system('clear')
        print(datetime.datetime.now())
        
        print("\nWelcome to PasswordManger. This is a lightweight command line interface application intended to store user information with associated client login information. Enter 'help' to console to see list of available actions.\n")

        print("Known Clients: \n")

        with open('data.json') as outfile:
                clients = json.load(outfile)

        for client in clients['data_entries']:

                for names in client.values():

                        print(names['client'])

        print("\n")


def help():
        
        os.system('clear')
        print(datetime.datetime.now())
        
        print("\nmenu - returns to main menu")
        print("login - automate login into a client from the command line")
        print("display - displays all currently listed client-password pair contained in dictionary")
        print("fetch - returns a specified key within contained in dictionary")
        print("add - adds a client-password pair to dictionary")
        print("remove - removes a specified cient password pair from dictionary")
        print("edit - change a pre-existing password with an associated client")
        print("clear - deletes all currently existing client-password pairs held within data file")
        print("backup - writes current data to a new backup to be stored in backups folder")
        print("restore - restores data from a given backup")
        print("version - displays version info and credits")
        print("exit - terminate application\n")


def info():
        os.system('clear')
        print(datetime.datetime.now())

        print("\nPasswordManager (v.0.0.1)\nDate Created: 06/06/2024 - Written by matesuu\n")
        

def showClients():

        os.system('clear')

        print(datetime.datetime.now())
        print("\nKnown Clients: \n")

        with open('data.json') as outfile:
                clients = json.load(outfile)

        for client in clients['data_entries']:

                for names in client.values():

                        print(names['client'])

        print("\n")


def display():

        os.system('clear')
        
        print(datetime.datetime.now())
        print("\nKnown Information of Clients: \n")
        
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

        if cleaned_input == "-a":

                os.system('clear')
                print("Clients Information: \n\n")
                
                for local_dicts in curr_data['data_entries']:

                        for keys in local_dicts.values():

                                print("Client Name: " + keys['client'])
                                print("Username: " + keys['username'])
                                print("Password: " + keys['password'])
                                print("Login URL: " + keys['url'])
                                print("\n")
                                
                                flag = True

        else:
                
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
        
        showClients()
        
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
        
        user_input = input("Enter Client to Delete: \n")
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

       
        
def edit():

        showClients()

        user_input = input("Enter Client to Edit: ")
        cleaned_input = user_input.replace(' ', '')

        with open('data.json') as file:

                data = json.load(file)

        for entry in data['data_entries']:
                
                for i in entry.values():
                        
                        if cleaned_input == i['client']:
                                
                                os.system('clear')
                                new_pass = input("Enter New Password: \n")
                                clean_pass = new_pass.replace(' ', '')
                                i['password'] = clean_pass
                                flag = True
                                break

        with open('data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

        os.system('clear')
                
       
        
        if flag == False:
                print("error: could not locate client\n")

        else:
                print("Edited Entry: \n")

        print("\n")

        display()
        


def clear():

        os.system('clear')
        print(datetime.datetime.now())
        
        user_input = input("\nAre you sure you want to delete all entries? (y/n)\n")
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


def backup():

        os.system('clear')
        curr_time = str(datetime.datetime.now())

        with open('data.json') as file:

                data = json.load(file)


        new_json = open('/home/matesu/PasswordManager/backups/backup.json' + ' (' + curr_time + ')', 'x').close() 
        
        #reminder to edit this when released to public to change this statement so that it promps for filepath instead of using my own path    #same for this one below it
        
        with open('/home/matesu/PasswordManager/backups/backup.json' + ' (' + curr_time + ')','w') as json_file:
                
                json.dump(data, json_file, indent=4)


        os.system('clear')
        print("Data Save at " + str(datetime.datetime.now()) + "\n")
                        

def invalid_argument():

        os.system('clear')
        
        print(datetime.datetime.now())
        print("\nerorr: command not found. For a list of supported comamnds, enter 'help' to console.\n")




my_username = configure()

os.system("clear")
print("<STARTING> PasswordManager v.0.0.1\n")

menu()

while True:

        user_input = input("(" + my_username + ")" + " > ")
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
                        edit()
                        
                case "clear":
                        clear()

                case "backup":
                        backup()
        
                case "version":
                        info()

                case "exit":
                        break
                case "quit":
                        break
                case "q":
                        break
                case _:
                        invalid_argument()
                
                
os.system('clear')

print(datetime.datetime.now())
print("\nFibonacci Yeah! (>_<)\n")
