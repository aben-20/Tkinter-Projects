import tkinter as tk
import math

cal = tk.Tk()
cal.geometry("450x479")
cal.title("Calculator")
cal.resizable(0, 0)


operator = ''

def click(number):
    global operator
    operator = operator + str(number)
    variable.set(operator)

def answer():
    try:
        global operator
        if '√(' in operator:
            operator = operator.replace('√(', 'math.sqrt(')
            operator = str(eval(operator))
        else:
            operator = str(eval(operator))
        variable.set(operator)
    except ZeroDivisionError:
        operator = 'NaN'
        variable.set(operator)

# def answer():
#     try:
#         global operator
#         if 'sqrt(' in operator:
#             operator = operator.replace('sqrt(', 'math.sqrt(')
#         else:
#             operator = str(eval(operator))
#         variable.set(operator)
#     except ZeroDivisionError:
#         operator = 'NaN'
#         variable.set(operator)

def clear():
    global operator
    operator = ""
    variable.set(operator)

# operator = ''

# ============================================ display screen =========================================================
variable = tk.StringVar()
display = tk.Entry(cal, font=('arial', 20, 'bold'), bd=25, insertwidth=4, relief="sunken", textvariable=variable)
#display.configure(state="disabled")
display.grid(columnspan=8, sticky="n,e,s,w")

# ============================================( buttons 7 8 9 plus)=====================================================
button7 = tk.Button(cal, text='7', font=('arial', 20, 'bold'), bd=8, padx=16, pady=16, command=lambda: click(7))
button7.grid(row=3, column=0)

button8 = tk.Button(cal, text='8', font=('arial', 20, 'bold'), bd=8, padx=16, pady=16, command=lambda: click(8))
button8.grid(row=3, column=1)

button9 = tk.Button(cal, text='9', font=('arial', 20, 'bold'), bd=8, padx=16, pady=16, command=lambda: click(9))
button9.grid(row=3, column=2)

button_sqrt = tk.Button(cal, text='√', font=('arial', 20, 'bold'), bd=8, padx=16, pady=16, command=lambda: click('√('))
button_sqrt.grid(row=3, column=3)

button_plus = tk.Button(cal, text='+', font=('arial', 20, 'bold'), bd=8, padx=30, pady=16,command=lambda:click('+'))
button_plus.grid(row=3, column=4)

# =============================================( buttons 4 5 6 minus = )==============================================
button4 = tk.Button(cal, text='4', font=('arial', 20, 'bold'), bd=8, padx=16, pady=16, command=lambda: click(4))
button4.grid(row=4, column=0)

button5 = tk.Button(cal, text='5', font=('arial', 20, 'bold'), bd=8, padx=16, pady=16, command=lambda: click(5))
button5.grid(row=4, column=1)

button6 = tk.Button(cal, text='6', font=('arial', 20, 'bold'), bd=8, padx=16, pady=16, command=lambda: click(6))
button6.grid(row=4, column=2)

button_minus = tk.Button(cal, text='-', font=('arial', 20, 'bold'), bd=8, padx=19, pady=16, command=lambda: click('-'))
button_minus.grid(row=4, column=3)

button_equal = tk.Button(cal, text='=', font=('arial', 20, 'bold'), bd=8, padx=30, pady=16, command=answer)
button_equal.grid(row=4, column=4)

# ============================================( buttons 1 2 3 x )====================================================
button1 = tk.Button(cal, text='1', font=('arial', 20, 'bold'), bd=8, padx=16, pady=16, command=lambda: click(1))
button1.grid(row=5, column=0)

button2 = tk.Button(cal, text='2', font=('arial', 20, 'bold'), bd=8, padx=16, pady=16, command=lambda: click(2))
button2.grid(row=5, column=1)

button3 = tk.Button(cal, text='3', font=('arial', 20, 'bold'), bd=8, padx=16, pady=16, command=lambda: click(3))
button3.grid(row=5, column=2)

button_multi = tk.Button(cal, text='*', font=('arial', 20, 'bold'), bd=8, padx=16, pady=16, command=lambda: click('*'))
button_multi.grid(row=5, column=3)

button_point = tk.Button(cal, text='.', font=('arial', 20, 'bold'), bd=8, padx=34, pady=16, command=lambda: click('.'))
button_point.grid(row=5, column=4)

# ===========================================( buttons 0 () / clear )==============================================
button0 = tk.Button(cal, text='0', font=('arial', 20, 'bold'), bd=8, padx=16, pady=16, command=lambda: click(0))
button0.grid(row=6, column=0)

button_l = tk.Button(cal, text=' (', font=('arial', 20, 'bold'), bd=8, padx=16, pady=16, command=lambda: click('('))
button_l.grid(row=6, column=1)

button_r = tk.Button(cal, text=')', font=('arial', 20, 'bold'), bd=8, padx=16, pady=16, command=lambda: click(')'))
button_r.grid(row=6, column=2)

button_div = tk.Button(cal, text=' /', font=('arial', 20, 'bold'), bd=8, padx=16, pady=16, command=lambda: click('/'))
button_div.grid(row=6, column=3)

button_clear = tk.Button(cal, text='clc', font=('arial', 20, 'bold'),  bd=8, padx=16, pady=16, command=clear)
button_clear.grid(row=6, column=4)
button_clear. configure(background='red')

# ==================================================================================================================

cal. configure(background='grey')

cal.mainloop()

