from PyQt5 import QtWidgets
from ssh import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys, os, paramiko, re

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.model = QStandardItemModel(self.ui.listView)
        self.client = paramiko.SSHClient()
        self.port = 22
        self.host = None
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


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
        self.host = text[-15::]
        print(self.host)
        print(self.ui.lineEdit_2.text())
        print(self.ui.lineEdit_3.text())

    def Change_port(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Смена порта',
            'Введите порт для подключения:')
        if ok:
            self.port = text
            print(self.port)

    def Testing_local_network(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        n = 0
        for i in range(31,39):
            ip = '192.168.88.' + str(i)
            number_pc = str(i - 30)
            line = 'Computer number {0} ip {1} \n'.format(number_pc, ip)
            print(line)
            self.ui.comboBox.addItem(line)
            #passw = input('Enter pass\n')
            try:
                client.connect(hostname=ip, username="leninadm",
                password="liblen19", port=22)
                stdin, stdout, stderr = client.exec_command('ifconfig')
                data = stdout.read() + stderr.read()
                print(data.decode('utf-8'))
            except Exception as err:
                print("Can`t connect! " + str(err) + '\n')
            finally:
                client.close()
            print("--------------------------------------\n")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    application.client.close()
    sys.exit(app.exec())
