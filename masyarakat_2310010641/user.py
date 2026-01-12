# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_masyarakat

class form_User(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Pemasyarakatan - Halaman Data User")
        filenya = QFile('User.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formUser = muatfile.load(filenya,self)
        self.aksi = crud_masyarakat()
        self.formUser.BtnSimpan.clicked.connect(self.simpanUser)
        self.formUser.BtnUbah.clicked.connect(self.ubahUser)
        self.formUser.BtnHapus.clicked.connect(self.hapusUser)
        self.tampilDataUser()
        self.formUser.lineCari.textChanged.connect(self.cariDataUser)
        self.formUser.btnCetak.clicked.connect(self.laporanUser)

    def simpanUser(self):
        if not self.formUser.idUserLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID User belum diisi")
            self.formUser.iduserLineEdit.setFocus()
        elif not self.formUser.usernameLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Username belum diisi")
            self.formUser.usernameLineEdit.setFocus()
        elif not self.formUser.emailLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Email belum diisi")
            self.formUser.emailLineEdit.setFocus()
        elif not self.formUser.passwordLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Password belum diisi")
            self.formUser.passwordLineEdit.setFocus()
        elif not self.formUser.alamatLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Alamat belum diisi")
            self.formUser.alamatLineEdit.setFocus()
        elif not self.formUser.id_kelurahanLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Kelurahan belum diisi")
            self.formUser.id_kelurahanLineEdit.setFocus()
        else:
            # Ambil data dari form
            id_user = self.formUser.idUserLineEdit.text()
            nama = self.formUser.namaLineEdit.text()
            password = self.formUser.idPasswordLineEdit.text()
            id_kelurahan = self.formUser.idUserLineEdit.text()

            self.aksi.tambahUser(id_user, nama, password, id_kelurahan)
            self.tampilDataUser()
            QMessageBox.information(None, "Informasi", "Data berhasil disimpan")

    def ubahUser(self):
        if not self.formUser.idUserLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID User harus diisi untuk mengubah data")
            self.formUser.idUsertaLineEdit.setFocus()
            return

        id_user = self.formUser.idUserLineEdit.text()
        username = self.formUser.usernameLineEdit.text()
        email = self.formUser.emailLineEdit.text()
        password = self.formUser.passwordLineEdit.text()
        alamat = self.formUser.alamatLineEdit.text()
        id_kelurahan = self.formUser.id_kelurahanLineEdit.text()

        self.aksi.updateUser(id_user, username, email, password,alamat, id_kelurahan)
        self.tampilDataUser()
        QMessageBox.information(None, "Informasi", "Data berhasil diubah")

    def hapusUser(self):
        pesan = QMessageBox.information(None, "Informasi", "Apakah yakin menghapus data ini?",
        QMessageBox.Yes | QMessageBox.No)

        if pesan == QMessageBox.Yes:
            id_user = self.formUser.idUserLineEdit.text()
            self.aksi.hapusUser(id_user)
            self.tampilDataUser()
        else:
            pass

    def tampilDataUser(self):
        self.formUser.tblUser.setRowCount(0)
        data = self.aksi.dataUser() # Memanggil method dari crud_masyarakat

        for i, baris in enumerate(data):
            self.formUser.tblUser.insertRow(i)
            # Asumsi kolom data: id_user, username, email, password,alamat, id_kelurahan
            self.formUser.tblUser.setItem(i, 0, QTableWidgetItem(str(baris["id_user"])))
            self.formUser.tblUser.setItem(i, 1, QTableWidgetItem(str(baris["username"])))
            self.formUser.tblUser.setItem(i, 2, QTableWidgetItem(str(baris["email"])))
            self.formUser.tblUser.setItem(i, 3, QTableWidgetItem(str(baris["password"])))
            self.formUser.tblUser.setItem(i, 4, QTableWidgetItem(str(baris["alamat"])))
            self.formUser.tblUser.setItem(i, 5, QTableWidgetItem(str(baris["id_kelurahan"])))


    def cariDataUser(self):
        varCari = self.formUser.lineCari.text()
        self.formUser.tblUser.setRowCount(0)
        data = self.aksi.filterUser(varCari) # Memanggil method dari crud_masyarakat

        for i, baris in enumerate(data):
            self.formUser.tblUser.insertRow(i)
            # Asumsi kolom data
            self.formUser.tblUser.setItem(i, 0, QTableWidgetItem(str(baris["id_user"])))
            self.formUser.tblUser.setItem(i, 1, QTableWidgetItem(str(baris["username"])))
            self.formUser.tblUser.setItem(i, 2, QTableWidgetItem(str(baris["email"])))
            self.formUser.tblUser.setItem(i, 3, QTableWidgetItem(str(baris["password"])))
            self.formUser.tblUser.setItem(i, 4, QTableWidgetItem(str(baris["alamat"])))
            self.formUser.tblUser.setItem(i, 5, QTableWidgetItem(str(baris["id_kelurahan"])))


    def laporanUser(self):
        self.aksi.cetakUser()
