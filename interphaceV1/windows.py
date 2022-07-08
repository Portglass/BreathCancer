from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

from bddConnection import bddRequest
from modele import model
from account import doctor
from PIL import Image, ImageTk
import numpy as np
import cv2

class MyWindow(Tk):

    def __init__(self, fenetre):
        Tk.__init__(self)
        self.mod = model("../BreastCancerSegmentor.h5")
        self.createLogin()
        bddRequest.initDatabase()

    def createLogin(self):
        for c in self.winfo_children():
            c.destroy()
        print("create login launch")
        self.isConnected = False
        self.doctor = None

        self.create_menu_bar()
        self.geometry("720x480")
        self.configure(bg="white")
        self.title("Cancer Detection")

        dessin = Canvas(self, bg="white", height=250, width=330)
        dessin.create_rectangle(330, 250, 4, 4, outline='gray', width=4)
        dessin.place(relx=0.5, rely=0.5, anchor=CENTER)

        font10 = "-family {DejaVu Sans} -size 12 -weight bold"
        title = Label(text="Doctor Login", bg="white")
        title.configure(font=font10)
        title.place(x=310, y=130)

        user = Entry(self, width=40)
        user.insert(0, "Username")
        user.place(x=250, y=200, height=30)

        mdp = Entry(self, width=40)
        mdp.insert(0, "Password")
        mdp.place(x=250, y=250, height=30)

        validateBtn = Button(self, text="Sign in", bg="black", fg="white", command=lambda: self.checkAccount(user.get(),mdp.get()))
        validateBtn.place(x=340, y=300, height=30)

    def createChoiceAnalyse(self):
        for c in self.winfo_children():
            c.destroy()
        print("createChoiceAnalyse window")

        self.create_menu_bar()
        dessin = Canvas(self, bg="black", height=200, width=300)
        dessin.place(x=-200,y=-10)
        dessin.create_rectangle(300, 200, 4, 4, outline='black', width=4)
        dessin.place(relx=0.5, rely=0.5, anchor=CENTER)

        dessinV2 = Canvas(self, bg="grey", height=200, width=300)
        dessinV2.place(x=150, y=-10)
        dessinV2.create_rectangle(300, 200, 4, 4, outline='grey', width=4)
        dessinV2.place(relx=0.5, rely=0.5, anchor=CENTER)

        diagnosisBtn = Button(self,text="Launch Diagnosis",bg="white", command=self.createDiagnosis)
        diagnosisBtn.place(x=60,y=280)

        statgingBtn = Button(self, text="Launch Staging", bg="white", command=self.do_something())
        statgingBtn.place(x=430, y=280)

        font12 = "-family {DejaVu Sans} -size 12 -weight bold"
        title = Label(text="Breast Cancer analysis", bg="white")
        title.configure(font=font12)
        title.place(x=30, y=80)

        font20 = "-family {DejaVu Sans} -size 20 -weight bold"
        titleV1 = Label(text="Step 1",fg="white" ,bg="black")
        titleV1.configure(font=font20)
        titleV1.place(x=40, y=200)

        titleV2 = Label(text="Step 2", fg="white", bg="grey")
        titleV2.configure(font=font20)
        titleV2.place(x=400, y=200)


        titleV1 = Label(text="Diagnosis", fg="white", bg="black")
        titleV1.configure(font=font12)
        titleV1.place(x=50, y=230)

        titleV1 = Label(text="Staging", fg="white", bg="grey")
        titleV1.configure(font=font12)
        titleV1.place(x=410, y=230)

    def createDiagnosis(self):
        for c in self.winfo_children():
            c.destroy()
        print("createDiagnosis window")

        self.create_menu_bar()
        diagnosisBtn = Button(self, text="Choose file", bg="white", command=self.displayPredictImage)
        diagnosisBtn.place(relx=0.5, rely=0.5, anchor=CENTER)


    def create_menu_bar(self):
        menu_bar = Menu(self)

        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="Home", command=self.checkIsConnected)
        menu_file.add_command(label="patient", command=self.checkIsConnected)
        menu_bar.add_cascade(label="Menu", menu=menu_file)

        menu_edit = Menu(menu_bar, tearoff=0)
        menu_edit.add_command(label="Signup", command=self.do_something)
        menu_edit.add_separator()
        menu_edit.add_command(label="Login", command=self.createLogin)
        menu_bar.add_cascade(label="Connexion", menu=menu_edit)

        menu_help = Menu(menu_bar, tearoff=0)
        menu_help.add_command(label="About Us", command=self.do_about)
        menu_bar.add_cascade(label="Help", menu=menu_help)

        self.config(menu=menu_bar)

    def displayPredictImage(self):
        pathImg = self.open_file()
        prediction, imgProc =self.mod.predict(pathImg)
        prediction = np.reshape(prediction,(256,256))
        img = Image.fromarray(prediction*255)
        imgDisplay = ImageTk.PhotoImage(image=img)

        canvas = Canvas(self, width=300, height=300,bg="white",highlightthickness=0)
        canvas.pack()
        canvas.create_image(20, 20, anchor="nw", image=imgDisplay)

        self.mainloop()

    def open_file(self):
        file = askopenfilename(title="Choose the file to open",
                               filetypes=[("PNG image", ".png"), ("JPG image", ".jpg")])
        print(file)
        return file

    def do_about(self):
        messagebox.showinfo("My title", "My message")

    def do_something(self):
        print("I am doing something")

    def checkAccount(self,user,mdp):
        comptes = bddRequest.getDoctors()
        tupleAccount = (user,mdp)
        for tup in comptes:
            if(tup == tupleAccount):
                self.createChoiceAnalyse()
                self.isConnected = True
                self.doctor = doctor(tupleAccount[0])
                break
            else:
                self.isConnected = False
                zone_texte = Label(text="Le compte n'est pas valide",fg="red",bg="white")
                zone_texte.place(x=290,y=340)

    def checkIsConnected(self):
        if(self.isConnected):
            self.createChoiceAnalyse()
        else:
            messagebox.showinfo("Alert", "Vous devez vous connecter pour pouvoir accéder à ces informations")