import customtkinter as ctk
import tkinter as tk
import sqlite3


# تابع برای دریافت اطلاعات خرید بیمه از دیتابیس
def get_insurance_purchases():
    # اتصال به دیتابیس (تغییر دهید به مسیر و نام دیتابیس خود)
    conn = sqlite3.connect('insurance.db')
    cursor = conn.cursor()

    # اجرای کوئری برای دریافت اطلاعات خرید بیمه
    cursor.execute("SELECT * FROM insurance_purchases")
    purchases = cursor.fetchall()

    conn.close()
    return purchases


# تابع برای به‌روزرسانی صفحه "خرید بیمه" با داده‌های دریافتی
def update_insurance_purchase_page():
    # پاک کردن محتوای قبلی
    for widget in insurance_purchase_frame.winfo_children():
        widget.destroy()

    # دریافت داده‌های خرید بیمه از دیتابیس
    purchases = get_insurance_purchases()

    # نمایش داده‌های خرید بیمه
    for purchase in purchases:
        # فرض می‌کنیم اطلاعات هر خرید بیمه شامل (id, policy_name, amount) است
        ctk.CTkLabel(insurance_purchase_frame,
                     text=f"ID: {purchase[0]}, نام بیمه: {purchase[1]}, مبلغ: {purchase[2]}").pack(pady=5)


# توابع برای انتقال به صفحات مختلف
def show_person_page():
    hide_all_pages()
    person_frame.pack(fill="both", expand=True)


def show_insurance_page():
    hide_all_pages()
    insurance_frame.pack(fill="both", expand=True)


def show_insurance_purchase_page():
    hide_all_pages()
    update_insurance_purchase_page()  # به‌روزرسانی صفحه خرید بیمه با داده‌ها
    insurance_purchase_frame.pack(fill="both", expand=True)


def hide_all_pages():
    person_frame.pack_forget()
    insurance_frame.pack_forget()
    insurance_purchase_frame.pack_forget()


# ساخت پنجره اصلی
app = ctk.CTk()
app.title("برنامه نمونه")
app.geometry("400x300")

# ساخت فریم‌ها برای صفحات مختلف
person_frame = ctk.CTkFrame(app)
insurance_frame = ctk.CTkFrame(app)
insurance_purchase_frame = ctk.CTkFrame(app)

# اضافه کردن محتوا به صفحات مختلف
ctk.CTkLabel(person_frame, text="صفحه شخص").pack(pady=20)
ctk.CTkLabel(insurance_frame, text="صفحه بیمه").pack(pady=20)
ctk.CTkLabel(insurance_purchase_frame, text="صفحه خرید بیمه").pack(pady=20)

# ساخت فریم برای دکمه‌ها
button_frame = ctk.CTkFrame(app)
button_frame.pack(side="top", fill="x")

# اضافه کردن دکمه‌ها به صفحه اصلی
person_button = ctk.CTkButton(button_frame, text="شخص", command=show_person_page)
person_button.pack(side="left", padx=10, pady=10)

insurance_button = ctk.CTkButton(button_frame, text="بیمه", command=show_insurance_page)
insurance_button.pack(side="left", padx=10, pady=10)

insurance_purchase_button = ctk.CTkButton(button_frame, text="خرید بیمه", command=show_insurance_purchase_page)
insurance_purchase_button.pack(side="left", padx=10, pady=10)

# نمایش صفحه اولیه
show_person_page()  # این خط صفحه "شخص" را به‌طور پیش‌فرض نمایش می‌دهد

# اجرای برنامه
app.mainloop()
