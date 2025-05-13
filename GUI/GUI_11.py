import tkinter as tk

window = tk.Tk()

def convert():
    # Retrieve the Fahrenheit value from the entry widget
    Fahrenheit = ent_F.get()
    
    try:
        # Convert Fahrenheit to Celsius
        Celsius = (5/9) * (float(Fahrenheit) - 32)
        # Update the label with the converted Celsius value
        lbl_C["text"] = f"{round(Celsius, 2)} Celsius"
    except ValueError:
        # Handle the case where the input cannot be converted to float (non-numeric input)
        lbl_C["text"] = "Invalid input"

window.title('Temperature converter')

# Frame for entry widgets
frm_entry = tk.Frame(master=window)
frm_entry.pack()

# Entry widget for Fahrenheit input
ent_F = tk.Entry(master=frm_entry, width=10)
ent_F.grid(row=0, column=1)

# Label for Fahrenheit entry
lbl_F = tk.Label(master=frm_entry, text='Degrees Fahrenheit')
lbl_F.grid(row=0, column=0)

# Button to trigger conversion
btn_converter = tk.Button(master=window, text="Convert to Celsius", command=convert)
btn_converter.pack()

# Label to display Celsius result
lbl_C = tk.Label(master=window, text="")
lbl_C.pack()

window.mainloop()
