from insurance_app.view import *


class InsuranceSell:
    def __init__(self):
        super().__init__()
        self.win = tk.Tk()
        self.win.title("Insurance Sell Details")
        w, h = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
        self.win.geometry(f"{w}x{h}")

        ttk.Label(self.win, text=f" : لطفا مشخصات زیر را کامل کنید", width=30, anchor="e").place(x=1063, y=20)

        ttk.Label(self.win, text=": تاریخ شروع فروش", width=20,anchor="e").place(x=1120, y=70)
        tk.Entry(self.win).place(x=1020, y=70)

        ttk.Label(self.win, text=": تاریخ پایان فروش", width=20, anchor="e").place(x=1120, y=110)
        tk.Entry(self.win).place(x=1020, y=110)

        ttk.Label(self.win, text=": تاریخ فروش", width=20, anchor="e").place(x=1120, y=150)
        tk.Entry(self.win).place(x=1020, y=150)

        ttk.Button(self.win, text="تایید", command=self.win.destroy).place(x=1045, y=200)

        self.win.mainloop()


ui = InsuranceSell()