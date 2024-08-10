import customtkinter as ctk
import sqlite3

from insurance_app.view.insurance_sell_view import insurance_sell_view
from insurance_app.view.insurance_view import insurance_view
from insurance_app.view.insured_view import insured_view


def get_insurance_purchases():
    # اتصال به دیتابیس (تغییر دهید به مسیر و نام دیتابیس خود)
    conn = sqlite3.connect('insurance.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM insurance_purchases")
    purchases = cursor.fetchall()

    conn.close()
    return purchases


def update_insurance_purchase_page():
    for widget in insurance_purchase_frame.winfo_children():
        widget.destroy()

    purchases = get_insurance_purchases()

    for purchase in purchases:
        ctk.CTkLabel(insurance_purchase_frame,
                     text=f"ID: {purchase[0]}, نام بیمه: {purchase[1]}, مبلغ: {purchase[2]}").pack(pady=5)


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


app = ctk.CTk()
app.title("برنامه نمونه")
app.geometry("500x400")

person_frame = ctk.CTkFrame(app)
insurance_frame = ctk.CTkFrame(app)
insurance_purchase_frame = ctk.CTkFrame(app)

ctk.CTkLabel(person_frame, text="صفحه شخص").pack(pady=20)
ctk.CTkLabel(insurance_frame, text="صفحه بیمه").pack(pady=20)
ctk.CTkLabel(insurance_purchase_frame, text="صفحه خرید بیمه").pack(pady=20)

button_frame = ctk.CTkFrame(app)
button_frame.pack(side="top", fill="x")

person_button = ctk.CTkButton(button_frame, text="شخص", command=show_insured_view)
person_button.pack(side="left", padx=10, pady=10)

insurance_button = ctk.CTkButton(button_frame, text="بیمه", command=show_insurance_view)
insurance_button.pack(side="left", padx=10, pady=10)

insurance_purchase_button = ctk.CTkButton(button_frame, text="خرید بیمه", command=show_insurance_sell_view)
insurance_purchase_button.pack(side="left", padx=10, pady=10)

app.mainloop()
