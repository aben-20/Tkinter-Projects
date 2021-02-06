import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageTk
import sqlite3

window = tk.Tk()
window.geometry('500x500')
window.title('Registration form')
# window.resizable(0, 0)

img = Image.open("C:\\Users\\BENJAMIN ABOAGYE\\Pictures\\python_logo.PNG")
photo = ImageTk.PhotoImage(img)
lab = tk.Label(image=photo)
lab.pack()


def exit_window():
    exit()


def about():
    tkinter.messagebox.showinfo('Welcome!', 'This is a demo')


def database():
    name1 = first_name.get()
    last1 = last_name.get()
    date = dob.get()
    country_info = var_country.get()
    # male_info = var_male.get()
    # female_info = var_female.get()
    con = sqlite3.connect('Form.db')
    with con:
        cursor = con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Student (Name Text, Last TEXT, DOB TEXT, Country TEXT')#, Gender TEXT')
    cursor.execute('INSERT INTO Student(Name, Last, DOB, Country) VALUES(????)', (name1, last1, date, country_info))
    con.commit()


menu = tk.Menu(window)
window.config(menu=menu)

submenu1 = tk.Menu(menu)
menu.add_cascade(label='File', menu=submenu1)
submenu1.add_command(label='Exit', command=exit_window)

submenu2 = tk.Menu(menu)
menu.add_cascade(label='Option', menu=submenu2)
submenu2.add_command(label='About', command=about)


first_name = tk.StringVar()
last_name = tk.StringVar()
dob = tk.StringVar()
var_country = tk.StringVar()
var_male = tk.IntVar()
var_female = tk.IntVar()


def info():
    name_1 = first_name.get()
    name_2 = last_name.get()
    birth_date = dob.get()
    country = var_country.get()
    
    print(f"Your name is {name_1}{name_2}")
    print(f"Your date of birth is {birth_date}")
    print(f"Your country is {country}")
    print('Male: '+str(var_male.get()), 'Female: '+str(var_female.get()))
    tk.messagebox.showinfo('Welcome', 'Sign up was successful!')


def second_window():
    window_2 = tk.Tk()
    window_2.title('Hello !')
    window_2.geometry('250x200')
    label_01 = tk.Label(window_2, text='Registration Successful', relief='solid', font=("arial", 12, "bold"))
    label_01.place(x=30, y=70)
    button_01 = tk.Button(window_2, text='demo', width=12, bg='brown', fg='white', command=about)
    button_01.place(x=30, y=110)


header = tk.Label(window, text="Registration Form", relief="solid", width=18, font=("arial", 19, "bold"))
header.place(x=94, y=120)


label2 = tk.Label(window, text="First Name:", width=15, font=("arial", 10, "bold"))
label2.place(x=80, y=200)
entry2 = tk.Entry(window, relief="sunken", textvar=first_name)
entry2.place(x=240, y=202)


label3 = tk.Label(window, text="Last Name:", width=15, font=("arial", 10, "bold"))
label3.place(x=80, y=240)
entry3 = tk.Entry(window, relief="sunken", textvar=last_name)
entry3.place(x=240, y=242)


label4 = tk.Label(window, text="DOB:", width=15, font=("arial", 10, "bold"))
label4.place(x=80, y=280)
entry4 = tk.Entry(window, relief="sunken", textvar=dob)
entry4.place(x=240, y=282)


label5 = tk.Label(window, text="Country:", width=15, font=("arial", 10, "bold"))
label5.place(x=80, y=320)
country_list = ['America', 'Ghana', 'Egypt']
drop_list = tk.OptionMenu(window, var_country, *country_list)
var_country.set("Select country")
drop_list.place(x=240, y=316)

label6 = tk.Label(window, text="Gender:", width=15, font=("arial", 10, "bold"))
label6.place(x=80, y=360)
sex_male = tk.Checkbutton(window, text='Male', variable=var_male)
sex_male.place(x=240, y=360)
sex_female = tk.Checkbutton(window, text='Female', variable=var_female)
sex_female.place(x=320, y=360)


signup_button = tk.Button(window, text="Sign Up", width=12, bg="brown", fg="white", command=info)
signup_button.place(x=120, y=420)

# exit_button = tk.Button(window, text="Exit", width=12, bg="brown", fg="white", command=exit_window)
# exit_button.place(x=280, y=420)

exit_button = tk.Button(window, text="Exit", width=12, bg="brown", fg="white", command=exit_window)
exit_button.place(x=280, y=420)
window.bind("<Return>", database)

login_button = tk.Button(window, text="login", width=12, bg="brown", fg="white", command=database)
login_button.place(x=400, y=30)


# login_button = tk.Button(window, text="login", width=12, bg="brown", fg="white", command=database)
# login_button.place(x=400, y=30)
# window.bind("<Return>", database)

window.mainloop()