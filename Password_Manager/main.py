import login
import entry
import generate_password
import pyperclip

key = login.login('normal')

while True:
    
    usr_input = input("Select Option:\n [1] Add Entry\n [2] Read Entry \n [3] Delete Entry \n [4] Reset Login\n [5] Generate Password\n [q] Quit\n")

    if usr_input == '1':
        entry.add_entry(key)
        
    if usr_input == '2':
        entry.read_entry(key, 'read')

    if usr_input == '3':
        entry.read_entry(key, 'delete')

    if usr_input == '4':
        key = login.login('reset')

    if usr_input == '5':
        password = generate_password.generate_password()
        print(password)
        if input("Copy Password To Clipboard? [y][n]\n") == 'y':
            pyperclip.copy(password)

    if usr_input == 'q':
        quit()

        
        
        



