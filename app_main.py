from tkinter import *
import customtkinter as CTk
import customtkinter
from CTkTable import *
import sqlite3
import os

class Pasien:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        try:
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
            self.cursor.execute(query)
            self.conn.commit()
            print(f"Table '{table_name}' created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def close_connection(self):
        self.conn.close()

class WindowMainApp(Pasien):
    def __init__(self, app, db_name='pasien.db'):
        self.app = app
        app.title('Aplikasi')
        app.geometry('700x200')

        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        title_label = CTk.CTkLabel(
            app,
            text='Aplikasi Manajemen Data Pasien',
            font=('Helvetica', 26),
            fg_color="transparent",
            corner_radius=8,
            pady=20
        )
        title_label.pack()

        buttonRiwayat = CTk.CTkButton(
            app,
            text='Riwayat Data',
            command=self.read,
            width=100,
            height=50,
            text_color='white',
            fg_color='darkblue',
            corner_radius=100
        )
        buttonRiwayat.pack(pady=50, padx=50, anchor='nw')
        buttonRiwayat.place(x=50, y=71)

        button_create = CTk.CTkButton(
            app,
            text='Tambah Data',
            command=self.createTop,
            width=100,
            height=50,
            text_color='white',
            fg_color='darkblue',
            corner_radius=100
        )
        button_create.pack(pady=50, padx=50, anchor='nw')
        button_create.place(x=200, y=71)

        buttonUpdate = CTk.CTkButton(
            app,
            text='Edit Data Data',
            command=self.updateTOP,
            width=100,
            height=50,
            text_color='white',
            fg_color='darkblue',
            corner_radius=100
        )
        buttonUpdate.pack(pady=50, padx=50, anchor='nw')
        buttonUpdate.place(x=350, y=71)

        buttonDelete = CTk.CTkButton(
            app,
            text='Hapus Data Data',
            command=self.deleteTop,
            width=100,
            height=50,
            text_color='white',
            fg_color='darkblue',
            corner_radius=100
        )
        buttonDelete.pack(pady=50, padx=50, anchor='nw')
        buttonDelete.place(x=500, y=71)

    def createTop(self):
        new = CTk.CTkToplevel(app)
        new.title("Tambah Data")
        new.geometry('550x450')
        
        title_label = CTk.CTkLabel(
            new,
            text='Tambah Data',  # Add your desired title here
            font=('Helvetica', 20),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )
        title_label.pack()
        # title_label.place(x=10,y=10)

        self.nik = CTk.CTkEntry(
            new,
            placeholder_text='NIK Pasien'
        )
        nik_label = CTk.CTkLabel(
            new,
            text='Nik Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )
        self.nama = CTk.CTkEntry(
            new,
            placeholder_text='Nama Pasien'
        )
        nama_label = CTk.CTkLabel(
            new,
            text='Nama Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )
        self.umur = CTk.CTkEntry(
            new,
            placeholder_text='Umur Pasien'
        )
        umur_label = CTk.CTkLabel(
            new,
            text='Umur Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        self.gender = CTk.CTkEntry(
            new,
            placeholder_text='Gender Pasien'
        )
        gender_label = CTk.CTkLabel(
            new,
            text='Gender Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        self.telp = CTk.CTkEntry(
            new,
            placeholder_text='Telp Pasien'
        )
        telp_label = CTk.CTkLabel(
            new,
            text='Telp Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        self.sakit = CTk.CTkEntry(
            new,
            placeholder_text='Penyakit Pasien'
        )
        sakit_label = CTk.CTkLabel(
            new,
            text='Penyakit Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        self.ruang = CTk.CTkOptionMenu(
            new,
            fg_color='#144272',
            button_color ='#0A2647',
            button_hover_color='#205295',
            dropdown_fg_color='#2C74B3',
            dropdown_hover_color='#205295',
            values=["Ruang Reguler", "Ruang VIP"]
        )
        ruang_label = CTk.CTkLabel(
            new,
            text='Ruang Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )                
        self.status = CTk.CTkOptionMenu(
            new,
            fg_color='#144272',
            button_color ='#0A2647',
            button_hover_color='#205295',
            dropdown_fg_color='#2C74B3',
            dropdown_hover_color='#205295',
            values=["Aktif", "Inaktif", "Meninggal"]

        )
        status_label = CTk.CTkLabel(
            new,
            text='Status Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        # self.nik.pack(pady = 5,padx =10)
        self.nik.place(x=50, y=75)
        nik_label.pack()
        nik_label.place(x=10, y=35)
        # self.nama.pack(pady = 5)
        self.nama.place(x=50, y=145)   
        nama_label.pack()
        nama_label.place(x=10, y=105)
        # self.umur.pack(pady = 5)
        self.umur.place(x=50, y=225)   
        umur_label.pack()
        umur_label.place(x=10, y=185)
        # self.gender.pack(pady = 5)
        self.gender.place(x=50, y=295)
        gender_label.pack()
        gender_label.place(x=10, y=255)
        # self.telp.pack(pady = 5)
        self.telp.place(x=375, y=75)
        telp_label.pack()
        telp_label.place(x=335, y=35)
        # self.sakit.pack(pady = 5)
        self.sakit.place(x=375, y=145)
        sakit_label.pack()
        sakit_label.place(x=335, y=105)
        # self.ruang.pack(pady = 5)
        self.ruang.place(x=375, y=225)
        ruang_label.pack()
        ruang_label.place(x=335, y=185)
        # self.status.pack(pady = 5)
        self.status.place(x=375, y=295)
        status_label.pack()
        status_label.place(x=335, y=255)
        self.button_create = CTk.CTkButton(
            new,
            text='Add',
            command=self.create,
            width=100,
            height=50,
            text_color='white',
            hover_color='#205295',
            fg_color='#0A2647',
            corner_radius=15
        )
        self.button_create.pack(pady=10)
        self.button_create.place(x=225, y=350)

    def updateTOP(self):
        newUpdate = CTk.CTkToplevel(app)
        newUpdate.title("Edit Data")
        newUpdate.geometry('550x500')
        title_label = CTk.CTkLabel(
            newUpdate,
            text='Update Data',  # Add your desired title here
            font=('Helvetica', 20),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )
        title_label.pack()

        self.nik = CTk.CTkEntry(
            newUpdate,
            placeholder_text='NIK Pasien'
        )
        nik_label = CTk.CTkLabel(
            newUpdate,
            text='Nik Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )

        self.id = CTk.CTkEntry(
            newUpdate,
            placeholder_text='Masukan ID'
        )
        id_label = CTk.CTkLabel(
            newUpdate,
            text='ID',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )

        self.nama = CTk.CTkEntry(
            newUpdate,
            placeholder_text='Nama Pasien'
        )
        nama_label = CTk.CTkLabel(
            newUpdate,
            text='Nama Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )
        self.umur = CTk.CTkEntry(
            newUpdate,
            placeholder_text='Umur Pasien'
        )
        umur_label = CTk.CTkLabel(
            newUpdate,
            text='Umur Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        self.gender = CTk.CTkEntry(
            newUpdate,
            placeholder_text='Gender Pasien'
        )
        gender_label = CTk.CTkLabel(
            newUpdate,
            text='Gender Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        self.telp = CTk.CTkEntry(
            newUpdate,
            placeholder_text='Telp Pasien'
        )
        telp_label = CTk.CTkLabel(
            newUpdate,
            text='Telp Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        self.sakit = CTk.CTkEntry(
            newUpdate,
            placeholder_text='Penyakit Pasien'
        )
        sakit_label = CTk.CTkLabel(
            newUpdate,
            text='Penyakit Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        self.ruang = CTk.CTkOptionMenu(
            newUpdate,
            fg_color='#144272',
            button_color ='#0A2647',
            button_hover_color='#205295',
            dropdown_fg_color='#2C74B3',
            dropdown_hover_color='#205295',
            values=["Ruang Reguler", "Ruang VIP"]
        )
        ruang_label = CTk.CTkLabel(
            newUpdate,
            text='Ruang Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )                
        self.status = CTk.CTkOptionMenu(
            newUpdate,
            fg_color='#144272',
            button_color ='#0A2647',
            button_hover_color='#205295',
            dropdown_fg_color='#2C74B3',
            dropdown_hover_color='#205295',
            values=["Aktif", "Inaktif"]

        )
        status_label = CTk.CTkLabel(
            newUpdate,
            text='Status Pasien',  # Add your desired title here
            font=('Calibri', 14),  # Adjust the font size and family as needed
            fg_color=("transparent"),
            corner_radius=8,
            pady=10,padx=50
        )        
        self.nik.place(x=50, y=75)
        nik_label.pack()
        nik_label.place(x=10, y=35)
    
        self.nama.place(x=50, y=145)   
        nama_label.pack()
        nama_label.place(x=10, y=105)

        self.umur.place(x=50, y=225)   
        umur_label.pack()
        umur_label.place(x=10, y=185)

        self.gender.place(x=50, y=295)
        gender_label.pack()
        gender_label.place(x=10, y=255)

        self.telp.place(x=375, y=75)
        telp_label.pack()
        telp_label.place(x=335, y=35)

        self.sakit.place(x=375, y=145)
        sakit_label.pack()
        sakit_label.place(x=335, y=105)

        self.ruang.place(x=375, y=225)
        ruang_label.pack()
        ruang_label.place(x=335, y=185)

        self.status.place(x=375, y=295)
        status_label.pack()
        status_label.place(x=335, y=255)

        self.id.place(x=375, y=360)
        id_label.pack()
        id_label.place(x=335, y=320)

        self.button_create = CTk.CTkButton(
            newUpdate,
            text='Edit',
            command=self.update,
            width=100,
            height=50,
            text_color='white',
            hover_color='#205295',
            fg_color='#0A2647',
            corner_radius=15
        )
        self.button_create.pack(pady=10)
        self.button_create.place(x=200, y=400)

    def deleteTop(self):
        newDelete = CTk.CTkToplevel(app)
        newDelete.title("Hapus Data")
        newDelete.geometry('190x150')   
        self.id = CTk.CTkEntry(
            newDelete,
            placeholder_text='Masukan ID'
        )
        self.id.pack(pady = 10)

        button_delete = CTk.CTkButton(
            newDelete,
            text='Delete',
            command=self.delete,
            width=100,
            height=50,
            text_color='white',
            fg_color='darkblue',
            corner_radius=100
        )
        button_delete.pack(pady=10)
    
    def create(self):
        self.cursor.execute('''
            INSERT INTO tabel_pasien (nik, nama, umur, gender, telp, sakit, ruang, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.nik.get(), self.nama.get(), self.umur.get(), self.gender.get(), self.telp.get(), self.sakit.get(), self.ruang.get(), self.status.get()))
        self.connection.commit()

    def read(self):
        print("Test!")

    def update(self):
        id = int(self.id.get())
        self.cursor.execute("UPDATE tabel_pasien SET nik = ?, nama = ?, umur = ?, gender = ?, telp = ?, sakit = ?, ruang = ?, status = ? WHERE id = ?", 
                            (self.nik.get(), self.nama.get(), self.umur.get(), self.gender.get(), self.telp.get(), self.sakit.get(), self.ruang.get(), self.status.get(), id))
        self.connection.commit()

    def delete(self):
        id = int(self.id.get())
        self.cursor.execute("DELETE FROM tabel_pasien WHERE id = ?", (id,))
        self.connection.commit()

class WindowAddData(Pasien):
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

class WindowEditData(Pasien):
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

class WindowDeleteData(Pasien):
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

class WindowHistory(Pasien):
    def __init__(self, app, db_name='pasien.db'):
        self.app = app
        app.title('Riwayat')
        app.iconbitmap('icon.png')
        app.geometry('600x600')

        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        button_read = CTk.CTkButton(
            app,
            text='Muat Ulang',
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

    def realtime(self):
        self.cursor.execute("SELECT * FROM tabel_pasien")
        rows = self.cursor.fetchall()
        tree = rows
        for row in tree.get_children():
            tree.delete(row)

        for row in rows:
            tree.insert("", "end", iid=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

        app.after(1000, self.read)

app = CTk.CTk()
WindowMainApp(app)
app.mainloop()

# db_creator = Pasien("example.db")
# person_columns = ["id INTEGER PRIMARY KEY", "nik INTEGER", "nama VARCHAR(255)", "umur VARCHAR(255)", "gender VARCHAR(255)", "telp INTEGER", "sakit VARCHAR(255)", "ruang VARCHAR(255), status VARCHAR(255)"]
# db_creator.create_table("person", person_columns)
# db_creator.close_connection()