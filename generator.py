from tkinter import *
import pyperclip
import random
root = Tk()
root.geometry("400x400")
passstr = StringVar()
passlen = IntVar()
passlen.set(0)

def generate():
	#all char between 33 and 125 except 34 and 92
	password = ""
	for i in range(passlen.get()):
		randomint = random.randint(33,125)
		if randomint != 92 and randomint != 34:
			password += chr(randomint)
		else:
			password += random.choice([chr(33),chr(random.randint(35,91)),chr(random.randint(93,125))])
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
