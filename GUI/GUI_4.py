import tkinter as tk

window=tk.Tk()

def submit():
  a=text.get(1.0) #not like entity we have to give line number and position
  print(a)


def submit2():
  b=text.get('1.0','1.7') #not like entity we have to give line number and position
  print(b)

def submit3():
  C=text.get('1.0',tk.END) #not like entity we have to give line number and position
  print(C)

text=tk.Text(fg='red',bg='white')
text.pack()

button=tk.Button(text='submit', command= submit)
button.pack()

button=tk.Button(text='submit2', command= submit2)
button.pack()

button=tk.Button(text='submit3', command= submit3)
button.pack()

window.mainloop()

