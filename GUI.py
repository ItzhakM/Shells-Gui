import os
import sys
from tkinter import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (QWidget)
from tkinter import messagebox

import subprocess
file = '/home/ItzhakM/PycharmProjects/Qt-GUI-/Widget_Record.xed'
f = open(file, "w")


class LOGIN_UI(QWidget):
    """This class initialize the Login phase"""
    def __init__(self):
        super(LOGIN_UI, self).__init__()
        ui_path = r"/home/ItzhakM/PycharmProjects/Qt-GUI-/Login.ui"
        uic.loadUi(ui_path, self)


class EQ_UI(QWidget):
    """This class initialize the main UI"""
    def __init__(self):
        super(EQ_UI, self).__init__()
        ui_path = r"/home/ItzhakM/PycharmProjects/Qt-GUI-/Widget.ui"
        uic.loadUi(ui_path, self)
        self.ui = self

class EQ_APP():
    """This class represent the application functionality"""
    def __init__(self):
        """This function link between Qt buttons and their functions"""
        # self.edit_clicked_event = None
        self.login_ui = LOGIN_UI()
        self.login_ui.show()
        self.login_ui.Ok_B.clicked.connect(lambda: self.connect_to_dbs())

        self.ui = EQ_UI()
        self.netA_clicked, self.netB_clicked = False, False
        self.ui.netA.clicked.connect(self.netA_clicked_event)
        self.ui.netB.clicked.connect(self.netB_clicked_event)
        self.ui.update.clicked.connect(self.update_clicked_event)
        self.ui.finish.clicked.connect(self.perform_clicked)


    def connect_to_dbs(self):
        """This function connect between the two UIs"""
        password = self.login_ui.Password_B.text()
        username = self.login_ui.Username_B.text()
        if (username == "username" and password == "pssword") or (username == "" and password == ""):
            self.login_ui.hide()
            # os.system("gnome-terminal -e 'bash -c \"sudo dnf update; exec bash\"'")
            # self.db = Equipment_DB()
            # self.db.db_login()
            os.system("gnome-terminal -e 'bash -c \"echo Welcome to Widget!; exec bash\"'")
            self.ui.show()
        else:
            self.Message('Error', "Wrong Username/Password")

    def _unset_all(self):
        """This function initializes the app to start"""
        self.netA_clicked = False
        self.netB_clicked = False
        self.update_clicked = False

    def Message(self, title, txt):
        """This function creates a messagebox"""
        root = Tk()
        root.withdraw()
        messagebox.showinfo(title, txt)
        root.destroy()

    def yes_no_msg(self, title, txt):
        """This function raise a second type of messagebox"""
        root = Tk()
        root.withdraw()
        ans = messagebox.askyesno(title=title, message=txt)
        root.destroy()
        return ans

    def netA_clicked_event(self):
        """This function transfer to the netA function if clicked"""
        self._unset_all()
        self.netA_clicked = True

    def netB_clicked_event(self):
        """This function transfer to the netB function if clicked"""
        self._unset_all()
        self.netB_clicked = True

    def update_clicked_event(self):
        """This function transfer to the update function if clicked"""
        self._unset_all()
        self.update_clicked = True

        os.system("gnome-terminal -e 'bash -c \"sudo dnf update; exec bash\"'")

    def perform_clicked(self):
        """Main Back-end. This object initializes all the functions and their functionalities"""
        rbtn1 = self.ui.netA.isChecked()
        rbtn2 = self.ui.netB.isChecked()
        if rbtn1 == rbtn2:
            self.Message('Error', 'Choose a network. (A/B)')
            return

        performed_by = self.ui.MTESTER.currentText()
        if '' == performed_by:
            self.Message('Error', 'Choose a performer.')
            return

        type = self.ui.ASREV_2.currentText()
        if '' == type:
            self.Message('Error', 'Choose a command type.')
            return

        elif 'ifconfig' == type:
            os.system("gnome-terminal -e 'bash -c \"ifconfig; exec bash\"'")
            f = open(file, "w")
            f.write('\n\nCommand: ifconfig')
            f.write('\n\nPerformed By: ' + performed_by)
            f.write('\n\nShell: \n')
            # subprocess.Popen("ifconfig", stdout=f)
            subprocess.Popen('ifconfig', shell=True, stdout=f)
            f.close()

        elif 'arp -n' == type:
            os.system("gnome-terminal -e 'bash -c \"arp -n; exec bash\"'")
            f = open(file, "w")
            f.write('\n\nCommand: arp -n')
            f.write('\n\nPerformed By: ' + performed_by)
            f.write('\n\nShell: \n')
            subprocess.Popen('arp -n', shell=True, stdout=f)
            f.close()

        elif 'iptables -t mangle -nvL' == type:
            os.system("gnome-terminal -e 'bash -c \"sudo iptables -t mangle -nvL; exec bash\"'")
            f = open(file, "w")
            f.write('\n\nCommand: iptables -t mangle -nvL')
            f.write('\n\nPerformed By: ' + performed_by)
            f.write('\n\nShell: \n')
            subprocess.Popen('iptables -t mangle -nvL', shell=True, stdout=f)
            f.close()

        elif 'iptables -t nat -nvL' == type:
            os.system("gnome-terminal -e 'bash -c \"sudo iptables -t nat -nvL; exec bash\"'")
            f = open(file, "w")
            f.write('\n\nCommand: iptables -t nat -nvL')
            f.write('\n\nPerformed By: ' + performed_by)
            f.write('\n\nShell: \n')
            subprocess.Popen('sudo iptables -t nat -nvL from shell', shell=True, stdout=f)
            f.close()

        elif 'clear' == type:
            os.system("gnome-terminal -e 'bash -c \"clear; exec bash\"'")


            # file = open('Widget_Record.txt', 'w')
            #     file.write('\n\nOperator: Get an equipment')
            #     file.write('\nType: ' + type)
                # fh.write('\nSerial: ' + serial_number)
                # fh.write('\nCalibration: ' + due_calibration)
                # file.write('\nPerformed By: ' + performed_by)
                # file.close()

        # ip_address = self.ui.ASSN_2.text()
        # if '' == ip_address:
        #     self.Message('Error', 'Enter IP !')
        #     return
        #
        # due_calibration = self.ui.ASSN_3.text()
        # if not self.get_clicked:
        #     if '' == due_calibration:
        #         self.Message('Error', 'Enter calibration date !')
        #         return

        # performed_by = self.ui.MTESTER.currentText()
        # if '' == performed_by and not self.get_clicked:
        #     self.Message('Error', 'Choose a performer !')
        #     return

        # if self.netA_clicked:
        #     date_cal = self.get_ip_address(ip, type)
        #     if date_cal == None:
        #         self.Message('Error', 'IP address does not exist !')
        #         return
        #     self.ui.ASSN_3.setText(self.get_ip_address(ip, type))
        #     self.self.get_ip_address = True
        #     fh = open('App_Record.txt', 'a')
        #     fh.write('\n\nOperator: Get an equipment')
        #     fh.write('\nType: ' + type)
        #     fh.write('\nSerial: ' + serial_number)
        #     fh.write('\nCalibration: ' + due_calibration)
        #     fh.write('\nPerformed By: ' + performed_by)
        #     fh.close()


if __name__ == '__main__':  # Execute the Front-end
    app = QtWidgets.QApplication(sys.argv)
    sw = EQ_APP()
    sys.exit(app.exec_())
