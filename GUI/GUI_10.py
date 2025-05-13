import tkinter as tk

window = tk.Tk()

def clickme(event):
    print('Button was clicked')

button = tk.Button(window, text='Click Me', command = clickme)
#button.bind("<Button-1>", clickme) if we used command attribute we dont want to use bind method
button.pack()

window.mainloop()
