allpasswords = {}

print ("\n\nWelcome to your password keeping app! Now type in a password to get started.")
password=input ("Please enter your password here> ")
print ("Good. You will have to remember that so you can see your passwords.")
username=input ("Now, please type in your name> ")
print (f"Well {username}, in this password keeping app, you can do a couple of things. To add a new password/username, type in new login and enter the website name that you are adding for. Then add the login for it. Now to search your password/username, type in the name of it and you can see it. Good. Well, now you know how to use this app. Continue!")

for _ in range(1000):
    search=input ("\n Type in [New Login] [Search Logins] ")
    if search.upper()=="NEW LOGIN":
        sitename=input("New Login. Okay, for which website? ")
        sitepass=input(f"Got it. what is your password for {sitename}? ")
        allpasswords[sitename]=sitepass
        
    elif search.upper()=="SEARCH LOGINS":
        sitename=input("Okay, so which website's logging do you want? ")
        masterpass=input(f"Got it, what is your master password? ")
        if masterpass==password:
            print(f"The password for {sitename} is {allpasswords[sitename]}.")
        else:
            print("Sorry, that is not the master password, so I cannot give you what you want. ")

    else:
        print("The only options are [New Login] [Search Logins] - please select properly")
