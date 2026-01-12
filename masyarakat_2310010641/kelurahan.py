# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_masyarakat

class form_Kelurahan(QWidget):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.setWindowTitle("Pemasyarakatan - Halaman Data Kelurahan ")
        filenya = QFile('kelurahan.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formKelurahan = muatfile.load(filenya,self)
        self.aksi = crud_masyarakat()
        self.formKelurahan.btnSimpan.clicked.connect(self.simpanKelurahan)
        self.formKelurahan.btnUbah.clicked.connect(self.ubahKelurahan)
        self.formKelurahan.btnHapus.clicked.connect(self.hapusKelurahan)
        self.tampilDataKelurahan()
        self.formKelurahan.lineCari.textChanged.connect(self.cariDataKelurahan)
        self.formKelurahan.btnCetak.clicked.connect(self.laporanKelurahan)

    def simpanKelurahan(self):
        if not self.formKelurahan.idKelurahanLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Kelurahan belum diisi")
            self.formKelurahan.idKelurahanLineEdit.setFocus()
        elif not self.formKelurahan.namakelurahanLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "namakelurahan belum diisi")
            self.formKelurahan.namakelurahanLineEdit.setFocus()
        elif not self.formKelurahan.idlurahLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "idlurah diisi")
            self.formKelurahan.idlurahLineEdit.setFocus()

        else:
            # Ambil data dari form
            id_Kelurahan = self.formKelurahan.idKelurahanLineEdit.text()
            nama_kelurahan = self.formKelurahan.namakelurahanLineEdit.text()
            id_lurah = self.formKelurahan. idlurahLineEdit.text()

            self.aksi.tambahKelurahan(id_kelurahan, nama_kelurahan, id_lurah)
            self.tampilDataKelurahan()
            QMessageBox.information(None, "Informasi", "Data berhasil disimpan")

    def ubahKelurahan(self):
        if not self.formKelurahan.idAgendaLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Kelurahan harus diisi untuk mengubah data")
            self.formKelurahan.idKelurahanLineEdit.setFocus()
            return

        id_Kelurahan = self.formKelurahan.idKelurahanLineEdit.text()
        nama_kelurahan = self.formKelurahan.namakelurahanLineEdit.text()
        id_lurah = self.formKelurahan.idlurahLineEdit.text()


        self.aksi.updateKelurahan(id_kelurahan, nama_kelurahan,id_lurah)
        self.tampilDataKelurahan()
        QMessageBox.information(None, "Informasi", "Data berhasil diubah")

    def hapusKelurahan(self):
        pesan = QMessageBox.information(None, "Informasi", "Apakah yakin menghapus data ini?",
        QMessageBox.Yes | QMessageBox.No)

        if pesan == QMessageBox.Yes:
            id_Kelurahan = self.formKelurahan.idKelurahanLineEdit.text()
            self.aksi.hapusKelurahan(id_kelurahan)
            self.tampilDataKelurahan()
        else:
            pass

    def tampilDataKelurahan(self):
        self.formKelurahan.tblKelurahan.setRowCount(0)
        data = self.aksi.dataKelurahan() # Memanggil method dari crud_masyarakat

        for i, baris in enumerate(data):
            self.formKelurahan.tblKelurahan.insertRow(i)
            # Asumsi kolom data: id_Kelurahan,nama_kelurahan  , id_lurah
            self.formKelurahan.tblKelurahan.setItem(i, 0, QTableWidgetItem(str(baris["id_kelurahan"])))
            self.formKelurahan.tblKelurahan.setItem(i, 1, QTableWidgetItem(str(baris["nama_kelurahan"])))
            self.formKelurahan.tblKelurahan.setItem(i, 2, QTableWidgetItem(str(baris["id_lurah"])))


    def cariDataKelurahan(self):
        varCari = self.formKelurahan.lineCari.text()
        self.formKelurahan.tblKelurahan.setRowCount(0)
        data = self.aksi.filterKelurahan(varCari) # Memanggil method dari crud_masyarakat

        for i, baris in enumerate(data):
            self.formKelurahan.tblKelurahan.insertRow(i)
            # Asumsi kolom data
            self.formKelurahan.tblKelurahan.setItem(i, 0, QTableWidgetItem(str(baris["id_Kelurahan"])))
            self.formKelurahan.tblKelurahan.setItem(i, 1, QTableWidgetItem(str(baris["nama_kelurahan"])))
            self.formKelurahan.tblKelurahan.setItem(i, 2, QTableWidgetItem(str(baris["id_lurah"])))


    def laporanKelurahan(self):
        self.aksi.cetakKelurahan()
