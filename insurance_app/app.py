import customtkinter as ctk
import sqlite3

from insurance_app.view.insurance_sell_view import insurance_sell_view
from insurance_app.view.insurance_view import insurance_view
from insurance_app.view.insured_view import insured_view


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
def show_insured_view():
    insured_view()


def show_insurance_view():
    insurance_view()


def show_insurance_sell_view():
    insurance_sell_view()


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
person_button = ctk.CTkButton(button_frame, text="شخص", command=show_insured_view)
person_button.pack(side="left", padx=10, pady=10)

insurance_button = ctk.CTkButton(button_frame, text="بیمه", command=show_insurance_view)
insurance_button.pack(side="left", padx=10, pady=10)

insurance_purchase_button = ctk.CTkButton(button_frame, text="خرید بیمه", command=show_insurance_sell_view)
insurance_purchase_button.pack(side="left", padx=10, pady=10)

# اجرای برنامه
app.mainloop()
