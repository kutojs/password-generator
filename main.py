import os
import sys
import string
import random
import tkinter as tk
from tkinter.constants import DISABLED, NORMAL
import tkinter.font as tkFont
import time

application_path = os.path.dirname(sys.executable)

window = tk.Tk()
title = window.title("Password Generator")
window.geometry("500x500")
window.resizable(0, 0)
window.configure(bg="#404040")

font = tkFont.Font(family="Calibri", size=36)


def gen():
    label = window.children["frame_main"].children["password"]
    sequence = string.ascii_letters + string.digits
    pw = "".join(random.choice(sequence) for i in range(15))
    label.configure(text=pw)


def copy():
    password_label: tk.Label = window.children["frame_main"].children["password"]
    copy_button: tk.Button = window.children["frame_main"].children["copy_password"]
    text = password_label["text"]
    if text == "Password will show here.":
        copy_button.config(text="No password to copy.", state=DISABLED)
        time.sleep(1.5)
        copy_button.config(text="Copy Password", state=NORMAL)
        pass
    else:
        window.clipboard_clear()
        window.clipboard_append(password_label["text"])
        copy_button.config(text="Copied", state=DISABLED)
        time.sleep(1.5)
        copy_button.config(text="Copy Password", state=NORMAL)


frame = tk.Frame(master=window, bg="#404040", name="frame_main")
frame.pack_propagate(0)
frame.pack(fill=tk.BOTH, expand=1)
label = tk.Label(master=frame, text="Password Generator", font=font)
password = tk.Label(
    master=frame,
    text="Password will show here.",
    name="password",
    font=font,
    wraplength=500,
    justify="center",
)
button = tk.Button(master=frame, text="Generate Password",
                   command=gen, font=font)
copyButton = tk.Button(
    master=frame, text="Copy Password", name="copy_password", command=copy, font=font
)

label.pack()
button.pack()
password.pack()
copyButton.pack()
window.mainloop()
