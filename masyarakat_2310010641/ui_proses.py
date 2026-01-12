# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proses.ui'
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
        Form.resize(625, 334)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 241, 221))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.idproses = QLabel(self.formLayoutWidget)
        self.idproses.setObjectName(u"idproses")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.idproses)

        self.lineidproses = QLineEdit(self.formLayoutWidget)
        self.lineidproses.setObjectName(u"lineidproses")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineidproses)

        self.jenissurat = QLabel(self.formLayoutWidget)
        self.jenissurat.setObjectName(u"jenissurat")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.jenissurat)

        self.linejenissurat = QLineEdit(self.formLayoutWidget)
        self.linejenissurat.setObjectName(u"linejenissurat")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.linejenissurat)

        self.tanggalpengajuan = QLabel(self.formLayoutWidget)
        self.tanggalpengajuan.setObjectName(u"tanggalpengajuan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.tanggalpengajuan)

        self.linetanggalpengajuan = QLineEdit(self.formLayoutWidget)
        self.linetanggalpengajuan.setObjectName(u"linetanggalpengajuan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.linetanggalpengajuan)

        self.proses = QLabel(self.formLayoutWidget)
        self.proses.setObjectName(u"proses")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.proses)

        self.iduser = QLabel(self.formLayoutWidget)
        self.iduser.setObjectName(u"iduser")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.iduser)

        self.lineproses = QLineEdit(self.formLayoutWidget)
        self.lineproses.setObjectName(u"lineproses")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineproses)

        self.lineiduser = QLineEdit(self.formLayoutWidget)
        self.lineiduser.setObjectName(u"lineiduser")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.lineiduser)

        self.btnsimpan = QPushButton(self.formLayoutWidget)
        self.btnsimpan.setObjectName(u"btnsimpan")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.btnsimpan)

        self.btnubah = QPushButton(self.formLayoutWidget)
        self.btnubah.setObjectName(u"btnubah")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.btnubah)

        self.btnhapus = QPushButton(self.formLayoutWidget)
        self.btnhapus.setObjectName(u"btnhapus")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.btnhapus)

        self.linecari = QLineEdit(Form)
        self.linecari.setObjectName(u"linecari")
        self.linecari.setGeometry(QRect(260, 10, 113, 20))
        self.tblproses = QTableWidget(Form)
        if (self.tblproses.columnCount() < 5):
            self.tblproses.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblproses.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblproses.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblproses.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblproses.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblproses.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tblproses.setObjectName(u"tblproses")
        self.tblproses.setGeometry(QRect(260, 40, 361, 192))
        self.formLayoutWidget_2 = QWidget(Form)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(260, 240, 231, 80))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.FillterData = QLabel(self.formLayoutWidget_2)
        self.FillterData.setObjectName(u"FillterData")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.FillterData)

        self.comboFillterData = QComboBox(self.formLayoutWidget_2)
        self.comboFillterData.addItem("")
        self.comboFillterData.setObjectName(u"comboFillterData")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboFillterData)

        self.pushButton_4 = QPushButton(self.formLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.pushButton_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.idproses.setText(QCoreApplication.translate("Form", u"Id Proses", None))
        self.jenissurat.setText(QCoreApplication.translate("Form", u"Jenis Surat", None))
        self.tanggalpengajuan.setText(QCoreApplication.translate("Form", u"Tanggal Pengajuan", None))
        self.proses.setText(QCoreApplication.translate("Form", u"Proses", None))
        self.iduser.setText(QCoreApplication.translate("Form", u"Id User", None))
        self.btnsimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnubah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnhapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        ___qtablewidgetitem = self.tblproses.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Id Proses", None));
        ___qtablewidgetitem1 = self.tblproses.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Jenis Surat", None));
        ___qtablewidgetitem2 = self.tblproses.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Tanggal Pengajuan", None));
        ___qtablewidgetitem3 = self.tblproses.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Proses", None));
        ___qtablewidgetitem4 = self.tblproses.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Id User", None));
        self.FillterData.setText(QCoreApplication.translate("Form", u"Fillter Data", None))
        self.comboFillterData.setItemText(0, QCoreApplication.translate("Form", u"Semua", None))

        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Cetak", None))
    # retranslateUi

