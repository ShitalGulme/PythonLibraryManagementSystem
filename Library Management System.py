from tkinter import *
import tkinter.messagebox as msg

class Multiple():
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("300x300")
        self.root.title("Library Management System")
        self.root.config(bg="pink")

        title = Label(self.root,text="Home Page",bg="pink",font=('bold','20'))
        title.pack()

        admin_button = Button(self.root,text="Admin",command=self.admin_page)
        admin_button.place(x=120,y=90)

        user_button = Button(self.root,text="User",command=self.user_page)
        user_button.place(x=120,y=180)

    def admin_page(self):
        Window = Tk()
        Window.title("Admin page")
        Window.geometry("290x400")
        Window.config(bg="pink")

        book_name_label = Label(Window,text="Book Name:",bg="pink",font=('bold','18'))
        book_name_label.place(x=10,y=50)

        author_label = Label(Window,text="Author Name:",bg="pink",font=('bold','18'))
        author_label.place(x=10,y=140)

        quantity_label = Label(Window,text="Quantity:",bg="pink",font=('bold','18'))
        quantity_label.place(x=10,y=230)

        self.book_entry = Entry(Window)
        self.book_entry.place(x=150,y=55)

        self.author_entry = Entry(Window)
        self.author_entry.place(x=160, y=149)

        self.quantity_entry = Entry(Window)
        self.quantity_entry.place(x=120, y=239)

        admin_submit = Button(Window,text="Submit",command=self.admin_data)
        admin_submit.place(x=120,y=320)

    def user_page(self):
        Window1 = Tk()
        Window1.title("User Page")
        Window1.geometry("290x300")
        Window1.config(bg="pink")

        book_user_label = Label(Window1, text="Book Name:", bg="pink", font=('bold', '18'))
        book_user_label.place(x=10, y=50)

        author_user_label=Label(Window1,text="Author Name:",bg="pink",font=('bold','18'))
        author_user_label.place(x=10,y=140)

        self.user_book=Entry(Window1)
        self.user_book.place(x=150,y=55)

        self.user_author=Entry(Window1)
        self.user_author.place(x=160,y=149)

        user_submit = Button(Window1,text="Submit",command=self.user_data)
        user_submit.place(x=120,y=230)

    def admin_data(self):
        import mysql.connector

        mydb = mysql.connector.connect(host='localhost',port='3366',user='root',password='root',database='library_management')
        mycursor=mydb.cursor()

        bookname=self.book_entry.get()
        author=self.author_entry.get()
        quantity =self.quantity_entry.get()

        mycursor.execute("insert into admin values(%s,%s,%s)",(bookname,author,quantity))
        mydb.commit()
        msg.showinfo("Admin Books","Book added to stock")

    def user_data(self):
        import mysql.connector

        mydb=mysql.connector.connect(host='localhost',port='3366',user='root',password='root',database='library_management')
        mycursor=mydb.cursor()

        book_name=self.user_book.get()
        author=self.user_author.get()

        mycursor.execute("select Quantity from admin where Book_name=%s and author=%s",(book_name,author))

        q=0
        for i in mycursor:
            q=int(i[0])
        if q>=1:
            q=q-1
            mycursor.execute("update admin set Quantity=%s where Book_name=%s and author=%s",(q,book_name,author))
            mycursor.execute("insert into user values(%s,%s)",(book_name,author))
            mydb.commit()
            msg.showinfo("Book Availablity","Book available")
        else:
            msg.showerror("Book Avialability","Book not found")
root=Tk()
obj = Multiple(root)
root.mainloop()

