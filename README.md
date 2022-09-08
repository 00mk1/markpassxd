# MarkPassxD - A Simple CLI Password Manager
FOSS - Mark Barlass 2022, use as you wish.

This program was made for the NCEA standards AS91906 and AS91907 and is written in Python.
While I have done my best to make this program secure, Python is incapible of low level memory management so sectors where sensitive data was stored cannot be wiped. In addition to this, I am still an amature programmer so please DO NOT use this program to store ANY sensitive information.


MarkPassxD has the following features:

Generate a random password of specified length and character types.
Encrypt and save a password along with a username and identifiable title.
Decrypt and read saved passwords.
Delete saved passwords.

Passwords are encrypted using AES 256. The program requires a master password which is saved as a salted hash value. 


## Installation Instructions

#### Dependancies 
This program requires Python 3 as well as the following third party libraries. It will not work unless they are installed:

'pyAesCrypt'
'Pyperclip'

These can be installed with the following commands:

'pip install pyperclip'
'pip install pyAesCrypt'


#### Method One (GitHub)
Go to 'https://github.com/00mk1/markpassxd/releases' in your browser, find the most recent release and download the correct version for your device from the 'assets' section. Extract the downloaded .zip file to the desired location e.g. 'Home/ or Users\You\Program Files\'.

#### Method Two (source code)
If you have git installed on your device, open a terminal and enter the following:
'git clone https://github.com/00mk1/markpassxd.git'.

Then cd into the cloned directory. Use ls to make sure you can see 'main.py'.

If on Linux use:
'python3 main.py'

If on Windows use:
'python main.py'


## Use Instructions
Run 'main.py'

To select a option type in the corrosponding number or letter when prompted.
When prompted you may enter 'b' to return to a previous state.
When given a '[y][n]' option you may enter nothing to skip or cancel the operation. 


