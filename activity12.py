import getpass

username = "yanyan"
password = "yan050612"

user_name = input("Please enter your username: ")
pass_word = getpass.getpass("Please enter your password: ")

if user_name == username and pass_word == password:
	print("Access Granted")
else:
	print("Access Denied")