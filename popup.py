import tkinter as tk

def create_popupwindow():
    popupwindow = tk.Toplevel()
    popupwindow.title("Popup Window")
    popupwindow.geometry("300x300")

    label = tk.Label(popupwindow, text="This is a popup window.")
    label.pack()

    button = tk.Button(popupwindow, text="Close", command=popupwindow.destroy)
    button.pack()

root = tk.Tk()
root.title("Main Window")
root.geometry("400x400")

button = tk.Button(root, text="Create Popup Window", command=create_popupwindow)
button.pack()

root.mainloop()