import customtkinter
from customtkinter import *
import json
import os
import socket
import datetime

user_name = str(os.getcwd()) + "/data/user.json"
data_name = str(os.getcwd()) + "/data/data.json"

class MYLogin(customtkinter.CTk):

	def __init__(self):

		super().__init__()
		self.title("MYLogin")
		self.geometry(f"{1500}X{3000}")

		# main frame

		self.grid_columnconfigure(1, weight = 1)
		self.grid_rowconfigure(1, weight = 1)

		# footer frame

		self.footer_frame = customtkinter.CTkFrame(self, height = 25, corner_radius = 0, fg_color = "#007ACC")
		self.footer_frame.grid(row = 3, column = 1, padx = 0, pady = (5, 0), sticky = "nsew")
		self.footer_frame.grid_columnconfigure(0, weight = 1)
		self.footer_label = customtkinter.CTkLabel(master = self.footer_frame, text = "Developed by matesuu © 2024",text_color=("#FFFFFF"),font=customtkinter.CTkFont(size=12),justify = "center")
		self.footer_label.grid(row = 0, column = 0, sticky = "se")

		# side frame

		self.sidebar_frame = customtkinter.CTkFrame(self, width = 140, corner_radius = 0)
		self.sidebar_frame.grid(row = 0, column = 0, rowspan = 5, sticky = "nsew")
		self.sidebar_frame.grid_rowconfigure(5, weight = 1)

		self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, anchor = "w")
		self.appearance_mode_label.grid(row = 7, column = 0, padx = 20, pady = (10, 0))
		self.apperance_mode_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values = ["Dark", "System"])
		
		# creates a welcome frame

		self.welcome_frame = customtkinter.CTkFrame(self)
		self.welcome_frame.grid(row=1, column=1, sticky="ns")
		self.welcome_label = customtkinter.CTkLabel(self.welcome_frame,  justify="left", text="\n Fibonacci Yeah! \n\nWelcome to MYLogin. This is a lightweight command line interface application intended to store user information with associated client login information. \nEnter 'help' to console to see the list of supported operations."
		, font=customtkinter.CTkFont(size=14))
		self.welcome_label.grid(row=0, column=0, padx=(20,0), pady=(20, 30))

		# creates a sidebar

		self.sidebar_button_frame = customtkinter.CTkFrame(self, width = 140, corner_radius = 0)
		self.sidebar_button_frame.grid(row = 0, column = 0, rowspan = 5, sticky = "nsew")
		self.sidebar_button_frame.grid_rowconfigure(5, weight = 1)
		self.logo_label = customtkinter.CTkLabel(self.sidebar_button_frame, text = "Select Option: ", font = customtkinter.CTkFont(size = 20, weight = "bold"))
		self.logo_label.grid(row = 1, column = 0, padx = 20, pady = (20, 10))

		# command buttons on sidebar

		self.sidebar_button_view = customtkinter.CTkButton(self.sidebar_button_frame, text = "View")
		self.sidebar_button_view.grid(row = 1, column = 0, padx = 20, pady = 50)
		self.sidebar_button_search = customtkinter.CTkButton(self.sidebar_button_frame, text = "Search")
		self.sidebar_button_search.grid(row = 2, column = 0, padx = 20, pady = 50)
		self.sidebar_button_add = customtkinter.CTkButton(self.sidebar_button_frame, text = "Add")
		self.sidebar_button_add.grid(row = 3, column = 0, padx = 20, pady = 50)
		self.sidebar_button_delete = customtkinter.CTkButton(self.sidebar_button_frame, text = "Delete")
		self.sidebar_button_delete.grid(row = 4, column = 0, padx = 20, pady = 50)
		self.sidebar_button_edit = customtkinter.CTkButton(self.sidebar_button_frame, text = "Edit")
		self.sidebar_button_edit.grid(row = 5, column = 0, padx = 20, pady = 50)
		self.sidebar_button_backup = customtkinter.CTkButton(self.sidebar_button_frame, text = "Backup")
		self.sidebar_button_backup.grid(row = 6, column = 0, padx = 20, pady = 50)
		self.sidebar_button_restore = customtkinter.CTkButton(self.sidebar_button_frame, text = "Restore")
		self.sidebar_button_restore.grid(row = 7, column = 0, padx = 20, pady = 50)
		self.sidebar_button_settings = customtkinter.CTkButton(self.sidebar_button_frame, text = "Settings")
		self.sidebar_button_settings.grid(row = 8, column = 0, padx = 20, pady = 50)

	def add_button_event(self):

		self.add_label = customtkinter.CTkLabel(self.welcome_frame,  justify="right", text="\n add"
		, font=customtkinter.CTkFont(size=14))
		self.add_label.grid(row=0, column=0, padx=(20,0), pady=(20, 30))
		'''
		self.entry_label.configure(text = "Add your associated information: ")
		self.label_client.grid(row = 1, column = 0, padx = (20, 5), pady = (5, 5))
		self.label_username.grid(row = 2, column = 0, padx = (20, 5), pady = (5, 5))
		self.label_password.grid(row = 3, column = 0, padx = (20, 5), pady = (5, 5))
		self.label_url.grid(row = 4, column = 0, padx = (20, 5), pady = (5, 5))
	
		self.label_client.configure(text = "Enter Web Client Name: ")
		self.label_username.configure(text = "Enter Username: ")
		self.label_password.configure(text = "Enter Password: ")
		self.label_url.configure(text = "Enter URL: ")

		self.entry_client.grid(row = 1, column = 1, padx = 20, pady = (5, 5))
		self.entry_username.grid(row = 2, column = 1, padx = 20, pady = (5, 5))
		self.entry_password.grid(row = 3, column = 1, padx = 20, pady = (5, 5))
		self.entry_url.gird(row = 4, column = 1, padx = 20, pady = (5, 5))

		self.entry_client.delete(0, 'end')
		self.entry_username.delete(0, 'end')
		self.entry_password.delete(0, 'end')
		self.entry_url.delete(0, 'end')

		self.textBox(text = '')
		self.entry_button.configure(text = "Enter", command = self.add)

	def add(self):

		client = self.entry_client.get()
		username = self.entry_username.get()
		password = self.entry_password.get()
		url = self.entry_url.get()

		flag  = False

		with open(data_name) as check_file:

			check_data = json.load(check_file)

			cleaned_client = client.replace(' ', '')

			for entry in check_data['data_entries']:

				for i in entry.values():

					if cleaned_client == i['client']:

						flag = True
			
			if cleaned_client == '':

				flag = True
		
			if flag == False:

				new_username = username
				new_password = password
				new_url = url
			
				cleaned_username = new_username.replace(' ', '')
				cleaned_password = new_password.replace(' ', '')

				new_entry = {'client' : cleaned_client, 'username' : cleaned_username, 'password' : cleaned_password, 'url' : new_url}
				new_dict = {cleaned_client : new_entry}

				with open(data_name, 'r+') as outfile:

					outfile_data = json.load(outfile)
					outfile_data['data_entries'].append(new_dict)
					outfile.seek(0)
					json.dump(outfile_data, outfile, indent=4)

			else:

				print("error,")
'''




if __name__ == "__main__":

	mylogin = MYLogin()
	mylogin.mainloop()