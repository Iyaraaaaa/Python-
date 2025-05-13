import tkinter as tk

window=tk.Tk()

frame_1=tk.Frame(master=window,width=100,height=100,bg='red')
frame_1.pack(fill=tk.X) #THIS WILL ARRANGE LARGEST ARRANGE

frame_2=tk.Frame(master=window,width=100,height=100,bg='blue')
frame_2.pack(fill=tk.X)

frame_3=tk.Frame(master=window,width=100,height=100,bg='brown')
frame_3.pack(fill=tk.X)

frame_4=tk.Frame(master=window,width=100,height=100,bg='red')
frame_4.pack(fill=tk.Y,side=tk.LEFT,expand=True) 

frame_5=tk.Frame(master=window,width=100,height=100,bg='blue')
frame_5.pack(fill=tk.Y,side=tk.LEFT,expand=True)

frame_6=tk.Frame(master=window,width=100,height=100,bg='yellow')
frame_6.pack(fill=tk.Y,side=tk.LEFT,expand=True)

window.mainloop()
