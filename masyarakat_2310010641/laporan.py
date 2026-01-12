# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_masyarakat

class form_Laporan(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Pemasyarakatan - Halaman Data Laporan")
        filenya = QFile('Laporan.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formLaporan = muatfile.load(filenya,self)
        self.aksi = crud_masyarakat()
        self.formLaporan.btnSimpan.clicked.connect(self.simpanLaporan)
        self.formLaporan.btnUbah.clicked.connect(self.ubahLaporan)
        self.formLaporan.btnHapus.clicked.connect(self.hapusLaporan)
        self.tampilDataLaporan()
        self.formLaporan.lineCari.textChanged.connect(self.cariDataLaporan)
        self.formLaporan.btnCetak.clicked.connect(self.laporanLaporan)

    def simpanLaporan(self):
        if not self.formLaporan.idLaporanLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID laporan belum diisi")
            self.formLaporan.idLaporanLineEdit.setFocus()
        elif not self.formLaporan.judullaporanLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Judul laporan belum diisi")
            self.formLaporan.judulLaporanaporanLineEdit.setFocus()
        elif not self.formLaporan.lokasilaporanLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Lokasi Laporan diisi")
            self.formLaporan.lokasilaporanLineEdit.setFocus()
        elif not self.formLaporan.jenislaporanLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Jenis Laporan belum diisi")
            self.formLaporan.jenislaporanLineEdit.setFocus()
        elif not self.formLaporan.deskripsiLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "deskripsi belum diisi")
            self.formLaporan.deskripsiLineEdit.setFocus()
        elif not self.formLaporan.iduserLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID User Laporan belum diisi")
            self.formLaporan.iduserLineEdit.setFocus()
        else:
            # Ambil data dari form
            id_laporan = self.formLaporan.idLaporanLineEdit.text()
            judul_laporan = self.formLaporan.judullaporanLineEdit.text()
            lokasi_laporan = self.formLaporan.lokasilaporanLineEdit.text()
            Jenis_laporan = self.formLaporan.jenislaporanLineEdit.text()
            deskripsi = self.formLaporan.deskripsiLineEdit.text()
            id_user = self.formLaporan.iduserLineEdit.text()

            self.aksi.tambahlaporan(id_laporan, judul_laporan, lokasi_laporan, Jenis_laporan, deskripsi, id_user)
            self.tampilDatalaporan()
            QMessageBox.information(None, "Informasi", "Data berhasil disimpan")

    def ubahlaporan(self):
        if not self.formlaporan.idlaporanLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID laporan harus diisi untuk mengubah data")
            self.formlaporan.idlaporanLineEdit.setFocus()
            return

        id_laporan = self.formLaporan.idLaporanLineEdit.text()
        judul_laporan = self.formLaporan.judulLineEdit.text()
        lokasi_laporan = self.formLaporan.lokasilaporanLineEdit.text()
        Jenis_laporan = self.formLaporan.JenislaporanLineEdit.text()
        deskripsi = self.formLaporan.deskripsiLineEdit.text()
        id_user = self.formLaporan. iduserLineEdit.text()

        self.aksi.updateLaporan(id_laporan, judul_laporan, lokasi_laporan, Jenis_laporan, deskripsi, id_user)
        self.tampilDataLaporan()
        QMessageBox.information(None, "Informasi", "Data berhasil diubah")

    def hapusLaporan(self):
        pesan = QMessageBox.information(None, "Informasi", "Apakah yakin menghapus data ini?",
        QMessageBox.Yes | QMessageBox.No)

        if pesan == QMessageBox.Yes:
            id_laporan = self.formLaporan.idLaporanLineEdit.text()
            self.aksi.hapusLaporan(id_laporan)
            self.tampilDataLaporan()
        else:
            pass

    def tampilDataLaporan(self):
        self.formLaporan.tblLaporan.setRowCount(0)
        data = self.aksi.dataLaporan() # Memanggil method dari crud_masyarakat

        for i, baris in enumerate(data):
            self.formLaporan.tblLaporan.insertRow(i)
            # Asumsi kolom data: id_laporan, judul_laporan, lokasi_laporan, Jenis_laporan, deskripsi, id_user
            self.formLaporan.tblLaporan.setItem(i, 0, QTableWidgetItem(str(baris["id_laporan"])))
            self.formLaporan.tblLaporan.setItem(i, 1, QTableWidgetItem(str(baris["Judul laporan "])))
            self.formLaporan.tblLaporan.setItem(i, 2, QTableWidgetItem(str(baris["Lokasi Laporan"])))
            self.formLaporan.tblLaporan.setItem(i, 3, QTableWidgetItem(str(baris["Jenis Laporan"])))
            self.formLaporan.tblLaporan.setItem(i, 4, QTableWidgetItem(str(baris["deskripsi"])))
            self.formLaporan.tblLaporan.setItem(i, 5, QTableWidgetItem(str(baris["id_user"])))


    def cariDataLaporan(self):
        varCari = self.formLaporan.lineCari.text()
        self.formLaporan.tblLaporan.setRowCount(0)
        data = self.aksi.filterLaporan(varCari) # Memanggil method dari crud_masyarakat

        for i, baris in enumerate(data):
            self.formLaporan.tblLaporan.insertRow(i)
            # Asumsi kolom data
            self.formLaporan.tblLaporan.setItem(i, 0, QTableWidgetItem(str(baris["id_laporan"])))
            self.formLaporan.tblLaporan.setItem(i, 1, QTableWidgetItem(str(baris["Judul laporan"])))
            self.formLaporan.tblLaporan.setItem(i, 2, QTableWidgetItem(str(baris["Lokasi Laporan"])))
            self.formLaporan.tblLaporan.setItem(i, 3, QTableWidgetItem(str(baris["Jenis Laporan"])))
            self.formLaporan.tblLaporan.setItem(i, 4, QTableWidgetItem(str(baris["deskripsi"])))
            self.formLaporan.tblLaporan.setItem(i, 5, QTableWidgetItem(str(baris["id_user"])))

    def laporanLaporan(self):
        self.aksi.cetakLaporan()
