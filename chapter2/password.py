# password is 1234

password = input('What is the password?\n')
while password != '1234':
    password = input('Incorrect password.\nWhat is the password?\n')
if password == '1234':
    print('The password is correct')
