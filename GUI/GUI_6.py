import tkinter as tk

window=tk.Tk()

frame_a=tk.Frame() #its going to vey small initially, I mean only this code have.
frame_b=tk.Frame()
label_a=tk.Label(master=frame_a,text='Frame A') #master is a attribute
label_b=tk.Label(master=frame_b,text='Frame B')
label_a.pack()
label_b.pack()
frame_a.pack() #Try swap frame_a and frame_b
frame_b.pack()

window.mainloop()