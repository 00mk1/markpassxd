global logged_in 
logged_in = False


def main(logged_in):
    import login
    import entry
    import generate_password
    import pyperclip

    global key

    if logged_in == False:
        key = login.login('normal')
    else:
        pass

    logged_in = True

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
            try:
                char_length = int(input("How Many Characters Should Be Included?\n"))
            except:
                main(logged_in)
            password = generate_password.generate_password(char_length)
            print(password)
            if input("Copy Password To Clipboard? [y][n]\n") == 'y':
                pyperclip.copy(password)

        if usr_input == 'q':
            quit()

        
        
main(logged_in)



