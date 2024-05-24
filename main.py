import tkinter as tk

def close_window():
    root.destroy()

root = tk.Tk()
root.title("Hello, Tkinter!")
root.geometry("300x200")

button = tk.Button(root, text="Закрыть", command=close_window)
button.pack()

root.mainloop()
