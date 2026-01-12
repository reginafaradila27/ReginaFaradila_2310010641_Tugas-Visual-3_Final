# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kelurahan.ui'
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
        Form.resize(579, 326)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 251, 261))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.IdKelurahan = QLabel(self.formLayoutWidget)
        self.IdKelurahan.setObjectName(u"IdKelurahan")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.IdKelurahan)

        self.Id_Kelurahan = QLineEdit(self.formLayoutWidget)
        self.Id_Kelurahan.setObjectName(u"Id_Kelurahan")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.Id_Kelurahan)

        self.NamaKelurahan = QLabel(self.formLayoutWidget)
        self.NamaKelurahan.setObjectName(u"NamaKelurahan")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.NamaKelurahan)

        self.Nama_Kelurahan = QLineEdit(self.formLayoutWidget)
        self.Nama_Kelurahan.setObjectName(u"Nama_Kelurahan")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.Nama_Kelurahan)

        self.IdLurah = QLabel(self.formLayoutWidget)
        self.IdLurah.setObjectName(u"IdLurah")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.IdLurah)

        self.Id_Lurah = QLineEdit(self.formLayoutWidget)
        self.Id_Lurah.setObjectName(u"Id_Lurah")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.Id_Lurah)

        self.btnSimpan = QPushButton(self.formLayoutWidget)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.btnSimpan)

        self.btnUbah = QPushButton(self.formLayoutWidget)
        self.btnUbah.setObjectName(u"btnUbah")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.btnUbah)

        self.btnHapus = QPushButton(self.formLayoutWidget)
        self.btnHapus.setObjectName(u"btnHapus")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.btnHapus)

        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(320, 10, 113, 20))
        self.tblKelurahan = QTableWidget(Form)
        if (self.tblKelurahan.columnCount() < 3):
            self.tblKelurahan.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblKelurahan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblKelurahan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblKelurahan.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tblKelurahan.setObjectName(u"tblKelurahan")
        self.tblKelurahan.setGeometry(QRect(270, 50, 256, 192))
        self.formLayoutWidget_2 = QWidget(Form)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(270, 250, 231, 80))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.FillterData = QLabel(self.formLayoutWidget_2)
        self.FillterData.setObjectName(u"FillterData")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.FillterData)

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
        self.IdKelurahan.setText(QCoreApplication.translate("Form", u"Id Kelurahan", None))
        self.NamaKelurahan.setText(QCoreApplication.translate("Form", u"Nama Kelurahan", None))
        self.IdLurah.setText(QCoreApplication.translate("Form", u"Id Lurah", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        ___qtablewidgetitem = self.tblKelurahan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Id Kelurahan", None));
        ___qtablewidgetitem1 = self.tblKelurahan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Kelurahan", None));
        ___qtablewidgetitem2 = self.tblKelurahan.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Id Lurah", None));
        self.FillterData.setText(QCoreApplication.translate("Form", u"Fillter Data", None))
        self.comboFillter.setItemText(0, QCoreApplication.translate("Form", u"Semua", None))

        self.btnCetak.setText(QCoreApplication.translate("Form", u"Cetak", None))
    # retranslateUi

