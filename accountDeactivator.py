import tkinter as tk
import sqlite3
import os
connection = sqlite3.connect("userdata.db")
cursor = connection.cursor()
with open("signedInAs.txt","r") as file:
    username = file.read()
    if username == "":
        os.startfile("loginGui.py")
        quit()
def drawErrorMessage(errMessage):
    newLabel = tk.Label(window, text=errMessage, highlightcolor="#ff0000")
    newLabel.place(x=225,y=275)
window = tk.Tk()
window.title("Account deactivator")
window.geometry("900x500")
window.resizable(False,False)

deactivateLabel = tk.Label(window,text = f"Do you want to deactivate your account named {username}(yes,no)")
deactivateEntry = tk.Entry(window,width=15)
deactivateLabel.place(x=50,y=250)
deactivateEntry.place(x=400,y=250)
def submit():
    deactivateText = deactivateEntry.get()
    deactivateEntry.delete(0,tk.END)
    match(deactivateText):
        case "yes":
            drawErrorMessage("account deactivated")
            with open("signedInAs.txt","w") as file:
                file.write("")
            cursor.execute("DELETE FROM Login WHERE Username = ?",(username,))
            cursor.execute("DELETE FROM Progress WHERE Username = ?",(username,))
            cursor.execute("DELETE FROM Ownership WHERE Username = ?",(username,))
            connection.commit()
            os.startfile("signin.py")
            quit()
        case "no":
            drawErrorMessage("account not deactivated")
        case _:
            drawErrorMessage("invalid choice")
def backToMainMenu():
    os.startfile("mainMenu.py")
    quit()
submitButton = tk.Button(window,text="submit",command=submit)
submitButton.place(x = 200,y=300)
backButton = tk.Button(window,text="⌫ Back to main menu",command=backToMainMenu)
backButton.place(x=0,y=0)
window.mainloop()