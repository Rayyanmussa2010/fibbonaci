# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 15:50:48 2021

@author: DELL
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 12:21:13 2021

@author: DELL
"""

from tkinter import *
root=Tk()
root.title("Fibonacci")
root.geometry("400x400")
entry_number=Entry(root)
entry_number.place(relx=0.5, rely=0.5, anchor=CENTER)
label_series=Label(root, text="Fibonacci Series")
label_flower=Label(root)
label_spiral=Label(root)

def Fibonacci():
    num=int(entry_number.get())
    first_number=0
    second_number=1
    sum=0
    counter=1
    while(counter<=num):
        label_series["text"]+=str(sum)+" "
        counter=counter+1
        first_number=second_number
        second_number=sum
        sum=first_number+second_number
        label_flower["text"]="flower is bloomed"
        label_spiral["text"]="Spirals in right direction are" +str(first_number)+" " +"Spirals in left direction"+str(second_number)+" \ n Total number of spiral"+str(sum)
        
btn=Button(root, text="show Fibonacci series", command=Fibonacci)
btn.pack()
label_flower.pack()
label_series.pack()
label_spiral.pack()









root.mainloop()