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
app.title("فرم اطلاعات شخصی")
app.geometry("1920x1080")  # اندازه اولیه پنجره
ctk.set_appearance_mode("dark")


# ایجاد فریم اصلی
frame = ctk.CTkFrame(app)
frame.place(relwidth=1, relheight=1)  # فریم را به طور کامل در صفحه قرار می‌دهد

label_instruction = ctk.CTkLabel(frame, text=".لطفاً مشخصات بازاریاب را وارد نمایید", font=("b nazanin", 20, "bold"))
label_instruction.place(x=1015, y=20, anchor="w")

# ایجاد و قرار دادن ویجت‌ها
label_first_name = ctk.CTkLabel(frame, text="نام", font=("b nazanin", 20, "bold"))
label_first_name.place(x=1250, y=70, anchor="w")
entry_first_name = ctk.CTkEntry(frame, width=300)
entry_first_name.place(x=870, y=70, anchor="w")

label_last_name = ctk.CTkLabel(frame, text="  نام خانوادگی", font=("b nazanin", 20, "bold"))
label_last_name.place(x=1175, y=110, anchor="w")
entry_last_name = ctk.CTkEntry(frame, width=300)
entry_last_name.place(x=870, y=110, anchor="w")

label_gender = ctk.CTkLabel(frame, text="جنسیت", font=("b nazanin", 20, "bold"))
label_gender.place(x=1215, y=150, anchor="w")
combo_gender = ctk.CTkComboBox(frame, values=["مرد","زن"], width=300)
combo_gender.place(x=870, y=150, anchor="w")

label_national_code = ctk.CTkLabel(frame, text="  کد ملی", font=("b nazanin", 20, "bold"))
label_national_code.place(x=1210, y=190, anchor="w")
entry_national_code = ctk.CTkEntry(frame, width=300)
entry_national_code.place(x=870, y=190, anchor="w")

label_phone_number = ctk.CTkLabel(frame, text="  شماره تلفن", font=("b nazanin", 20, "bold"))
label_phone_number.place(x=1180, y=230, anchor="w")
entry_phone_number = ctk.CTkEntry(frame, width=300)
entry_phone_number.place(x=870, y=230, anchor="w")

label_email = ctk.CTkLabel(frame, text="ایمیل", font=("b nazanin", 20, "bold"))
label_email.place(x=1225, y=270, anchor="w")
entry_email = ctk.CTkEntry(frame, width=300)
entry_email.place(x=870, y=270, anchor="w")

label_address = ctk.CTkLabel(frame, text="آدرس", font=("b nazanin", 20, "bold"))
label_address.place(x=1225, y=340, anchor="w")
text_address = ctk.CTkEntry(frame, width=300, height=80)
text_address.place(x=870, y=340, anchor="w")

button_submit = ctk.CTkButton(frame, text="ذخیره", font=("b nazanin", 20, "bold"), command=submit_form)
button_submit.place(x=950, y=440, anchor="w")

app.mainloop()
