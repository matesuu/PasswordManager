#Welcome to the MYLogin project. Currently, this is an attempt to create a full application so progress is limited to functionaity at the moment. Will comment out all of the code at some point.

import os
import json
import socket
import datetime

data_name = str(os.getcwd()) + "/data/data.json"

def clear(): #clears console and checks to see what os is being used

        if os.name == 'nt': # windows
                
                os.system('cls')
                
        else: # mac/linux
                os.system('clear')

def icon():

        print(str(datetime.datetime.now()) + """
                            _
 __  ___    ___            |+|                       
|  \/  \ \ / / |   ___ __ _ _ _ _
| |\/| |\ V /| |__| _ / _` | | '  \                        
|_|  |_| |_| |____|___\__, |_|_||_|
                      |___/ 
        """) # prints icon
                

def configure() -> str: # gets username and path used for backups

        my_name = "NULL"
        
        with open(data_name) as user_file:

                this_user = json.load(user_file)

                if this_user['user'] == "NULL":

                        clear()
                        this_user['user'] = input("Enter a Username: ")
                        my_name = this_user['user']
                        
                else:
                        
                        my_name = this_user['user']

                if this_user['backup_path'] == "NULL":

                        
                        #path_input = input("\nEnter Path of backups Folder (ex: /home/username/Applications/PasswordManager/backups) :\n")                    
                        
                        #cleaned_path = path_input.replace(' ','')

                        cleaned_path = str(os.getcwd()) + "/backups"
                        this_user['backup_path'] = cleaned_path

                if this_user['date_created'] == "NULL":

                        this_user['date_created'] = str(datetime.datetime.now())

                
                with open(data_name, 'w') as user_data:
                        
                        json.dump(this_user, user_data, indent=4)
        

        
        return my_name


def menu():
        
        clear()
        icon()
        
        print("Welcome to MYLogin. This is a lightweight command line interface application intended to store user information with associated client login information. Enter 'help' to console to see the list of supported operations.\n")
        


def help():
        
        clear()
        icon()
        
        print("menu - returns to main menu")
        print("view - displays all current clients as a list")
        print("search - returns all associated login information with a given client")
        print("create - creates a new client-information pair in dictionary - Optional Flags: [-all] [-client]")
        print("remove - removes a specified cient password pair from dictionary")
        print("edit - change a pre-existing password with an associated client")
        print("reset - deletes all currently existing client-password pairs held within data file")
        print("backup - writes current data to a new backup to be stored in backups folder")
        print("restore - restores data from a given backup")
        #print("add - adds a connection to a personal server or device for transfer")
        #print("delete - deletes a connection to a currently listed device")
        #print("transfer - adminster a FTP to a currently listed connected device")
        print("version - displays version info and credits")
        print("quit - terminate application\n")


def info():
        
        clear()
        icon()

        print("\nMyLogin (Build 0)\nDate Created: 06/06/2024 - Written by matesuu")
        print("Fibonacci Yeah! (>_<)\n")


def display():

        clear()
        icon()

        
        print("Known Clients: \n")

        with open(data_name) as outfile:
                clients = json.load(outfile)

        for client in clients['data_entries']:

                for names in client.values():

                        print(names['client'])

        print("\n")


def search():

        display()
        
        user_input = input("Enter Client to Fetch: ")
        cleaned_input = user_input.replace(' ','')

        with open(data_name) as outfile:
                curr_data = json.load(outfile)
                
        flag = False

                
        for local_dicts in curr_data['data_entries']:

                for keys in local_dicts.values():

                        if cleaned_input == keys['client']:

                                clear()
                                print("Client Information: \n")
                                print("Client Name: " + keys['client'])
                                print("Username: " + keys['username'])
                                print("Password: " + keys['password'])
                                print("Login URL: " + keys['url'])
                                flag = True
                                

        if flag == False:
                clear()
                print("error: could not locate client\n")
                
        print("\n")


def search_all():

        clear()
        print("Clients Information: \n")

        with open(data_name) as outfile:
                curr_data = json.load(outfile)
                
        for local_dicts in curr_data['data_entries']:

                for keys in local_dicts.values():

                        print("Client Name: " + keys['client'])
                        print("Username: " + keys['username'])
                        print("Password: " + keys['password'])
                        print("Login URL: " + keys['url'])
                        print("\n")

        print("\n")


def create():
        
        display()
        flag = False

        with open(data_name) as check_file:
                check_data = json.load(check_file)
        
        new_client = input("Enter New Client: ")
        cleaned_client = new_client.replace(' ', '')
        

        for entry in check_data['data_entries']:

                for i in entry.values():

                        if cleaned_client == i['client']:

                                flag = True

        if cleaned_client == '':

                flag = True

                
        if flag == False:

                new_username = input("Enter Username: ")
                new_password = input("Enter Password: ")
                new_url = input("Enter Login URL: ")

                cleaned_username = new_username.replace(' ','')
                cleaned_password = new_password.replace(' ','')
                
                new_entry = {"client" : cleaned_client, "username" : cleaned_username, "password" : cleaned_password, "url" : new_url}
                new_dict = {cleaned_client : new_entry}
        
                with open(data_name, 'r+') as outfile:
                        
                        outfile_data = json.load(outfile)
                        outfile_data['data_entries'].append(new_dict)
                        outfile.seek(0)
                        json.dump(outfile_data, outfile, indent=4)

                display()
                
        else:

                clear()
                print("error: client already exists in directory\n")

