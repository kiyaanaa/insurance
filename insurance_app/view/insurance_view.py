import customtkinter as ctk
from tkinter import messagebox
from insurance_app.controller.insurance_controller import InsuranceController


class insurance_view:
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

        label_first_name = ctk.CTkLabel(frame, text="نوع بیمه", font=("b nazanin", 20, "bold"))
        label_first_name.place(x=445, y=110, anchor="w")
        self.entry_insurance_type = ctk.CTkEntry(frame, width=320)
        self.entry_insurance_type.place(x=20, y=110, anchor="w")

        label_sale_date = ctk.CTkLabel(frame, text="  تاریخ فروش", font=("b nazanin", 20, "bold"))
        label_sale_date.place(x=370, y=365, anchor="w")
        self.entry_sell_date = ctk.CTkEntry(frame, width=320)
        self.entry_sell_date.place(x=20, y=365, anchor="w")

        label_price = ctk.CTkLabel(frame, text="قیمت", font=("b nazanin", 20, "bold"))
        label_price.place(x=420, y=450, anchor="w")
        self.entry_price = ctk.CTkEntry(frame, width=320)
        self.entry_price.place(x=20, y=450, anchor="w")

        self.button_submit = ctk.CTkButton(frame, text="ذخیره", font=("b nazanin", 18, "bold"),
                                           command=self.submit_form)
        self.button_submit.place(x=180, y=535, anchor="w")
        app.mainloop()

    def submit_form(self):
        insurance_type = self.entry_insurance_type.get()
        entry_sell_date = self.entry_sell_date.get()
        entry_price = self.entry_price.get()

        status, insurance = InsuranceController.save(f"{insurance_type} {entry_sell_date}",entry_price)
        if status:
            messagebox.showinfo("Success", "اطلاعات با موفقیت ذخیره شد.")
        else:
            messagebox.showerror("Error","اطلاعات را صحیح وارد کنید")