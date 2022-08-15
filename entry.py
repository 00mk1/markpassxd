import generate_password
import pyAesCrypt
import os

def add_entry(key):

    cwd = os.getcwd()
    title = str(input("Enter A Title:\n"))
    username = input("Enter The Username, Email Address or Leave Blank:\n")
    file_path = cwd + "/Password_Manager/Saved_Passwords/" + title + ".txt"

    if input("1. Generate Random Password \n2. Add Password Manually\n") == '1':
        password = generate_password.generate_password()
    else:
        password = input("Enter Password:\n")

    try:
        file = open(file_path, 'x')
    except:
        if input("This File Already Exists, Would You Like To Overwrite It? 'y' 'n' \n") == 'y':
            file = open(file_path, 'w')

    file_text = "Title: " + title + '\n' + "Username: " + username + '\n' + "Password: " + password
    file.write(file_text)
    file.close()
    output = file_path + ".aes"

    pyAesCrypt.encryptFile(file_path, output, key)
    os.remove(file_path)
    return
    
def read_entry(key, mode):
    x = 1

    res = []
    dir_path = '/home/mark/Desktop/Python/Password_Manager/Saved_Passwords/'
    for path in os.listdir(dir_path):
        
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)

    for results in res:
        print("Saved Passwords:\n" + str(x) + ". " + results) 
        x += 1
    if mode == 'read':

        try:
            file_path = dir_path + res[int(input("Select File To Read:\n"))-1]
            output = str(file_path).replace('.aes', '')

            print(str(file_path))
            pyAesCrypt.decryptFile(str(file_path), output, key)
            sel = open(output)
            print(sel.read())
            os.remove(output)
        except:
            return
    
    if mode == 'delete':

        try:
            file_path = dir_path + res[int(input("Select File To Delete:\n"))-1]
            if input("Confirm ['y' 'n']\n") == 'y':
                os.remove(file_path)
        except:
            return



    
           

    

    

    

    





