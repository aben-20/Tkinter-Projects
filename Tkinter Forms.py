import tkinter as tk
import sqlite3
window = tk.Tk()
window.geometry('650x650')

full_name = tk.StringVar()
full_address = tk.StringVar()
full_email = tk.StringVar()
full_number = tk.StringVar()
var_gender = tk.StringVar()
var_politic = tk.StringVar()
var_edu = tk.StringVar()
var_check1 = tk.IntVar()
var_check2 = tk.IntVar()
var_check3 = tk.IntVar()
var_check4 = tk.IntVar()
var_check5 = tk.IntVar()


def info():
    _name = full_name.get()
    _address = full_address.get()
    _email = full_email.get()
    _number = full_number.get()
    _gender = var_gender.get()
    _political = var_politic.get()
    _edu = var_edu.get()
    _check_1 = var_check1.get()
    _check_2 = var_check2.get()
    _check_3 = var_check3.get()
    _check_4 = var_check4.get()
    _check_5 = var_check5.get()
    if _check_1 == 1:
        _check_1 = 'I have tattoos and/or piercings'
    else:
        _check_1 = 'Not applicable'
    if _check_2 == 1:
        _check_2 = 'I am more than two years older than my daughter'
    else:
        _check_2 = 'Not applicable'
    if _check_3 == 1:
        _check_3 = 'I own a panel van or V8'
    else:
        _check_3 = 'Not applicable'
    if _check_4 == 1:
        _check_4 = 'I work full time'
    else:
        _check_4 = 'Not applicable'
    if _check_5 == 1:
        _check_5 = 'My parents are rich'
    else:
        _check_5 = 'Not applicable'

    into_text_file(_name, _address, _email, _number, _gender, _political, _edu, _check_1, _check_2, _check_3, _check_4,
                   _check_5)

    print(f"Your name is {_name}")
    print(f"Your address is {_address}")
    print(f"Your email is {_email}")
    print(f"Your number is {_number}")
    print(f"Your gender is {_gender}")
    print(f"You are a {_political}")
    print(f"You completed {_edu}")
    print(_check_1)
    print(_check_2)
    print(_check_3)
    print(_check_4)
    print(_check_5)
    print('')


def into_text_file(a, b, c, d, e, f, g, h, i, j, k, l):
    file = open("details.txt", "a")
    file.write(f"\nName: {a}\nAddress: {b}\nEmail: {c}\nNumber:{d}\nGender: {e}\nPolitical: {f}\nEdu_level: {g}\n1: {h}"
               f"\n2: {i}\n3: {j}\n4: {k}\n5: {l}\n-----------------------------------------------")
    file.close()


def database():
    _name = full_name.get()
    _address = full_address.get()
    _email = full_email.get()
    _number = full_number.get()
    _gender = var_gender.get()
    _political = var_politic.get()
    _edu = var_edu.get()
    _check_1 = var_check1.get()
    _check_2 = var_check2.get()
    _check_3 = var_check3.get()
    _check_4 = var_check4.get()
    _check_5 = var_check5.get()
    if _check_1 == 1:
        _check_1 = 'I have tattoos and/or piercings'
    else:
        _check_1 = 'Not applicable'
    if _check_2 == 1:
        _check_2 = 'I am more than two years older than my daughter'
    else:
        _check_2 = 'Not applicable'
    if _check_3 == 1:
        _check_3 = 'I own a panel van or V8'
    else:
        _check_3 = 'Not applicable'
    if _check_4 == 1:
        _check_4 = 'I work full time'
    else:
        _check_4 = 'Not applicable'
    if _check_5 == 1:
        _check_5 = 'My parents are rich'
    else:
        _check_5 = 'Not applicable'

    con_form = sqlite3.connect('M_Forms.db')
    with con_form:
        cursor = con_form.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Bachelor (Name TEXT, Address TEXT, Email TEXT, Number TEXT, Gender TEXT,'
                   'Political TEXT, Education TEXT, Check_1 TEXT, Check_2 TEXT, Check_3 TEXT, Check_4 TEXT,'
                   'Check_5 TEXT)')
    cursor.execute('INSERT INTO Bachelor(Name, Address, Email, Number, Gender, Political, Education, Check_1, Check_2,'
                   'Check_3, Check_4, Check_5) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (str(_name), str(_address), str(_email), str(_number),
                                                                                  str(_gender), str(_political), str(_edu), str(_check_1),
                                                                                  str(_check_2), str(_check_3), str(_check_4), str(_check_5))
                   )
    con_form.commit()


