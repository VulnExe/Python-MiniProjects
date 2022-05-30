from tkinter import *
import time
def clocktime(time1 = ""):
    time2= time.strftime("%H:%M:%S")
    if time2!=time1:
        time1 = time2
        clock.config(text=time2)


    clock.after(200,clocktime)
clockface=TK()
clock = Label(clockface, font = "verdans 15 bold")
clock.pack(fill="both",expand=1)
clocktime()
clockface.mainloop()