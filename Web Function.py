print("Welcome to CalliSues")
print("Sign up or Log in")
print("1. Sign Up")
print("2. Log in")
which = input("1/2: ")
     
if which == '1':
    print("Sign Up")
    par_stu = input("Parent or Student: ")
    if par_stu == 'Parent':
        print("Enter Username")
        username = input("Username: ")
        print("Welcome, " + username)
             
    if par_stu == 'Student':
        print("Enter Username")
        username = input("Username: ")
        class_code = ("ayi1259")
        cls_code = input("Enter your teacher's class code: ")
        if cls_code == class_code:
            print("Welcome, " + username)
        else:        
           print("Try again! - Error 404")
                       
if which == '2':        
    print("Log in")      
    log_user = ('Denzel' or 'Iyebiye' or 'Olamide')
    log_in = input("Enter Username: ")
    if log_in == log_user:  
        print("Welcome, " + log_in)
    if log_in != log_user:    
        print("Try again - Error 311")