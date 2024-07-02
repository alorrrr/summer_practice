from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
import sys
import ui
import cv2 as cv


class MainWindow(QtWidgets.QMainWindow, ui.Ui_mainWindow):
    """Class for main window"""
    def __init__(self):
        """Init function"""
        super().__init__()
        self.image = None
        self.setupUi(self)

        self.takePhoto.clicked.connect(self.take_photo)
        self.uploadPhoto.clicked.connect(self.upload_photo)
        self.showRedChannel.clicked.connect(lambda: self.show_channel(2))
        self.showBlueChannel.clicked.connect(lambda: self.show_channel(0))
        self.showGreenChannel.clicked.connect(lambda: self.show_channel(1))
        self.averageImage.clicked.connect(self.average_image)
        self.grayPhoto.clicked.connect(self.gray_photo)
        self.drawOnPhoto.clicked.connect(self.draw_on_photo)

    def take_photo(self):
        cam_port = 0
        cam = cv.VideoCapture(cam_port)
        result, self.image = cam.read()
        if result:
            cv.imshow("Image", self.image)
            cv.imwrite("image.png", self.image)
            msg = QMessageBox()
            msg.setText("Фото сделано и сохранено!")
            msg.setWindowTitle("Информация")
            msg.exec_()
            pixmap = QtGui.QPixmap("image.png")
            self.label.setPixmap(pixmap)
            self.label.setAlignment(Qt.AlignCenter)
        else:
            show_error("Проверьте подключение камеры!")

    def upload_photo(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Открыть файл", "", "Изображения (*.jpg *.png)")
        if file_path:
            self.image = cv.imread(file_path)
            cv.imshow("Image", self.image)
            pixmap = QtGui.QPixmap(file_path)
            self.label.setPixmap(pixmap)
            self.label.setAlignment(Qt.AlignCenter)

    def show_channel(self, channel):
        if self.image is not None:
            cv.imshow("Image", self.image[:, :, channel])
        else:
            show_error("Сначала нужно загрузить изображение или сделать снимок!")

    def average_image(self):
        if self.image is not None:
            widget = Form()
            widget.exec_()
            blurred = cv.blur(self.image, (kernel_size[-1], kernel_size[-1]))
            cv.imshow("Image", blurred)
        else:
            show_error("Сначала нужно загрузить изображение или сделать снимок!")

    def gray_photo(self):
        if self.image is not None:
            gray_image = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
            cv.imshow("Image", gray_image)
        else:
            show_error("Сначала нужно загрузить изображение или сделать снимок!")

    def draw_on_photo(self):
        if self.image is not None:
            widget = RectangleForm()
            widget.exec_()
            if widget.valid:
                output = self.image.copy()
                cv.rectangle(output, coord_left_up[-1], coord_right_down[-1], (255, 0, 0), 10)
                cv.imshow("Image", output)
        else:
            show_error("Сначала нужно загрузить изображение или сделать снимок!")

class Form(QtWidgets.QDialog, ui.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.set_kernel_size)

    def set_kernel_size(self):
        try:
            number = int(self.textEdit.toPlainText())
            if number > 0:
                kernel_size.append(number)
                self.close()
            else:
                raise ValueError
        except ValueError:
            show_error("Введите число>1!")

class RectangleForm(QtWidgets.QDialog, ui.Ui_DialogRectangle):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.valid = False

        self.pushButton.clicked.connect(self.set_coordinates)

    def set_coordinates(self):
        try:
            left_up = tuple(int(x) for x in (self.textEdit.toPlainText()).split())
            right_down = tuple(int(x) for x in (self.textEdit1.toPlainText()).split())
            if len(left_up) != 2 or len(right_down) != 2:
                raise ValueError
            if any(coord < 0 or coord > 1000 for coord in left_up) or any(
                    coord < 0 or coord > 1000 for coord in right_down):
                show_error("Координаты должны быть в диапазоне от 0 до 1000!")
            else:
                self.valid = True
                coord_left_up.append(left_up)
                coord_right_down.append(right_down)
                self.close()
        except ValueError:
            show_error("Введите правильные значения!")

def show_error(message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Ошибка. " + message)
    msg.setWindowTitle("Ошибка")
    msg.exec_()

if __name__ == "__main__":
    kernel_size = []
    coord_left_up = []
    coord_right_down = []
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
