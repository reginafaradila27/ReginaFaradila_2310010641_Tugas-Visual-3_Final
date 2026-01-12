# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_masyarakat

class form_Admin(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Pemasyarakatan - Halaman Data Admin")
        filenya = QFile('admin.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formAdmin = muatfile.load(filenya,self)
        self.aksi = crud_masyarakat()
        self.formAdmin.btnSimpan.clicked.connect(self.simpanAdmin)
        self.formAdmin.btnUbah.clicked.connect(self.ubahAdmin)
        self.formAdmin.btnHapus.clicked.connect(self.hapusAdmin)
        self.tampilDataAdmin()
        self.formAdmin.lineCari.textChanged.connect(self.cariDataAdmin)
        self.formAdmin.btnCetak.clicked.connect(self.laporanAdmin)

    def simpanAdmin(self):
        if not self.formAdmin.idadminLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Admin belum diisi")
            self.formAdmin.idadminLineEdit.setFocus()
        elif not self.formAdmin.namaLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Nama belum diisi")
            self.formAdmin.namaLineEdit.setFocus()
        elif not self.formAdmin.passwordLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Password diisi")
            self.formAdmin.passwordLineEdit.setFocus()
        elif not self.formAdmin.kelurahanLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Kelurahan belum diisi")
            self.formAdmin.idkelurahanLineEdit.setFocus()
        else:
            # Ambil data dari form
            id_admin = self.formAdmin.idadminLineEdit.text()
            nama = self.formAdmin.namaLineEdit.text()
            password = self.formAdmin.passwordLineEdit.text()
            id_kelurahan = self.formAdmin.kelurahanLineEdit.text()

            self.aksi.tambahAdmin(id_admin, nama, password, id_kelurahan)
            self.tampilDataAdmin()
            QMessageBox.information(None, "Informasi", "Data berhasil disimpan")

    def ubahAdmin(self):
        if not self.formAdmin.idadminLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Admin harus diisi untuk mengubah data")
            self.formAdmin.idAdminLineEdit.setFocus()
            return

        id_admin = self.formAdmin.idAdminLineEdit.text()
        nama = self.formAdmin.namaLineEdit.text()
        password = self.formAdmin.passwordLineEdit.text()
        id_kelurahan = self.formAdmin.id_kelurahanLineEdit.text()

        self.aksi.updateAdmin(id_admin, nama, password, id_kelurahan)
        self.tampilDataAdmin()
        QMessageBox.information(None, "Informasi", "Data berhasil diubah")

    def hapusAdmin(self):
        pesan = QMessageBox.information(None, "Informasi", "Apakah yakin menghapus data ini?",
        QMessageBox.Yes | QMessageBox.No)

        if pesan == QMessageBox.Yes:
            id_admin = self.formAdmin.idadminLineEdit.text()
            self.aksi.hapusAdmin(id_admin)
            self.tampilDataAdmin()
        else:
            pass

    def tampilDataAdmin(self):
        self.formAdmin.tblAdmin.setRowCount(0)
        data = self.aksi.dataAdmin() # Memanggil method dari crud_masyarakat

        for i, baris in enumerate(data):
            self.formAdmin.tblAdmin.insertRow(i)
            # Asumsi kolom data: id_admin, nama, password, id_kelurahan
            self.formAdmin.tblAdmin.setItem(i, 0, QTableWidgetItem(str(baris["id_admin"])))
            self.formAdmin.tblAdmin.setItem(i, 1, QTableWidgetItem(str(baris["nama"])))
            self.formAdmin.tblAdmin.setItem(i, 2, QTableWidgetItem(str(baris["password"])))
            self.formAdmin.tblAdmin.setItem(i, 3, QTableWidgetItem(str(baris["id_kelurahan"])))


    def cariDataAdmin(self):
        varCari = self.formAdmin.lineCari.text()
        self.formAdmin.tblAdmin.setRowCount(0)
        data = self.aksi.filterAdmin(varCari) # Memanggil method dari crud_masyarakat

        for i, baris in enumerate(data):
            self.formAdmin.tblAdmin.insertRow(i)
            # Asumsi kolom data
            self.formAdmin.tblAdmin.setItem(i, 0, QTableWidgetItem(str(baris["id_admin"])))
            self.formAdmin.tblAdmin.setItem(i, 1, QTableWidgetItem(str(baris["nama"])))
            self.formAdmin.tblAdmin.setItem(i, 2, QTableWidgetItem(str(baris["password"])))
            self.formAdmin.tblAdmin.setItem(i, 3, QTableWidgetItem(str(baris["id_kelurahan"])))

    def laporanAdmin(self):
        self.aksi.cetakAdmin()
