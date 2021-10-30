from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


PINK = "#E9A6A6"
RED = "#e7305b"
GREEN = "#9bdeac"
ORANGE = "#FDA65D"
BLUE = "#88E0EF"
YELLOW = "#f7f5dd"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nUsername: {username} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                data = f"{website} | {username} | {password}\n"
                file.write(data)
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(123, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, pady=3)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0, pady=3)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, pady=3)

website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

username_entry = Entry(width=50)
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
username_entry.insert(0, "example@email.com")

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, sticky="EW")

add_button = Button(text="Add", width=35, bd=0, bg=GREEN, activebackground=YELLOW, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW", pady=2)

generatepass_button = Button(text="Generate Password", bd=0, bg=BLUE, activebackground=YELLOW, command=generate_password)
generatepass_button.grid(column=2, row=3, sticky="EW", ipadx=2, padx=1)

window.mainloop()
