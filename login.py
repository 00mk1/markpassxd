def login():
    import hashlib 

    master_password_file = open('/home/mark/google-drive/2022/3TCS/Python/Password_Manager/Saved_Passwords/master_password.txt')
    master_password = master_password_file.read()
        
    #not blank
    if master_password != '':

        #compares to the hashed user input
        usr_imput = input("Enter Master Password:\n")
        if hashlib.sha256(usr_imput.encode('utf-8')).hexdigest() == master_password:  
            print("Great Success!")
        else:
            print("Not Success!")

        master_password_file.close()

    #creates a new master password
    else:
        master_password = open('/home/mark/google-drive/2022/3TCS/Python/Password_Manager/Saved_Passwords/master_password.txt', 'w')
        usr_imput = input("Enter New Master Password:\n")
        master_password.write(hashlib.sha256(usr_imput.encode('utf-8'))).hexdigest()
        master_password_file.close()

    encrypt_hash = hashlib.sha224(usr_imput.encode('utf-8')).hexdigest()
    return encrypt_hash