header = tk.Label(window, text='Application Form', font=("Times New Roman", 19, "bold"), bg='grey')
header.pack()

note = tk.Label(window, text='Note:', font=('Times New Roman', 15, 'bold'), bg='#35424a')
note.place(x=10, y=40)
note_info = tk.Label(window, text='Form is to be completed at least 21 days prior to date', font=('Times New Roman', 12), bg='#35424a')
note_info.place(x=68, y=44)

sub_header = tk.Label(window, text='Personal Details', font=('Times New Roman', 13, 'bold'), bg='#35424a')
sub_header.place(x=10, y=80)

name = tk.Label(window, text='Name:', font=('Times New Roman', 12), bg='#35424a')
name.place(x=10, y=100)
name_entry = tk.Entry(window, relief='sunken', textvar=full_name)
name_entry.place(x=110, y=105)

address = tk.Label(window, text='Address:', font=('Times New Roman', 12), bg='#35424a', padx=0.08, pady=0.3)
address.place(x=10, y=130)
address_entry = tk.Entry(window, relief='sunken', textvar=full_address)
address_entry.place(x=110, y=130)

email = tk.Label(window, text='Email:', font=('Times New Roman', 12), bg='#35424a')
email.place(x=10, y=160)
email_entry = tk.Entry(window, relief='sunken', textvar=full_email)
email_entry.place(x=110, y=160)

phone = tk.Label(window, text='Phone Number:', font=('Times New Roman', 12), bg='#35424a')
phone.place(x=10, y=190)
phone_entry = tk.Entry(window, relief='sunken', textvar=full_number)
phone_entry.place(x=110, y=190)

gender = tk.Label(window, text='Gender', font=('Times New Roman', 12), bg='#35424a')
gender.place(x=10, y=220)

gender_1 = tk.Radiobutton(window, text='Male', bg='#35424a', variable=var_gender, value='Male')
gender_1.select()
gender_1.place(x=12, y=240)

gender_2 = tk.Radiobutton(window, text='Female', bg='#35424a', variable=var_gender, value='Female')
gender_2.place(x=14, y=260)


check = tk.Label(window, text='Check all that apply', font=('Times New Roman', 13, 'bold'), bg='#35424a')
check.place(x=10, y=310)

check_1 = tk.Checkbutton(window, text='I have tattoos and/or piercings', variable=var_check1, offvalue=0, font=('Times New Roman', 13), bg='#35424a')
check_1.place(x=10, y=340)

check_2 = tk.Checkbutton(window, text='I am more than two years older than my daughter', variable=var_check2, offvalue=0, font=('Times New Roman', 13), bg='#35424a')
check_2.place(x=10, y=360)

check_3 = tk.Checkbutton(window, text='I own a panel van or V8', variable=var_check3, offvalue=0, font=('Times New Roman', 13), bg='#35424a')
check_3.place(x=10, y=382)

check_4 = tk.Checkbutton(window, text='I work full time', variable=var_check4, offvalue=0, font=('Times New Roman', 13), bg='#35424a')
check_4.place(x=10, y=408)

check_5 = tk.Checkbutton(window, text='My parents are rich', variable=var_check5, offvalue=0, font=('Times New Roman', 13), bg='#35424a')
check_5.place(x=10, y=435)

pol = tk.Label(window, text='Political Persuasion:', font=('Times New Roman', 13), bg='#35424a')
pol.place(x=10, y=480)
pol_list = ['Conservative', 'Liberal', 'Centrist']
dropList_1 = tk.OptionMenu(window, var_politic, *pol_list)
var_politic.set("Select")
dropList_1.place(x=167, y=476)

edu = tk.Label(window, text='Education Level Completed:', font=('Times New Roman', 13), bg='#35424a')
edu.place(x=325, y=480)
edu_list = ['University', 'High School', 'None']
dropList_2 = tk.OptionMenu(window, var_edu, *edu_list)
var_edu.set("Select")
dropList_2.place(x=530, y=476)

submit_button = tk.Button(window, text="Submit application", bg='green', font=('Times New Roman', 13), command=lambda: [
    info(), database()])
submit_button.place(x=10, y=570)


window.configure(bg='#35424a')
window.mainloop()