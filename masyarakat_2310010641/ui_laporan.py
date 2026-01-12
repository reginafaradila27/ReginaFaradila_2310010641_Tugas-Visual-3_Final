# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'laporan.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(670, 312)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 231, 251))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.id_Laporan = QLabel(self.formLayoutWidget)
        self.id_Laporan.setObjectName(u"id_Laporan")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.id_Laporan)

        self.lineidlaporan = QLineEdit(self.formLayoutWidget)
        self.lineidlaporan.setObjectName(u"lineidlaporan")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineidlaporan)

        self.Judul_Laporan = QLabel(self.formLayoutWidget)
        self.Judul_Laporan.setObjectName(u"Judul_Laporan")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.Judul_Laporan)

        self.linejudullaporan = QLineEdit(self.formLayoutWidget)
        self.linejudullaporan.setObjectName(u"linejudullaporan")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.linejudullaporan)

        self.Lokasi_Laporan = QLabel(self.formLayoutWidget)
        self.Lokasi_Laporan.setObjectName(u"Lokasi_Laporan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.Lokasi_Laporan)

        self.linelokasilaporan = QLineEdit(self.formLayoutWidget)
        self.linelokasilaporan.setObjectName(u"linelokasilaporan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.linelokasilaporan)

        self.Jenis_Laporan = QLabel(self.formLayoutWidget)
        self.Jenis_Laporan.setObjectName(u"Jenis_Laporan")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.Jenis_Laporan)

        self.linejenislaporan = QLineEdit(self.formLayoutWidget)
        self.linejenislaporan.setObjectName(u"linejenislaporan")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.linejenislaporan)

        self.Deskripsi = QLabel(self.formLayoutWidget)
        self.Deskripsi.setObjectName(u"Deskripsi")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.Deskripsi)

        self.linedeskripsi = QLineEdit(self.formLayoutWidget)
        self.linedeskripsi.setObjectName(u"linedeskripsi")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.linedeskripsi)

        self.iduser = QLabel(self.formLayoutWidget)
        self.iduser.setObjectName(u"iduser")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.iduser)

        self.lineiduser = QLineEdit(self.formLayoutWidget)
        self.lineiduser.setObjectName(u"lineiduser")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.lineiduser)

        self.btnSimpan = QPushButton(self.formLayoutWidget)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.btnSimpan)

        self.btnUbah = QPushButton(self.formLayoutWidget)
        self.btnUbah.setObjectName(u"btnUbah")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.btnUbah)

        self.btnHapus = QPushButton(self.formLayoutWidget)
        self.btnHapus.setObjectName(u"btnHapus")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.btnHapus)

        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(250, 10, 211, 20))
        self.tblLaporan = QTableWidget(Form)
        if (self.tblLaporan.columnCount() < 6):
            self.tblLaporan.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblLaporan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblLaporan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblLaporan.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblLaporan.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblLaporan.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblLaporan.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tblLaporan.setObjectName(u"tblLaporan")
        self.tblLaporan.setGeometry(QRect(250, 40, 431, 192))
        self.formLayoutWidget_2 = QWidget(Form)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(250, 240, 271, 80))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.FillterDatalabel = QLabel(self.formLayoutWidget_2)
        self.FillterDatalabel.setObjectName(u"FillterDatalabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.FillterDatalabel)

        self.comboFillter = QComboBox(self.formLayoutWidget_2)
        self.comboFillter.addItem("")
        self.comboFillter.setObjectName(u"comboFillter")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboFillter)

        self.btnCetak = QPushButton(self.formLayoutWidget_2)
        self.btnCetak.setObjectName(u"btnCetak")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.btnCetak)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.id_Laporan.setText(QCoreApplication.translate("Form", u"Id Laporan", None))
        self.Judul_Laporan.setText(QCoreApplication.translate("Form", u"Judul Laporan", None))
        self.Lokasi_Laporan.setText(QCoreApplication.translate("Form", u"Lokasi Laporan", None))
        self.Jenis_Laporan.setText(QCoreApplication.translate("Form", u"Jenis Laporan", None))
        self.Deskripsi.setText(QCoreApplication.translate("Form", u"Deskripsi", None))
        self.iduser.setText(QCoreApplication.translate("Form", u"Id User", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        ___qtablewidgetitem = self.tblLaporan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Id Laporan", None));
        ___qtablewidgetitem1 = self.tblLaporan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Judul Laporan", None));
        ___qtablewidgetitem2 = self.tblLaporan.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Lokasi Laporan", None));
        ___qtablewidgetitem3 = self.tblLaporan.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Jenis Laporan", None));
        ___qtablewidgetitem4 = self.tblLaporan.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Deskripsi", None));
        ___qtablewidgetitem5 = self.tblLaporan.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Id User", None));
        self.FillterDatalabel.setText(QCoreApplication.translate("Form", u"Fillter Data", None))
        self.comboFillter.setItemText(0, QCoreApplication.translate("Form", u"Semua", None))

        self.btnCetak.setText(QCoreApplication.translate("Form", u"Cetak", None))
    # retranslateUi

