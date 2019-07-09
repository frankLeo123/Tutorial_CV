# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt5demo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
import scipy.misc

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 366)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnOpenCamera = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenCamera.setGeometry(QtCore.QRect(20, 260, 75, 23))
        self.btnOpenCamera.setObjectName("btnOpenCamera")
        self.btnCapture = QtWidgets.QPushButton(self.centralwidget)
        self.btnCapture.setGeometry(QtCore.QRect(170, 260, 75, 23))
        self.btnCapture.setObjectName("btnCapture")
        self.btnReadImage = QtWidgets.QPushButton(self.centralwidget)
        self.btnReadImage.setGeometry(QtCore.QRect(320, 260, 75, 23))
        self.btnReadImage.setObjectName("btnReadImage")
        self.btnGray = QtWidgets.QPushButton(self.centralwidget)
        self.btnGray.setGeometry(QtCore.QRect(490, 260, 75, 23))
        self.btnGray.setObjectName("btnGray")
        self.btnThreshold = QtWidgets.QPushButton(self.centralwidget)
        self.btnThreshold.setGeometry(QtCore.QRect(640, 260, 75, 23))
        self.btnThreshold.setObjectName("btnThreshold")
        self.labelCamera = QtWidgets.QLabel(self.centralwidget)
        self.labelCamera.setGeometry(QtCore.QRect(80, 70, 150, 150))
        self.labelCamera.setObjectName("labelCamera")
        self.labelCapture = QtWidgets.QLabel(self.centralwidget)
        self.labelCapture.setGeometry(QtCore.QRect(320, 60, 150, 150))
        self.labelCapture.setObjectName("labelCapture")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(610, 60, 150, 150))
        self.labelResult.setObjectName("labelResult")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnOpenCamera.clicked.connect(MainWindow.btnOpenCamera_Clicked)
        self.btnCapture.clicked.connect(MainWindow.btnCapture_Clicked)
        self.btnReadImage.clicked.connect(MainWindow.btnReadImage_Clicked)
        self.btnGray.clicked.connect(MainWindow.btnGray_Clicked)
        self.btnThreshold.clicked.connect(MainWindow.btnThreshold_Clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnOpenCamera.setText(_translate("MainWindow", "打开摄像头"))
        self.btnCapture.setText(_translate("MainWindow", "捕获图片"))
        self.btnReadImage.setText(_translate("MainWindow", "打开图片"))
        self.btnGray.setText(_translate("MainWindow", "灰度化"))
        self.btnThreshold.setText(_translate("MainWindow", "阈值分割"))
        self.labelCamera.setText(_translate("MainWindow", "摄像头"))
        self.labelCapture.setText(_translate("MainWindow", "捕获图"))
        self.labelResult.setText(_translate("MainWindow", "结果图"))

class PyQtMainEntry(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.camera = cv2.VideoCapture(1)
        self.is_camera_opened = True  # 摄像头有没有打开标记
        # 定时器：30ms捕获一帧
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self._queryFrame)
        self._timer.setInterval(30)
    def btnOpenCamera_Clicked(self):
        '''
        打开和关闭摄像头
        '''
        self.is_camera_opened = ~self.is_camera_opened
        if self.is_camera_opened:
            self.btnOpenCamera.setText("关闭摄像头")
            self._timer.start()
        else:
            self.btnOpenCamera.setText("打开摄像头")
            self._timer.stop()
    def btnCapture_Clicked(self):
        '''
        捕获图片
        '''
        # 摄像头未打开，不执行任何操作
        # if not self.is_camera_opened:
        #     return
        # self.captured = self.frame
        # 后面这几行代码几乎都一样，可以尝试封装成一个函数
        rows, cols, channels = scipy.misc.face(gray=False).shape
        # rows, cols, channels = self.captured.shape
        bytesPerLine = channels * cols
        # Qt显示图片时，需要先转换成QImgage类型
        QImg = QImage(scipy.misc.face(gray=False), cols, rows, bytesPerLine, QImage.Format_RGB888)
        # QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)
        self.labelCapture.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelCapture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
    def btnReadImage_Clicked(self):
        '''
        从本地读取图片
        '''
        # 打开文件选取对话框
        filename,  _ = QFileDialog.getOpenFileName(self, '打开图片')
        if filename:
            self.captured = cv2.imread(str(filename))
            # OpenCV图像以BGR通道存储，显示时需要从BGR转到RGB
            self.captured = cv2.cvtColor(self.captured, cv2.COLOR_BGR2RGB)
            rows, cols, channels = self.captured.shape
            bytesPerLine = channels * cols
            QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)
            # QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)
            self.labelCapture.setPixmap(QPixmap.fromImage(QImg).scaled(
                self.labelCapture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
    def btnGray_Clicked(self):
        '''
        灰度化
        '''
        # 如果没有捕获图片，则不执行操作
        if not hasattr(self, "captured"):
            return
        self.cpatured = cv2.cvtColor(self.captured, cv2.COLOR_RGB2GRAY)
        rows, columns = self.cpatured.shape
        bytesPerLine = columns
        # 灰度图是单通道，所以需要用Format_Indexed8
        QImg = QImage(self.cpatured.data, columns, rows, bytesPerLine, QImage.Format_Indexed8)
        self.labelResult.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelResult.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
    def btnThreshold_Clicked(self):
        '''
        Otsu自动阈值分割
        '''
        if not hasattr(self, "captured"):
            return
        _, self.cpatured = cv2.threshold(
            self.cpatured, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        rows, columns = self.cpatured.shape
        bytesPerLine = columns
        # 阈值分割图也是单通道，也需要用Format_Indexed8
        QImg = QImage(self.cpatured.data, columns, rows, bytesPerLine, QImage.Format_Indexed8)
        self.labelResult.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelResult.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
    @QtCore.pyqtSlot()
    def _queryFrame(self):
        '''
        循环捕获图片
        '''
        ret, self.frame = self.camera.read()
        img_rows, img_cols, channels = self.frame.shape
        bytesPerLine = channels * img_cols
        cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB, self.frame)
        QImg = QImage(self.frame.data, img_cols, img_rows, bytesPerLine, QImage.Format_RGB888)
        self.labelCamera.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelCamera.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PyQtMainEntry()
    window.show()
    sys.exit(app.exec_())