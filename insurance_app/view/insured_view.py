from insurance_app.view import *


class Insured:
    def __init__(self):
        super().__init__()
        self.win = tk.Tk()
        self.win.title("Insured Details")
        w, h = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
        self.win.geometry(f"{w}x{h}")

        ttk.Label(self.win, text=f" : لطفا مشخصات فرد بیمه شده را وارد کنید", width=40, anchor="e").place(x=1000, y=20)

        ttk.Label(self.win, text=": اسم", width=20,anchor="e").place(x=1120, y=70)
        tk.Entry(self.win).place(x=1050, y=70)

        ttk.Label(self.win, text=": فامیل", width=20, anchor="e").place(x=1120, y=110)
        tk.Entry(self.win).place(x=1050, y=110)

        ttk.Label(self.win, text=": جنسیت", width=20, anchor="e").place(x=1120, y=150)
        tk.Entry(self.win).place(x=1050, y=150)

        ttk.Label(self.win, text=": کد ملی", width=20, anchor="e").place(x=1120, y=190)
        tk.Entry(self.win).place(x=1050, y=190)

        ttk.Label(self.win, text=": شماره تلفن",width=20, anchor="e").place(x=1120, y=230)
        tk.Entry(self.win).place(x=1050, y=230)

        ttk.Label(self.win, text=": ایمیل", width=20, anchor="e").place(x=1120, y=270)
        tk.Entry(self.win).place(x=1050, y=270)

        ttk.Label(self.win, text=": آدرس", width=20, anchor="e").place(x=1120, y=310)
        tk.Entry(self.win).place(x=1050, y=310)

        ttk.Button(self.win, text="تایید", command=self.win.destroy).place(x=1080, y=350)

        self.win.mainloop()


ui = Insured()