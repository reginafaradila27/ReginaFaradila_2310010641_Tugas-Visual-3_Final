# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_masyarakat

class form_Super_Admin(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Pemasyarakatan - Halaman Data Super_Admin")
        filenya = QFile('Super_Admin.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formSuper_Admin = muatfile.load(filenya,self)
        self.aksi = crud_masyarakat()
        self.formSuper_Admin.BtnSimpan.clicked.connect(self.simpanSuper_Admin)
        self.formSuper_Admin.BtnUbah.clicked.connect(self.ubahSuper_Admin)
        self.formSuper_Admin.BtnHapus.clicked.connect(self.hapusSuper_Admin)
        self.tampilDataSuper_Admin()
        self.formSuper_Admin.lineCari.textChanged.connect(self.cariDataSuper_Admin)
        self.formSuper_Admin.btnCetak.clicked.connect(self.laporanSuper_Admin)

    def simpanSuper_Admin(self):
        if not self.formSuper_Admin.idSuper_AdminLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Super_Admin belum diisi")
            self.formSuper_Admin.idSuper_AdminLineEdit.setFocus()
        elif not self.formSuper_Admin.usernameLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Username belum diisi")
            self.formSuper_Admin.namaLineEdit.setFocus()
        elif not self.formSuper_Admin.passwordLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Password belum diisi")
            self.formSuper_Admin.passwordLineEdit.setFocus()

        else:
            # Ambil data dari form
            id_super_admin = self.formSuper_Admin.idSuper_AdminLineEdit.text()
            username = self.formSuper_Admin.usernameLineEdit.text()
            password = self.formSuper_Admin.idPasswordLineEdit.text()

            self.aksi.tambahSuper_Admin(id_super_admin, username, password)
            self.tampilDataSuper_Admin()
            QMessageBox.information(None, "Informasi", "Data berhasil disimpan")

    def ubahSuper_Admin(self):
        if not self.formSuper_Admin.idSuper_AdminLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Super_Admin harus diisi untuk mengubah data")
            self.formSuper_Admin.idSuper_AdmintaLineEdit.setFocus()
            return

        id_super_admin = self.formSuper_Admin.idSuper_AdminLineEdit.text()
        username = self.formSuper_Admin.usernameLineEdit.text()
        password = self.formSuper_Admin.passwordLineEdit.text()


        self.aksi.updateSuper_Admin(id_super_admin, username, password)
        self.tampilDataSuper_Admin()
        QMessageBox.information(None, "Informasi", "Data berhasil diubah")

    def hapusSuper_Admin(self):
        pesan = QMessageBox.information(None, "Informasi", "Apakah yakin menghapus data ini?",
        QMessageBox.Yes | QMessageBox.No)

        if pesan == QMessageBox.Yes:
            id_super_admin = self.formSuper_Admin.idSuper_AdminLineEdit.text()
            self.aksi.hapusSuper_Admin(id_super_admin)
            self.tampilDataSuper_Admin()
        else:
            pass

    def tampilDataSuper_Admin(self):
        self.formSuper_Admin.tblSuper_Admin.setRowCount(0)
        data = self.aksi.dataSuper_Admin() # Memanggil method dari crud_masyarakat

        for i, baris in enumerate(data):
            self.formSuper_Admin.tblSuper_Admin.insertRow(i)
            # Asumsi kolom data: id_super_admin, nama, password, id_kelurahan
            self.formSuper_Admin.tblSuper_Admin.setItem(i, 0, QTableWidgetItem(str(baris["id_super_admin"])))
            self.formSuper_Admin.tblSuper_Admin.setItem(i, 1, QTableWidgetItem(str(baris["username"])))
            self.formSuper_Admin.tblSuper_Admin.setItem(i, 2, QTableWidgetItem(str(baris["password"])))


    def cariDataSuper_Admin(self):
        varCari = self.formSuper_Admin.lineCari.text()
        self.formSuper_Admin.tblSuper_Admin.setRowCount(0)
        data = self.aksi.filterSuper_Admin(varCari) # Memanggil method dari crud_masyarakat

        for i, baris in enumerate(data):
            self.formSuper_Admin.tblSuper_Admin.insertRow(i)
            # Asumsi kolom data
            self.formSuper_Admin.tblSuper_Admin.setItem(i, 0, QTableWidgetItem(str(baris["id_super_admin"])))
            self.formSuper_Admin.tblSuper_Admin.setItem(i, 1, QTableWidgetItem(str(baris["username"])))
            self.formSuper_Admin.tblSuper_Admin.setItem(i, 2, QTableWidgetItem(str(baris["password"])))

    def laporanSuper_Admin(self):
        self.aksi.cetakSuper_Admin()
