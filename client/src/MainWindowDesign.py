# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import res_rc
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(600, 400)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(210, 20, 181, 171))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap(":/icon/icons/mai_logo.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 200, 481, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.recogniseButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recogniseButton.sizePolicy().hasHeightForWidth())
        self.recogniseButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.recogniseButton.setFont(font)
        self.recogniseButton.setStyleSheet("QPushButton {\n"
                                           "    background-color:  rgb(4, 128, 183);\n"
                                           "    color:  rgb(255, 255, 255);\n"
                                           "    font-size:  14px;\n"
                                           "    font-weight: bold;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color:  rgba(4, 128, 183, 200);\n"
                                           "}")
        self.recogniseButton.setObjectName("recogniseButton")
        self.verticalLayout.addWidget(self.recogniseButton)
        self.resultButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultButton.sizePolicy().hasHeightForWidth())
        self.resultButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.resultButton.setFont(font)
        self.resultButton.setStyleSheet("QPushButton {\n"
                                        "    background-color:  rgb(4, 128, 183);\n"
                                        "    color:  rgb(255, 255, 255);\n"
                                        "    font-size:  14px;\n"
                                        "    font-weight: bold;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color:  rgba(4, 128, 183, 200);\n"
                                        "}")
        self.resultButton.setObjectName("resultButton")
        self.verticalLayout.addWidget(self.resultButton)
        self.loadToServButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadToServButton.sizePolicy().hasHeightForWidth())
        self.loadToServButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.loadToServButton.setFont(font)
        self.loadToServButton.setStyleSheet("QPushButton {\n"
                                            "    background-color:  rgb(4, 128, 183);\n"
                                            "    color:  rgb(255, 255, 255);\n"
                                            "    font-size:  14px;\n"
                                            "    font-weight: bold;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color:  rgba(4, 128, 183, 200);\n"
                                            "}")
        self.loadToServButton.setObjectName("loadToServButton")
        self.verticalLayout.addWidget(self.loadToServButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TableRecogniser"))
        self.recogniseButton.setText(_translate("MainWindow", "Распознать"))
        self.resultButton.setText(_translate("MainWindow", "Результат"))
        self.loadToServButton.setText(_translate("MainWindow", "Загрузить на сервер"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
