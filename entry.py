import generate_password
import pyAesCrypt
import os
import pyperclip
import platform

def add_entry(key):
    system = platform.system()
    cwd = os.getcwd()
    title = str(input("Enter A Title:\n"))
    username = input("Enter The Username, Email Address or Leave Blank:\n")
    if system == 'Windows':
        file_path = cwd + "\Password_Manager\Saved_Passwords" + title + ".txt"
    else:
        file_path = cwd + "/Password_Manager/Saved_Passwords/" + title + ".txt"

    mode = str(input("[1] Generate Random Password \n[2] Add Password Manually\n[b] Back\n"))
    print(mode)
    if mode == "1":
        try:
            char_length = int(input("How Many Characters Should Be Included? (More = Better, Recomended: 128)\n"))
        except:
            print("Please Enter Whole Digits\n")
            add_entry(key)

        password = generate_password.generate_password(char_length)

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

    file_text = "Title: " + title + '\n' + "Username: " + username + '\n' + "Password: " + password
    file.write(file_text)
    file.close()
    output = file_path + ".aes"

    try:
        pyAesCrypt.encryptFile(file_path, output, key)
        os.remove(file_path)
        if input("Copy Password To Clipboard? [y][n]\n") == 'y':
            pyperclip.copy(password)
        print(file_path, output)
        

    except:
        print("The encyption key is incorrect or the file is corrupt.")
        

    return
    
def read_entry(key, mode):
    x = 1
    res = []
    if os.system == 'Windows':
        dir_path = os.getcwd() + '\Password_Manager\Saved_Passwords'
    else:
        dir_path = os.getcwd() + '/Password_Manager/Saved_Passwords/'

    for path in os.listdir(dir_path):
        
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    
    #checks if there are files to list, read or delete
    if len(res) == 0:
        print("There are no files")
        return

    else:
        print("Saved Passwords:\n")
        for results in res:
            print(str(x) + ". " + results) 
            x += 1

        if mode == 'read':
            file_path = dir_path + res[int(input("Select File To Read:\n"))-1]
            output = str(file_path).replace('.aes', '')

            print('\n\n\n' + str(file_path))
            pyAesCrypt.decryptFile(str(file_path), output, key)
            sel = open(output)
            print(sel.read() + '\n\n\n')
            sel = open(output)
            os.remove(output)
            if input("Copy Password To Clipboard? [y][n]\n") == 'y':
                pyperclip.copy(sel.readlines()[2].replace('Password:', ''))
                
            
            
        
        if mode == 'delete':

            try:
                file_path = dir_path + res[int(input("Select File To Delete:\n"))-1]
                if input("Confirm [y][n]\n") == 'y':
                    os.remove(file_path)
                else:
                    read_entry(key, 'delete')
            except:
                return



    
           

    

    

    

    





