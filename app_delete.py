from tkinter import *
import customtkinter

import sqlite3

class AplikasiManajemenPasien:
    def __init__(self, app, db_name='pasien.db'):
        self.app = app
        app.title('Delete')
        app.geometry('190x150')

        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        self.id = customtkinter.CTkEntry(
            app,
            placeholder_text='Masukan ID'
        )
        self.id.pack(pady = 10)

        button_delete = customtkinter.CTkButton(
            app,
            text='Delete',
            command=self.delete,
            width=100,
            height=50,
            text_color='white',
            fg_color='darkblue',
            corner_radius=100
        )
        button_delete.pack(pady=10)

    def delete(self):
        id = int(self.id.get())
        self.cursor.execute("DELETE FROM tabel_pasien WHERE id = ?", (id,))
        self.connection.commit()

app = customtkinter.CTk()
Customtkinter = AplikasiManajemenPasien(app)
app.mainloop()