def generate_password():
    import random

    inc_lc = False
    inc_uc = False
    inc_n = False
    inc_sym = False
    inc_extasc = False

    lower_case_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    upper_case_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ["{","|","}","~","[","]","^","_","`",":",";","<","=",">","?","@","!",",","#","$","%","&","'","(",")","*","+",",","-",".","/"]
    ext_ascii = ["","","","","","","","","","","","","","","","¡","¢","£","¤","¥","¦","§","¨","©","ª","«","¬","®","¯","°","±","²","³","´","µ","¶","·","¸","¹","º","»","¼","½","¾","¿","À","Á","Â","Ã","Ä","Å","Æ","Ç","È","É","Ê","Ë","Ì","Í","Î","Ï","Ð","Ñ","Ò","Ó","Ô","Õ","Ö","×","Ø","Ù","Ú","Û","Ü","Ý","Þ","ß","à","á","â","ã","ä","å","æ","ç","è","é","ê","ë","ì","í","î","ï","ð","ñ","ò","ó","ô","õ","ö","÷","ø","ù","ú","û","ü","ý","þ","ÿ"]

    char_len = int(input("How Many Characters Should Be Included?\n"))

    if input("Include Lowercase Letters? 'y' 'n'\n") == 'y':
        inc_lc = True
    if input("Include Uppercase Letters? 'y' 'n'\n") == 'y':
        inc_uc = True
    if input("Include Numbers? 'y' 'n'\n") == 'y':
        inc_n = True
    if input("Include Symbol Characters? 'y' 'n'\n") == 'y':
        inc_sym = True
    if input("Include Extended Ascii Characters? (these may not work on all sites) 'y' 'n'\n"):
        inc_extasc = True

    password = []


    for x in range(char_len):
        if inc_lc == True:
            password.append(random.choice(upper_case_letters))
        if inc_uc == True:
            password.append(random.choice(upper_case_letters))
        if inc_n == True:
            password.append(random.choice(numbers))
        if inc_sym == True:
            password.append(random.choice(symbols))
        if inc_extasc == True:
            password.append(random.choice(ext_ascii))
        del password[char_len:]
    return str(' '.join(password)).replace(' ', '')






