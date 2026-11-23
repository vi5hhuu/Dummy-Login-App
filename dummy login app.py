#correct - vishu@gmail.com
#password - 1234

email = input (" Enter your email: ")
if "@" in email:
    password = input (" Enter your password: ")

    if email == "vishu@gmail.com" and password == "1234":
        print ("Wellcome Vishu!")
    elif email == "vishu@gmail.com" and password != "1234":
        print ("Incorrect Password! Please try again. ")
        if password == "1234": 
         print ("Wellcome Vishu!")
        else:
         print ("Please try again. ")

    else:
     print ("Incorrect Credentisls! Plese try again. ")
else: 
 print("Incorrect Email. Plese enter again.")

