def login(mode):

    import hashlib 
    import os
    import pyAesCrypt
    
    
    #reads the master password
    mp_file_path = os.getcwd() + '/Password_Manager/Saved_Passwords/master_password/master_password.txt'
    master_password_file = open(mp_file_path)
    master_password = master_password_file.read()
        
    #if the master password is already set
    if master_password != '':
        #compares to the hashed user input
        usr_imput = input("Enter Master Password:\n")

        if hashlib.sha256(usr_imput.encode('utf-8')).hexdigest() == master_password:  
            print("Success!")
        else:
            print("Incorrect Password\n")
            login('normal')

        master_password_file.close()

    #creates a new master password if none is set
    else:
        master_password = open(mp_file_path, 'w')
        usr_imput = input("Enter New Master Password:\n")
        master_password.write(str(hashlib.sha256(usr_imput.encode('utf-8'))).hexdigest())
        
    #generates a key to use for file encyption
    encrypt_hash = hashlib.sha224(usr_imput.encode('utf-8')).hexdigest()

    if mode == 'normal':
        return encrypt_hash

    if mode == 'reset':
        new_password = str(input("Enter New Master Password:\n"))

        if input("Confirm ['y' 'n']\n") == 'y':
            #derives a new encypt/decrypt key from new master password
            key = str(hashlib.sha224(new_password.encode('utf-8')).hexdigest())
    
            res = []
            dir_path = str(os.getcwd()) + "/Password_Manager/Saved_Passwords/"

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
   



