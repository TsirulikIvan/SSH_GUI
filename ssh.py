# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(999, 614)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 9, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pc_lists_box = QtWidgets.QComboBox(self.centralwidget)
        self.pc_lists_box.setEnabled(True)
        self.pc_lists_box.setGeometry(QtCore.QRect(10, 40, 381, 20))
        self.pc_lists_box.setObjectName("pc_lists_box")
        self.pc_lists_box.addItem("")
        self.pc_lists_box.addItem("")
        self.pc_lists_box.addItem("")
        self.pc_lists_box.addItem("")
        self.pc_lists_box.addItem("")
        self.pc_lists_box.addItem("")
        self.pc_lists_box.addItem("")
        self.pc_lists_box.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.username_line = QtWidgets.QLineEdit(self.centralwidget)
        self.username_line.setEnabled(False)
        self.username_line.setGeometry(QtCore.QRect(10, 120, 381, 20))
        self.username_line.setObjectName("username_line")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.password_line = QtWidgets.QLineEdit(self.centralwidget)
        self.password_line.setEnabled(False)
        self.password_line.setGeometry(QtCore.QRect(10, 210, 381, 20))
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setObjectName("password_line")
        self.connect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.connect_btn.setGeometry(QtCore.QRect(240, 250, 151, 21))
        self.connect_btn.setObjectName("connect_btn")
        self.deafult_settings_check = QtWidgets.QCheckBox(self.centralwidget)
        self.deafult_settings_check.setGeometry(QtCore.QRect(100, 280, 176, 17))
        self.deafult_settings_check.setChecked(True)
        self.deafult_settings_check.setObjectName("deafult_settings_check")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(720, 320, 221, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(720, 350, 251, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.logger_list = QtWidgets.QListWidget(self.centralwidget)
        self.logger_list.setGeometry(QtCore.QRect(10, 330, 681, 241))
        self.logger_list.setMovement(QtWidgets.QListView.Free)
        self.logger_list.setProperty("isWrapping", False)
        self.logger_list.setObjectName("logger_list")
        item = QtWidgets.QListWidgetItem()
        self.logger_list.addItem(item)
        self.off_btn = QtWidgets.QPushButton(self.centralwidget)
        self.off_btn.setGeometry(QtCore.QRect(720, 390, 251, 23))
        self.off_btn.setObjectName("off_btn")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(720, 510, 251, 23))
        self.pushButton.setObjectName("pushButton")
        self.reboot_rtn = QtWidgets.QPushButton(self.centralwidget)
        self.reboot_rtn.setGeometry(QtCore.QRect(720, 420, 251, 23))
        self.reboot_rtn.setObjectName("reboot_rtn")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 540, 251, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 300, 1011, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(720, 450, 251, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(720, 480, 251, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(400, 0, 20, 308))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 7, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 250, 201, 21))
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(710, 37, 251, 231))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("kompjuter2-256x236.png"))
        self.label_6.setObjectName("label_6")
        self.local_ip_lbl = QtWidgets.QLabel(self.centralwidget)
        self.local_ip_lbl.setGeometry(QtCore.QRect(430, 47, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.local_ip_lbl.setFont(font)
        self.local_ip_lbl.setObjectName("local_ip_lbl")
        self.usability_tine_lbl = QtWidgets.QLabel(self.centralwidget)
        self.usability_tine_lbl.setGeometry(QtCore.QRect(430, 77, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.usability_tine_lbl.setFont(font)
        self.usability_tine_lbl.setObjectName("usability_tine_lbl")
        self.mac_lbl = QtWidgets.QLabel(self.centralwidget)
        self.mac_lbl.setGeometry(QtCore.QRect(430, 107, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mac_lbl.setFont(font)
        self.mac_lbl.setObjectName("mac_lbl")
        self.on_web_lbl = QtWidgets.QLabel(self.centralwidget)
        self.on_web_lbl.setGeometry(QtCore.QRect(430, 137, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.on_web_lbl.setFont(font)
        self.on_web_lbl.setObjectName("on_web_lbl")
        self.disk_space_lbl = QtWidgets.QLabel(self.centralwidget)
        self.disk_space_lbl.setGeometry(QtCore.QRect(430, 167, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.disk_space_lbl.setFont(font)
        self.disk_space_lbl.setObjectName("disk_space_lbl")
        self.pc_num_lbl = QtWidgets.QLabel(self.centralwidget)
        self.pc_num_lbl.setGeometry(QtCore.QRect(800, 150, 47, 13))
        self.pc_num_lbl.setObjectName("pc_num_lbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 999, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.adding_pc_menu = QtWidgets.QAction(MainWindow)
        self.adding_pc_menu.setObjectName("adding_pc_menu")
        self.change_port_menu = QtWidgets.QAction(MainWindow)
        self.change_port_menu.setObjectName("change_port_menu")
        self.info_menu = QtWidgets.QAction(MainWindow)
        self.info_menu.setObjectName("info_menu")
        self.exit_menu = QtWidgets.QAction(MainWindow)
        self.exit_menu.setObjectName("exit_menu")
        self.menu.addAction(self.adding_pc_menu)
        self.menu.addAction(self.change_port_menu)
        self.menu.addAction(self.info_menu)
        self.menu.addAction(self.exit_menu)
        self.menubar.addAction(self.menu.menuAction())
        self.label.setBuddy(self.label)
        self.label_5.setBuddy(self.label)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SSH - Client"))
        self.label.setText(_translate("MainWindow", "Выберете нужный компьютер:"))
        self.pc_lists_box.setItemText(0, _translate("MainWindow", "Comp-1 : 192.168.88.31"))
        self.pc_lists_box.setItemText(1, _translate("MainWindow", "Comp-2 : 192.168.88.32"))
        self.pc_lists_box.setItemText(2, _translate("MainWindow", "Comp-3 : 192.168.88.33"))
        self.pc_lists_box.setItemText(3, _translate("MainWindow", "Comp-4 : 192.168.88.34"))
        self.pc_lists_box.setItemText(4, _translate("MainWindow", "Comp-5 : 192.168.88.35"))
        self.pc_lists_box.setItemText(5, _translate("MainWindow", "Comp-6 : 192.168.88.36"))
        self.pc_lists_box.setItemText(6, _translate("MainWindow", "Comp-7 : 192.168.88.37"))
        self.pc_lists_box.setItemText(7, _translate("MainWindow", "Comp-8 : 192.168.88.38"))
        self.label_2.setText(_translate("MainWindow", "Введите имя пользователя:"))
        self.username_line.setText(_translate("MainWindow", "leninadm"))
        self.label_3.setText(_translate("MainWindow", "Введите пароль:"))
        self.password_line.setText(_translate("MainWindow", "liblen19"))
        self.connect_btn.setText(_translate("MainWindow", "Подключиться"))
        self.deafult_settings_check.setText(_translate("MainWindow", "Логин и пароль по умолчанию"))
        self.label_4.setText(_translate("MainWindow", "Введите команду:"))
        __sortingEnabled = self.logger_list.isSortingEnabled()
        self.logger_list.setSortingEnabled(False)
        item = self.logger_list.item(0)
        item.setText(_translate("MainWindow", "Начало работы! Приветствую вас!"))
        self.logger_list.setSortingEnabled(__sortingEnabled)
        self.off_btn.setText(_translate("MainWindow", "Выкллючить"))
        self.pushButton.setText(_translate("MainWindow", "Кнопка 3"))
        self.reboot_rtn.setText(_translate("MainWindow", "Перезагрузить"))
        self.pushButton_2.setText(_translate("MainWindow", "Кнопка 4"))
        self.pushButton_3.setText(_translate("MainWindow", "Кнопка 1"))
        self.pushButton_4.setText(_translate("MainWindow", "Кнопка 2"))
        self.label_5.setText(_translate("MainWindow", "Данные о подключенном ПК:"))
        self.local_ip_lbl.setText(_translate("MainWindow", "Локальный IP:"))
        self.usability_tine_lbl.setText(_translate("MainWindow", "Время пользования ПК:"))
        self.mac_lbl.setText(_translate("MainWindow", "MAC - Адрес:"))
        self.on_web_lbl.setText(_translate("MainWindow", "Доступ в Интернет:"))
        self.disk_space_lbl.setText(_translate("MainWindow", "Место на диске: "))
        self.pc_num_lbl.setText(_translate("MainWindow", "№ "))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.adding_pc_menu.setText(_translate("MainWindow", "Добавить компьютер"))
        self.adding_pc_menu.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.change_port_menu.setText(_translate("MainWindow", "Сменить порт"))
        self.change_port_menu.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.info_menu.setText(_translate("MainWindow", "Информация"))
        self.info_menu.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.exit_menu.setText(_translate("MainWindow", "Выход"))
        self.exit_menu.setShortcut(_translate("MainWindow", "Ctrl+Q"))
