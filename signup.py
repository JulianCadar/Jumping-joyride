import tkinter as tk
import sqlite3
import os
import datetime
connection = sqlite3.connect("userdata.db")
cursor = connection.cursor()
loginTable = cursor.execute("SELECT * FROM Login")
#cursor.execute("CREATE TABLE IF NOT EXISTS Login (Username varchar(255), Password varchar(255), UserID int, AccountType varchar(255), email varchar(255))")
window = tk.Tk()
window.geometry("900x900")
window.resizable(False,False)
window.title("Sign Up Page")
#num of rows
numOfRowsInLogin = len(cursor.fetchall())
#username label and entry
usernameLabel = tk.Label(window,text = "Create your username: ")
usernameLabel.place(x = 100,y = 100)

usernameEntry = tk.Entry(window,width=50)
usernameEntry.place(x=225,y=100)

#password label and entry
passwordLabel = tk.Label(window,text = "Create your Password: ")
passwordLabel.place(x = 100,y = 150)

passwordEntry = tk.Entry(window,width=50)
passwordEntry.place(x=225,y=150)
#password confirm label and entry
passwordConfirmLabel = tk.Label(window,text = "Confirm your password: ")
passwordConfirmLabel.place(x = 90,y = 200)

passwordConfirmEntry = tk.Entry(window,width=50)
passwordConfirmEntry.place(x=225,y=200)
#email label and entry
emailLabel = tk.Label(window,text = "Create your email: ")
emailLabel.place(x = 120,y = 250)
#button to go to sign in page if the user has already registered
def openSignInProgram():
    os.startfile("signin.py")
    quit()
signInButton = tk.Button(window,text="Already a user?, Sign in Here!", command=openSignInProgram)
signInButton.place(x=275,y=350)


emailEntry = tk.Entry(window,width=50)
emailEntry.place(x=225,y=250)
def drawErrorMessage(errMessage):
    newLabel = tk.Label(window, text=errMessage, highlightcolor="#ff0000")
    newLabel.place(x=225,y=275)

#create iterable object of all user data
allUserData = []
for item in cursor.execute("SELECT * FROM Login"):
    allUserData.append(item)
#submit function
def submit():
    #get value from entry widgets and then clear them
    usernameText = usernameEntry.get()
    usernameEntry.delete(0,tk.END)

    passwordText = passwordEntry.get()
    passwordEntry.delete(0,tk.END)

    passwordConfirmText = passwordConfirmEntry.get()
    passwordConfirmEntry.delete(0,tk.END)

    emailText = emailEntry.get()
    emailEntry.delete(0,tk.END)
    #presence check
    if usernameText == "" or passwordText == "" or passwordConfirmText == "" or emailText == "":
        drawErrorMessage("You must fill out all fields")
    #generate userID
    else:
        userID = numOfRowsInLogin+1 #the first user will have an ID of 1
    #account type(will be normal if created through registration, moderator if created some other way)
        accountType = "Normal"
        #double entry check
        if passwordText != passwordConfirmText:
            drawErrorMessage("Passwords do not match")
        else:
            if len(passwordText)<8:
                drawErrorMessage("password not long enough")
            else:
                #check if the user somehow already exists
                for row in allUserData:
                    if usernameText in row or emailText in row:
                        drawErrorMessage("username or email already exists")
                        break
                else:
                    userdata = [(usernameText,passwordText,userID,accountType,emailText)]
                    cursor.execute("INSERT OR REPLACE INTO Login VALUES(?,?,?,?,?)",userdata[0])
                    connection.commit()
                    drawErrorMessage(f"Account Created Successfully.")
                    cursor.execute("INSERT OR REPLACE INTO Ownership VALUES(?,?,?,?)",(usernameText,"1",str(datetime.datetime.now()),500))
                    connection.commit()
                    
#submit button
SubmitButton = tk.Button(window,text = "Submit",width= 5,height=1,command=submit)
SubmitButton.place(x= 350,y= 300)
window.mainloop()