import sqlite3
import tkinter as tk
import os
connection = sqlite3.connect("userdata.db")
cursor = connection.cursor()
#main loop
window = tk.Tk()
window.geometry("900x900")
window.resizable(False,False)
window.title("Sign in Page")

#widgets
usernameLabel = tk.Label(window,text="Username: ")
usernameEntry = tk.Entry(window,width="50")
usernameLabel.place(x=310,y=430)
usernameEntry.place(x=375,y=430)

passwordLabel = tk.Label(window,text="Password: ")
passwordEntry = tk.Entry(window,width ="50")
passwordLabel.place(x=310,y=470)
passwordEntry.place(x=375,y=470)

emailLabel = tk.Label(window,text="Email: ")
emailEntry = tk.Entry(window,width ="50")
emailLabel.place(x=310,y=510)
emailEntry.place(x=375,y=510)


#create iterable object of all user data
allUserData = []
for item in cursor.execute("SELECT * FROM Login"):
    allUserData.append(item)
#open main menu function
def openMainMenu():
    os.startfile("mainMenu.py")
    quit()
def openSignUpPage():
    os.startfile("signup.py")
    quit()
#error message function
signupbutton = tk.Button(window,command=openSignUpPage, text="Don't have an account? \n Sign up here!")
signupbutton.place(x=400,y=600)
def drawErrorMessage(errMessage):
    newLabel = tk.Label(window, text=errMessage, highlightcolor="#ff0000")
    newLabel.place(x=225,y=275)
#submit method
def submit():
    usernameText = usernameEntry.get()
    passwordText = passwordEntry.get()
    emailText = emailEntry.get()

    usernameEntry.delete(0,tk.END)
    passwordEntry.delete(0,tk.END)
    emailEntry.delete(0,tk.END)
    #check if exists in table
    recordExists = False

    for row in allUserData:
        if usernameText in row and emailText in row and passwordText in row:
            recordExists= True
            break
    if recordExists:
        drawErrorMessage("Sign in successful: You may proceed")
        #draw a button to go to the main menu
        mainMenuButton = tk.Button(window,text="Main Menu",command=openMainMenu)
        mainMenuButton.place(x=310,y=630)
        #keep track of who is currently signed in
        with open("signedInAs.txt","w") as file:
            file.write(f"{usernameText}")
            
    else:
        drawErrorMessage("User with those credentials does not exist")




submitButton = tk.Button(window,width=25,height=1,text="Submit",command=submit)
submitButton.place(x=400,y=550)

window.mainloop()