import customtkinter as ctk
import sqlite3
from tkinter import messagebox

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

label_instruction = ctk.CTkLabel(frame, text=".لطفاً مشخصات بیمه را وارد نمایید", font=("b nazanin", 20, "bold"))
label_instruction.place(x=135, y=30, anchor="w")

# ایجاد و قرار دادن ویجت‌ها
label_first_name = ctk.CTkLabel(frame, text="نام", font=("b nazanin", 20, "bold"))
label_first_name.place(x=445, y=110, anchor="w")
entry_first_name = ctk.CTkEntry(frame, width=320)
entry_first_name.place(x=20, y=110, anchor="w")

label_last_name = ctk.CTkLabel(frame, text="نام خانوادگی", font=("b nazanin", 20, "bold"))
label_last_name.place(x=375, y=195, anchor="w")
entry_last_name = ctk.CTkEntry(frame, width=320)
entry_last_name.place(x=20, y=195, anchor="w")

label_purchase_date = ctk.CTkLabel(frame, text="  تاریخ خرید", font=("b nazanin", 20, "bold"))
label_purchase_date.place(x=375, y=280, anchor="w")
entry_purchase_date = ctk.CTkEntry(frame, width=320)
entry_purchase_date.place(x=20, y=280, anchor="w")

label_sale_date = ctk.CTkLabel(frame, text="  تاریخ فروش", font=("b nazanin", 20, "bold"))
label_sale_date.place(x=370, y=365, anchor="w")
entry_sale_date = ctk.CTkEntry(frame, width=320)
entry_sale_date.place(x=20, y=365, anchor="w")

label_price = ctk.CTkLabel(frame, text="قیمت", font=("b nazanin", 20, "bold"))
label_price.place(x=420, y=450, anchor="w")
entry_price = ctk.CTkEntry(frame, width=320)
entry_price.place(x=20, y=450, anchor="w")

# توابع مربوط به رویدادهای موس برای تغییر ظاهر دکمه
def on_enter(event):
    button_submit.configure(fg_color="green")

def on_leave(event):
    button_submit.configure(fg_color="#3B8ED0")

# ایجاد دکمه و اتصال رویدادهای موس
button_submit = ctk.CTkButton(frame, text="ذخیره", font=("b nazanin", 18, "bold"), command=submit_form)
button_submit.place(x=180, y=535, anchor="w")
button_submit.bind("<Enter>", on_enter)
button_submit.bind("<Leave>", on_leave)

app.mainloop()
