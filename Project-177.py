import tkinter as tk

class userDB:
    def __init__(self):
        self.__username = "John"
        self.__password = "password123"
        self.captcha = "abcd"

    def showUser(self):
        name_label.config(text="Name : " + self.__username)
        password_label.config(text="Password : " + self.__password)
        captcha_label.config(text="Captcha : " + self.captcha)

def addUser():
    global user
    user.__username = name_entry.get()
    user.__password = password_entry.get()
    user.captcha = captcha_entry.get()
    print("Details Updated")

root = tk.Tk()
root.geometry("400x300")

name_label = tk.Label(root, text="Name : ")
name_label.place(relx=0.5, rely=0.1, anchor="center")

password_label = tk.Label(root, text="Password : ")
password_label.place(relx=0.5, rely=0.3, anchor="center")

captcha_label = tk.Label(root, text="Captcha : ")
captcha_label.place(relx=0.5, rely=0.5, anchor="center")

name_entry = tk.Entry(root)
name_entry.place(relx=0.7, rely=0.1, anchor="center")

password_entry = tk.Entry(root, show="*")
password_entry.place(relx=0.7, rely=0.3, anchor="center")

captcha_entry = tk.Entry(root)
captcha_entry.place(relx=0.7, rely=0.5, anchor="center")

update_button = tk.Button(root, text="Update Login Details", command=addUser)
update_button.place(relx=0.3, rely=0.7, anchor="center")

show_button = tk.Button(root, text="Show Profile", command=user.showUser)
show_button.place(relx=0.7, rely=0.7, anchor="center")

user = userDB()

root.mainloop()