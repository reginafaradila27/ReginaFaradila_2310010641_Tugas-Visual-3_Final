# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionData_Admin = QAction(MainWindow)
        self.actionData_Admin.setObjectName(u"actionData_Admin")
        self.actionData_Agenda = QAction(MainWindow)
        self.actionData_Agenda.setObjectName(u"actionData_Agenda")
        self.actionData_Kelurahan = QAction(MainWindow)
        self.actionData_Kelurahan.setObjectName(u"actionData_Kelurahan")
        self.actionData_Laporan = QAction(MainWindow)
        self.actionData_Laporan.setObjectName(u"actionData_Laporan")
        self.actionData_Orang_Penting = QAction(MainWindow)
        self.actionData_Orang_Penting.setObjectName(u"actionData_Orang_Penting")
        self.actionData_Proses = QAction(MainWindow)
        self.actionData_Proses.setObjectName(u"actionData_Proses")
        self.actionData_Super_Admin = QAction(MainWindow)
        self.actionData_Super_Admin.setObjectName(u"actionData_Super_Admin")
        self.actionData_User = QAction(MainWindow)
        self.actionData_User.setObjectName(u"actionData_User")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 18))
        self.menuMenu_Utama = QMenu(self.menubar)
        self.menuMenu_Utama.setObjectName(u"menuMenu_Utama")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu_Utama.menuAction())
        self.menuMenu_Utama.addSeparator()
        self.menuMenu_Utama.addSeparator()
        self.menuMenu_Utama.addAction(self.actionData_Admin)
        self.menuMenu_Utama.addAction(self.actionData_Agenda)
        self.menuMenu_Utama.addAction(self.actionData_Kelurahan)
        self.menuMenu_Utama.addAction(self.actionData_Laporan)
        self.menuMenu_Utama.addAction(self.actionData_Orang_Penting)
        self.menuMenu_Utama.addAction(self.actionData_Proses)
        self.menuMenu_Utama.addAction(self.actionData_Super_Admin)
        self.menuMenu_Utama.addAction(self.actionData_User)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionData_Admin.setText(QCoreApplication.translate("MainWindow", u"Data Admin", None))
        self.actionData_Agenda.setText(QCoreApplication.translate("MainWindow", u"Data Agenda", None))
        self.actionData_Kelurahan.setText(QCoreApplication.translate("MainWindow", u"Data Kelurahan", None))
        self.actionData_Laporan.setText(QCoreApplication.translate("MainWindow", u"Data Laporan ", None))
        self.actionData_Orang_Penting.setText(QCoreApplication.translate("MainWindow", u"Data Orang_Penting", None))
        self.actionData_Proses.setText(QCoreApplication.translate("MainWindow", u"Data Proses", None))
        self.actionData_Super_Admin.setText(QCoreApplication.translate("MainWindow", u"Data Super_Admin", None))
        self.actionData_User.setText(QCoreApplication.translate("MainWindow", u"Data User", None))
        self.menuMenu_Utama.setTitle(QCoreApplication.translate("MainWindow", u"Menu Utama", None))
    # retranslateUi

