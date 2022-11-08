import tkinter
from tkinter import *
import re


root=Tk()
root.title("Email Validation")
root.geometry("350x250")

class Muritala:
    
    def Email_validate(self): 
        try:
        
            UserResponse= Label_Email_Entry.get()
            ch=re.compile("^[\w.!#$%&’*+/]+@[\w]+\.\w{2,3}(\.\w{2,3})?$")
            mw=ch.match(UserResponse)
            print(mw)
            if mw==None:
                # print("error")
                 Resultlabel.config(text="Invalid Email Pattern", fg="Red")
            else:
                 Resultlabel.config(text="Valid Email", fg="Red")
        except:
            Resultlabel.config(text="Invalid Email", fg="Red")
        finally:
             print()
       
        
Raph= Muritala()
# print(Raph.Email_validate())


Mainframe= Frame(root)
Mainframe.pack()#grid()

# Label_Title= Label(Mainframe, text="", font=("Arial", 12))
# Label_Title.grid(row=0, column=0)
# Label_Title= Label(Mainframe, text="", font=("Arial", 12))
# Label_Title.grid(row=1, column=0)
Label_Email= Label(Mainframe, text="Email", font=("Baskerville", 12)).pack(pady=30)#grid(row=0, column=0)

Label_Email_Entry= Entry(Mainframe, font=("Arial", 16))
Label_Email_Entry.pack()#

# Label_Password= Label(Mainframe, text="Password", font=("Arial", 12)).grid(row=1, column=0)

# Label_Password_Entry= Entry(Mainframe, font=("Arial", 16))
# Label_Password_Entry.grid(row=1, column=2)

Validate_Btn= Button(Mainframe, text="Validate", width=10, font=("Arial", 11), bg="#6833FF", command=Raph.Email_validate)
Validate_Btn.pack()#grid(row=2, column=2)

Resultlabel= Label(Mainframe, text="", font=("Arial",12))
Resultlabel.pack()


# Raph.Email_validate()
root.mainloop()