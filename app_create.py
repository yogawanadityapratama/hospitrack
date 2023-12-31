from tkinter import *
import customtkinter
from CTkTable import *
import sqlite3
import os
from PIL import Image, ImageTk

class AplikasiManajemenPasien:
    def __init__(self, app, db_name='pasien.db'):
        self.app = app
        app.title('Create')
        app.geometry('190x450')

        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

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
        self.nik.pack(pady = 10)
        self.nama.pack(pady = 10)
        self.umur.pack(pady = 10)
        self.gender.pack(pady = 10)
        self.telp.pack(pady = 10)
        self.sakit.pack(pady = 10)
        self.ruang.pack(pady = 10)
        self.status.pack(pady = 10)

        button_create = customtkinter.CTkButton(
            app,
            text='Add',
            command=self.create,
            width=100,
            height=50,
            text_color='white',
            fg_color='darkblue',
            corner_radius=100
        )
        button_create.pack(pady=10)

    def create(self):
        self.cursor.execute('''
            INSERT INTO tabel_pasien (nik, nama, umur, gender, telp, sakit, ruang, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.nik.get(), self.nama.get(), self.umur.get(), self.gender.get(), self.telp.get(), self.sakit.get(), self.ruang.get(), self.status.get()))
        self.connection.commit()

app = customtkinter.CTk()
Customtkinter = AplikasiManajemenPasien(app)
app.mainloop()