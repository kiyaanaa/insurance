import customtkinter as ctk
from tkinter import messagebox
from insurance_app.controller.insurance_controller import InsuredController


class insured_view:
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
        label_first_name.place(x=445, y=90, anchor="w")
        self.entry_first_name = ctk.CTkEntry(frame, width=320)
        self.entry_first_name.place(x=20, y=90, anchor="w")

        label_first_name = ctk.CTkLabel(frame, text="نام خانوادگی", font=("b nazanin", 20, "bold"))
        label_first_name.place(x=375, y=155, anchor="w")
        self.entry_first_name = ctk.CTkEntry(frame, width=320)
        self.entry_first_name.place(x=20, y=155, anchor="w")

        label_gender = ctk.CTkLabel(frame, text="جنسیت", font=("b nazanin", 20, "bold"))
        label_gender.place(x=410, y=220, anchor="w")
        self.combo_gender = ctk.CTkComboBox(frame, values=["مرد", "زن"], width=320)
        self.combo_gender.place(x=20, y=220, anchor="w")

        label_national_code = ctk.CTkLabel(frame, text="  کد ملی", font=("b nazanin", 20, "bold"))
        label_national_code.place(x=398, y=285, anchor="w")
        self.entry_national_code = ctk.CTkEntry(frame, width=320)
        self.entry_national_code.place(x=20, y=285, anchor="w")

        label_phone_number = ctk.CTkLabel(frame, text="  شماره تلفن", font=("b nazanin", 20, "bold"))
        label_phone_number.place(x=365, y=350, anchor="w")
        self.entry_phone_number = ctk.CTkEntry(frame, width=320)
        self.entry_phone_number.place(x=20, y=350, anchor="w")

        label_email = ctk.CTkLabel(frame, text="ایمیل", font=("b nazanin", 20, "bold"))
        label_email.place(x=410, y=415, anchor="w")
        self.entry_email = ctk.CTkEntry(frame, width=320)
        self.entry_email.place(x=20, y=415, anchor="w")

        label_address = ctk.CTkLabel(frame, text="آدرس", font=("b nazanin", 20, "bold"))
        label_address.place(x=410, y=480, anchor="w")
        self.text_address = ctk.CTkEntry(frame, width=320, height=60)
        self.text_address.place(x=20, y=480, anchor="w")

        self.button_submit = ctk.CTkButton(frame, text="ذخیره", font=("b nazanin", 18, "bold"),
                                           command=self.submit_form)
        self.button_submit.place(x=180, y=535, anchor="w")
        app.mainloop()

    def submit_form(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_first_name.get()
        combo_gender = self.combo_gender.get()
        national_code = self.entry_national_code.get()
        phone_number = self.entry_phone_number.get()
        email = self.entry_email.get()
        address = self.text_address.get()

        status, insurance = InsuredController.save(f"{first_name} {last_name}", combo_gender, national_code,
                                                   phone_number, email, address)
        if status:
            messagebox.showinfo("Success", "اطلاعات با موفقیت ذخیره شد.")
        else:
            messagebox.showerror("Error", "اطلاعات را صحیح وارد کنید")
