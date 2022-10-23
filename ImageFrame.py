import customtkinter
from PIL import ImageTk, Image

'''
    @author: Theo Madikgetla
    @date: 16 October 2022
    @function:
            This module is responsible for stacking the drop down menu for
            the COM ports and and baudrate.
'''


class ImageFrame (customtkinter.CTkFrame):
    def __init__(self, *args, header_name="ImageFrame", **kwargs):
        super().__init__(*args, **kwargs)

        # Creates an object of tkinter ImageTk
        #image = Image.open("AlienLogo0.jpg")
        #image = image.resize((50, 50), Image.ANTIALIAS)
        #image = ImageTk.PhotoImage(image)

        # A list of COMx options. [NOTE: "x" is the com number]
        # If there's still time, add a function that detects all the active PORTS on
        # the system and displayed them instead.
        COMS = ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "COM10"]

        # A list of Baud-rate options
        baud_rate = ["9600", "11000", "22000", "12090", "22032"]

        # Creates combo-box for COMs
        self.combobox_coms = customtkinter.CTkComboBox(master=self, values=COMS, command=self.combobox_callback_coms)
        self.combobox_coms.pack(padx=5, pady=2)
        self.combobox_coms.set("           COM-x") # set initial value

        # Creates combo-box for Baudrate
        self.combobox = customtkinter.CTkComboBox(master=self, values=baud_rate, command=self.combobox_callback_baudrate)
        self.combobox.pack(padx=5, pady=2)
        self.combobox.set("          Baudrates") # set initial value



        self.header_name  = header_name
        self.header = customtkinter.CTkLabel(self, text=self.header_name)
        #self.header.grid(row=300, column=300, padx=10, pady=10)
       # self.header.grid(row=10, column=0, padx=5, pady=10)

    def combobox_callback_coms(self, choice):
        print("Combobox for COMS dropbox clicked: ", choice)

    def combobox_callback_baudrate(self, choice):
        print("Combobox for Baudrate dropbox clicked: ", choice)
