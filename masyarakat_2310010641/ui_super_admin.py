# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'super_admin.ui'
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
        Form.resize(525, 332)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 211, 201))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.idSuperAdminLabel = QLabel(self.formLayoutWidget)
        self.idSuperAdminLabel.setObjectName(u"idSuperAdminLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.idSuperAdminLabel)

        self.idSuperAdminLineEdit = QLineEdit(self.formLayoutWidget)
        self.idSuperAdminLineEdit.setObjectName(u"idSuperAdminLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.idSuperAdminLineEdit)

        self.usernamaLabel = QLabel(self.formLayoutWidget)
        self.usernamaLabel.setObjectName(u"usernamaLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.usernamaLabel)

        self.usernamaLineEdit = QLineEdit(self.formLayoutWidget)
        self.usernamaLineEdit.setObjectName(u"usernamaLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.usernamaLineEdit)

        self.passwordLabel = QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.passwordLabel)

        self.passwordLineEdit = QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.passwordLineEdit)

        self.btnsimpan = QPushButton(self.formLayoutWidget)
        self.btnsimpan.setObjectName(u"btnsimpan")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.btnsimpan)

        self.btnubah = QPushButton(self.formLayoutWidget)
        self.btnubah.setObjectName(u"btnubah")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.btnubah)

        self.btnhapus = QPushButton(self.formLayoutWidget)
        self.btnhapus.setObjectName(u"btnhapus")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.btnhapus)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(230, 20, 221, 20))
        self.tblsuperadmin = QTableWidget(Form)
        if (self.tblsuperadmin.columnCount() < 3):
            self.tblsuperadmin.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblsuperadmin.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblsuperadmin.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblsuperadmin.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tblsuperadmin.setObjectName(u"tblsuperadmin")
        self.tblsuperadmin.setGeometry(QRect(230, 50, 231, 192))
        self.formLayoutWidget_2 = QWidget(Form)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(230, 250, 211, 80))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fillterDataLabel = QLabel(self.formLayoutWidget_2)
        self.fillterDataLabel.setObjectName(u"fillterDataLabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.fillterDataLabel)

        self.comboFillterdata = QComboBox(self.formLayoutWidget_2)
        self.comboFillterdata.addItem("")
        self.comboFillterdata.setObjectName(u"comboFillterdata")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboFillterdata)

        self.btncetak = QPushButton(self.formLayoutWidget_2)
        self.btncetak.setObjectName(u"btncetak")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.btncetak)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.idSuperAdminLabel.setText(QCoreApplication.translate("Form", u"Id Super Admin", None))
        self.usernamaLabel.setText(QCoreApplication.translate("Form", u"Username", None))
        self.passwordLabel.setText(QCoreApplication.translate("Form", u"Password", None))
        self.btnsimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnubah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnhapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        ___qtablewidgetitem = self.tblsuperadmin.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Id Super Admin", None));
        ___qtablewidgetitem1 = self.tblsuperadmin.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Username", None));
        ___qtablewidgetitem2 = self.tblsuperadmin.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Password", None));
        self.fillterDataLabel.setText(QCoreApplication.translate("Form", u"Fillter Data", None))
        self.comboFillterdata.setItemText(0, QCoreApplication.translate("Form", u"Semua", None))

        self.btncetak.setText(QCoreApplication.translate("Form", u"Cetak", None))
    # retranslateUi

