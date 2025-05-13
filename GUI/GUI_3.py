import tkinter as tk

window=tk.Tk()

#def submit():
  #entry.delete(0,tk.END)
  #print("My Name=", entry)

def submit():
   entry.delete(6)
   print("My Name=", entry)
   

name=tk.Label(text='Name', bg='black',fg='white')
name.pack()

entry=tk.Entry(fg='yellow',bg='black')
entry.insert(0,'What is your name?')
entry.pack()


submit=tk.Button(text='submit',fg='black',bg='white',command=submit)
submit.pack()

window.mainloop()