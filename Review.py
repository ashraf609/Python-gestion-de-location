from tkinter import *
from tkinter import messagebox
def save_info():
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    age_info = age.get()
    age_info = str(age_info)
    print(firstname_info, lastname_info , age_info)
    
    file = open("user.txt","w")
    file.write(firstname_info)
    file.write(lastname_info)
    file.write(age_info)
    file.close()
    messagebox.showinfo("Merci" , "votre")
    
    
    
screen=Tk()
screen.geometry("500x500")
screen.title("Python Form")
screen.configure(bg="#fff")
heading = Label(text="Review app ",bg = "#0B4C5F" , fg = "white" , font=('tajawal' , 13 , 'bold'), width = "500", height = "3" ) 
heading.pack()
firstname_text=Label(text="Firstname * ",)
lastname_text=Label(text="lastname * ",)
age_text=Label(text="Age * ",)

age_text.place(x = 15, y = 210)
firstname_text.place(x = 15 , y= 70)
lastname_text.place(x = 15 , y = 140)


firstname = StringVar()
lastname = StringVar()
age = IntVar()

firstname_entry = Entry(textvariable = firstname, width = "30")
lastname_entry = Entry(textvariable = lastname, width = "30")
age_entry = Entry(textvariable = age, width = "30")


firstname_entry.place(x =15, y= 100)
lastname_entry.place(x =15, y= 180)
age_entry.place(x =15, y= 240)

register= Button(screen,text = "Register", width = "30", height = "2" , font=('tajawal' , 10 , 'bold') ,  fg="white" ,  command = save_info, bg = "#0B4C5F")
register.place(x = 95, y = 320)





screen.mainloop()