import tkinter as tk

def close_window():
    root.destroy()

root = tk.Tk()
root.title("Hello, Tkinter!")

button = tk.Button(root, text="Закрыть", command=close_window)
button.pack()

root.mainloop()
