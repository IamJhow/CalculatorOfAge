from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date

window = Tk()
window.title("Calculator Of Age")
window.geometry('310x400')

color1 = "#3b3b3b"
color2 = "#333333"
color3 = "#ffffff"
color4 = "#c9184a"
color5 = "#ff4d6d"
color6 = "#800f2f"

frameup = Frame(window, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=color1)
frameup.grid(row=0, column=0)
framedown = Frame(window, width=310, height=300, pady=0, padx=0, relief=FLAT, bg=color2)
framedown.grid(row=1, column=0)


lcalculator = Label(frameup, text="Calculator", width=25, height=1, padx=3, relief='flat', anchor='center', font=('MonoSpace 15 bold'), bg=color1, fg=color3)
lcalculator.place(x=0, y=30)

lage = Label(frameup, text="Of Age", width=11, height=1, padx=0, relief='flat', anchor='center', font=('Arial 35 bold italic'), bg=color1, fg=color4)
lage.place(x=0, y=70)

def calculate():
    initial = calcone.get()
    end = calctwo.get()
  
    monthone, dayone, yearone = [ int(f) for f in initial.split('/') ]
    initialdate = date(yearone, monthone, dayone)

    monthtwo, daytwo, yeartwo = [ int(f) for f in end.split('/') ]
    birthdate = date(yeartwo, monthtwo, daytwo)

    year = relativedelta(initialdate, birthdate).years
    month = relativedelta(initialdate, birthdate).months
    day = relativedelta(initialdate, birthdate).days

    lappyear['text'] = year
    lappmonth['text'] = month
    lappday['text'] = day 

  

linitialdate = Label(framedown, text="Initial Date", height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('MonoSpace 11'), bg=color2, fg=color3)
linitialdate.place(x=50, y=30)

calcone = DateEntry(framedown, width=13, bg='darkblue', fg=color3, borderwidth=2, date_pattern='mm/dd/y', y=2023)
calcone.place(x=170, y=30)

lbirthdate = Label(framedown, text="Birth Date", height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('MonoSpace 11'), bg=color2, fg=color3)
lbirthdate.place(x=50, y=70)

calctwo = DateEntry(framedown, width=13, bg='darkblue', fg=color3, borderwidth=2, date_pattern='mm/dd/y', y=2023)
calctwo.place(x=170, y=70)

lappyear = Label(framedown, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('MonoSpace 25 bold'), bg=color2, fg=color3)
lappyear.place(x=60, y=135)
lappyearname = Label(framedown, text="Year's", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('MonoSpace 11 bold'), bg=color2, fg=color5)
lappyearname.place(x=60, y=180)

lappmonth = Label(framedown, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('MonoSpace 25 bold'), bg=color2, fg=color3)
lappmonth.place(x=140, y=135)
lappmonthname = Label(framedown, text="Month's", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('MonoSpace 11 bold'), bg=color2, fg=color5)
lappmonthname.place(x=140, y=180)

lappday = Label(framedown, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('MonoSpace 25 bold'), bg=color2, fg=color3)
lappday.place(x=220, y=135)
lappdayname = Label(framedown, text="Day's", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('MonoSpace 11 bold'), bg=color2, fg=color5)
lappdayname.place(x=220, y=180)

buttoncalc = Button(framedown, command=calculate, text="CALCULATE", width=20, height=1, relief='raised', overrelief='ridge', font=('MonoSpace 10 bold'), bg=color6, fg=color3)
buttoncalc.place(x=70, y=225)

window.mainloop()