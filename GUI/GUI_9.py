import tkinter as tk

window=tk.Tk()

window.columnconfigure(0,minsize=270)
window.rowconfigure([0,1], minsize=100)

frame=tk.Frame(bg='red')
frame.grid(row=0,column=0,padx=100,pady=200,sticky='n') #using sticky parameter we can change location of the tables

frame1=tk.Frame(bg='red')
frame1.grid(row=2,column=2)

lbl_01=tk.Label(master=frame,text='I am at (0,0)',bg='red')
lbl_01.place(x=0,y=0)

lbl_02=tk.Label(master=frame,text='I am at (60,50)',bg='red')
lbl_02.place(x=60,y=50)




window.mainloop()