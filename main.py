from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from ssh import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys, os, paramiko, re

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.client = None
        self.port = 738
        self.host = None
        self.Create_client()
        self.ui.connect_btn.clicked.connect(self.Connect_2_PC)
        self.ui.pc_lists_box.activated[str].connect(self.On_Activated)
        self.ui.deafult_settings_check.stateChanged.connect(self.Locking_lines)

    def Adding_msg(self, text):
        self.ui.logger_list.addItem(text)

    def Create_client(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        return 0



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
        self.Adding_msg("Connecting to " + self.host)
        try:
            self.client.connect(hostname=self.host, username=self.ui.username_line.text,
        password=self.ui.password_line.text, port=self.port)
        except Exception as err:
            self.Adding_msg("Can`t connect!")
            strng = str(err)
            print(type(strng))
            print(strng)
            self.Adding_msg(strng)

    def On_Activated(self, text):
        self.host = text[-13::]

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

    def Locking_lines(self, state):
        if state != Qt.Checked:
            self.ui.username_line.setEnabled(True)
            self.ui.password_line.setEnabled(True)
        else:
            self.ui.username_line.setEnabled(False)
            self.ui.password_line.setEnabled(False)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Сообщение',
            "Вы действительно хотите выйти?", QtWidgets.QMessageBox.Yes |
            QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    application.client.close()
    sys.exit(app.exec())
