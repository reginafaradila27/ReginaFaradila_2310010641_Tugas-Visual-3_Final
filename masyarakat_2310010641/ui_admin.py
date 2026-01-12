# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
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
        Form.resize(624, 313)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 251, 261))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.idadmin = QLabel(self.formLayoutWidget)
        self.idadmin.setObjectName(u"idadmin")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.idadmin)

        self.idadminLineEdit = QLineEdit(self.formLayoutWidget)
        self.idadminLineEdit.setObjectName(u"idadminLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.idadminLineEdit)

        self.Nama = QLabel(self.formLayoutWidget)
        self.Nama.setObjectName(u"Nama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.Nama)

        self.namaLineEdit = QLineEdit(self.formLayoutWidget)
        self.namaLineEdit.setObjectName(u"namaLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.namaLineEdit)

        self.password = QLabel(self.formLayoutWidget)
        self.password.setObjectName(u"password")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.password)

        self.passwordLineEdit = QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.passwordLineEdit)

        self.kelurahan = QLabel(self.formLayoutWidget)
        self.kelurahan.setObjectName(u"kelurahan")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.kelurahan)

        self.kelurahanLineEdit = QLineEdit(self.formLayoutWidget)
        self.kelurahanLineEdit.setObjectName(u"kelurahanLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.kelurahanLineEdit)

        self.btnSimpan = QPushButton(self.formLayoutWidget)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.btnSimpan)

        self.btnHapus = QPushButton(self.formLayoutWidget)
        self.btnHapus.setObjectName(u"btnHapus")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.btnHapus)

        self.btnUbah = QPushButton(self.formLayoutWidget)
        self.btnUbah.setObjectName(u"btnUbah")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.btnUbah)

        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(280, 20, 201, 20))
        self.tblAdmin = QTableWidget(Form)
        if (self.tblAdmin.columnCount() < 4):
            self.tblAdmin.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblAdmin.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblAdmin.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblAdmin.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblAdmin.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tblAdmin.setObjectName(u"tblAdmin")
        self.tblAdmin.setGeometry(QRect(280, 50, 301, 181))
        self.formLayoutWidget_2 = QWidget(Form)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(280, 240, 231, 81))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.fillterDataLabel = QLabel(self.formLayoutWidget_2)
        self.fillterDataLabel.setObjectName(u"fillterDataLabel")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.fillterDataLabel)

        self.comboFillter = QComboBox(self.formLayoutWidget_2)
        self.comboFillter.addItem("")
        self.comboFillter.setObjectName(u"comboFillter")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboFillter)

        self.btnCetak = QPushButton(self.formLayoutWidget_2)
        self.btnCetak.setObjectName(u"btnCetak")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.btnCetak)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.idadmin.setText(QCoreApplication.translate("Form", u"Id Admin", None))
        self.Nama.setText(QCoreApplication.translate("Form", u"Nama", None))
        self.password.setText(QCoreApplication.translate("Form", u"Password", None))
        self.kelurahan.setText(QCoreApplication.translate("Form", u"Kelurahan", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        ___qtablewidgetitem = self.tblAdmin.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Id Admin ", None));
        ___qtablewidgetitem1 = self.tblAdmin.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama", None));
        ___qtablewidgetitem2 = self.tblAdmin.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Password", None));
        ___qtablewidgetitem3 = self.tblAdmin.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Kelurahan", None));
        self.fillterDataLabel.setText(QCoreApplication.translate("Form", u"Fillter Data", None))
        self.comboFillter.setItemText(0, QCoreApplication.translate("Form", u"Semua", None))

        self.btnCetak.setText(QCoreApplication.translate("Form", u"Cetak", None))
    # retranslateUi

