from PyQt5 import QtWidgets
from ssh import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys, os, paramiko, re

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Load_PC()
        self.model = QStandardItemModel(self.ui.listView)
        self.client = paramiko.SSHClient()
        self.port = 22
        self.host = None
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ui.action_2.triggered.connect(self.Add_New_PC)
        self.ui.action_4.triggered.connect(self.Change_port)
        self.ui.pushButton_5.clicked.connect(self.Connect_2_PC)
        self.ui.comboBox.activated[str].connect(self.On_Activated)


    def Add_New_PC(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Добавление нового ПК',
            'Введите IP адрес ПК:')
        numb = QtWidgets.QInputDialog.getText(self, 'Добавление нового ПК',
            'Введите № ПК:')
        item = str("Comp-" + str(numb[0]) + ": " + text + '\n')
        file = open('computers.txt', 'a')
        file.write(item)
        file.close()
        if ok:
            self.ui.comboBox.addItem(item)

    def Load_PC(self):
        file = open('computers.txt', 'r')
        for line in file:
            print(line)
            self.ui.comboBox.addItem(line)
        file.close()

    def Connect_2_PC(self):
        try:
            self.client.connect(hostname=self.host, username=self.ui.lineEdit_2.text,
        password=self.ui.lineEdit_3.text, port=self.port)
        except Exception as err:
            print("Can`t connect! " + str(err))

    def On_Activated(self, text):
        self.host = text[-14::]
        print(self.host)
        print(self.ui.lineEdit_2.text())
        print(self.ui.lineEdit_3.text())

    def Change_port(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Смена порта',
            'Введите порт для подключения:')
        if ok:
            self.port = text
            print(self.port)

def Testing_local_network():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    file = open('computers.txt', 'r')
    for line in file:
        ip = line[-14::]
        print('Computer number {}'.format(ip))
        try:
            client.connect(hostname=ip, username="leninadm",
            password="12345", port=22)
        except Exception as err:
            print("Can`t connect! " + str(err))
        finally:
            client.close()


if __name__ == "__main__":
    Testing_local_network()
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    application.client.close()
    sys.exit(app.exec())
