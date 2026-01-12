# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_masyarakat

class form_Proses(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Pemasyarakatan - Halaman Data Proses")
        filenya = QFile('Proses.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formProses = muatfile.load(filenya,self)
        self.aksi = crud_masyarakat()
        self.formProses.BtnSimpan.clicked.connect(self.simpanProses)
        self.formProses.BtnUbah.clicked.connect(self.ubahProses)
        self.formProses.BtnHapus.clicked.connect(self.hapusProses)
        self.tampilDataProses()
        self.formProses.lineCari.textChanged.connect(self.cariDataProses)
        self.formProses.btnCetak.clicked.connect(self.laporanProses)

    def simpanProses(self):
        if not self.formProses.idProsesLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Proses belum diisi")
            self.formProses.idProsesLineEdit.setFocus()
        elif not self.formProses.jenis_suratLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Jenis Surat belum diisi")
            self.formProses.jenissuratLineEdit.setFocus()
        elif not self.formProses.tanggal_pengajuanLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Tanggal Pengajuan belum diisi")
            self.formProses.tanggalpengajuanLineEdit.setFocus()
        elif not self.formProses.prosesLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Proses belum diisi")
            self.formProses.prosesLineEdit.setFocus()
        elif not self.formProses.id_userLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID User belum diisi")
            self.formProses.id_userLineEdit.setFocus()
        else:
            id_proses = self.formProses.idProsesLineEdit.text()
            jenis_surat = self.formProses.jenissuratLineEdit.text()
            tanggal_pengajuan = self.formProses.tanggalpengajuanLineEdit.text()
            proses = self.formProses.idProsesLineEdit.text()
            id_user = self.formProses.iduserLineEdit.text()

            self.aksi.tambahProses(id_proses, jenis_surat, tanggal_pengajuan,proses, id_user)
            self.tampilDataProses()
            QMessageBox.information(None, "Informasi", "Data berhasil disimpan")

    def ubahProses(self):
        if not self.formProses.idProsesLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Proses harus diisi untuk mengubah data")
            self.formProses.idProsesLineEdit.setFocus()
            return

        id_proses = self.formProses.idProsesLineEdit.text()
        jenis_surat= self.formProses.jenis_suratLineEdit.text()
        tanggal_pengajuan = self.formProses.tanggal_pengajuanLineEdit.text()
        proses = self.formProses.prosesLineEdit.text()
        id_user = self.formProses.id_userLineEdit.text()

        self.aksi.updateProses(id_proses, jenis_surat, tanggal_pengajuan,proses, id_user)
        self.tampilDataProses()
        QMessageBox.information(None, "Informasi", "Data berhasil diubah")

    def hapusProses(self):
        pesan = QMessageBox.information(None, "Informasi", "Apakah yakin menghapus data ini?",
        QMessageBox.Yes | QMessageBox.No)

        if pesan == QMessageBox.Yes:
            id_proses = self.formProses.idProsesLineEdit.text()
            self.aksi.hapusProses(id_proses)
            self.tampilDataProses()
        else:
            pass

    def tampilDataProses(self):
        self.formProses.tblProses.setRowCount(0)
        data = self.aksi.dataProses()

        for i, baris in enumerate(data):
            self.formProses.tblProses.insertRow(i)
            self.formProses.tblProses.setItem(i, 0, QTableWidgetItem(str(baris["id_proses"])))
            self.formProses.tblProses.setItem(i, 1, QTableWidgetItem(str(baris["Jenis Surat"])))
            self.formProses.tblProses.setItem(i, 2, QTableWidgetItem(str(baris["Tanggal Pengajuan"])))
            self.formProses.tblProses.setItem(i, 3, QTableWidgetItem(str(baris["Proses"])))
            self.formProses.tblProses.setItem(i, 4, QTableWidgetItem(str(baris["id_User"])))

    def cariDataProses(self):
        varCari = self.formProses.lineCari.text()
        self.formProses.tblProses.setRowCount(0)
        data = self.aksi.filterProses(varCari)

        for i, baris in enumerate(data):
            self.formProses.tblProses.insertRow(i)
            self.formProses.tblProses.setItem(i, 0, QTableWidgetItem(str(baris["id_proses"])))
            self.formProses.tblProses.setItem(i, 1, QTableWidgetItem(str(baris["Jenis Surat"])))
            self.formProses.tblProses.setItem(i, 2, QTableWidgetItem(str(baris["Tanggal Pengajuan"])))
            self.formProses.tblProses.setItem(i, 2, QTableWidgetItem(str(baris["Proses"])))
            self.formProses.tblProses.setItem(i, 3, QTableWidgetItem(str(baris["id_User"])))

    def laporanProses(self):
        self.aksi.cetakProses()
