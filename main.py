from PySide2 import QtWidgets
import time
import json
import hashlib
import os
import sys
from github import Github


time.strftime("%d%m%Y")
# try:
#     os.mkdir("logs")
# except:
#     pass

# log = open("./logs/{}{}{}.log".format(time.strftime("%d"), time.strftime("%m"), time.strftime("%Y")), "at")
try:
    data = open("./data.json")
    data = json.loads(data.read())
# log.write("\n==============================================================\n")
app = QtWidgets.QApplication()
g = Github()
srv = g.get_repo("sergoum/login_project")



class Auth(object):
    def __init__(self):
        global a
#         log.write("Checking for stored credentials...")
        if data["username"] != "" and data["password"] != "":
#             log.write("\nCredentials found. Attempting to authenticate...")
            if self.verify(data["username"], data["password"]):
#                 log.write("\nAuthentication successful! Starting App...")
                a = App()
            else:
#                 log.write("\nAuthentication failed. Requesting authentication from user.")
                self.request()

    
    def request(self):
        '''Displays a login dialog to the user. It will then pass the credentials to auth.verify() and if it returns true, the app will be launched.'''
        self.submitted = False
        self.login_diag = QtWidgets.QWidget()
        self.login_diag.setWindowTitle("Login")
        self.bg_image = QtWidgets.QLabel(self.login_diag)
        self.bg_image.setPixmap("bg.png")
        self.bg_image.move(0, 0)
        self.bg_image.adjustSize()
        self.bg_image.show()
        self.login_diag.adjustSize()
        self.login_diag.setFixedSize(self.login_diag.size())
        self.container = QtWidgets.QLabel(self.login_diag)
        self.container.setStyleSheet("background-color: white; border: 10px solid white; border-radius: 20px;")
        self.container.setGeometry(300, 200, 400, 400)
        self.container.show()
        self.l1 = QtWidgets.QLabel(self.login_diag)
        self.l1.setText("Login")
        self.l1.setStyleSheet("font-family: Trebuchet MS, Calibri; font-size: 40px;")
        self.l1.move(450, 230)
        self.l1.show()
        self.login_diag.show()
        self.ubox = QtWidgets.QLineEdit(self.login_diag)
        self.ubox.setGeometry(360, 302, 280, 50)
        self.ubox.setStyleSheet("border: 3px solid #AAAAAA; border-radius: 10px; font-family: Trebuchet MS, Helvetica; font-size: 20px; padding: 8px;")
        self.ul = QtWidgets.QLabel(self.login_diag)
        self.ul.setText("Username")
        self.ul.move(370, 315)
        self.ul.setStyleSheet("color: #AAAAAA; font-family: Trebuchet MS, Helvetica; font-size: 20px;")
        self.ul.show()
        self.pbox = QtWidgets.QLineEdit(self.login_diag)
        self.pbox.setGeometry(360, 362, 280, 50)
        self.pbox.setStyleSheet("border: 3px solid #AAAAAA; border-radius: 10px; font-family: Trebuchet MS, Helvetica; font-size: 20px; padding: 8px;")
        self.pl = QtWidgets.QLabel(self.login_diag)
        self.pl.setText("Password")
        self.pl.move(370, 375)
        self.pl.setStyleSheet("color: #AAAAAA; font-family: Trebuchet MS, Helvetica; font-size: 20px;")
        self.pl.show()
        self.submit = QtWidgets.QPushButton(self.login_diag)
        self.submit.setText("Submit")
        self.submit.setGeometry(360, 420, 280, 40)
        self.submit.clicked.connect(self.s)
        self.submit.setStyleSheet("background-color: #0099FF; color: white; font-family: Trebuchet MS, Helvetica; font-size: 20px; border: 3px solid #0099FF; border-radius: 10px;")
        self.submit.show()
        self.ubox.show()
        self.pbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pbox.show()
        while not self.submitted:
            if self.ubox.text() != "":
                self.ul.hide()
            else:
                self.ul.show()
            if self.pbox.text() != "":
                self.pl.hide()
            else:
                self.pl.show()
            if self.login_diag.isHidden():
                quit()
            app.processEvents()
            
            
        
        
    
    def verify(self, username, password):
        global srv
        temp = hashlib.sha512()
        temp.update(username.encode())
        username = temp.hexdigest()
        temp = hashlib.sha512()
        temp.update(password.encode())
        password = temp.hexdigest()
        db = srv.get_contents("database.json").decoded_content
        db = json.loads(db)
        try:    
            if db[username] == password:
                return True
            else:
                return False
        except:
            return False


    def s(self):
        global a
        if len(self.ubox.text()) <= 20 and len(self.ubox.text()) >= 2:
            self.submitted = True
            if self.verify(self.ubox.text(), self.pbox.text()):
#                 log.write("\nAuthentication successful! Starting app...")
                self.login_diag.destroy()
#                 log.close()
                self.a = App()
            else:
                self.request()
        else:
            self.request()
            
   
class App(object):
    def __init__(self):
        self.launch()

    def launch(self):
        '''Main code for the application you are making'''
        self.win = QtWidgets.QMainWindow()
        self.label = QtWidgets.QLabel(self.win)
        self.label.setText("YAY YOU LOGGED IN")
        self.label.adjustSize()
        self.label.show()
        self.win.show()
        
        while True:
            if self.win.isHidden():
                quit()
            app.processEvents()



if __name__ == "__main__":
    auth = Auth()
    sys.exit(app.exec_())
