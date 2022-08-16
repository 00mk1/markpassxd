import login
import entry

key = login.login('normal')

while True:
    
    usr_input = input("Select Option:\n [1] Add Entry\n [2] Read Entry \n [3] Delete Entry \n [4] Reset Login\n")

    if usr_input == '1':
        entry.add_entry(key)
    if usr_input == '2':
        entry.read_entry(key, 'read')
    if usr_input == '3':
        entry.read_entry(key, 'delete')
    if usr_input == '4':
        key = login.login('reset')
        



