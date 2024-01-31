from tkinter import Tk
from tkinter.ttk import Frame, Label
import time


class Timer(Frame):
    def __init__(self):
        super().__init__()
        self.clock = Label(background="white", font=("Arial", 24), anchor="ne")
        self.clock.pack()
        self.timing = time.time()
        self.update_clock()

    def update_clock(self) -> None:
        time_now = time.strftime("%H:%M:%S")
        timer = str(round(time.time() - self.timing) // 3600).rjust(2, "0") + ":" + str(round(time.time() - self.timing) // 60 % 60).rjust(2, "0") + ":" + str(
            round(time.time() - self.timing) % 60).rjust(2, "0")
        time_down = 60 * 60 * 1.5
        timer_down = str(round(time_down - (time.time() - self.timing)) // 3600).rjust(2, "0") + ":" + str(
            round(time_down - (time.time() - self.timing)) // 60 % 60).rjust(2, "0") + ":" + str(
            round(time_down - (time.time() - self.timing)) % 60).rjust(2, "0")
        self.clock.configure(text=(time_now + "   " + timer + "   " + timer_down))
        self.after(1000, self.update_clock)


def main() -> None:
    root = Tk()
    root.title("timer")
    root.iconbitmap(default="clock.ico")
    root.geometry("450x40+0-40")
    root.resizable(False, False)
    root["bg"] = "white"
    root.attributes("-topmost", True)
    app = Timer()
    root.mainloop()


if __name__ == '__main__':
    main()
