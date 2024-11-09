# GUI mile to kilometer converter

from tkinter import *

window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=200,height=150)
window.config(padx="40",pady="30")


label1=Label(text="Miles")
label1.grid(column=2,row=0)

label2=Label(text="is equal to")
label2.grid(column=0,row=1)

label3=Label(text="0")
label3.grid(column=1,row=1)

label4=Label(text="km")
label4.grid(column=2,row=1)

def calculate():
    mile=float(input_txt.get())
    km=int(mile*1.609)
    label3.config(text=f"{km}")

button=Button(text="Calculate",command=calculate)
button.grid(column=1,row=2)

input_txt = Entry(width=10)
input_txt.grid(column=1,row=0)



window.mainloop()