def remove():

        display()
        
        user_input = input("Enter Client to Delete: \n\n")
        cleaned_input = user_input.replace(' ','')
        
        with open(data_name) as outfile:
                curr_data = json.load(outfile)
                
        flag = False

        for entry in curr_data['data_entries']:
                
                for i in entry.values():
                        
                        if cleaned_input == i['client']:

                                removed_value = i['client']
                                curr_data['data_entries'].remove(entry)
                                flag = True
                                break

        with open(data_name, 'w') as json_file:
                json.dump(curr_data, json_file, indent=4)

        clear()
                
       
        
        if flag == False:
                print("error: could not locate client\n")

        else:
                print("Deleted Entry: " + removed_value)

        print("\n")

       
        
def edit():

        display()

        user_input = input("Enter Client to Edit: ")
        cleaned_input = user_input.replace(' ', '')

        flag = False

        with open(data_name) as file:

                data = json.load(file)

        for entry in data['data_entries']:
                
                for i in entry.values():
                        
                        if cleaned_input == i['client']:
                                
                                clear()
                                print(i['client'])
                                edited_value = i['client']
                                new_pass = input("\nEnter New Password: \n\n")
                                clean_pass = new_pass.replace(' ', '')
                                i['password'] = clean_pass
                                flag = True
                                break

        with open(data_name, 'w') as json_file:
                json.dump(data, json_file, indent=4)
       
        
        if flag == False:
                clear()
                print("error: could not locate client\n")

        else:
                clear()
                print("Edited Entry: " + edited_value + "\n")

        print("\n")
        


def reset():

        clear()
        print(datetime.datetime.now())
        
        user_input = input("\nAre you sure you want to delete all entries? (y/n)\n\n")
        cleaned_input = user_input.replace(' ', '')
        flag = False

        with open(data_name) as outfile:

                data = json.load(outfile)

        if cleaned_input == 'y':

                for entry in data['data_entries']:

                        for i in entry.values():
                                data['data_entries'].clear()
                                flag = True
                                break
                        
        with open(data_name, 'w') as json_file:
                json.dump(data, json_file, indent=4)

        clear()
        
        if flag == True:
                
                print("All Data was Sucessfully Deleted\n")

        else:
                print("process aborted\n")


def backup():

        clear()
        curr_time = str(datetime.datetime.now())

        with open(data_name) as file: # opens data.json to read from file and store in dictionary 'data'

                data = json.load(file)
                

        new_id = int(data['backups_made'])      # stores the current backup ID in new_id
        new_id+=1                               # increments ID by 1
        data['backups_made'] = str(new_id)      # casts new_id to string
        

        with open(data_name, 'w') as update_id:       # opens data.json to write to file and dumps data, the only difference being 
                                                        # the incremented ID
                        
                json.dump(data, update_id, indent=4)

        path = data['backup_path']                      # gets path of backup folder
        data['date_created'] = str(datetime.datetime.now())     # stores the date of creation in 'date_created' as a string
        

        new_json = open(path + '/backup-' + str(new_id) + '.json', 'x').close() # creates a new json file
        
        with open(path + '/backup-' + str(new_id) + '.json','w') as json_file:  # opens newly created json file and dumps data from current json file
                
                json.dump(data, json_file, indent=4)


        clear()
        print("Created Backup at " + str(datetime.datetime.now()) + "\n")
        

def restore():

        clear()
        print(datetime.datetime.now())

        with open(data_name) as get_path:
                path_data = json.load(get_path)

        dir_list = os.listdir(path_data['backup_path'])
        print(dir_list)

        new_master = int(path_data['backups_made'])
        
        backup_file = input("\nSelect Backup to Restore With: \n\n")

        #note: have to handle case where inputted string is not a valid file... try catch block maybe?

        try:
                with open(path_data['backup_path'] + '/' + backup_file) as json_file:
                        backup_data = json.load(json_file)
                        
                backup_data['backups_made'] = str(new_master)
                
                with open(data_name, 'w') as restored_file:
                        json.dump(backup_data, restored_file, indent=4)
                        
                clear()
                print("Restored from Backup at " + str(datetime.datetime.now()))
                print("\n")

        except FileNotFoundError:
                
                clear()
                print("error: file not found\n")
        

def invalid_argument():

        clear()
        
        print(datetime.datetime.now())
        print("\nerorr: command not found. For a list of supported comamnds, enter 'help' to console.\n")



my_username = configure()

clear()
print("<STARTING> LoginManager v.0.0.1\n")
changes = 0

menu()

while True:

        user_input = input("(" + my_username + ")" + " > ")
        cleaned_input = user_input.replace(' ', '')

        match cleaned_input:

                case "menu":
                        menu()
                        
                case "help":
                        help()
                        
                case "view":
                        display()
                        
                case "search":
                        search()

                case "search-all":
                        search_all()
                        
                case "create":
                        create()
                        
                case "remove":
                        remove()

                case "edit":
                        edit()
                        
                case "reset":
                        reset()

                case "backup":
                        backup()

                case "restore":
                        restore()
                        
                case "version":
                        info()
                        
                case "quit":
                        break
                case _:
                        invalid_argument()
                

clear()
print("Application Terminated at " + str(datetime.datetime.now()) + "\n")
