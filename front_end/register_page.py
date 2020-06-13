from  tkinter import *
from PIL import ImageTk,Image
import tkinter as tk

#from tkinter import messagebox
class Register_page:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Login page")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        #==bg image ====
        self.bg=ImageTk.PhotoImage(Image.open("back_ground.jpeg"))
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #frame for login and register
        Login_btn=Button(self.root,command=self.back,text="Go back",bg="#d77337",fg="white",font=("times new roman",10)).place(x=10,y=20,width=50)


        Frame_Login = Frame(self.root, bg="white")
        Frame_Login.place(x=150, y=150, height=400, width=500)

        title=Label(Frame_Login,text="Register Here",font=("Impact",35,"bold"),fg='#d77337',bg='white').place(x=50,y=20)

        lbl_user=Label(Frame_Login,text='name', font=("Goudy old style",15), fg='gray',bg='white').place(x=60,y=100)
        self.txt_user=Entry(Frame_Login,font=("calibri light",15),bg="white")
        self.txt_user.place(x=160,y=100,width=250,height=35)

        lbl_Id = Label(Frame_Login, text='User_Id', font=("Goudy old style", 15), fg='gray', bg='white').place(x=50,y=140)
        self.txt_Id = Entry(Frame_Login, font=("calibri light", 15), bg="white")
        self.txt_Id.place(x=160, y=140, width=250, height=35)

        Search_btn = Button(Frame_Login, text="search", bg="lightblue", fg="red",font=("times new roman", 15)).place(x=420, y=140, width=70)

        lbl_Id = Label(Frame_Login, text='Gmail', font=("Goudy old style", 15), fg='gray', bg='white').place(x=50,y=180)
        self.txt_Id = Entry(Frame_Login, font=("calibri light", 15), bg="white")
        self.txt_Id.place(x=160, y=180, width=250, height=35)

        lbl_Id = Label(Frame_Login, text='Number', font=("Goudy old style", 15), fg='gray', bg='white').place(x=50,y=220)
        self.txt_Id = Entry(Frame_Login, font=("calibri light", 15), bg="white")
        self.txt_Id.place(x=160, y=220, width=250, height=35)


        lbl_Id = Label(Frame_Login, text='password', font=("Goudy old style", 15), fg='gray', bg='white').place(x=50,y=260)
        self.txt_Id = Entry(Frame_Login, font=("calibri light", 15), bg="white")
        self.txt_Id.place(x=160, y=260, width=250, height=35)

        snap_btn = Button(Frame_Login, text="Take a snap", bg="lightblue", fg="red", font=("times new roman", 15)).place(x=160, y=310, width=250)

        Register_btn=Button(Frame_Login,text="Register",bg="#d77337",fg="white",font=("times new roman",15)).place(x=220,y=360,width=100)
        self.root.mainloop()

    def back(self):
        self.root.destroy()