from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry1.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please make sure you haven't left any fields empty.")

    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?")

        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(f"{website} | {email} | {password}\n")
                entry1.delete(0, END)
                pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=my_image)
canvas.grid(row=0, column=1)

# Labels
label1 = Label(text="Website")
label1.grid(row=1, column=0)
label2 = Label(text="Email/Username")
label2.grid(row=2, column=0)
label3 = Label(text="Password")
label3.grid(row=3, column=0)

# Entry
entry1 = Entry(width=43)
entry1.grid(row=1, column=1, columnspan=2)
entry1.focus()
email_entry = Entry(width=43)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'xyz@gmail.com')
pass_entry = Entry(width=20)
pass_entry.grid(row=3, column=1)

# Buttons
button1 = Button(text="Generate Password", command=generate_password)
button1.grid(row=3, column=2)
button2 = Button(text="Add", width=36, command=save)
button2.grid(row=4, column=1, columnspan=2)

window.mainloop()
