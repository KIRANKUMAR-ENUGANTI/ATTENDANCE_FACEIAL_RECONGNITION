from  tkinter import *
import tkinter as tk
from  tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
class Login_page:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.title("Login page")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        #==bg image ====
        self.bg=ImageTk.PhotoImage(Image.open("back_ground.jpeg"))
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #tab_control=ttk.Notebook(self.root)
        Login_btn=Button(self.root,command=self.back,text="Go back",bg="#d77337",fg="white",font=("times new roman",10)).place(x=10,y=20,width=50)

        # frame for login
        self.Frame_Login = Frame(self.root, bg="white")
        self.Frame_Login.place(x=150, y=150, height=340, width=480)
        #lable telling login here
        title=Label(self.Frame_Login,text="Login Here",font=("Impact",35,"bold"),fg='#d77337',bg='white').place(x=90,y=30)

        lbl_user=Label(self.Frame_Login,text='User_Id', font=("Goudy old style",15), fg='gray',bg='white').place(x=80,y=100)
        self.txt_user=Entry(self.Frame_Login,font=("calibri light",15),bg="white")
        self.txt_user.place(x=80,y=130,width=330,height=35)

        lbl_pass = Label(self.Frame_Login,text='password', font=("Goudy old style", 15), fg='gray',bg='white').place(x=80, y=180)
        self.txt_pass = Entry(self.Frame_Login, font=("calibri light", 15), bg="white")
        self.txt_pass.place(x=80, y=210, width=330, height=35)

        forget_pass=Button(self.Frame_Login, text="Forget password",fg="#d77337",bg='white',bd=0,font=("times new roman",15,'underline')).place(x=80,y=250)

        Login_btn=Button(self.Frame_Login,text="Login",bg="#d77337",fg="white",font=("times new roman",15)).place(x=190,y=300,width=100)


        # self.root.mainloop()

    def back(self):
        self.root.destroy()