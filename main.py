import tkinter as tk
from PIL import Image, ImageTk

class Window:
    def __init__(self):
        #Initiate Window
        self.win = tk.Tk()
        self.win.title("Maintenance App")
        self.win.geometry("1200x600")
        self.win.resizable(False, False)
        self.win.config(bg="#008DDA")

        #Call Methods
        self.frame()
        self.createWidgets()
        
    def frame(self):
        #Frame
        self.frame1 = tk.Frame(self.win, width=570, height=550, bg="#ACE2E1", bd=5, relief=tk.GROOVE)
        self.frame2 = tk.Frame(self.win, width=550, height=550, bg="#ACE2E1", bd=5, relief=tk.GROOVE)

        #Frame pos
        self.frame1.place(x=20, y=20)
        self.frame2.place(x=620, y=20)

    def createWidgets(self):
        #Frame1
        #Label
        self.lbl_title = tk.Label(self.frame1, text="Car Maintenance", font=("Arial", 21, "underline"), bg="#ACE2E1")
        self.lbl_car_title = tk.Label(self.frame1, text="Car Selection", font=("Arial", 18, "underline"), bg="#ACE2E1")
        self.lbl_interior_option_title = tk.Label(self.frame1, text="Interior Option", font=("Arial", 18, "underline"), bg="#ACE2E1")
        self.lbl_exterior_finish_title = tk.Label(self.frame1, text="Exterior Finish", font=("Arial", 18, "underline"), bg="#ACE2E1")
        self.lbl_exterior_option_title = tk.Label(self.frame1, text="Exterior Option", font=("Arial", 18, "underline"), bg="#ACE2E1")

        #Label pos
        self.lbl_title.place(x=170, y=10)
        self.lbl_car_title.place(x=30, y=60)
        self.lbl_interior_option_title.place(x=30, y=200)
        self.lbl_exterior_finish_title.place(x=30, y=320)
        self.lbl_exterior_option_title.place(x=30, y=410)

        #Radiobutton
        self.rd_bmw = tk.Radiobutton(self.frame1, text="BMW" + " " * 50 + "$5,000.00", font=("Arial", 16), bg="#ACE2E1")
        self.rd_subaru = tk.Radiobutton(self.frame1, text="Subaru" + " " * 48 + "$2,500.00", font=("Arial", 16), bg="#ACE2E1")
        self.rd_chevrolet = tk.Radiobutton(self.frame1, text="chevrolet" + " " * 45 + "$4,100.00", font=("Arial", 16), bg="#ACE2E1")

        self.rd_hardTop = tk.Radiobutton(self.frame1, text="Hard Top", font=("Arial", 16), bg="#ACE2E1")
        self.rd_Convertible = tk.Radiobutton(self.frame1, text="Convertible", font=("Arial", 16), bg="#ACE2E1")

        #Radiobutton pos
        self.rd_bmw.place(x=30, y=100)
        self.rd_subaru.place(x=30, y=130)
        self.rd_chevrolet.place(x=30, y=160)

        self.rd_hardTop.place(x=60, y=360)
        self.rd_Convertible.place(x=290, y=360)

        #CheckButton
        self.ck_btn_leather = tk.Checkbutton(self.frame1, text="Leather" + " " * 50 + "$550.00", font=("Arial", 16), bg="#ACE2E1")
        self.ck_btn_GPS = tk.Checkbutton(self.frame1, text="GPS" + " " * 50 + " $1,000.00", font=("Arial", 16), bg="#ACE2E1")

        self.ck_btn_wheel_Upgrade = tk.Checkbutton(self.frame1, text="Wheel Upgrade", font=("Arial", 16), bg="#ACE2E1")
        self.ck_btn_Perf_pack = tk.Checkbutton(self.frame1, text="Performance Package", font=("Arial", 16), bg="#ACE2E1")

        #Checkbutton pos
        self.ck_btn_leather.place(x=30, y=240)
        self.ck_btn_GPS.place(x=30, y=270)

        self.ck_btn_wheel_Upgrade.place(x=60, y=450)
        self.ck_btn_Perf_pack.place(x=290, y=450)

        #Button
        self.btn_enter = tk.Button(self.frame2, text="Enter", font=("Arial", 16))
        self.btn_clear = tk.Button(self.frame1, text="Clear", font=("Arial", 12), width=6)

        #Button pos
        self.btn_enter.place(x=10, y=500)
        self.btn_clear.place(x=10, y=500)

        #Frame2
        #Label
        self.receipt_title = tk.Label(self.frame2, text="Receipt", font=("Arial", 21, "underline"), bg="#ACE2E1")
        self.receipt_car_img = tk.Label(self.frame2, text="")
        self.receipt_car_price = tk.Label(self.frame2, text="$5,000.00", font=("Arial", 16), bg="#ACE2E1")

        #Label pos
        self.receipt_title.place(x=230, y=10)
        self.receipt_car_img.place(x=30, y=60)
        self.receipt_car_price.place(x=300, y=80) 

        #Load Image
        bmw_image = Image.open("Main/img/BMW.gif").resize((180, 100))
        subaru_image = Image.open("Main/img/Subaru.gif")
        chevrolet_image = Image.open("Main/img/Chevrolet.gif")

        #Convert Img to PhotoImage
        self.img_bmw = ImageTk.PhotoImage(bmw_image)
        self.img_subaru = ImageTk.PhotoImage(subaru_image)
        self.img_chevrolet = ImageTk.PhotoImage(chevrolet_image)

        self.receipt_car_img.config(image=self.img_bmw, compound=tk.LEFT)

window = Window()
window.win.mainloop()