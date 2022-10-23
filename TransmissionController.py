from tkinter import PhotoImage

import customtkinter, tkinter
from ImageFrame import ImageFrame

'''
    @Author: Theo Madikgetla
    @Date: 15 October 2022
    @Function:
            This class/module is responsible setting up the GUI
            implementation.
'''

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Will store filename
        self.filename = "ADC_readings.csv"

        self.geometry("500x300")
        self.title("Message by Light")
        self.minsize(300, 200)

        # Creates a 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # Creates Progress Bar
        self.progress_bar = customtkinter.CTkProgressBar(self, width=260,orient='horizontal', mode='determinate', determinate_speed=2)
        self.progress_bar.pack(side='top', padx=10, pady=10)
        self.progress_bar.place(x=110, y=10)

        # TEXT BOX USING customtkinter
       # self.textbox = customtkinter.CTkTextbox(self, width=460, height=80)
       #self.textbox.pack(side='bottom', pady=10)
       # self.textbox.configure(state="normal")  # Configures textbox to read-only

        # TEXTBOX using tkinter: This seems to work with regards to writing
        # text from the text widget into a file. Not pretty, but it will do
        # for now.
        self.text_box = tkinter.Text(self, width=60, height=6, bg="gray")
        self.text_box.pack(side='bottom', pady=10)
        self.text_box.configure(state="normal")

        # Creates 'START' Button
        self.start_button = customtkinter.CTkButton(self, text="START", command=self.start_transmission)
        self.start_button.pack(side='left',padx=10, pady=10)
        self.start_button.place(x=10, y=60)

        # Creates 'DISPLAY' Button
        self.display_button = customtkinter.CTkButton(self, text="DISPLAY", command=self.display_data())
        self.display_button.pack(side='left',padx=10, pady=10)
        self.display_button.place(x=180, y=60)

        # Creates the 'GENERATE' button which generates a logfile
        self.generate_button = customtkinter.CTkButton(self, text="GENERATE", command=self.generate_file())
        self.generate_button.pack(side='right',padx=10, pady=10)
        self.generate_button.place(x=340, y=60)

        # Creates the 'ECHO TEST' button which tests the serial connection
        self.echo_test_button = customtkinter.CTkButton(self, text="ECHO TEST", command=self.echo_test())
        self.echo_test_button.pack(side='left',padx=10, pady=10)
        self.echo_test_button.place(x=10, y=120)

        # Creates the 'STOP' button which stops the transmission and closes serial connection
        self.stop_button = customtkinter.CTkButton(self, text="STOP", command=self.stop_transmission())
        self.stop_button.pack(side='right',padx=10, pady=10)
        self.stop_button.place(x=340,y=120)

        # Adds LOGO for the GUI
        self.image_frame = ImageFrame(self, header_name="ImageFrame", width=200,height=150)
        #self.image_frame.grid(row=300, column=300, padx=10, pady=10)
        self.image_frame.pack(side='left', padx=10, pady=10)
        self.image_frame.place(x=170, y=120)


        '''
            Code all the required widgets
        '''
    # Starts transmission
    def start_transmission(self):
        self.progress_bar.set(0)
        self.progress_bar.start()

    # Displays as data that is transmitted by the other node
    def display_data(self):
        # Still need to add 'read_serial_data' function from serialConnection
        # module.
        for i in range(100):
            self.text_box.insert("0.0", "Peace, Love and Positivity...\n")


    # Generates a log file of adc data
    def generate_file(self):
        print("Generate button clicked...")
        file = open(self.filename, "w")
        file.write(self.text_box.get("0.0", "end"))
        file.close()
      # If there's still time, add a pop window that allows the
      # user to enter filename, else hard code it.


    # Tests if the serial coms is working
    def echo_test(self):
        pass

    # Stops the transmission reading
    def stop_transmission(self):
        self.progress_bar.quit()
        # Still need to add 'close connection' function from
        # the SerialConnection module.


if __name__ == "__main__":
    app = App()
    app.mainloop()