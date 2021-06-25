from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
import os
from os.path import join
import sys


#HALAMAN AWAL
def hal_awal():
    global awal
    awal = Tk()
    # awal.iconbitmap("d:Downloads/Documents/Python/00 . Template/py/icon.ico")
    awal.title("Indogram")
    awal.geometry("400x250")
    awal.configure(background="cyan")
    global username_verify
    global password_verify
    username_verify= StringVar()
    password_verify = StringVar()
    global username_login_entry
    global password_login_entry
    

    Label(awal, text="Selamat datang di Indogram", font=("times new roman", 16, "bold"), fg="black", bg="cyan").pack()
    Label(awal, text="Username", bg="cyan").pack()
    username_login_entry = Entry(awal, width="20", textvariable=username_verify)
    username_login_entry.pack()
    Label(awal, text="Password", bg="cyan").pack()
    password_login_entry = Entry(awal, width="20", textvariable=password_verify, show="*")
    password_login_entry.pack()

    Label(awal, text="", bg="cyan").pack()
    Button(awal, text="Login", font=("Calibri", 12), width="7", height="1", command=login_user, cursor="hand2").place(x="125", y="120")
    Button(awal, text="Register", font=("Calibri", 12), width="7", height="1", command=register, cursor="hand2").place(x="210", y="120")
    Button(awal, text="Exit", font=("Calibri", 12), width="4", height="1", command=quit, cursor="hand2").place(x="175", y="185")
    Button(awal, text="Register")

    
    awal.mainloop()

#HALAMAN REGISTER
def register():
    global daftar
    daftar = Toplevel(awal)
    # daftar.iconbitmap("c:/Users/LENOVO/Downloads/Documents/Python/00 . Template/oke/icon.ico")
    daftar.geometry("400x320")
    daftar.title("Register")
    daftar.configure(background="cyan")

    global username
    global password
    global email
    global username_entry
    global password_entry
    global email_entry

    username = StringVar()
    password = StringVar()
    email = StringVar()
    agree = IntVar()
    gender = IntVar()

    Label(daftar, text="Daftar akun", font=("Calibri", 16, "bold"), bg="cyan").pack()
    Label(daftar, text="", bg="cyan").pack()
    username_label = Label(daftar, text="Username:", bg="cyan", font="Calibri")
    username_label.place(x="20", y="40")
    username_entry = Entry(daftar, width="20", textvariable=username)
    username_entry.place(x="120", y="45")
    
    password_label = Label(daftar, text="Password:", bg="cyan", font="Calibri")
    password_label.place(x="20", y="80")
    password_entry = Entry(daftar, width="20", textvariable=password)
    password_entry.place(x="120", y="85")

    Label(daftar, text="E-mail:", bg="cyan", font="Calibri").place(x="20", y="120")
    email_entry = Entry(daftar, width="20", textvariable=email)
    email_entry.place(x="120", y="125")
    
    Label(daftar, text="Jenis kelamin:", bg="cyan", font="Calibri").place(x="20", y="160")
    Radiobutton(daftar, text="Laki-laki", bg="cyan", variable = gender, value = 1).place(x="120", y="160")
    Radiobutton(daftar, text="Perempuan", bg="cyan", variable = gender, value = 2).place(x="200", y="160")
    
    Label(daftar, text="Asal pulau:", bg="cyan", font="Calibri").place(x="20", y="200")
    pulau = ["Jawa", "Sumatera", "Kalimantan", "Sulawesi", "Papua"]
    pulauVar = StringVar()
    pulauVar.set("Pulau")
    tabel = OptionMenu(daftar, pulauVar, *pulau)
    tabel.config(width="15")
    tabel.place(x="120", y="200")
    
    Checkbutton(daftar, text="Centang jika anda sudah yakin", variable=agree, bg="cyan").place(y=235, x=100)

    Button(daftar, text="Daftar", font=("Calibri", 11), width="8", command = register_user, cursor="hand2").place(x="95", y="265")
    Button(daftar, text="Kembali", font=("Calibri", 11), width="8", command = daftar.destroy, cursor="hand2").place(x="215", y="265")

#SISTEM REGISTRASI USER
def register_user():
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    
    if username_info == password_info:
        blank()
    else:
        not_blank()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)


#SISTEM LOGIN USER
def login_user():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_file = os.listdir()
    if username1 in list_file:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            info1()
            app1()
        else:
            info2()
    else:
        info3()

def quit():
    respon = messagebox.askquestion("Exit", "Apakah anda yakin ingin keluar?")
    if respon == "yes":
        awal.quit()

def blank():
    messagebox.showwarning("Warning", "Username dan Password tidak boleh sama")

def not_blank():
    messagebox.showinfo("Info", "Akun berhasil dibuat")

def info1():
    messagebox.showinfo("Login", "Login berhasil")

def info2():
    messagebox.showwarning("Warning", "Password salah")

def info3():
    messagebox.showerror("Error", "Username atau Paswword salah")

#Menambahkan gambar
def app1():
    global img
    global label
    global foto
    foto = Toplevel(awal)
    foto.geometry("300x300")
    foto.title("kera")
    # foto.iconbitmap("c:/Users/LENOVO/Downloads/Documents/Python/00 . Template/oke/icon.ico")
    foto.configure(background="cyan")
    img = ImageTk.PhotoImage(Image.open("c:/Users/LENOVO/Downloads/Documents/Python/00 . Template/oke/kera.jpg"))
    label = Label(foto, image=img, width="300", height="200")
    label.pack(padx=20, pady=20)

def app2():
    global absen
    absen = Toplevel(awal)
    absen.geometry("800x400")
    absen.title("Absensi Kelas")
    # absen.iconbitmap("c:/Users/LENOVO/Downloads/Documents/Python/00 . Template/oke/icon.ico")
    absen.configure(background="cyan")

    frame = Frame(absen, width="250", height="350")
    frame.pack(pady=10, side=LEFT, padx=25)
    frame = Frame(absen, width="500", height="350")
    frame.pack(pady=10, side=RIGHT, padx=30)

#Membuka file manager
def app3():
    global files
    global imagee
    files = Toplevel(awal)

    files.geometry("300x300")
    files.title("File")
    # files.iconbitmap("c:/Users/LENOVO/Downloads/Documents/Python/00 . Template/oke/icon.ico")

    files.filename = filedialog.askopenfilename(initialdir="c:/Users/LENOVO/Downloads/Documents/Python/00 . Template", title="Select A file", filetypes=(("png files", "*.png"),("all files", "*.*")))
    labell = Label(files, text=files.filename).pack()
    imagee = ImageTk.PhotoImage(Image.open(files.filename))
    image_label = Label(files, image=imagee).pack()
    
hal_awal()