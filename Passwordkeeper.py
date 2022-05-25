print ("Welcome to your password keeping app! Now type in a password to get started.")
password=input ("Please enter your password here> ")
print ("Good. You will have to remember that so you can see your passwords.")
username=input ("Now, please type in your name> ")
print (f"Well {username}, in this password keeping app, you can do a couple of things. To add a new password, type in new password and enter your brand new password. To add a new username, type in new username and enter your brand new username. You also have to give each one a name. Now to search your password/username, type in the name of it and you can see it. Good. Well, now you know how to use this app. Continue!")
search=input ("Type in new password, new username, or search an existing username/password.")
if search.upper()=="NEW PASSWORD":
    print("ok fine we'll do a new password")
