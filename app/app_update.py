from tkinter import *
import customtkinter

import sqlite3

class WindowEditData:
    def __init__(self, app, db_name='pasien.db'):
        self.app = app
        app.title('Update')
        app.iconbitmap('icon.png')
        app.geometry('190x500')

        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        self.id = customtkinter.CTkEntry(
            app,
            placeholder_text='Masukan ID'
        )
        self.nik = customtkinter.CTkEntry(
            app,
            placeholder_text='NIK Pasien'
        )
        self.nama = customtkinter.CTkEntry(
            app,
            placeholder_text='Nama Pasien'
        )
        self.umur = customtkinter.CTkEntry(
            app,
            placeholder_text='Umur Pasien'
        )
        self.gender = customtkinter.CTkEntry(
            app,
            placeholder_text='Gender Pasien'
        )
        self.telp = customtkinter.CTkEntry(
            app,
            placeholder_text='Email Pasien'
        )
        self.sakit = customtkinter.CTkEntry(
            app,
            placeholder_text='Penyakit Pasien'
        )
        self.ruang = customtkinter.CTkEntry(
            app,
            placeholder_text='Ruang Pasien'
        )
        self.status = customtkinter.CTkEntry(
            app,
            placeholder_text='Status Pasien'
        )
        self.id.pack(pady = 10)
        self.nik.pack(pady = 10)
        self.nama.pack(pady = 10)
        self.umur.pack(pady = 10)
        self.gender.pack(pady = 10)
        self.telp.pack(pady = 10)
        self.sakit.pack(pady = 10)
        self.ruang.pack(pady = 10)
        self.status.pack(pady = 10)

        button_update = customtkinter.CTkButton(
            app,
            text='Update',
            command=self.update,
            width=100,
            height=50,
            text_color='white',
            fg_color='darkblue',
            corner_radius=100
        )
        button_update.pack(pady=10)

    def update(self):
        id = int(self.id.get())
        self.cursor.execute("UPDATE tabel_pasien SET nik = ?, nama = ?, umur = ?, gender = ?, telp = ?, sakit = ?, ruang = ?, status = ? WHERE id = ?", 
                            (self.nik.get(), self.nama.get(), self.umur.get(), self.gender.get(), self.telp.get(), self.sakit.get(), self.ruang.get(), self.status.get(), id))
        self.connection.commit()

app = customtkinter.CTk()
Customtkinter = WindowEditData(app)
app.mainloop()