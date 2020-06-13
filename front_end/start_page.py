from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image

class MainWindow():

    def __init__(self, master = None):
        # Frame.__init__(self, master)

        self.master = master
        self.master = Tk()
        self.master.title("ATTANDANCE WITH FACE DETECTION")
        self.master.geometry("1199x600+100+50")
        self.master.resizable(False, False)

        # ==bg image ====
        self.bg = ImageTk.PhotoImage(Image.open("back_ground.jpeg"))
        self.bg_image = Label(self.master, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # tab_control=ttk.Notebook(self.master)

        # frame for login
        self.Frame_Login = Frame(self.master, bg="white")
        self.Frame_Login.place(x=150, y=150, height=340, width=600)
        title = Label(self.Frame_Login, text="ATTANDACE WITH FACE DETECTION", font=("Impact", 25, "bold"), fg='#d77337',bg='white').place(x=90, y=30)

        Login_btn = Button(self.Frame_Login, command=self.open_login, text="LOGIN", bg="#d77337", fg="white",font=("times new roman", 15)).place(x=150, y=200, width=150)
        Login_btn = Button(self.Frame_Login, command=self.open_register, text="REGESTER", bg="#d77337", fg="white",font=("times new roman", 15)).place(x=350, y=200, width=150)

        self.popup_login = None
        self.popup_register = None
        self.master.mainloop()




    def open_login(self):
        if self.popup_login is None or not self.popup_login.root_login.winfo_exists():
            self.popup_login = Login_page()
        else:
            self.popup_login.root_login.lift(self.master)
    def open_register(self):
        if self.popup_register is None or not self.popup_register.root_register.winfo_exists():
            self.popup_register = Register_page()
        else:
            self.popup_register.root_register.lift(self.master)


class Login_page:
    def __init__(self):
        self.root_login=tk.Toplevel()
        self.root_login.title("Login page")
        self.root_login.geometry("1199x600+100+50")
        self.root_login.resizable(False,False)

        #==bg image ====
        self.bg=ImageTk.PhotoImage(Image.open("back_ground.jpeg"))
        self.bg_image=Label(self.root_login,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #tab_control=ttk.Notebook(self.root_login)
        Login_btn=Button(self.root_login,command=self.back,text="Go back",bg="#d77337",fg="white",font=("times new roman",10)).place(x=10,y=20,width=50)

        # frame for login
        self.Frame_Login = Frame(self.root_login, bg="white")
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
    def back(self):
        self.root_login.destroy()

class Register_page:
    def __init__(self):
        self.root_register = tk.Toplevel()
        self.root_register.title("Login page")
        self.root_register.geometry("1199x600+100+50")
        self.root_register.resizable(False,False)

        #==bg image ====
        self.bg=ImageTk.PhotoImage(Image.open("back_ground.jpeg"))
        self.bg_image=Label(self.root_register,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #frame for login and register
        Login_btn=Button(self.root_register,command=self.back,text="Go back",bg="#d77337",fg="white",font=("times new roman",10)).place(x=10,y=20,width=50)


        Frame_Login = Frame(self.root_register, bg="white")
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

    def back(self):
        self.root_register.destroy()

a=MainWindow()