from  tkinter import *
from  tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
from register_page import Register_page
from login_page import Login_page
class Front_page:
    def __init__(self):
        self.root=Tk()
        self.root.title("ATTANDANCE WITH FACE DETECTION")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        self.this_page=False

        #==bg image ====
        self.bg=ImageTk.PhotoImage(Image.open("back_ground.jpeg"))
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #tab_control=ttk.Notebook(self.root)

        # frame for login
        self.Frame_Login = Frame(self.root, bg="white")
        self.Frame_Login.place(x=150, y=150, height=340, width=600)

        self.log()
        self.root.mainloop()

    def log(self):


        title=Label(self.Frame_Login,text="ATTANDACE WITH FACE DETECTION",font=("Impact",25,"bold"),fg='#d77337',bg='white').place(x=90,y=30)

        Login_btn=Button(self.Frame_Login,command=self.loginpage,text="LOGIN",bg="#d77337",fg="white",font=("times new roman",15)).place(x=150,y=200,width=150)
        Login_btn=Button(self.Frame_Login,command=self.regpage,text="REGESTER",bg="#d77337",fg="white",font=("times new roman",15)).place(x=350,y=200,width=150)
    def loginpage(self):
        l=Login_page()


    def regpage(self):
        r = Register_page()

fp=Front_page()