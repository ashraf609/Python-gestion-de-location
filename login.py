from tkinter import *
import tkinter as tk
from tkinter import messagebox
from email.message import EmailMessage
import mysql.connector
import webbrowser 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rootroot@@1234",
  database = "python_database",
)
root = Tk()

root.title("Login")
root.configure(bg="#fff")
window_width,window_height = 925,500    
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight() 
position_top = int(screen_height/3 - window_height/3)
position_right = int(screen_width / 2 - window_width/2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

root.resizable(False , False)
global Username
global Paswword
Username = tk.StringVar()#pour rendre les valeurs string
Password = tk.StringVar()
def logs():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM login WHERE BINARY Username = '%s' and BINARY Password = '%s'" % (Username.get(),Password.get())
    mycursor.execute(sql)
    if mycursor.fetchone():
        messagebox.showinfo("Succres" , "Vos donnes son enregistree")
        import Location
    else:
        messagebox.showerror("error" , "Les donness sont incorrects")

def signuUp():
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rootroot@@1234",
            database = "python_database",
        )
        c = connection.cursor()
        def insertDat():
            name = user.get()
            email = code.get()
            passw = conf.get()

            insert_data = "INSERT INTO `users`(`name` , `email` , `passw`) VALUES(%s,%s,%s)"
            vals = (name , email , passw)
            c.execute(insert_data , vals)
            connection.commit()
            messagebox.showinfo("Success" , "Bienvenue a l'application")
            import Location
        window = Toplevel(root)
        window.title("SignUp")
        window.configure(bg="#fff")
        window.resizable(False,False)
        window_width,window_height = 925,500    
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight() 
        position_top = int(screen_height/3 - window_height/3)
        position_right = int(screen_width / 2 - window_width/2)
        window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        img = PhotoImage(file="Singin.png")


        Label (window, image=img, border=0, bg='white').place(x=50,y=90)

        frame=Frame(window,width=350, height=390, bg='white')
        frame.place(x=480,y=50)

        heading=Label(frame,text='Sign up',fg="#57a1f8",bg='white',font=('Microsoft Yahei yr Light',23, 'bold'))
        heading. place(x=100, y=5)

        def on_enter(e):
            user.delete(0 , 'end')

        def on_leave(e):
            name = user.get()
            if name=='':
                user.insert(0 , "Username")
        user = Entry(frame,width=25,fg='black' ,border=2*0,bg='white', font=('Microsoft Yahei UI Light',11))
        user. place(x=30,y=80)
        user.insert(0 , "Username")
        user.bind('<FocusIn>' , on_enter)
        user.bind('<FocusOut>' , on_leave)
        Frame (frame, width=295, height=2,bg='black').place(x=25,y=107)
        def on_enter(e):
            code.delete(0 , 'end')

        def on_leave(e):
            name = code.get()
            if name=='':
                code.insert(0 , "Email")
        code = Entry(frame , width=25 , fg='black' , border=0 , bg='white'  , font=('Microsoft YaHei UI Light' , 11))
        code.place(x=30 , y=150)
        code.insert(0 , "Email")
        code.bind('<FocusIn>' , on_enter)
        code.bind('<FocusOut>' , on_leave)
        Frame(frame , width=295 , height=2 , bg='black').place(x=25 , y=177)
        def on_enter(e):
            conf.delete(0 , 'end')

        def on_leave(e):
            name = conf.get()
            if name=='':
                conf.insert(0 , "Password")
        conf = Entry(frame , width=25 , fg='black' , border=0 , bg='white' , font=('Microsoft YaHei UI Light' , 11))
        conf.place(x=30 , y=220)
        conf.insert(0 , "Password")
        conf.bind('<FocusIn>' , on_enter)
        conf.bind('<FocusOut>' , on_leave)
        Frame(frame , width=295 , height=2 , bg='black').place(x=25 , y=247)
        Button(frame,width=39, pady=7,text='Sign up',bg='#57a1f8' ,fg='white' , command=insertDat ,border=0) .place(x=35,y=280)
        label=Label(frame,text='I have an account',fg='black' ,bg='white',font=('Microsoft YaHei UI Light',9))
        label.place(x=90, y=340)
        u1 = 'https://www.facebook.com'
        u2 = 'https://www.instagram.com'
        u3 = 'https://www.linkedin.com'
        def open1():
            webbrowser.open_new(u1)
        def open2():
            webbrowser.open_new(u3)
        signin=Button(frame,width=6,text='Sign in',border=0,bg='white' ,cursor='hand2',fg='#57a1f8')
        signin.place(x=200,y=340)
        img1 = PhotoImage(file='icons8-logo-google-48.png')
        Button(window , image=img1 , bg='white' , border=0 , command=open2).place(x=580 , y=435)
        img2 = PhotoImage(file='icons8-facebook-48.png')
        Button(window , image=img2 , bg='white' , border=0 , command=open1).place(x=660 , y=435)
        window.mainloop()
img = PhotoImage(file='login.png')

Label(root , image=img , bg='white').place(x=50 , y=50)

frame = Frame(root , width=350 , height=350 , bg='white')
frame.place(x=480 , y=70)

text_label = Label(frame , text="Sign In" , fg="#57a1f8" , bg='white' , font=('Microsoft YaHei UI Light' , 23 , "bold"))
text_label.place(x=120 , y=5)
#################################################################################################################

def on_enter(e):
    user.delete(0 , 'end')

def on_leave(e):
    name = user.get()
    if name=='':
        user.insert(0 , "Username")

user = Entry(frame , width=25 , fg='black' , border=0 , bg='white',  textvariable=Username , font=('Microsoft YaHei UI Light' , 11))
user.place(x=30 , y=80)
user.insert(0 , "Username")
user.bind('<FocusIn>' , on_enter)
user.bind('<FocusOut>' , on_leave)
Frame(frame , width=295 , height=2 , bg='black').place(x=25 , y=107)
#################################################################################################################
def on_enter(e):
    code.delete(0 , 'end')

def on_leave(e):
    name = code.get()
    if name=='':
        code.insert(0 , "Password")
code = Entry(frame , width=25 , fg='black' , border=0 , bg='white' ,  textvariable=Password  ,  font=('Microsoft YaHei UI Light' , 11))
code.place(x=30 , y=150)
code.insert(0 , "Password")
code.bind('<FocusIn>' , on_enter)
code.bind('<FocusOut>' , on_leave)
Frame(frame , width=295 , height=2 , bg='black').place(x=25 , y=177)
#################################################################################################################
Button(frame , width=39 , pady=7 , text="Sign In" , bg="#57a1f8" , fg="white" , border=0 , command=logs).place(x=35, y=204)
label = Label(frame , text="Don't have a account?" , fg="black" , bg="white" ,  font=("Microsoft YaHei UI Light" , 9) )
label.place(x=75 , y=270)


sing_up_text = Button(frame , width=6 , text='Sing Up' , border=0 , bg="white" , cursor='hand2' , fg="#57a1f8" ,  command=signuUp)
sing_up_text.place(x=215 , y=270)

def Review():
    import Review

Review = Button(frame , width=20 , pady=7 , text="Review App" , bg="#57a1f8" , fg="white" , border=0 , command=Review).place(x=100 , y=320)



root.mainloop()