import tkinter as tk

window=tk.Tk()

def delete():
  text.delete('1.0')

def delete1():
  text.delete('1.0',tk.END)


text=tk.Text(fg='purple',bg='white')
text.insert('1.8','Hello')
text.insert('4.0','\n\n\nHello')
text.insert(tk.END,'\neNDING')
text.pack()

button=tk.Button(text='Delete', command=delete)
button.pack()

button2=tk.Button(text='Delete all', command=delete1)
button2.pack()

window.mainloop()