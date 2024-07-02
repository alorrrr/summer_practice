import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.takePhoto = QtWidgets.QPushButton(self.centralwidget)
        self.takePhoto.setObjectName("takePhoto")
        self.verticalLayout.addWidget(self.takePhoto)
        self.uploadPhoto = QtWidgets.QPushButton(self.centralwidget)
        self.uploadPhoto.setObjectName("uploadPhoto")
        self.verticalLayout.addWidget(self.uploadPhoto)
        self.showRedChannel = QtWidgets.QPushButton(self.centralwidget)
        self.showRedChannel.setObjectName("showRedChannel")
        self.verticalLayout.addWidget(self.showRedChannel)
        self.showBlueChannel = QtWidgets.QPushButton(self.centralwidget)
        self.showBlueChannel.setObjectName("showBlueChannel")
        self.verticalLayout.addWidget(self.showBlueChannel)
        self.showGreenChannel = QtWidgets.QPushButton(self.centralwidget)
        self.showGreenChannel.setObjectName("showGreenChannel")
        self.verticalLayout.addWidget(self.showGreenChannel)
        self.averageImage = QtWidgets.QPushButton(self.centralwidget)
        self.averageImage.setObjectName("averageImage")
        self.verticalLayout.addWidget(self.averageImage)
        self.grayPhoto = QtWidgets.QPushButton(self.centralwidget)
        self.grayPhoto.setObjectName("grayPhoto")
        self.verticalLayout.addWidget(self.grayPhoto)
        self.drawOnPhoto = QtWidgets.QPushButton(self.centralwidget)
        self.drawOnPhoto.setObjectName("drawOnPhoto")
        self.verticalLayout.addWidget(self.drawOnPhoto)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Main"))
        self.takePhoto.setText(_translate("mainWindow", "Сделать фото"))
        self.uploadPhoto.setText(_translate("mainWindow", "Загрузить фото"))
        self.showRedChannel.setText(_translate("mainWindow", "Показать красный канал"))
        self.showBlueChannel.setText(_translate("mainWindow", "Показать синий канал"))
        self.showGreenChannel.setText(_translate("mainWindow", "Показать зеленый канал"))
        self.averageImage.setText(_translate("mainWindow", "Усреднить изображение"))
        self.grayPhoto.setText(_translate("mainWindow", "Показать изображение в серых оттенках"))
        self.drawOnPhoto.setText(_translate("mainWindow", "Нарисовать синий прямоугольник"))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Введите размер ядра:"))
        self.pushButton.setText(_translate("Dialog", "Ок"))


class Ui_DialogRectangle(object):
    def setupUi(self, DialogRectangle):
        DialogRectangle.setObjectName("DialogRectangle")
        DialogRectangle.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogRectangle)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(DialogRectangle)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(DialogRectangle)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.label1 = QtWidgets.QLabel(DialogRectangle)
        self.label1.setObjectName("label1")
        self.verticalLayout.addWidget(self.label1)
        self.textEdit1 = QtWidgets.QTextEdit(DialogRectangle)
        self.textEdit1.setObjectName("textEdit1")
        self.verticalLayout.addWidget(self.textEdit1)
        self.pushButton = QtWidgets.QPushButton(DialogRectangle)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(DialogRectangle)
        QtCore.QMetaObject.connectSlotsByName(DialogRectangle)

    def retranslateUi(self, DialogRectangle):
        _translate = QtCore.QCoreApplication.translate
        DialogRectangle.setWindowTitle(_translate("DialogRectangle", "Dialog"))
        self.label.setText(_translate("DialogRectangle", "Введите координату верхнего левого угла x y через пробел:"))
        self.label1.setText(_translate("DialogRectangle", "Введите координату нижнего правого угла x y через пробел:"))
        self.pushButton.setText(_translate("DialogRectangle", "Ок"))
