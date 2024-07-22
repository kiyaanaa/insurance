from insurance_app.view import *


class Insurance:
    def __init__(self):
        super().__init__()
        self.win = tk.Tk()
        self.win.title("Insurance Details")
        w, h = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
        self.win.geometry(f"{w}x{h}")

        ttk.Label(self.win, text=f" : لطفا مشخصات بیمه را وارد کنید", width=30, anchor="e").place(x=1063, y=20)

        ttk.Label(self.win, text=": اسم", width=20,anchor="e").place(x=1120, y=70)
        tk.Entry(self.win).place(x=1050, y=70)

        ttk.Label(self.win, text=": تاریخ فروش", width=20, anchor="e").place(x=1120, y=110)
        tk.Entry(self.win).place(x=1050, y=110)

        ttk.Label(self.win, text=": قیمت", width=20, anchor="e").place(x=1120, y=150)
        tk.Entry(self.win).place(x=1050, y=150)

        ttk.Button(self.win, text="تایید", command=self.win.destroy).place(x=1080, y=350)

        self.win.mainloop()


ui = Insurance()