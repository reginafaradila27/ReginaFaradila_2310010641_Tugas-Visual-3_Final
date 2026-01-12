# -*- coding: utf-8 -*-
import mysql.connector
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

class crud_masyarakat:

    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='masyarakat_2310010641'
        )

    # ============================================================
    # CRUD TABEL admin
    # ============================================================
    def tambahAdmin(self, id_admin, nama, password, id_kelurahan):
        aksi = self.koneksi.cursor()
        sql = """INSERT INTO admin (id_admin, nama, password, id_kelurahan)
                 VALUES (%s,%s,%s,%s)"""
        aksi.execute(sql, (id_admin, nama, password, id_kelurahan))
        self.koneksi.commit()
        aksi.close()

    def updateAdmin(self, id_admin, nama, password, id_kelurahan):
        aksi = self.koneksi.cursor()
        sql = """UPDATE admin SET nama=%s, password=%s, id_kelurahan WHERE id_admin=%s"""
        aksi.execute(sql, (nama, password, id_kelurahan,id_admin ))
        self.koneksi.commit()
        aksi.close()

    def hapusAdmin(self, id_admin):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM admin WHERE id_admin=%s", (id_admin,))
        self.koneksi.commit()
        aksi.close()

    def dataAdmin(self):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("SELECT * FROM admin ORDER BY id_admin ASC")
        return aksi.fetchall()

    def filterAdmin(self, cari):
        aksi = self.koneksi.cursor(dictionary=True)
        # Mencari string 'cari' di kolom id_admin, nama, atau password
        aksi.execute("SELECT * FROM admin WHERE id_admin LIKE %s OR nama LIKE %s OR password LIKE %s",
        ([f"%{cari}%", f"%{cari}%", f"%{cari}%"]))
        return aksi.fetchall()

    def cetakAdmin(self):
            aksi = self.koneksi.cursor()
            aksi.execute("select * from admin")
            data = aksi.fetchall()
            barisData = [["id_admin, nama, password, id_kelurahan"]] + list(data)
            # print(barisData)
            fileLaporan = "Laporan admin.pdf"
            pdf = SimpleDocTemplate(fileLaporan, pagesize = A4)
            isiData = Table(barisData, colWidths = [65, 45, 45, 65, 65, 50, 50, 65, 45, 60, 60])
            pdf.build([isiData])

    def cetakFilterAdmin(self, cari):
            aksi = self.koneksi.cursor()
            aksi.execute("select * from admin where status = %s", ([f"{cari}"]))
            data = aksi.fetchall()
            barisData = [["id_admin, nama, password, id_kelurahan"]] + list(data)
            # print(barisData)
            fileLaporan = "Laporan admin.pdf"
            pdf = SimpleDocTemplate(fileLaporan, pagesize = A4)
            isiData = Table(barisData, colWidths = [65, 45, 45, 65, 65, 50, 50, 65, 45, 60, 60])
            pdf.build([isiData])

    # ============================================================
    # CRUD TABEL agenda
    # ============================================================
    def tambahAgenda(self, id_agenda, judul, tanggal_terselenggara, id_kelurahan):
        aksi = self.koneksi.cursor()
        sql = """INSERT INTO  agenda (id_agenda, judul, tanggal_terselenggara, id_kelurahan)
                 VALUES (%s,%s,%s,%s,%s)"""
        aksi.execute(sql, (id_agenda, judul, tanggal_terselenggara, id_kelurahan))
        self.koneksi.commit()
        aksi.close()

    def updateAgenda(self, id_agenda, judul, tanggal_terselenggara, id_kelurahan):
        aksi = self.koneksi.cursor()
        sql = """UPDATE agenda SET judul=%s, tanggal_terselenggara=%s, id_kelurahan=%s WHERE id_agenda=%s"""
        aksi.execute(sql, (judul, tanggal_terselenggara, id_kelurahan, id_agenda))
        self.koneksi.commit()
        aksi.close()

    def hapusAgenda(self, id_agenda):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM  agenda WHERE id_agenda=%s", (id_agenda,))
        self.koneksi.commit()
        aksi.close()

    def dataAgenda(self):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("SELECT * FROM  agenda ORDER BY id_agenda ASC")
        return aksi.fetchall()

    def filterAgenda(self, cari):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute("select * from  agenda where id_agenda like %s or judul like %s or tanggal_terselenggara like %s",
        ([f"%{cari}%", f"%{cari}%", f"%{cari}%"]))
        return aksi.fetchall()

    def cetakAgenda(self):
            aksi = self.koneksi.cursor()
            aksi.execute("select * from agenda")
            data = aksi.fetchall()
            barisData = [["id_agenda, judul, tanggal_terselenggara, id_kelurahan"]] + list(data)
            # print(barisData)
            fileLaporan = "Laporan agenda.pdf"
            pdf = SimpleDocTemplate(fileLaporan, pagesize = A4)
            isiData = Table(barisData, colWidths = [70, 90, 70, 80, 100])
            pdf.build([isiData])

    # ============================================================
    # CRUD TABEL kelurahan
    # ============================================================
    def tambahKelurahan(self, id_kelurahan, nama_kelurahan, id_lurah):
        aksi = self.koneksi.cursor()
        sql = """INSERT INTO kelurahan (id_kelurahan, nama_kelurahan, id_lurah)
                 VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        aksi.execute(sql, (id_kelurahan, nama_kelurahan, id_lurah))
        self.koneksi.commit()
        aksi.close()

    def updateKelurahan(self, id_kelurahan, nama_kelurahan, id_lurah):
        aksi = self.koneksi.cursor()
        sql = """UPDATE kelurahan SET nama_kelurahan=%s, id_lurah=%s WHERE id_kelurahan=%s"""
        aksi.execute(sql, (nama_kelurahan, id_lurah, id_kelurahan))
        self.koneksi.commit()
        aksi.close()

    def hapuskelurahan(self, id_kelurahan):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM kelurahan WHERE id_kelurahan=%s", (id_kelurahan,))
        self.koneksi.commit()
        aksi.close()

    def dataKelurahan(self):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("SELECT * FROM kelurahan ORDER BY id_kelurahan ASC")
        return aksi.fetchall()

    def filterKelurahan(self, cari):
        aksi = self.koneksi.cursor(dictionary=True)
        # Mencari string 'cari' di kolom id_kelurahan, nama_kelurahan, atau id_lurah
        aksi.execute("SELECT * FROM kelurahan WHERE id_kelurahan LIKE %s OR nama_kelurahan LIKE %s OR id_lurah LIKE %s",
        ([f"%{cari}%", f"%{cari}%", f"%{cari}%"]))
        return aksi.fetchall()

    def cetakKelurahan(self):
            aksi = self.koneksi.cursor()
            aksi.execute("select * from kelurahan")
            data = aksi.fetchall()
            barisData = [["id_kelurahan, nama_kelurahan, id_lurah"]] + list(data)
            # print(barisData)
            fileLaporan = "Laporan kelurahan.pdf"
            pdf = SimpleDocTemplate(fileLaporan, pagesize = A4)
            isiData = Table(barisData, colWidths = [90, 90, 90, 60, 100, 70, 60])
            pdf.build([isiData])

    # ============================================================
    # CRUD TABEL laporan
    # ============================================================
    def tambahLaporan(self, id_laporan, judul_laporan, lokasi_laporan, Jenis_laporan, deskripsi, id_user):
        aksi = self.koneksi.cursor()
        sql = """INSERT INTO laporan (id_laporan, judul_laporan, lokasi_laporan, Jenis_laporan, deskripsi, id_user)
                 VALUES (%s,%s,%s,%s,%s,%s)"""
        aksi.execute(sql, (id_laporan, judul_laporan, lokasi_laporan, Jenis_laporan, deskripsi, id_user))
        self.koneksi.commit()
        aksi.close()

    def updateLaporan(self, id_laporan, judul_laporan, lokasi_laporan, Jenis_laporan, deskripsi, id_user):
        aksi = self.koneksi.cursor()
        sql = """UPDATE laporan SET judul_laporan=%s, lokasi_laporan=%s, Jenis_laporan=%s, deskripsi=%s, id_user=%s WHERE id_laporan=%s"""
        aksi.execute(sql, (judul_laporan, lokasi_laporan, Jenis_laporan, deskripsi, id_user, id_laporan))
        self.koneksi.commit()
        aksi.close()

    def hapusLaporan(self, id_laporan):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM laporan WHERE id_laporan=%s", (id_laporan,))
        self.koneksi.commit()
        aksi.close()

    def dataLaporan(self):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("SELECT * FROM laporan ORDER BY id_laporan ASC")
        return aksi.fetchall()

    def filterLaporan(self, cari):
        aksi = self.koneksi.cursor(dictionary=True)
        # Mencari string 'cari' di kolom id_laporan, judul_laporan, atau  lokasi_laporan
        aksi.execute("SELECT * FROM laporan WHERE id_laporan LIKE %s OR judul_laporan LIKE %s OR  lokasi_laporan LIKE %s",
        ([f"%{cari}%", f"%{cari}%", f"%{cari}%"]))
        return aksi.fetchall()

    def cetakLaporan(self):
            aksi = self.koneksi.cursor()
            aksi.execute("select * from Laporan")
            data = aksi.fetchall()
            barisData = [["Id_Laporan, Judul_Laporan, Lokasi_Laporan, Jenis_Laporan, Deskripsi, Id_User"]] + list(data)
            # print(barisData)
            fileLaporan = "Laporan Laporan.pdf"
            pdf = SimpleDocTemplate(fileLaporan, pagesize = A4)
            isiData = Table(barisData, colWidths = [90, 90, 90, 60])
            pdf.build([isiData])

    # ============================================================
    # CRUD TABEL orang_penting
    # ============================================================
    def tambahOrang_penting(self, id_Orang_Penting, nama, jabatan, no_hp, id_kelurahan):
        aksi = self.koneksi.cursor()
        sql = """INSERT INTO orang_penting (id_Orang_Penting, nama, jabatan, no_hp, id_kelurahan)
                 VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        aksi.execute(sql, (id_Orang_Penting, nama, jabatan, no_hp, id_kelurahan))
        self.koneksi.commit()
        aksi.close()

    def updateorang_penting(self, id_Orang_Penting, nama, jabatan, no_hp, id_kelurahan):
        aksi = self.koneksi.cursor()
        sql = """UPDATE orang_penting SET nama=%s, jabatan=%s, no_hp=%s, id_kelurahan=%s WHERE id_orang_penting=%s"""
        aksi.execute(sql, (nama, jabatan, no_hp, id_kelurahan, id_orang_penting))
        self.koneksi.commit()
        aksi.close()

    def hapusorang_penting(self, id_orang_penting):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM orang_penting WHERE id_orang_penting=%s", (id_orang_penting,))
        self.koneksi.commit()
        aksi.close()

    def dataorang_penting(self):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("SELECT * FROM orang_penting ORDER BY id_orang_penting ASC")
        return aksi.fetchall()

    def filterorang_penting(self, cari):
        aksi = self.koneksi.cursor(dictionary=True)
        # Mencari string 'cari' di kolom id_orang_penting, nama, atau jabatan
        aksi.execute("SELECT * FROM orang_penting WHERE id_orang_penting LIKE %s OR nama LIKE %s OR jabatan LIKE %s",
        ([f"%{cari}%", f"%{cari}%", f"%{cari}%"]))
        return aksi.fetchall()

    def cetakorang_penting(self):
            aksi = self.koneksi.cursor()
            aksi.execute("select * from orang_penting")
            data = aksi.fetchall()
            barisData = [["id_Orang_Penting, nama, jabatan, no_hp, id_kelurahan"]] + list(data)
            # print(barisData)
            fileLaporan = "Laporan orang_penting.pdf"
            pdf = SimpleDocTemplate(fileLaporan, pagesize = A4)
            isiData = Table(barisData, colWidths = [65, 45, 85, 65, 80, 65, 50])
            pdf.build([isiData])

    def cetakFilterorang_penting(self, cari):
            aksi = self.koneksi.cursor()
            aksi.execute("select * from orang_penting where keterangan = %s", ([f"{cari}"]))
            data = aksi.fetchall()
            barisData = [["id_Orang_Penting, nama, jabatan, no_hp, id_kelurahan"]] + list(data)
            # print(barisData)
            fileLaporan = "Laporan orang_penting.pdf"
            pdf = SimpleDocTemplate(fileLaporan, pagesize = A4)
            isiData = Table(barisData, colWidths = [65, 45, 85, 65, 80, 65, 50])
            pdf.build([isiData])

    # ============================================================
    # CRUD TABEL proses
    # ============================================================
    def tambahproses(self, id_proses, jenis_surat, tanggal_pengajuan,proses, id_user):
        aksi = self.koneksi.cursor()
        sql = """INSERT INTO proses (id_proses, jenis_surat, tanggal_pengajuan,proses, id_user)
                 VALUES (%s,%s,%s,%s)"""
        aksi.execute(sql, (id_proses, jenis_surat, tanggal_pengajuan,proses, id_user))
        self.koneksi.commit()
        aksi.close()

    def updateproses(self, id_proses, jenis_surat, tanggal_pengajuan,proses, id_user):
        aksi = self.koneksi.cursor()
        sql = """UPDATE proses SET jenis_surat=%s, tanggal_pengajuan=%s, proses=%s, id_user=%s WHERE id_proses=%s"""
        aksi.execute(sql, (jenis_surat, tanggal_pengajuan,proses, id_user, id_proses))
        self.koneksi.commit()
        aksi.close()

    def hapusproses(self, id_proses):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM proses WHERE id_proses=%s", (id_proses,))
        self.koneksi.commit()
        aksi.close()

    def dataproses(self):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("SELECT * FROM proses ORDER BY id_proses ASC")
        return aksi.fetchall()

    def filterproses(self, cari):
        aksi = self.koneksi.cursor(dictionary=True)
        # Mencari string 'cari' di kolom id_proses, jenis_surat, atau tanggal_pengajuan
        aksi.execute("SELECT * FROM proses WHERE id_proses LIKE %s OR jenis_surat LIKE %s OR tanggal_pengajuan LIKE %s",
        ([f"%{cari}%", f"%{cari}%", f"%{cari}%"]))
        return aksi.fetchall()

    def cetakproses(self):
            aksi = self.koneksi.cursor()
            aksi.execute("select * from proses")
            data = aksi.fetchall()
            barisData = [["id_proses, jenis_surat, tanggal_pengajuan,proses, id_user"]] + list(data)
            # print(barisData)
            fileLaporan = "Laporan proses.pdf"
            pdf = SimpleDocTemplate(fileLaporan, pagesize = A4)
            isiData = Table(barisData, colWidths = [90, 90, 90, 60])
            pdf.build([isiData])


    # ============================================================
    # CRUD TABEL super_admin
    # ============================================================
    def tambahSuper_admin(self, id_super_admin, username, password):
        aksi = self.koneksi.cursor()
        sql = """INSERT INTO super_admin (id_super_admin, username, password)
                 VALUES (%s,%s,%s,%s,%s)"""
        aksi.execute(sql, (id_super_admin, username, password))
        self.koneksi.commit()
        aksi.close()

    def updateSuper_Admin(self, id_super_admin, username, password):
        aksi = self.koneksi.cursor()
        sql = """UPDATE super_admin SET username=%s, password=%s WHERE id_super_admin=%s"""
        aksi.execute(sql, (username, password,id_super_admin ))
        self.koneksi.commit()
        aksi.close()

    def hapusSuper_Admin(self, id_lahir):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM super_admin WHERE id_super_admin=%s", (id_super_admin,))
        self.koneksi.commit()
        aksi.close()

    def dataSuper_Admin(self):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("SELECT * FROM super_Admin ORDER BY id_super_admin ASC")
        return aksi.fetchall()

    def filterSuper_Admin(self, cari):
        aksi = self.koneksi.cursor(dictionary=True)
        # Mencari string 'cari' di kolom id_super_admin, username, atau password
        aksi.execute("SELECT * FROM super_admin WHERE id_super_admin LIKE %s OR username LIKE %s OR password LIKE %s",
        ([f"%{cari}%", f"%{cari}%", f"%{cari}%"]))
        return aksi.fetchall()

    def cetakSuper_Admin(self):
            aksi = self.koneksi.cursor()
            aksi.execute("select * from super_admin")
            data = aksi.fetchall()
            barisData = [["id_super_admin, username, password"]] + list(data)
            # print(barisData)
            fileLaporan = "Laporan super_admin.pdf"
            pdf = SimpleDocTemplate(fileLaporan, pagesize = A4)
            isiData = Table(barisData, colWidths = [65, 100, 75, 80, 65])
            pdf.build([isiData])

    def cetakFilterSuper_Admin(self, cari):
            aksi = self.koneksi.cursor()
            aksi.execute("select * from super_admin where username = %s", ([f"{cari}"]))
            data = aksi.fetchall()
            barisData = [["id_super_admin, username, password"]] + list(data)
            # print(barisData)
            fileLaporan = "Laporan Super_Admin.pdf"
            pdf = SimpleDocTemplate(fileLaporan, pagesize = A4)
            isiData = Table(barisData, colWidths = [65, 100, 75, 80, 65])
            pdf.build([isiData])

    # ============================================================
    # CRUD TABEL user
    # ============================================================
    def tambahUser(self, id_user, username, email, password,alamat, id_kelurahan):
        aksi = self.koneksi.cursor()
        sql = """INSERT INTO user (id_user, username, email, password,alamat, id_kelurahan)
                 VALUES (%s,%s,%s,%s,%s,%s)"""
        aksi.execute(sql, (id_user, username, email, password,alamat, id_kelurahan))
        self.koneksi.commit()
        aksi.close()

    def updateUser(self, id_user, username, email, password,alamat, id_kelurahan):
        aksi = self.koneksi.cursor()
        sql = """UPDATE user SET username=%s, email=%s, password=%s, alamat=%s, id_kelurahan=%s WHERE id_user=%s"""
        aksi.execute(sql, (username, email, password,alamat, id_kelurahan,id_user))
        self.koneksi.commit()
        aksi.close()

    def hapusUser(self, id_user):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM user WHERE id_user=%s", (id_user,))
        self.koneksi.commit()
        aksi.close()

    def dataUser(self):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("SELECT * FROM user ORDER BY id_user ASC")
        return aksi.fetchall()

    def filterUser(self, cari):
        aksi = self.koneksi.cursor(dictionary=True)
        # Mencari string 'cari' di kolom id_user, username, atau email
        aksi.execute("SELECT * FROM user WHERE id_user LIKE %s OR username LIKE %s OR email LIKE %s",
        ([f"%{cari}%", f"%{cari}%", f"%{cari}%"]))
        return aksi.fetchall()

    def cetakUser(self):
            aksi = self.koneksi.cursor()
            aksi.execute("select * from user")
            data = aksi.fetchall()
            barisData = [["id_user", "username", "email", "password", "alamat", "id_kelurahan"]] + list(data)
            # print(barisData)
            fileLaporan = "Laporan user.pdf"
            pdf = SimpleDocTemplate(fileLaporan, pagesize = A4)
            isiData = Table(barisData, colWidths = [90, 90, 90, 60, 50])
            pdf.build([isiData])
