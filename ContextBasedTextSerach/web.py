import tkinter as tk
import webbrowser

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

root = tk.Tk()
lbl = tk.Label(root, text=r"http://www.google.co", fg="blue", cursor="hand2")
lbl.pack()
lbl.bind("<Button-1>", callback)
root.mainloop()