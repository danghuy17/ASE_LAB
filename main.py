import tkinter as tk
from tkinter import Frame, ttk
from PIL import Image, ImageTk


class App(tk.Tk):

    def __init__(self):

        super().__init__()

        # Title
        self.title("Ha Noi University of Science and Technology")
        self.iconbitmap("./assets/title.ico")

        # Window
        self.height = 570
        self.width = 800
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(0, 0)

        # MENU
        self.createMenu()




    def createMenu(self):
        self.frame1 = tk.Frame(self, bg='#25A253')
        self.frame1.pack(side="left", ipadx=5, ipady=5, fill="both")

        self.frame2 = tk.Frame(self, bg="white")
        self.frame2.pack(side="right", expand=True, fill="both")

        for i in range(10):
            self.frame1.rowconfigure(i, weight=1)

        self.font_size = 12

        # Button 0
        c_row = 2
        self.image_home = ImageTk.PhotoImage(Image.open("./assets/home_icon.png"))
        button_home = ttk.Button(self.frame1, image=self.image_home, text="Home", compound=tk.LEFT, command=self.buttonHome)
        button_home.grid(row=c_row, sticky=tk.N, padx=5)

        # Button 1
        self.image_info = ImageTk.PhotoImage(Image.open("./assets/info_icon.png"))
        self.icon_info = 100
        button_info = ttk.Button(self.frame1, image=self.image_info, text="Giới thiệu", compound=tk.LEFT, command=self.buttonInfo)
        button_info.grid(row=c_row + 1, sticky=tk.N, padx=5)


        # Button 2
        self.image_2 = ImageTk.PhotoImage(Image.open("./assets/icon_2.png"))
        button_2 = ttk.Button(self.frame1, image=self.image_2, text="Định hướng", compound=tk.LEFT, command=self.button2)
        button_2.grid(row=c_row + 2, sticky=tk.N, padx=5)

        # Button 3
        self.image_3 = ImageTk.PhotoImage(Image.open("./assets/acti_icon.png"))
        button_3 = ttk.Button(self.frame1, image=self.image_3, text="Hoạt động", compound=tk.LEFT, command=self.button3)
        button_3.grid(row=c_row+3, sticky=tk.N, padx=5)

    # Button 0
    def buttonHome(self):
        self.frame2.destroy()
        self.frame2 = tk.Frame(self, bg="white")
        self.frame2.pack(side="right", expand=True, fill="both")


        self.image_ase = ImageTk.PhotoImage(Image.open("./assets/ase_lab.png"))
        label_home = ttk.Label(self.frame2, image=self.image_ase, text="ASE LAB" , font=("Arial", 25), compound=tk.LEFT)
        label_home.pack(side="right", expand=True)

    # Button 1
    def buttonInfo(self):
        self.frame2.destroy()
        self.frame2 = tk.Frame(self, bg="white")
        self.frame2.pack(side="right", expand=True, fill="both")

        # Column Frame
        self.frame2.columnconfigure(0, weight=6)
        self.frame2.columnconfigure(1, weight=1)
        # Row Frame
        self.frame2.rowconfigure(0, weight=1)
        self.frame2.rowconfigure(1, weight=1)
        self.frame2.rowconfigure(2, weight=1)
        self.frame2.rowconfigure(3, weight=5)
        self.frame2.rowconfigure(4, weight=1)

        self.image_d = ImageTk.PhotoImage(Image.open("./assets/ase_lab_icon.png"))
        label_d = ttk.Label(self.frame2, image=self.image_d)
        label_d.grid(column=1, sticky=tk.NE)

        label_foundation = ttk.Label(self.frame2, text="Ở thời điểm hiện tại, Lab hoạt động dưới sự quản lý và \
chỉ đạo trực tiếp từ 2 Thầy :", font=("Arial", self.font_size))
        label_foundation.grid(column=0, row=0, sticky=tk.N, padx=5, pady=5)

        self.image_t1 = ImageTk.PhotoImage(Image.open("./assets/thay_tuan.png"))
        label_i1 = ttk.Label(self.frame2, image=self.image_t1, text="PGS. TS. Đỗ Trọng Tuấn", compound=tk.LEFT)
        label_i1.grid(row=3, sticky=tk.NW)

        self.image_t2 = ImageTk.PhotoImage(Image.open("./assets/thay_thanh.png"))
        label_i2 = ttk.Label(self.frame2, image=self.image_t2, text="TS. Hán Trọng Thanh", compound=tk.LEFT)
        label_i2.grid(row=3, sticky=tk.NE)

    # Button 2
    def button2(self):
        self.frame2.destroy()
        self.frame2 = tk.Frame(self, bg="white")
        self.frame2.pack(side="right", expand=True, fill='both')
        
        self.frame2.columnconfigure(0, weight=6)
        self.frame2.columnconfigure(1, weight=1)

        self.image_d = ImageTk.PhotoImage(Image.open("./assets/ase_lab_icon.png"))
        label_d = ttk.Label(self.frame2, image=self.image_d)
        label_d.grid(column=1, sticky=tk.NE)

        start = 1
        label_0 = ttk.Label(self.frame2, text="IOT(Interner of things)", font=("Arial", self.font_size - 2))
        label_0.grid(column=0, row=start + 1, sticky=tk.W, padx=20, pady=10)

        label_1 = ttk.Label(self.frame2, text="Phát triển hệ thống không người lái(UAV)")
        label_1.grid(column=0, row=start + 2, sticky=tk.W, padx=20, pady=10)
        
        label_2 = ttk.Label(self.frame2, text="Trí tuệ nhân tạo(AI)")
        label_2.grid(column=0, row=start + 3, sticky=tk.W, padx=20, pady=10)

        label_3 = ttk.Label(self.frame2, text="Phát triển xe tự hành")
        label_3.grid(column=0, row=start + 4, sticky=tk.W, padx=20, pady=10)

        label_4 = ttk.Label(self.frame2, text="AI trong xử lý và phân loại dữ liệu")
        label_4.grid(column=0, row=start + 5, sticky=tk.W, padx=20, pady=10)

        label_5 = ttk.Label(self.frame2, text="Thiết kế hệ thống sân bay và máy bay cứu hộ")
        label_5.grid(column=0, row=start + 6, sticky=tk.W, padx=20, pady=10)

    # Button 3
    def button3(self):
        self.frame2.destroy()
        self.frame2 = tk.Frame(self, bg="white")
        self.frame2.pack(side="right", expand=True, fill="both")

        self.frame2.columnconfigure(0, weight=6)
        self.frame2.columnconfigure(1, weight=1)

        self.image_ac1 = ImageTk.PhotoImage(Image.open("./assets/ac1.png"))
        label_1 = ttk.Label(self.frame2, image=self.image_ac1)
        label_1.grid(column=0, row=0)

        self.image_ac2 = ImageTk.PhotoImage(Image.open("./assets/ac2.png"))
        label_2 = ttk.Label(self.frame2, image=self.image_ac2)
        label_2.grid(column=0, row=1)

        # Next
        self.image_n = ImageTk.PhotoImage(Image.open("./assets/next_icon.png"))
        button_next = ttk.Button(self.frame2, image=self.image_n, command=self.buttonN)
        button_next.grid(column=1, row=2, sticky=tk.N)

    # Button 3
    def buttonN(self):
        self.frame2.destroy()
        self.frame2 = tk.Frame(self, bg="white")
        self.frame2.pack(side="right", expand=True, fill="both")

        self.image_ac3 = ImageTk.PhotoImage(Image.open("./assets/ac3.png"))
        label_1 = ttk.Label(self.frame2, image=self.image_ac3)
        label_1.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()


