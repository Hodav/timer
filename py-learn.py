from tkinter import Tk
from tkinter.ttk import Frame, Label
import time


class Timer(Frame):
    def __init__(self):
        super().__init__()

        self.label = Label(background="white", font=("Arial", 32), anchor="ne")
        self.label.pack()

        self.timing = time.time()
        self.update_clock()

    def update_clock(self):
        timer = str(round(time.time() - self.timing) // 3600).rjust(2, "0") + ":" + str(round(time.time() - self.timing) // 60 % 60).rjust(2, "0") + ":" + str(
            round(time.time() - self.timing) % 60).rjust(2, "0")
        self.label.configure(text=(time.strftime("%H:%M:%S") + "   " + timer))
        self.after(1000, self.update_clock)


def main():
    root = Tk()
    root.title("timer")
    root.iconbitmap(default="clock.ico")
    root.geometry("500x50+0-40")
    root.resizable(False, False)
    root["bg"] = "white"
    root.attributes("-topmost",True)
    app = Timer()
    root.mainloop()


if __name__ == '__main__':
    main()