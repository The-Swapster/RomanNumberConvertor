from tkinter import *
import tkinter.font as tkfont

def value(r):
    if r == 'I':
        return 1
    if r == 'V':
        return 5
    if r == 'X':
        return 10
    if r == 'L':
        return 50
    if r == 'C':
        return 100
    if r == 'D':
        return 500
    if r == 'M':
        return 1000
    return -1


def romanToDecimal(str):
    res = 0
    i = 0

    while i < len(str):

        s1 = value(str[i])

        if i + 1 < len(str):

            s2 = value(str[i + 1])

            if s1 >= s2:

                res = res + s1
                i = i + 1
            else:

                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1

    display(res)

t = Tk()
t.title('Roman Number Converter')
f = tkfont.Font(family='Century Gothic', size=12)
s = StringVar(t)
t.config(bg='pink')
l1 = Label(t, text='Roman Number', font=f, bg='pink')
l1.grid(row=0, column=0)
l2 = Label(t, textvariable=s, font=f, bg='pink')
l2.grid(row=0, column=1)
l3 = Label(t, text='Decimal Number', font=f, bg='pink')
l3.grid(row=1, column=0)
b1 = Button(t, text='I', font=f, bg='green1', command=lambda: s.set(s.get() + 'I'))
b1.grid(row=2, column=0, ipadx=40, pady=20)
b2 = Button(t, text='V', font=f, bg='green1', command=lambda: s.set(s.get() + 'V'))
b2.grid(row=2, column=1, ipadx=40, padx=20)
b3 = Button(t, text='X', font=f, bg='green1', command=lambda: s.set(s.get() + 'X'))
b3.grid(row=2, column=2, ipadx=40, padx=20)
b4 = Button(t, text='L', font=f, bg='green1', command=lambda: s.set(s.get() + 'L'))
b4.grid(row=3, column=0, ipadx=40, pady=20)
b5 = Button(t, text='C', font=f, bg='green1', command=lambda: s.set(s.get() + 'C'))
b5.grid(row=3, column=1, ipadx=40, padx=20)
b6 = Button(t, text='D', font=f, bg='green1', command=lambda: s.set(s.get() + 'D'))
b6.grid(row=3, column=2, ipadx=40, padx=20)
b7 = Button(t, text='M', font=f, bg='green1', command=lambda: s.set(s.get() + 'M'))
b7.grid(row=4, column=0, ipadx=38, pady=20)
b8 = Button(t, text='Convert', font=f, bg='green1', command=lambda: romanToDecimal(s.get()))
b8.grid(row=4, column=1, columnspan=2, ipadx=90)
def display(r):
    l4 = Label(t, text=r, font=f, bg='pink')
    l4.grid(row=1, column=1)
t.mainloop()