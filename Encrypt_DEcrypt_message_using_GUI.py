# import tkinter module
from tkinter import *

# import fernet function from cryptography module
from cryptography.fernet import Fernet

# creating root object
root = Tk()

# defining size of the window
root.geometry('1500x800')

# setting up the title of the window
root.title("Python Project")

Tops = Frame(root)
Tops.pack(side=TOP)

Bottom = Frame(root)
Bottom.pack(side=LEFT)

# set heading
l1 = Label(Tops, text="Encrypt and decrypt message", font='comicsansms 20 bold', fg="Black", bd=10, anchor='w', pady=50)
l1.grid(column=0, row=0)

# initializing variables
message = StringVar()
Encrypt_message = StringVar()
Decrypt_message = StringVar()

# label for the message
l1_message = Label(Bottom, text='Enter a message : ', font=('Verdana', 15), bd=16, anchor="w", padx=20, pady=15)
l1_message.grid(column=0, row=1)

# Entry box for the message
txt_msg = Entry(Bottom, width=50, font='comicsansms 16', textvariable=message, bd=10, insertwidth=6, bg="powder blue")
txt_msg.grid(column=1, row=1)

# label for the Encrypted message
l2_EncryptMessage = Label(Bottom, text='Encrypted message : ', font=('Verdana', 15), bd=16, anchor="w", padx=20,
                          pady=15)
l2_EncryptMessage.grid(column=0, row=2)

# Entry box for the Encrypted message
Encrypt_txt_msg = Entry(Bottom, width=50, font='comicsansms 16', textvariable=Encrypt_message, bd=10, insertwidth=6,
                        bg="powder blue")
Encrypt_txt_msg.grid(column=1, row=2)

# label for the Decrypted  message
l3_DecryptMessage = Label(Bottom, text='Decrypted Message : ', font=('Verdana', 15), bd=16, anchor="w", padx=20,
                          pady=15)
l3_DecryptMessage.grid(column=0, row=3)

# Entry box for the Decrypted message
Decrypt_txt_msg = Entry(Bottom, width=50, font='comicsansms 16', textvariable=Decrypt_message, bd=10, insertwidth=6,
                        bg="powder blue")
Decrypt_txt_msg.grid(column=1, row=3)


# Function of encrypting and Decrypting message
def Encrypt_Decrypt_Message():
    Msg = message.get()
    key = Fernet.generate_key()

    f = Fernet(key)

    encode_message = Msg.encode()
    encryptMsg = f.encrypt(encode_message)
    if Msg == "":
        Encrypt_message.set("")
    else:
        Encrypt_message.set(encryptMsg)

    decryptMsg = f.decrypt(encryptMsg)
    decode_message = decryptMsg.decode()
    Decrypt_message.set(decode_message)


# Function to reset the window
def Reset():
    message.set("")
    Decrypt_message.set("")
    Encrypt_message.set("")


# Exit function
def Exit():
    root.destroy()


# Show message button
btnResult = Button(Bottom, padx=15, pady=8, bd=16, fg="black",
                   font=('arial', 16, 'bold'), width=10, bg="grey",
                   text="Result", command=Encrypt_Decrypt_Message).grid(column=1, row=4)

# Reset button
btnReset = Button(Bottom, bd=16, padx=15, pady=8,
                  fg="black", font=('arial', 16, 'bold'),
                  width=10, text="Reset", bg="green",
                  command=Reset).grid(row=7, column=2)

# Exit button
btnExit = Button(Bottom, bd=16, padx=15, pady=8,
                 fg="black", font=('arial', 16, 'bold'),
                 width=10, text="Exit", bg="red",
                 command=Exit).grid(row=7, column=3)

# keeps window alive
root.mainloop()
