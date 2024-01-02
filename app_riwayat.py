from tkinter import *
import customtkinter as CTk
from CTkTable import *
import sqlite3
import os
from PIL import Image, ImageTk

class WindowHisory:
    def __init__(self, app, db_name='pasien.db'):
        self.app = app
        app.title('Riwayat')
        app.iconbitmap('icon.png')
        app.geometry('600x600')

        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        button_read = CTk.CTkButton(
            app,
            text='Lihat Riwayat Perubahan',
            command=self.read,
            width=100,
            height=50,
            text_color='white',
            fg_color='darkblue',
            corner_radius=100
        )
        button_read.pack(pady = 10)

    def read(self):
        self.cursor.execute('SELECT * FROM tabel_pasien LIMIT 0,10')
        data = self.cursor.fetchall()

        column_names = [description[0] for description in self.cursor.description]

        values = [column_names] + [list(row) for row in data]

        table = CTkTable(master=self.app, row=len(values), column=len(values[0]), values=values)
        table.pack(pady = 10)

app = CTk.CTk()
WindowHisory(app)
app.mainloop()