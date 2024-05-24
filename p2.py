import tkinter as tk

def update_label():
    text = entry.get()
    label.config(text=text)

root = tk.Tk()
root.title("Tkinter Example")

label = tk.Label(root, text="Введите текст и нажмите кнопку")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Отобразить текст", command=update_label)
button.pack()

root.mainloop()
