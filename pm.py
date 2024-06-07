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

                if this_user['backup_path'] == "NULL":

                        
                        path_input = input("\nEnter Path of backups Folder: \n")
                        cleaned_path = path_input.replace(' ','')
                
                        this_user['backup_path'] = cleaned_path

                if this_user['date_created'] == "NULL":

                        this_user['date_created'] = str(datetime.datetime.now())

                
                with open('data.json', 'w') as user_data:
                        json.dump(this_user, user_data, indent=4)
        

        
        return my_name


def menu():
        
        os.system('clear')
        print(datetime.datetime.now())
        
        print("\nWelcome to LoginManger. This is a lightweight command line interface application intended to store user information with associated client login information. Enter 'help' to console to see list of available operations.\n")

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
        print("display - displays all current clients as a list")
        print("fetch - returns all associated login information with a given client")
        print("add - adds a client-password pair to dictionary - Optional Flag -> [-all] fetches all clients")
        print("remove - removes a specified cient password pair from dictionary")
        print("edit - change a pre-existing password with an associated client")
        print("clear - deletes all currently existing client-password pairs held within data file")
        print("backup - writes current data to a new backup to be stored in backups folder")
        print("restore - restores data from a given backup")
        print("version - displays version info and credits")
        print("quit - terminate application\n")


def info():
        os.system('clear')
        print(datetime.datetime.now())

        print("\nLoginManager (v.0.0.1)\nDate Created: 06/06/2024 - Written by matesuu\n")


def display():

        os.system('clear')

        print(datetime.datetime.now())
        print("\nKnown Clients: \n")

        with open('data.json') as outfile:
                clients = json.load(outfile)

        for client in clients['data_entries']:

                for names in client.values():

                        print(names['client'])

        print("\n")


def fetch():

        display()
        
        user_input = input("Enter Client to Fetch: ")
        cleaned_input = user_input.replace(' ','')

        with open('data.json') as outfile:
                curr_data = json.load(outfile)
                
        flag = False

        if cleaned_input == "-a":

                os.system('clear')
                print("Clients Information: \n")
                
                for local_dicts in curr_data['data_entries']:

                        for keys in local_dicts.values():

                                print("Client Name: " + keys['client'])
                                print("Username: " + keys['username'])
                                print("Password: " + keys['password'])
                                print("Login URL: " + keys['url'])
                                
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


def fetch_all():

        os.system('clear')
        print("Clients Information: \n")

        with open('data.json') as outfile:
                curr_data = json.load(outfile)
                
        for local_dicts in curr_data['data_entries']:

                for keys in local_dicts.values():

                        print("Client Name: " + keys['client'])
                        print("Username: " + keys['username'])
                        print("Password: " + keys['password'])
                        print("Login URL: " + keys['url'])
                        print("\n")

        print("\n")


def add():
        
        os.system('clear')
        
        display()
        
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

        display()
        
        user_input = input("Enter Client to Delete: \n\n")
        cleaned_input = user_input.replace(' ','')
        
        with open('data.json') as outfile:
                curr_data = json.load(outfile)
                
        flag = False

        for entry in curr_data['data_entries']:
                
                for i in entry.values():
                        
                        if cleaned_input == i['client']:

                                removed_value = i['client']
                                curr_data['data_entries'].remove(entry)
                                flag = True
                                break

        with open('data.json', 'w') as json_file:
                json.dump(curr_data, json_file, indent=4)

        os.system('clear')
                
       
        
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

        with open('data.json') as file:

                data = json.load(file)

        for entry in data['data_entries']:
                
                for i in entry.values():
                        
                        if cleaned_input == i['client']:
                                
                                os.system('clear')
                                print(i['client'])
                                edited_value = i['client']
                                new_pass = input("\nEnter New Password: \n\n")
                                clean_pass = new_pass.replace(' ', '')
                                i['password'] = clean_pass
                                flag = True
                                break

        with open('data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
       
        
        if flag == False:
                os.system('clear')
                print("error: could not locate client\n")

        else:
                os.system('clear')
                print("Edited Entry: " + edited_value + "\n")

        print("\n")
        


def clear():

        os.system('clear')
        print(datetime.datetime.now())
        
        user_input = input("\nAre you sure you want to delete all entries? (y/n)\n\n")
        cleaned_input = user_input.replace(' ', '')
        flag = False

        with open('data.json') as outfile:

                data = json.load(outfile)

        if cleaned_input == 'y':

                for entry in data['data_entries']:

                        for i in entry.values():
                                data['data_entries'].clear()
                                flag = True
                                break
                        
        with open('data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

        os.system('clear')
        
        if flag == True:
                
                print("All Data was Sucessfully Deleted\n")

        else:
                print("process aborted\n")


def backup():

        os.system('clear')
        curr_time = str(datetime.datetime.now())

        with open('data.json') as file:

                data = json.load(file)
                

        new_id = int(data['backups_made'])
        new_id+=1
        data['backups_made'] = str(new_id)
        

        with open('data.json', 'w') as update_id:
                
                json.dump(data, update_id, indent=4)

        path = data['backup_path']
        data['date_created'] = str(datetime.datetime.now()) 
        

        new_json = open(path + '/backup-' + str(new_id) + '.json', 'x').close() 
        
        with open(path + '/backup-' + str(new_id) + '.json','w') as json_file:
                
                json.dump(data, json_file, indent=4)


        os.system('clear')
        print("Created Backup at " + str(datetime.datetime.now()) + "\n")
        

def restore():

        os.system('clear')
        print(datetime.datetime.now())

        with open('data.json') as get_path:
                path_data = json.load(get_path)

        dir_list = os.listdir(path_data['backup_path'])
        print(dir_list)

        new_master = int(path_data['backups_made'])
        
        backup_file = input("\nSelect Backup to Restore With: \n\n")

        #note: have to handle case where inputted string is not a valid file... try catch block maybe?

        with open(path_data['backup_path'] + '/' + backup_file) as json_file:
                backup_data = json.load(json_file)

        backup_data['backups_made'] = str(new_master)

        with open('data.json', 'w') as restored_file:
                json.dump(backup_data, restored_file, indent=4)

        os.system('clear')
        print("Restored from Backup at " + str(datetime.datetime.now()))
        print("\n")
        

def invalid_argument():

        os.system('clear')
        
        print(datetime.datetime.now())
        print("\nerorr: command not found. For a list of supported comamnds, enter 'help' to console.\n")



my_username = configure()

os.system("clear")
print("<STARTING> LoginManager v.0.0.1\n")

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

                case "fetch-all":
                        fetch_all()
                        
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

                case "restore":
                        restore()
                        
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
print("Application Terminated at " + str(datetime.datetime.now()))
print("\nFibonacci Yeah! (>_<)\n")
