#MarkPassxD v1.0.0 - A simple CLI Password Manager By Mark Barlass. 2022, FOSS, Use as you wish.

#'Main' is the the main routine. Options are printed in a numbered list. The user inputs the number of thier selection.
# Functions return here. 

global logged_in 
logged_in = False

def main(logged_in):
    import login
    import entry
    import generate_password
    import pyperclip

    #a hash output from the master password, used as the encyption key.
    global key

    if logged_in == False:
        #if not logged in, log in and return the key.
        key = login.login('normal')
   
    

    logged_in = True

    #main routine.
    while True:
        
        mode = input("Select Option:\n [1] Add Entry\n [2] Read Entry \n [3] Delete Entry \n [4] Reset Login\n [5] Generate Password\n [q] Quit\n")

        if mode == '1':
            entry.add_entry(key)
            
        if mode == '2':
            entry.read_entry(key, 'read')

        if mode == '3':
            entry.read_entry(key, 'delete')

        if mode == '4':
            key = login.login('reset')

        if mode == '5':
            #generates and prints a random password.
            invalid = True

            #reruns if the input is not a number.
            while invalid == True:
                try:
                    char_length = int(input("How Many Characters Should Be Included?\n"))
                    invalid = False
                except:
                    print("Please Enter Whole Digits\n")

            #returns a random password from the 'generate password' module.
            password = generate_password.generate_password(char_length)
            print(password)
            if input("Copy Password To Clipboard? [y][n]\n") == 'y':
                pyperclip.copy(password)

        if mode == 'q':
            quit()

main(logged_in)



