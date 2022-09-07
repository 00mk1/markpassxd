#MarkPassxD - Mark Barlass 2022

#Handles creating a master password, logging in and changing the master password.

#mode is the operating mode of this function. It can be used in normal mode or reset [master password] mode.
def login(mode):
    import platform
    import hashlib 
    import os
    import pyAesCrypt

    #gets the operating system.
    system = platform.system()
   
    #windows uses "\" to seperate folders, while unix like (Mac, DSB, Linux) systems use "/".
    if system == 'Windows':
        mp_file_path = os.getcwd() + '\Saved_Passwords\master_password\master_password.txt'
        salt_path = os.getcwd() + '\Saved_Passwords\master_password\salt.txt'
    else:
        mp_file_path = os.getcwd() + '/Saved_Passwords/master_password/master_password.txt'
        salt_path = os.getcwd() + '/Saved_Passwords/master_password/salt.txt'

    #reads the master password.
    master_password_file = open(mp_file_path)
    master_password = master_password_file.read()
    

    #if the master password is already set.
    if master_password != '':
        #the salt is a string added to the password to make it more secure.
        salt_file = open(salt_path)
        salt = salt_file.read()
        
        #gets the user input and adds the salt value.
        usr_imput = input("Enter Master Password:\n") + salt

        #compares the hased user input with the saved password.
        if hashlib.sha256(usr_imput.encode('utf-8')).hexdigest() == master_password:  
            print("Success!")
        else:
            print("Incorrect Password\n")
            login('normal')

        master_password_file.close()

    #creates a new master password if none is set
    else:
        salt_file = open(salt_path, 'w')
        #writes a random salt to the salt file
        salt_file.write(str(os.urandom(32)))
        salt_file = open(salt_path, 'r')
        salt = salt_file.read()

        master_password = open(mp_file_path, 'w')
        usr_imput = input("Enter New Master Password:\n") + salt
        #writes the new master password
        master_password.write(hashlib.sha256(usr_imput.encode('utf-8')).hexdigest())
    
    salt_file.close()
    
    #generates a key to use for file encyption
    encrypt_hash = hashlib.sha224(usr_imput.encode('utf-8')).hexdigest()

    if mode == 'normal':
        return encrypt_hash

    #allows the user to change the master password.
    if mode == 'reset':
        new_password = str(input("Enter New Master Password:\n"))

        if input("Confirm [y][n]\n") == 'y':
            #derives a new encypt/decrypt key from new master password
            key = str(hashlib.sha224(new_password.encode('utf-8')).hexdigest())
    
            res = []

            if system == 'Windows':
                dir_path = str(os.getcwd()) + "\Saved_Passwords"
            else:
                dir_path = str(os.getcwd()) + "/Saved_Passwords/"
            
            #for each saved password
            for path in os.listdir(dir_path):
                # check if current path is a file
                if os.path.isfile(os.path.join(dir_path, path)):

                    res.append(path)
                    file_path = dir_path + path
                    output = file_path.replace('.aes', '')

                    #decrypts saved password with old password
                    pyAesCrypt.decryptFile(file_path, output, encrypt_hash)
                    os.remove(file_path)
                    #re-encrypts file wth new password
                    pyAesCrypt.encryptFile(output, file_path, key)
                    os.remove(output)
                    #saves the new master password
                    master_password = open(mp_file_path, 'w')
                    master_password.write(str(hashlib.sha256(new_password.encode('utf-8')).hexdigest()))
                    master_password_file.close()
                    return key

        else:
            return
   



