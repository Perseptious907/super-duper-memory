def setCred():
    username = input("create new username: ")
    password = input("create new password: ")

setCred()
print (username)
print (password)

def lifeIsGood():
    print('you are in')

def username():                             #username function
    confirm = input ('Username: ')  #this is my username variable
    
def password():                     #password function
    confirm_1 = input('Password: ')     #this is my password variable


    if (confirm == 'username'):   #if this reads yes then it lets you in
        password()
    elif (confirm != 'username'):       #if it is no then it does not and repeats
        print('try again')
        
    if (confirm_1 == 'password'):   #if this reads yes then it lets you in
        lifeIsGood()
    elif (confirm_1 != 'password'):       #if it is no then it does not and repeats
        print ("try again")
        

setCred()
username()

