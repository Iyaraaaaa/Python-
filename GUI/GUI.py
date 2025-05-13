import tkinter as tk

def close_window():
   global ent
   ent=entry.get()
   print(ent)
   root.destroy()

def submit():
   submitted_name=entry.get()
   print('My name is' + submitted_name)

window = tk.Tk() #Tk is a class to create a window

greet=tk.Label(text='Hello World',
               foreground='white',
               background='black')


para=tk.Label(text='I am Janith Athapaththu',
              fg='red',
              bg='yellow',
              width=50,
              height=20)


subscribe=tk.Button(text='Subscribe Now',width=5,height=2,fg='white',bg='red')
subscribe.pack()
greet.pack() #pack is a method
para.pack()

entry=tk.Entry(fg='blue',bg='green',width=50)
entry.pack()

button2=tk.Button(text='SUBMIT', command='SUBMIT')
button2.pack()

window.mainloop()
