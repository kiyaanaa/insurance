import customtkinter as ctk
from tkinter import messagebox
from customtkinter import *

app = ctk.CTk()
app.title("صفحه ورود")
app.geometry("400x500")
set_appearance_mode("dark")


def login():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        messagebox.showinfo("ورود", "ورود با موفقیت انجام شد!")
    else:
        messagebox.showwarning("خطای ورودی", "لطفاً نام کاربری و رمز عبور را وارد کنید.")


def exit_app():
    app.quit()


login_frame = ctk.CTkFrame(app, width=300, height=300)
login_frame.pack(pady=50)

username_frame = ctk.CTkFrame(login_frame, width=280, height=50, corner_radius=20)
username_frame.pack(pady=(20, 10))

username_label = ctk.CTkLabel(username_frame, text="کاربری نام", anchor="w")
username_label.pack(pady=(10, 0), padx=15)

username_entry = ctk.CTkEntry(username_frame, placeholder_text="کنید وارد را خود کاربری نام")
username_entry.pack(pady=10, padx=15, fill="x")

password_frame = ctk.CTkFrame(login_frame, width=280, height=50, corner_radius=20)
password_frame.pack(pady=(10, 20))

password_label = ctk.CTkLabel(password_frame, text="عبور رمز", anchor="w")
password_label.pack(pady=(10, 0), padx=15)

password_entry = ctk.CTkEntry(password_frame, placeholder_text="کنید وارد را خود عبور رمز", show="*")
password_entry.pack(pady=10, padx=15, fill="x")

remember_me_var = ctk.BooleanVar()
remember_me_checkbox = ctk.CTkCheckBox(login_frame, text="بسپار خاطر به مرا", variable=remember_me_var)
remember_me_checkbox.pack(pady=10)

login_button = ctk.CTkButton(login_frame, text="ورود", command=login)
login_button.pack(pady=10)

exit_button = ctk.CTkButton(login_frame, text="خروج", command=exit_app)
exit_button.pack(pady=(10, 0))

app.mainloop()
