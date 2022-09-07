#MarkPassxD - Mark Barlass 2022

#The 'entry' module is responsible for writing new entries, as well as reading or deleting existing entries. 

import generate_password
import pyAesCrypt
import os
import pyperclip
import platform

#key is the secondary hash derived from the master password. 
def add_entry(key):
    global password
    

    #cwd is the current working directory.
    cwd = os.getcwd()

    title = str(input("Enter A Title:\n"))
    
    #file_path is the location where the unecrypted file is temporarily stored.
    
    file_path = cwd + "/Saved_Passwords/" + title + ".txt"
    
    #dir_path is the directory where passwords are stored.
    dir_path = os.getcwd() + '/Saved_Passwords/'


    if title + ".txt.aes" in os.listdir(dir_path):
        if input("This File Already Exists, Would You Like To Overwrite It? [y][n]\n") == 'y':
            pass
        else:
            add_entry(key)

    username = input("Enter The Username, Email Address or Leave Blank:\n")
    mode = str(input("[1] Generate Random Password \n[2] Add Password Manually\n[b] Cancel\n"))
    
    if mode == "1":
        invalid = True
        while invalid == True:
            try:
                char_length = int(input("How Many Characters Should Be Included? (More = Better, Recomended: 128)\n"))
                password = generate_password.generate_password(char_length)
                invalid = False
                
            except:
                print("Please Enter Whole Digits\n")
                
    
    elif mode == "2":
        password = input("Enter Password:\n")

    elif mode == "b":
        return

    else: 
        add_entry(key)
    
    try:
        file = open(file_path, 'x')
    except:
        if input("This File Already Exists, Would You Like To Overwrite It? [y][n]\n") == 'y':
            file = open(file_path, 'w')
    
    #concatenates and formats the text to be written in the entry.
    file.write("Title: " + title + '\n' + "Username: " + username + '\n' + "Password: " + password)
    
    #output is the name of the encrypted file. 
    file.close()
    output = file_path + ".aes"

    #encrypts the txt file then removes it.
    try:
        pyAesCrypt.encryptFile(file_path, output, key)
        os.remove(file_path)
        
    except:
        print("The encyption key is incorrect or the file is corrupt.")
        return

    copy = input("Copy Password To Clipboard? [y][n]\n") 
    if copy == 'y':
        pyperclip.copy(password)
    
    return
        
        
#mode can be 'read' or 'delete' if the user wishes to delete a file.
def read_entry(key, mode):
    #'x' is a counter.
    x = 1
    #'res' is a list of currently saved passwords.
    res = []

    
    dir_path = os.getcwd() + '/Saved_Passwords/'

    #for each file in 'Saved_Passwords/' 
    for path in os.listdir(dir_path):
        
        #check if current path is a file and if so add it to 'res'.
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    
    #checks if there are files to list, read or delete
    if len(res) == 0:
        print("There are no files")
        return

    else:
        #prints a numbered list of saved entries.
        print("Saved Passwords:\n")
        for results in res:
            print(str(x) + ". " + results) 
            x += 1

        if mode == 'read':
            
            usr_input = input("Select File To Read Or [b] To Cancel:\n")
            invalid = True
            while invalid == True:
                try:
                    #the user enters the number of the entry to read, which is found by its list position (hence -1).
                    file_path = dir_path + res[int(usr_input)-1]
                    invalid = False
                    
                except:
                    if usr_input == 'b':
                        return
                    else:
                        print("Please Enter The Number Of The Entry e.g. 4\n")
                        return
                    

            #output is be the plain text decryption output to be read.
            output = str(file_path).replace('.aes', '')

            print('\n\n\n' + str(file_path))
            pyAesCrypt.decryptFile(str(file_path), output, key)
            sel = open(output)
            print(sel.read() + '\n\n\n')
            sel = open(output)
            os.remove(output)

            if input("Copy Password To Clipboard? [y][n]\n") == 'y':
                pyperclip.copy(sel.readlines()[2].replace('Password:', ''))
            sel.close()

        

                
            
        if mode == 'delete':

            try:
                file_path = dir_path + res[int(input("Select File To Delete:\n"))-1]
                if input("Confirm [y][n]\n") == 'y':
                    os.remove(file_path)
                else:
                    read_entry(key, 'delete')
            except:
                return



    
           

    

    

    

    





