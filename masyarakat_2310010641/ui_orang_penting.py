# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orang_penting.ui'
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
        Form.resize(646, 365)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 221, 261))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.Orang_Penting = QLabel(self.formLayoutWidget)
        self.Orang_Penting.setObjectName(u"Orang_Penting")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.Orang_Penting)

        self.lineidOrang_Penting = QLineEdit(self.formLayoutWidget)
        self.lineidOrang_Penting.setObjectName(u"lineidOrang_Penting")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineidOrang_Penting)

        self.nama = QLabel(self.formLayoutWidget)
        self.nama.setObjectName(u"nama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.nama)

        self.linenama = QLineEdit(self.formLayoutWidget)
        self.linenama.setObjectName(u"linenama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.linenama)

        self.jabatan = QLabel(self.formLayoutWidget)
        self.jabatan.setObjectName(u"jabatan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.jabatan)

        self.linejabatan = QLineEdit(self.formLayoutWidget)
        self.linejabatan.setObjectName(u"linejabatan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.linejabatan)

        self.nohp = QLabel(self.formLayoutWidget)
        self.nohp.setObjectName(u"nohp")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.nohp)

        self.linenohp = QLineEdit(self.formLayoutWidget)
        self.linenohp.setObjectName(u"linenohp")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.linenohp)

        self.idkelurahan = QLabel(self.formLayoutWidget)
        self.idkelurahan.setObjectName(u"idkelurahan")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.idkelurahan)

        self.lineidkelurahan = QLineEdit(self.formLayoutWidget)
        self.lineidkelurahan.setObjectName(u"lineidkelurahan")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.lineidkelurahan)

        self.btnsimpan = QPushButton(self.formLayoutWidget)
        self.btnsimpan.setObjectName(u"btnsimpan")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.btnsimpan)

        self.btnubah = QPushButton(self.formLayoutWidget)
        self.btnubah.setObjectName(u"btnubah")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.btnubah)

        self.btnhapus = QPushButton(self.formLayoutWidget)
        self.btnhapus.setObjectName(u"btnhapus")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.btnhapus)

        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(250, 10, 221, 20))
        self.tblOrang_Penting = QTableWidget(Form)
        if (self.tblOrang_Penting.columnCount() < 5):
            self.tblOrang_Penting.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblOrang_Penting.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblOrang_Penting.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblOrang_Penting.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblOrang_Penting.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblOrang_Penting.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tblOrang_Penting.setObjectName(u"tblOrang_Penting")
        self.tblOrang_Penting.setGeometry(QRect(250, 40, 381, 192))
        self.formLayoutWidget_2 = QWidget(Form)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(250, 240, 261, 80))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelFillterData = QLabel(self.formLayoutWidget_2)
        self.labelFillterData.setObjectName(u"labelFillterData")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelFillterData)

        self.comboFillterData = QComboBox(self.formLayoutWidget_2)
        self.comboFillterData.addItem("")
        self.comboFillterData.setObjectName(u"comboFillterData")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboFillterData)

        self.btncetak = QPushButton(self.formLayoutWidget_2)
        self.btncetak.setObjectName(u"btncetak")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.btncetak)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Orang_Penting.setText(QCoreApplication.translate("Form", u"Id Orang_Penting", None))
        self.nama.setText(QCoreApplication.translate("Form", u"Nama", None))
        self.jabatan.setText(QCoreApplication.translate("Form", u"Jabatan", None))
        self.nohp.setText(QCoreApplication.translate("Form", u"No Hp", None))
        self.idkelurahan.setText(QCoreApplication.translate("Form", u"Id Kelurahan", None))
        self.btnsimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnubah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnhapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        ___qtablewidgetitem = self.tblOrang_Penting.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Id Orang_Penting", None));
        ___qtablewidgetitem1 = self.tblOrang_Penting.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama", None));
        ___qtablewidgetitem2 = self.tblOrang_Penting.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Jabatan", None));
        ___qtablewidgetitem3 = self.tblOrang_Penting.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"No Hp", None));
        ___qtablewidgetitem4 = self.tblOrang_Penting.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Id Kelurahan", None));
        self.labelFillterData.setText(QCoreApplication.translate("Form", u"Fillter Data", None))
        self.comboFillterData.setItemText(0, QCoreApplication.translate("Form", u"Semua", None))

        self.btncetak.setText(QCoreApplication.translate("Form", u"Cetak", None))
    # retranslateUi

