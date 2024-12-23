import tkinter as tk
root = tk.Tk()
name = "Callado, Kurt Cyrus B."
section = "BSCS 2A"
root.title(f"OOP")
root.geometry("300x200")
root.configure(bg = "white")
def on_press():
    anime = "One Piece"
    print(f"My favorite anime is {anime}")

button = tk.Button(root, text="Pindutin mo ako", command=on_press)
button.pack(pady = 10)
root.mainloop()