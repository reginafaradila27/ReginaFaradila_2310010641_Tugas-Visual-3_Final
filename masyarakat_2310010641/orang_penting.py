# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_masyarakat

class form_Orang_Penting(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Pemasyarakatan - Halaman Data Admin")
        filenya = QFile('Orang_Penting.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formOrang_Penting = muatfile.load(filenya,self)
        self.aksi = crud_masyarakat()
        self.formOrang_Penting.BtnSimpan.clicked.connect(self.simpanOrang_Penting)
        self.formOrang_Penting.BtnUbah.clicked.connect(self.ubahOrang_Penting)
        self.formOrang_Penting.BtnHapus.clicked.connect(self.hapusOrang_Penting)
        self.tampilDataOrang_Penting()
        self.formOrang_Penting.lineCari.textChanged.connect(self.cariDataOrang_Penting)
        self.formOrang_Penting.btnCetak.clicked.connect(self.laporanOrang_Penting)

    def simpanOrang_Penting(self):
        if not self.formOrang_Penting.idOrang_PentingLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Orang_Penting belum diisi")
            self.formOrang_Penting.idOrang_PentingLineEdit.setFocus()
        elif not self.formOrang_Penting.namaLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Nama belum diisi")
            self.formOrang_Penting.namaLineEdit.setFocus()
        elif not self.formOrang_Penting.jabatanLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Jabatan belum diisi")
            self.formOrang_Penting.no_hpLineEdit.setFocus()
        elif not self.formOrang_Penting.no_hpLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "No_hp belum diisi")
            self.formOrang_Penting.no_hpLineEdit.setFocus()
        elif not self.formOrang_Penting.id_kelurahanLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Kelurahan belum diisi")
            self.formOrang_Penting.id_kelurahanLineEdit.setFocus()
        else:
            # Ambil data dari form
            id_Orang_Penting = self.formOrang_Penting.idOrang_PentingLineEdit.text()
            nama = self.formOrang_Penting.namaLineEdit.text()
            jabatan = self.formOrang_Penting.jabatanLineEdit.text()
            no_hp = self.formOrang_Penting.nohpLineEdit.text()
            id_kelurahan = self.formAdmin.idAdminLineEdit.text()

            self.aksi.tambahOrang_Penting(id_Orang_Penting, nama, jabatan, no_hp, id_kelurahan)
            self.tampilDataOrang_Penting()
            QMessageBox.information(None, "Informasi", "Data berhasil disimpan")

    def ubahOrang_Penting(self):
        if not self.formOrang_Penting.idOrang_PentingLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Orang_Penting harus diisi untuk mengubah data")
            self.formOrang_Penting.idOrang_PentingtaLineEdit.setFocus()
            return

        id_Orang_Penting = self.formOrang_Penting.idOrang_PentingLineEdit.text()
        nama = self.formOrang_Penting.namaLineEdit.text()
        jabatan = self.formOrang_Penting.jabatanLineEdit.text()
        no_hp = self.formOrang_Penting.nohpLineEdit.text()
        id_kelurahan = self.formOrang_Penting.id_kelurahanLineEdit.text()

        self.aksi.updateOrang_Penting(id_Orang_Penting, nama, jabatan, no_hp, id_kelurahan)
        self.tampilDataOrang_Penting()
        QMessageBox.information(None, "Informasi", "Data berhasil diubah")

    def hapusOrang_Penting(self):
        pesan = QMessageBox.information(None, "Informasi", "Apakah yakin menghapus data ini?",
        QMessageBox.Yes | QMessageBox.No)

        if pesan == QMessageBox.Yes:
            id_Orang_Penting = self.formAdmin.idOrang_PentingLineEdit.text()
            self.aksi.hapusOrang_Penting(id_Orang_Penting)
            self.tampilDataOrang_Penting()
        else:
            pass

    def tampilDataOrang_Penting(self):
        self.formOrang_Penting.tblOrang_Penting.setRowCount(0)
        data = self.aksi.dataOrang_Penting() # Memanggil method dari crud_masyarakat

        for i, baris in enumerate(data):
            self.formOrang_Penting.tblOrang_Pentingn.insertRow(i)
            # Asumsi kolom data: id_Orang_Penting, nama, jabatan, no_hp, id_kelurahan
            self.formOrang_Penting.tblOrang_Penting.setItem(i, 0, QTableWidgetItem(str(baris["id_admin"])))
            self.formOrang_Penting.tblOrang_Penting.setItem(i, 1, QTableWidgetItem(str(baris["nama"])))
            self.formOrang_Penting.tblOrang_Penting.setItem(i, 2, QTableWidgetItem(str(baris["jabatan"])))
            self.formOrang_Penting.tblOrang_Penting.setItem(i, 3, QTableWidgetItem(str(baris["no_hp"])))
            self.formOrang_Penting.tblOrang_Penting.setItem(i, 4, QTableWidgetItem(str(baris["id_kelurahan"])))


    def cariDataOrang_Penting(self):
        varCari = self.formAdmin.lineCari.text()
        self.formOrang_Penting.tblOrang_Penting.setRowCount(0)
        data = self.aksi.filterOrang_Penting(varCari) # Memanggil method dari crud_masyarakat

        for i, baris in enumerate(data):
            self.formOrang_Penting.tblOrang_Penting.insertRow(i)
            # Asumsi kolom data
            self.formOrang_Penting.tblOrang_Penting.setItem(i, 0, QTableWidgetItem(str(baris["id_Orang_Penting"])))
            self.formOrang_Penting.tblOrang_Penting.setItem(i, 1, QTableWidgetItem(str(baris["nama"])))
            self.formOrang_Penting.tblOrang_Penting.setItem(i, 2, QTableWidgetItem(str(baris["jabatan"])))
            self.formOrang_Penting.tblOrang_Penting.setItem(i, 3, QTableWidgetItem(str(baris["no_hp"])))
            self.formOrang_Penting.tblOrang_Penting.setItem(i, 4, QTableWidgetItem(str(baris["id_kelurahan"])))

    def laporanOrang_Penting(self):
        self.aksi.cetakOrang_Penting()
