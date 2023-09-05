from tkinter import *
import tkinter.messagebox as messagebox
from gnenrator import *
from clipboard import *

#! -------------------------------- window settings ----------------------------------- !#
window = Tk() # import all the tkinter tool in a var and creat a window
icon_path = ".\Password generator\lock.ico"
window.iconbitmap(icon_path)
window.geometry("500x250")  #set a size for our window
window.configure(background="white")
window.resizable(width=False, height=False) # disable window resizabling
window.title("Password Generator") # add a title to the window
#! ------------------------------------------------------------------------------------ !#

#!---------------------------------- window title -------------------------------------- !#
main_title = Label(window, text="Password Generator", bg="white", font="Bold") # add a label to show the title 
main_title.pack(fill="both", side="top") # start the label
#!--------------------------------------------------------------------------------------- !#

#? ------------------------------------ Add Frames --------------------------------------- #?
passwordinfo = Frame(window, relief="solid", bg="white", width=250, height=125) # create a frame to hold complex and strength
strength_frame = Frame(passwordinfo, width=20, height=20, bg="white", bd=2, relief="solid") # create strength frame to hold lbl and text box
complex_frame = Frame(passwordinfo, width=20, height=20, bg="white", bd=2, relief="solid") # create the complex frame to hold checkboxes
generate_frame = Frame(window, relief="solid", bg="white", borderwidth=2) # create generate frame to hold generate button and generated password 
#? --------------------------------------------------------------------------------------- #?

#!---------------------------- strength objects --------------------------- #!
title_lbl_strength = Label(strength_frame, text="Strength", fg="black", bg="white") # add a lbl for strength frame title
length_lbl = Label(strength_frame, text="length : ", bg="white") # show user where to add the length of password

length_num = StringVar(window)

length_text = Entry(strength_frame, bg="white", textvariable=length_num, width=10) # text box for user length password
title_lbl_strength.pack(side="top", fill="both") 
length_lbl.pack(side="left", fill="both")
length_text.pack(side="left")
#! ------------------------------------------------------------------------ #!

#? ------------------------------------------- password complex frame objects-------------------------------------------- ?#
complex_var = IntVar()
simple_var = IntVar()
simplechk = Checkbutton(complex_frame,  text="Simple Password", bg="white", onvalue= 1, offvalue=0, variable=simple_var) # add a check box with simple password option text
complexchk = Checkbutton(complex_frame, text="Complex Password", bg="white", onvalue=1, offvalue=0, variable=complex_var) # add a check box with complex password option text
title_lbl_complex = Label(complex_frame, text="Complexies", fg="black", bg="white") # add title for complex frame
title_lbl_complex.pack(side="top", fill="both")
simplechk.pack(padx= 10, side="left") # run complex pass check box
complexchk.pack(padx= 10, side="left") # run simple pass check box
#? --------------------------------------------------------------------------------------------------------------------- ?#

#?-------------------------------- Event Handler----------------------------?#
def gen_pass_btn():
    try:
        if (complex_var.get() == 1 and simple_var.get() == 0) :
            generated_password_txtbox.delete(0, END)
            pass_length = length_num.get()
            pass_length = int(pass_length)
            password = generate_password(pass_length, True)
            generated_password_txtbox.insert(0, password)
        elif (simple_var.get() == 1 and complex_var.get() == 0) :
            generated_password_txtbox.delete(0, END)
            pass_length = length_num.get()
            pass_length = int(pass_length)
            password = generate_password(pass_length, False)
            generated_password_txtbox.insert(0, password)
        else:
            messagebox.showinfo("wrong input", "please check if you do something wrong")
    except:
        generated_password_txtbox.insert(0, "wrong input! try again")
#?--------------------------------------------------------------------------?#

#? --------------------------- Generate Password Frame Objects ------------------------- #?
pass_frame_lbl = Label(generate_frame, text="Generate Password", bg="white", fg="black")
geberatbtn = Button(generate_frame, text="Generate Password", font=("Arial", 10),
                     bg = "white", fg = "black",command=gen_pass_btn, relief="groove",
                     border=0) # creat a button and personalized it
copy_btn = Button(generate_frame, text="Copy", relief="groove", bg="white", border=0) # add a btn to copy text that generate btn show in the text box

generated_password_txtbox = Entry(generate_frame, relief="groove", border=2, width= 25) # an entry to show the password

def copy_text(): # define a function to copy the generated password
    text = generated_password_txtbox.get()
    copy(text)
    messagebox.showinfo("Copy", "Text copied to clipboard.") # show a messege for user and say the password is ready to use
copy_btn.configure(command=copy_text) # bind the copy function to the copy btn

copy_btn.pack(side="left")
generated_password_txtbox.pack(side="left",fill="x")
#pass_frame_lbl.pack(side="top", fill="x")
geberatbtn.pack(side="right", padx=20, pady= 20) # run generate button 
#? -------------------------------------------------------------------------------------- #?

#! ---------------------------- Pack the Frames --------------------------- #!
passwordinfo.pack(fill="both", expand=True, pady=5) 
strength_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
complex_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
generate_frame.pack(side="bottom", fill="both", expand=True, padx=10, pady=10)
#! ------------------------------------------------------------------------ #!

window.mainloop() # run the window 
