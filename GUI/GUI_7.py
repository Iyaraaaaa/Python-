import tkinter as tk

window=tk.Tk()

frame=tk.Frame(master=window,relief=tk.FLAT,borderwidth=5)
frame.pack(side=tk.LEFT)
label=tk.Label(master=frame,text='Flat')
label.pack()

frame=tk.Frame(master=window,relief=tk.SUNKEN,borderwidth=5)
frame.pack(side=tk.LEFT)
label=tk.Label(master=frame,text='Sunken')
label.pack()

frame=tk.Frame(master=window,relief=tk.RAISED,borderwidth=5)
frame.pack(side=tk.LEFT)
label=tk.Label(master=frame,text='Raised')
label.pack()

frame=tk.Frame(master=window,relief=tk.GROOVE,borderwidth=5)
frame.pack(side=tk.LEFT)
label=tk.Label(master=frame,text='Groove')
label.pack()

frame=tk.Frame(master=window,relief=tk.RIDGE,borderwidth=5)
frame.pack(side=tk.LEFT)
label=tk.Label(master=frame,text='Ridge')
label.pack()

window.mainloop()