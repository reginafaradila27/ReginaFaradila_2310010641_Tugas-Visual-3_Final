# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agenda.ui'
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
        Form.resize(546, 339)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 211, 221))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.id_agenda = QLabel(self.formLayoutWidget)
        self.id_agenda.setObjectName(u"id_agenda")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.id_agenda)

        self.idAgendaLineEdit = QLineEdit(self.formLayoutWidget)
        self.idAgendaLineEdit.setObjectName(u"idAgendaLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.idAgendaLineEdit)

        self.judul = QLabel(self.formLayoutWidget)
        self.judul.setObjectName(u"judul")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.judul)

        self.judulLineEdit = QLineEdit(self.formLayoutWidget)
        self.judulLineEdit.setObjectName(u"judulLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.judulLineEdit)

        self.tanggal_terselenggara = QLabel(self.formLayoutWidget)
        self.tanggal_terselenggara.setObjectName(u"tanggal_terselenggara")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.tanggal_terselenggara)

        self.tanggal_terselenggaraLineEdit = QLineEdit(self.formLayoutWidget)
        self.tanggal_terselenggaraLineEdit.setObjectName(u"tanggal_terselenggaraLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.tanggal_terselenggaraLineEdit)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.id_kelurahan = QLabel(self.formLayoutWidget)
        self.id_kelurahan.setObjectName(u"id_kelurahan")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.id_kelurahan)

        self.idkelurahanLineEdit = QLineEdit(self.formLayoutWidget)
        self.idkelurahanLineEdit.setObjectName(u"idkelurahanLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.idkelurahanLineEdit)

        self.btnSimpan = QPushButton(self.formLayoutWidget)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.btnSimpan)

        self.btnHapus = QPushButton(self.formLayoutWidget)
        self.btnHapus.setObjectName(u"btnHapus")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.btnHapus)

        self.btnUbah = QPushButton(self.formLayoutWidget)
        self.btnUbah.setObjectName(u"btnUbah")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.btnUbah)

        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(230, 20, 113, 20))
        self.tblAgenda = QTableWidget(Form)
        if (self.tblAgenda.columnCount() < 4):
            self.tblAgenda.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblAgenda.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblAgenda.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblAgenda.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblAgenda.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tblAgenda.setObjectName(u"tblAgenda")
        self.tblAgenda.setGeometry(QRect(230, 50, 291, 192))
        self.formLayoutWidget_2 = QWidget(Form)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(230, 250, 251, 80))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.FillterDataLabel = QLabel(self.formLayoutWidget_2)
        self.FillterDataLabel.setObjectName(u"FillterDataLabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.FillterDataLabel)

        self.comboFillter = QComboBox(self.formLayoutWidget_2)
        self.comboFillter.addItem("")
        self.comboFillter.setObjectName(u"comboFillter")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboFillter)

        self.btnCetak = QPushButton(self.formLayoutWidget_2)
        self.btnCetak.setObjectName(u"btnCetak")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.btnCetak)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.id_agenda.setText(QCoreApplication.translate("Form", u"Id Agenda", None))
        self.judul.setText(QCoreApplication.translate("Form", u"Judul", None))
        self.tanggal_terselenggara.setText(QCoreApplication.translate("Form", u"Tanggal Terselenggara", None))
        self.label_4.setText("")
        self.id_kelurahan.setText(QCoreApplication.translate("Form", u"Id Kelurahan", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        ___qtablewidgetitem = self.tblAgenda.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Id Agenda", None));
        ___qtablewidgetitem1 = self.tblAgenda.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Judul", None));
        ___qtablewidgetitem2 = self.tblAgenda.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"New Column", None));
        ___qtablewidgetitem3 = self.tblAgenda.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Id Kelurahan", None));
        self.FillterDataLabel.setText(QCoreApplication.translate("Form", u"Fillter Data", None))
        self.comboFillter.setItemText(0, QCoreApplication.translate("Form", u"Semua", None))

        self.btnCetak.setText(QCoreApplication.translate("Form", u"Cetak", None))
    # retranslateUi

