import tkinter

window = tkinter.Tk()
window.geometry('250x150')

deg_f = tkinter.StringVar()
deg_c = tkinter.StringVar()


def convert(*args):
    try:
        value = float(deg_f.get())
        deg_c.set(round((value - 32) * 5 / 9, 4))
    except ValueError:
        pass


def exit_window():
    exit()


fahrenheit = tkinter.Label(window, text='Fahrenheit', font=('Times New roman', 12))
fahrenheit.place(x=10, y=20)

f_entry = tkinter.Entry(window, relief='sunken', textvariable=deg_f)
f_entry.place(x=120, y=21)

celsius = tkinter.Label(window, text='Celsius', font=('Times New roman', 12))
celsius.place(x=10, y=45)

c_entry = tkinter.Entry(window, relief='sunken', textvariable=deg_c)
c_entry.place(x=120, y=45)

button = tkinter.Button(window, text='convert', font=('Times New roman', 12), command=convert)
button.place(x=10, y=85)

quit_button = tkinter.Button(window, text='close', font=('Times New roman', 12), command=exit_window)
quit_button.place(x=150, y=85)

window.bind('<Return>', convert)
window.mainloop()
