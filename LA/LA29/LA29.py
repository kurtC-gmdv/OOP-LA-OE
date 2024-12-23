import tkinter as tk

name = "Callado, Kurt Cyrus B."
section = "BSCS 2A"
root = tk.Tk()
root.title("OOP LA29")
text_disp = tk.Label(root, text=f"OOP 29 {name} {section}")
text_disp.grid(row=0, column=0, padx=100, pady=100)
root.mainloop()