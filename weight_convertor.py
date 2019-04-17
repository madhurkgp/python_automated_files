from tkinter import *

window = Tk()

def kg_to_others():

    grams = round(float(value.get())* 1000.0,3)
    pounds = round(float(value.get())* 2.205,3)
    ounces = round(float(value.get())* 35.274,3)
    text_gms.delete(1.0, END)
    text_gms.insert(END,grams)
    text_pounds.delete(1.0, END)
    text_pounds.insert(END,pounds)
    text_ounces.delete(1.0, END)
    text_ounces.insert(END,ounces)

label = Label(text='kg')
label.grid(row=0,column=0)
# label.pack(side="left")

b1 = Button(window,text='Convert',command=kg_to_others)
b1.grid(row=0,column=2 )

value=StringVar()
kg_entry = Entry(window, textvariable=value)
kg_entry.grid(row=0,column=1)

label = Label(text='grams')
label.grid(row=1,column=0)

label = Label(text='pounds')
label.grid(row=1,column=1)

label = Label(text='ounces')
label.grid(row=1,column=2)

text_gms = Text(window,height=1,width=20)
text_gms.grid(row=2,column=0)

text_pounds = Text(window,height=1,width=20)
text_pounds.grid(row=2,column=1)

text_ounces = Text(window,height=1,width=20)
text_ounces.grid(row=2,column=2)




window.mainloop()