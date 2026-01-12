# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user.ui'
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
        Form.resize(719, 328)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 231, 202))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.idUserLabel = QLabel(self.formLayoutWidget)
        self.idUserLabel.setObjectName(u"idUserLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.idUserLabel)

        self.idUserLineEdit = QLineEdit(self.formLayoutWidget)
        self.idUserLineEdit.setObjectName(u"idUserLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.idUserLineEdit)

        self.usernameLabel = QLabel(self.formLayoutWidget)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.usernameLabel)

        self.usernameLineEdit = QLineEdit(self.formLayoutWidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.usernameLineEdit)

        self.emailLabel = QLabel(self.formLayoutWidget)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.emailLabel)

        self.emailLineEdit = QLineEdit(self.formLayoutWidget)
        self.emailLineEdit.setObjectName(u"emailLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.emailLineEdit)

        self.passwordLabel = QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.passwordLabel)

        self.passwordLineEdit = QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.passwordLineEdit)

        self.alamatLabel = QLabel(self.formLayoutWidget)
        self.alamatLabel.setObjectName(u"alamatLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.alamatLabel)

        self.alamatLineEdit = QLineEdit(self.formLayoutWidget)
        self.alamatLineEdit.setObjectName(u"alamatLineEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.alamatLineEdit)

        self.idKelurahanLabel = QLabel(self.formLayoutWidget)
        self.idKelurahanLabel.setObjectName(u"idKelurahanLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.idKelurahanLabel)

        self.idKelurahanLineEdit = QLineEdit(self.formLayoutWidget)
        self.idKelurahanLineEdit.setObjectName(u"idKelurahanLineEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.idKelurahanLineEdit)

        self.pushButton = QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.pushButton)

        self.pushButton_2 = QPushButton(self.formLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.pushButton_2)

        self.pushButton_3 = QPushButton(self.formLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.pushButton_3)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(250, 10, 113, 20))
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(250, 40, 441, 192))
        self.formLayoutWidget_2 = QWidget(Form)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(250, 240, 160, 80))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fillterDataLabel = QLabel(self.formLayoutWidget_2)
        self.fillterDataLabel.setObjectName(u"fillterDataLabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.fillterDataLabel)

        self.comboBox = QComboBox(self.formLayoutWidget_2)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboBox)

        self.pushButton_4 = QPushButton(self.formLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.pushButton_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.idUserLabel.setText(QCoreApplication.translate("Form", u"Id User", None))
        self.usernameLabel.setText(QCoreApplication.translate("Form", u"Username", None))
        self.emailLabel.setText(QCoreApplication.translate("Form", u"Email", None))
        self.passwordLabel.setText(QCoreApplication.translate("Form", u"Password", None))
        self.alamatLabel.setText(QCoreApplication.translate("Form", u"Alamat", None))
        self.idKelurahanLabel.setText(QCoreApplication.translate("Form", u"Id Kelurahan", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Id User", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Username", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Email", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Password", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Alamat", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Id Kelurahan", None));
        self.fillterDataLabel.setText(QCoreApplication.translate("Form", u"Fillter Data", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Semua", None))

        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Cetak", None))
    # retranslateUi

