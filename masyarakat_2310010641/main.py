import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from admin import form_Admin
from agenda import form_Agenda
from kelurahan import form_Kelurahan
from laporan import form_Laporan
from orang_penting import form_Orang_Penting
from proses import form_Proses
from super_admin import form_Super_Admin
from user import form_User


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Pemasyarakatan - Halaman Utama")
        filenya = QFile('main.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formutama = muatfile.load(filenya,self)
        self.resize(self.formutama.size())
        self.setMenuBar(self.formutama.menuBar())

        self.formutama.actionData_Admin.triggered.connect(self.bukaAdmin)
        self.formutama.actionData_Agenda.triggered.connect(self.bukaAgenda)
        self.formutama.actionData_Kelurahan.triggered.connect(self.bukaKelurahan)
        self.formutama.actionData_Laporan.triggered.connect(self.bukaLaporan)
        self.formutama.actionData_Orang_Penting.triggered.connect(self.bukaOrang_Penting)
        self.formutama.actionData_Proses.triggered.connect(self.bukaProses)
        self.formutama.actionData_Super_Admin.triggered.connect(self.bukaSuper_Admin)
        self.formutama.actionData_User.triggered.connect(self.bukaUser)

    def bukaAdmin(self):
        self.formAdmi = form_Admin()
        self.formAdmi.show()

    def bukaAgenda(self):
        self.formAgenda = form_Agenda()
        self.formAgenda.show()

    def bukaKelurahan(self):
        self.form_Kelurahan = form_Kelurahan()
        self.form_Kelurahan.show()

    def bukaLaporan(self):
        self.formLaporan = form_Laporan()
        self.formLaporan.show()

    def bukaOrang_Penting(self):
        self.formOran = form_Orang_Penting()
        self.formOran.show()

    def bukaProses(self):
        self.formPros = form_Proses()
        self.formPros.show()

    def bukaSuper_Admin(self):
        self.formSupe = form_Super_Admin()
        self.formSupe.show()

    def bukaUser(self):
        self.formUser = form_User()
        self.formUser.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    jendela = MainWindow()
    jendela.show()
    sys.exit(app.exec())

