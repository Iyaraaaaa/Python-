import tkinter as tk

window=tk.Tk()

def submit():
  name_submitted=entry.get()
  print('Your Name is ' + name_submitted)

name=tk.Label(text='Name', bg='black',fg='white')
name.pack()

entry=tk.Entry(fg='yellow',bg='black')
entry.pack()


submit=tk.Button(text='submit',fg='black',bg='white',command=submit)
submit.pack()

window.mainloop()