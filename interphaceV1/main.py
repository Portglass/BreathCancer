from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

class MyWindow(Tk):

    def __init__(self, fenetre):
        Tk.__init__(self)
        if(fenetre == 1):
            self.createLogin()
        if (fenetre == 2):
                self.createLogin()

    def createLogin(self):
        print("create login launch")
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

        validateBtn = Button(self, text="Sign in", bg="black", fg="white", command=self.createChoiceAnalyse)
        validateBtn.place(x=340, y=300, height=30)

    def createChoiceAnalyse(self):
        for c in self.winfo_children():
            c.destroy()
        print("createChoiceAnalyse launch")

        dessin = Canvas(self, bg="black", height=200, width=300)
        dessin.place(x=-200,y=-10)
        dessin.create_rectangle(300, 200, 4, 4, outline='black', width=4)
        dessin.place(relx=0.5, rely=0.5, anchor=CENTER)

        dessinV2 = Canvas(self, bg="grey", height=200, width=300)
        dessinV2.place(x=150, y=-10)
        dessinV2.create_rectangle(300, 200, 4, 4, outline='grey', width=4)
        dessinV2.place(relx=0.5, rely=0.5, anchor=CENTER)

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


    def create_menu_bar(self):
        menu_bar = Menu(self)

        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="Home", command=self.do_something)
        menu_file.add_command(label="Home", command=self.do_something)
        menu_bar.add_cascade(label="Menu", menu=menu_file)

        menu_edit = Menu(menu_bar, tearoff=0)
        menu_edit.add_command(label="Signup", command=self.do_something)
        menu_edit.add_separator()
        menu_edit.add_command(label="Login", command=self.do_something)
        menu_bar.add_cascade(label="Connexion", menu=menu_edit)

        menu_help = Menu(menu_bar, tearoff=0)
        menu_help.add_command(label="About Us", command=self.do_about)
        menu_bar.add_cascade(label="Help", menu=menu_help)

        self.config(menu=menu_bar)

    def open_file(self):
        file = askopenfilename(title="Choose the file to open",
                               filetypes=[("PNG image", ".png"), ("GIF image", ".gif"), ("All files", ".*")])
        print(file)

    def do_something(self):
        print("Menu clicked")

    def do_about(self):
        messagebox.showinfo("My title", "My message")




def launcher(name):
    window = MyWindow(2)
    window.mainloop()

if __name__ == '__main__':
    nom = "Username"
    password = "password"
    launcher('PyCharm')

