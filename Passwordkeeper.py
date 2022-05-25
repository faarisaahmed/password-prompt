print ("Welcome to your password keeping app! Now type in a password to get started.")
password=input ("Please enter your password here> ")
print ("Good. You will have to remember that so you can see your passwords.")
username=input ("Now, please type in your name> ")
print (f"Well {username}, in this password keeping app, you can do a couple of things. To add a new password, type in new password and enter the website name that you are adding for. Then add the password for it. To add a new username, type in new username and enter the website name that you are adding for. Then add the username for it. Now to search your password/username, type in the name of it and you can see it. Good. Well, now you know how to use this app. Continue!")
search=input ("Type in new password, new username, or search an existing username/password. ")
if search.upper()=="NEW PASSWORD":
    for _ in range(3):
        sitename=input("Ok. To add a password, I will ask you some questions. What is the website you are adding your password for? ")
        sitepass=input(f"What is your password for {sitename}? ")
        allpasswords[sitename]=sitepass
