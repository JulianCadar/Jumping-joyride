import tkinter as tk
import os
def backToMainMenu():
    os.startfile("mainMenu.py")
    quit()
window = tk.Tk()
window.geometry("900x450")
window.resizable(False,False)
window.title("Info")

labelText = """Welcome to Jumping Joyride! \n This is a platformer game about a cube traversing deadly obstacle courses \n in order to obtain valuables that allow him to customise his character and buy powerups to enhance his abilities"""
introLabel = tk.Label(window, text = labelText)
introLabel.place(x=150,y=20)

backButton = tk.Button(window,text="⌫ Back to main menu",command=backToMainMenu)
backButton.place(x=0,y=0)

controlsText= """Jump: Space Bar \n Move Right: D or Right arrow key \n Move Left: A or Left arrow key"""
controlsLabel = tk.Label(window, text=controlsText)
controlsLabel.place(x=350,y=100)
window.mainloop()