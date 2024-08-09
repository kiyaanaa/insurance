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

    if any(field.strip() == "" for field in
           [first_name, last_name, gender, national_code, phone_number, address, email]):
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
label_instruction.place(x=128, y=30, anchor="w")

# ایجاد و قرار دادن ویجت‌ها
label_first_name = ctk.CTkLabel(frame, text="نوع بیمه", font=("b nazanin", 20, "bold"))
label_first_name.place(x=415, y=130, anchor="w")
entry_first_name = ctk.CTkEntry(frame, width=340)
entry_first_name.place(x=20, y=130, anchor="w")

label_last_name = ctk.CTkLabel(frame, text="  تاریخ فروش", font=("b nazanin", 20, "bold"))
label_last_name.place(x=380, y=200, anchor="w")
entry_last_name = ctk.CTkEntry(frame, width=340)
entry_last_name.place(x=20, y=200, anchor="w")

label_gender = ctk.CTkLabel(frame, text="قیمت", font=("b nazanin", 20, "bold"))
label_gender.place(x=430, y=270, anchor="w")
combo_gender = ctk.CTkEntry(frame, width=340)
combo_gender.place(x=20, y=270, anchor="w")

button_submit = ctk.CTkButton(frame, text="ذخیره", font=("b nazanin", 20, "bold"), command=submit_form)
button_submit.place(x=180, y=420, anchor="w")

app.mainloop()
