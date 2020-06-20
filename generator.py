from tkinter import *
import pyperclip
import random
root = Tk()
root.geometry("400x400")
passstr = ""
passlen = 0

def generate():
	#all char between 33 and 125 except 34 and 92
	password = ""
	for i in range(passlen):
		password += random.choice(char(33),char(randomint(35,91)),char(randomint(93,125)))
	passstr.set(password)

def copytoclipboard():
	random_password = passstr.get()
	pyperclip.copy(random_password)

Label(root,text="Password Generator",font="Helvetica 20 bold").pack()
Label(root, text= "Enter password length").pack(pady=3)
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text="Generate Password", command=generate).pack(pady=7)
Entry(root, textvariable=passstr).pack(pady=3)
Button(root,text="Copy to clipboard",command=copytoclipboard).pack()

root.mainloop() 	
