import customtkinter as ctk
from tkinter import messagebox
from insurance_app.controller.insurance_controller import InsuranceController


class insurance_sell_view:
    def __init__(self):
        app = ctk.CTk()
        app.title("فرم ثبت بیمه")
        app.geometry("500x600")
        ctk.set_appearance_mode("dark")
        frame = ctk.CTkFrame(app)
        frame.pack(fill="both", expand=True)
        label_instruction = ctk.CTkLabel(frame, text=".لطفاً مشخصات بیمه را وارد نمایید",
                                         font=("b nazanin", 20, "bold"))
        label_instruction.place(x=135, y=30, anchor="w")

        label_first_name = ctk.CTkLabel(frame, text="نام", font=("b nazanin", 20, "bold"))
        label_first_name.place(x=445, y=110, anchor="w")
        self.entry_first_name = ctk.CTkEntry(frame, width=320)
        self.entry_first_name.place(x=20, y=110, anchor="w")

        label_last_name = ctk.CTkLabel(frame, text="نام خانوادگی", font=("b nazanin", 20, "bold"))
        label_last_name.place(x=375, y=195, anchor="w")
        self.entry_last_name = ctk.CTkEntry(frame, width=320)
        self.entry_last_name.place(x=20, y=195, anchor="w")

        label_purchase_date = ctk.CTkLabel(frame, text="  تاریخ خرید", font=("b nazanin", 20, "bold"))
        label_purchase_date.place(x=375, y=280, anchor="w")
        self.entry_purchase_date = ctk.CTkEntry(frame, width=320)
        self.entry_purchase_date.place(x=20, y=280, anchor="w")

        label_sale_date = ctk.CTkLabel(frame, text="  تاریخ فروش", font=("b nazanin", 20, "bold"))
        label_sale_date.place(x=370, y=365, anchor="w")
        self.entry_sale_date = ctk.CTkEntry(frame, width=320)
        self.entry_sale_date.place(x=20, y=365, anchor="w")

        label_price = ctk.CTkLabel(frame, text="قیمت", font=("b nazanin", 20, "bold"))
        label_price.place(x=420, y=450, anchor="w")
        self.entry_price = ctk.CTkEntry(frame, width=320)
        self.entry_price.place(x=20, y=450, anchor="w")

        self.button_submit = ctk.CTkButton(frame, text="ذخیره", font=("b nazanin", 18, "bold"),
                                           command=self.submit_form)
        self.button_submit.place(x=180, y=535, anchor="w")
        app.mainloop()

    def submit_form(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        entry_purchase_date = self.entry_purchase_date.get()
        entry_sale_date = self.entry_sale_date.get()
        entry_price = self.entry_price.get()

        status, insurance = InsuranceController.save(f"{first_name} {last_name}", entry_sale_date, entry_price)
        if status:
            messagebox.showinfo("Success", "اطلاعات با موفقیت ذخیره شد.")
        else:
            messagebox.showerror("Error","اطلاعات را صحیح وارد کنید")