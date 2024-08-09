import customtkinter as ctk
import sqlite3
from tkinter import messagebox

from insurance_app.view.insurance_sell_view import entry_last_name

# تنظیمات پایگاه داده
DATABASE_URL = "mysql+pymysql://root:root123@localhost:3306/mft"

# ایجاد پایگاه داده و جدول
def create_database():
    conn = sqlite3.connect('../model/da/personal_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS personal_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            gender TEXT NOT NULL,
            national_code TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            address TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_to_database(first_name, last_name, gender, national_code, phone_number, address, email):
    conn = sqlite3.connect('../model/da/personal_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO personal_info (first_name, last_name, gender, national_code, phone_number, address, email)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, gender, national_code, phone_number, address, email))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "اطلاعات با موفقیت ذخیره شد.")

def submit_form():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    gender = combo_gender.get()
    national_code = entry_national_code.get()
    phone_number = entry_phone_number.get()
    address = text_address.get("1.0", "end-1c")
    email = entry_email.get()

    if any(field.strip() == "" for field in [first_name, last_name, gender, national_code, phone_number, address, email]):
        messagebox.showwarning("Warning", "لطفاً تمامی فیلدها را پر کنید.")
    else:
        save_to_database(first_name, last_name, gender, national_code, phone_number, address, email)

# ایجاد پایگاه داده و جدول
create_database()

# ایجاد رابط کاربری با استفاده از customtkinter
app = ctk.CTk()
app.title("فرم ثبت بیمه")
app.geometry("500x600")  # اندازه پنجره
ctk.set_appearance_mode("dark")

# ایجاد فریم اصلی
frame = ctk.CTkFrame(app)
frame.pack(fill="both", expand=True)  # فریم را به طور کامل در صفحه قرار می‌دهد

label_instruction = ctk.CTkLabel(frame, text=".لطفاً مشخصات بازاریاب را وارد نمایید", font=("b nazanin", 20, "bold"))
label_instruction.place(x=115, y=30, anchor="w")

# ایجاد و قرار دادن ویجت‌ها
label_first_name = ctk.CTkLabel(frame, text="نام", font=("b nazanin", 20, "bold"))
label_first_name.place(x=445, y=90, anchor="w")
entry_first_name = ctk.CTkEntry(frame, width=320)
entry_first_name.place(x=20, y=90, anchor="w")

label_first_name = ctk.CTkLabel(frame, text="نام خانوادگی", font=("b nazanin", 20, "bold"))
label_first_name.place(x=375, y=155, anchor="w")
entry_first_name = ctk.CTkEntry(frame, width=320)
entry_first_name.place(x=20, y=155, anchor="w")

label_gender = ctk.CTkLabel(frame, text="جنسیت", font=("b nazanin", 20, "bold"))
label_gender.place(x=410, y=220, anchor="w")
combo_gender = ctk.CTkComboBox(frame, values=["مرد","زن"], width=320)
combo_gender.place(x=20, y=220, anchor="w")

label_national_code = ctk.CTkLabel(frame, text="  کد ملی", font=("b nazanin", 20, "bold"))
label_national_code.place(x=398, y=285, anchor="w")
entry_national_code = ctk.CTkEntry(frame, width=320)
entry_national_code.place(x=20, y=285, anchor="w")

label_phone_number = ctk.CTkLabel(frame, text="  شماره تلفن", font=("b nazanin", 20, "bold"))
label_phone_number.place(x=365, y=350, anchor="w")
entry_phone_number = ctk.CTkEntry(frame, width=320)
entry_phone_number.place(x=20, y=350, anchor="w")

label_email = ctk.CTkLabel(frame, text="ایمیل", font=("b nazanin", 20, "bold"))
label_email.place(x=410, y=415, anchor="w")
entry_email = ctk.CTkEntry(frame, width=320)
entry_email.place(x=20, y=415, anchor="w")

label_address = ctk.CTkLabel(frame, text="آدرس", font=("b nazanin", 20, "bold"))
label_address.place(x=410, y=480, anchor="w")
text_address = ctk.CTkEntry(frame, width=320, height=60)
text_address.place(x=20, y=480, anchor="w")

# توابع مربوط به رویدادهای موس برای تغییر ظاهر دکمه
def on_enter(event):
    button_submit.configure(fg_color="green")

def on_leave(event):
    button_submit.configure(fg_color="#3B8ED0")

# ایجاد دکمه و اتصال رویدادهای موس
button_submit = ctk.CTkButton(frame, text="ذخیره", font=("b nazanin", 18, "bold"), command=submit_form)
button_submit.place(x=180, y=560, anchor="w")
button_submit.bind("<Enter>", on_enter)
button_submit.bind("<Leave>", on_leave)

app.mainloop()
