import login
import entry


key = login.login()
input = input("What Do?\n")
if input == '1':
    entry.add_entry(key, 'Add')
if input == '2':
    entry.read_entry(key)




