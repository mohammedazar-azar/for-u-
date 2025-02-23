import tkinter as tk
from tkinter import*
from tkinter import messagebox
import random



window=tk.Tk()
window.title("will you be my_$_0_$_")
window.geometry("440x440")
window.iconbitmap(r"c:\Users\LENOVO\Downloads\xyz.png")
window['bg']="white"

window.resizable(False,False)
window.attributes('-alpha',0.8)


ś
label_text = tk.StringVar()
label_text.set("Will you be my GF\n <3")

def n():
    random_x = random.randint(0, window.winfo_width() - b.winfo_width())
    random_y = random.randint(0, window.winfo_height() - b.winfo_height())
    b.place(x=random_x, y=random_y)
    
    
    label_text.set("are you sure")
    window['bg']="sky blue"




def k():
  
   
 label_text.set("bye..tc<3")


 window.after(3000,window.destroy)
   

def s():

     
 window['bg']="light pink"
 
 label_text.set("i love you \n my life... \n <3")

 j=Button(window,text="bye..<3",font=("italic",15,"bold"),bg="sky blue",command=k)
 j.pack(side=LEFT)
 
a = tk.Label(window, textvariable=label_text, justify="center", font=("italic", 15, "bold"),  bg="light pink", cursor="plus", relief="solid")
a.pack(padx=10, pady=10, expand=True)

c=Button(window,text="yes<3",font=("italic",15,"bold"),bg="green",command=s,relief="raised")
c.place(x=130, y=300)

b=Button(window,text="noo!!",font=("italic",15,"bold"),bg="red",command=n,relief="raised")

b.place(x=230, y=300)



window.mainloop()
