import tkinter as tk
from tkinter import ttk
import sqlite3

def read():
    cursor.execute("SELECT * FROM tabel_pasien")
    rows = cursor.fetchall()

    for row in tree.get_children():
        tree.delete(row)

    for row in rows:
        tree.insert("", "end", iid=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    root.after(1000, read)

root = tk.Tk()
root.title("Realtime")

tree = ttk.Treeview(root, columns=("Col1", "Col2", "Col3", "Col4", "Col5", "Col6", "Col7", "Col8"))
tree.heading("Col1", text="1")
tree.heading("Col2", text="2")
tree.heading("Col3", text="3")
tree.heading("Col4", text="4")
tree.heading("Col5", text="5")
tree.heading("Col6", text="6")
tree.heading("Col7", text="7")
tree.heading("Col8", text="8")
tree.pack()

connection = sqlite3.connect("pasien.db")
cursor = connection.cursor()

read()

root.mainloop()