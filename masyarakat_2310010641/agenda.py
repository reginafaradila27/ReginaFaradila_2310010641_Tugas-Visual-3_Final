# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_masyarakat

class form_Agenda(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Pemasyarakatan - Halaman Data Agenda")
        filenya = QFile('Agenda.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formAgenda = muatfile.load(filenya,self)
        self.aksi = crud_masyarakat()
        self.formAgenda.btnSimpan.clicked.connect(self.simpanAgenda)
        self.formAgenda.btnUbah.clicked.connect(self.ubahAgenda)
        self.formAgenda.btnHapus.clicked.connect(self.hapusAgenda)
        self.tampilDataAgenda()
        self.formAgenda.lineCari.textChanged.connect(self.cariDataAgenda)
        self.formAgenda.btnCetak.clicked.connect(self.laporanAgenda)

    def simpanAgenda(self):
        if not self.formAgenda.idAgendaLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Agenda belum diisi")
            self.formAgenda.idAgendaLineEdit.setFocus()
        elif not self.formAgenda.judulLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "judul belum diisi")
            self.formAgenda.judulLineEdit.setFocus()
        elif not self.formAgenda.tanggalterselenggaraLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Tanggal Terselenggara diisi")
            self.formAgenda.tanggalterselenggaraLineEdit.setFocus()
        elif not self.formAgenda.idkelurahanLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Kelurahan belum diisi")
            self.formAgenda.idkelurahanLineEdit.setFocus()
        else:
            # Ambil data dari form
            id_agenda = self.formAgenda.idAgendaLineEdit.text()
            judul = self.formAgenda.judulLineEdit.text()
            tanggal_terselenggara = self.formAgenda.tanggalterselenggaraLineEdit.text()
            id_kelurahan = self.formAgenda.idkelurahanLineEdit.text()

            self.aksi.tambahAgenda(id_agenda, judul, tanggal_terselenggara, id_kelurahan)
            self.tampilDataAgenda()
            QMessageBox.information(None, "Informasi", "Data berhasil disimpan")

    def ubahAgenda(self):
        if not self.formAgenda.idAgendaLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Agenda harus diisi untuk mengubah data")
            self.formAgenda.idAgendaLineEdit.setFocus()
            return

        id_Agenda = self.formAgenda.idAgendaLineEdit.text()
        judul = self.formAgenda.judulLineEdit.text()
        tanggal_terselenggara = self.formAgenda.tanggal_terselenggaraLineEdit.text()
        id_kelurahan = self.formAgenda.id_kelurahanLineEdit.text()

        self.aksi.updateAgenda(id_agenda, judul, tanggal_terselenggara, id_kelurahan)
        self.tampilDataAgenda()
        QMessageBox.information(None, "Informasi", "Data berhasil diubah")

    def hapusAgenda(self):
        pesan = QMessageBox.information(None, "Informasi", "Apakah yakin menghapus data ini?",
        QMessageBox.Yes | QMessageBox.No)

        if pesan == QMessageBox.Yes:
            id_anggota = self.formAgenda.idAgendaLineEdit.text()
            self.aksi.hapusAgenda(id_agenda)
            self.tampilDataAgenda()
        else:
            pass

    def tampilDataAgenda(self):
        self.formAgenda.tblAgenda.setRowCount(0)
        data = self.aksi.dataAgenda() # Memanggil method dari crud_masyarakat

        for i, baris in enumerate(data):
            self.formAgenda.tblAgenda.insertRow(i)
            # Asumsi kolom data: id_agenda, judul, tanggal_terselenggara, id_kelurahan
            self.formAgenda.tblAgenda.setItem(i, 0, QTableWidgetItem(str(baris["id_agenda"])))
            self.formAgenda.tblAgenda.setItem(i, 1, QTableWidgetItem(str(baris["judul"])))
            self.formAgenda.tblAgenda.setItem(i, 2, QTableWidgetItem(str(baris["tanggal_terselenggara"])))
            self.formAgenda.tblAgenda.setItem(i, 3, QTableWidgetItem(str(baris["id_kelurahan"])))


    def cariDataAgenda(self):
        varCari = self.formAgenda.lineCari.text()
        self.formAgenda.tblAgenda.setRowCount(0)
        data = self.aksi.filterAgenda(varCari) # Memanggil method dari crud_masyarakat

        for i, baris in enumerate(data):
            self.formAgenda.tblAgenda.insertRow(i)
            # Asumsi kolom data
            self.formAgenda.tblAgenda.setItem(i, 0, QTableWidgetItem(str(baris["id_Agenda"])))
            self.formAgenda.tblAgenda.setItem(i, 1, QTableWidgetItem(str(baris["judul"])))
            self.formAgenda.tblAgenda.setItem(i, 2, QTableWidgetItem(str(baris["tanggal_terselenggara"])))
            self.formAgenda.tblAgenda.setItem(i, 3, QTableWidgetItem(str(baris["id_kelurahan"])))

    def laporanAgenda(self):
        self.aksi.cetakAgenda()
