# Source https://github.com/MinThetNaung/BMI_Calculator/blob/master/BMI_Program.py
# Small adaptions


import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QPushButton, QAction, QLineEdit, QMessageBox, QMainWindow


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.cal_button = None
        self.weight_input = None
        self.height_input = None
        self.title = "BMI Program"
        self.left = 200
        self.top = 200
        self.width = 500
        self.height = 300
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('bmi_logo.ico'))
        # Create a menu bar
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("File")

        # Add a category button to the menu bar file
        exit_button = QAction('Exit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.setStatusTip('Exit application')
        exit_button.triggered.connect(self.close)
        file_menu.addAction(exit_button)

        # Calculation and GUI part
        label_title = QLabel(self)
        label_title.setText(
            "Body Mass Index (BMI) Calculation Program Written in Python")
        label_title.setStyleSheet("font-weight: bold")
        label_title.setGeometry(0, 80, 1000, 100)
        label_title.move(50, 0)

        label_height = QLabel(self)
        label_height.setText("Enter height:")
        label_height.move(30, 95)

        label_weight = QLabel(self)
        label_weight.setText("Enter weight:")
        label_weight.move(30, 145)

        # Create a textbox for input
        self.height_input = QLineEdit(self)
        self.height_input.move(100, 100)
        self.height_input.resize(50, 20)

        self.weight_input = QLineEdit(self)
        self.weight_input.move(100, 150)
        self.weight_input.resize(50, 20)

        # Create a Calculate Button in the window
        self.cal_button = QPushButton("Calculate", self)
        self.cal_button.setToolTip(
            "This is to calculate the result.")
        self.cal_button.move(200, 220)

        label_legend_weight = QLabel(self)
        label_legend_weight.setText("weight (in kilos)")
        label_legend_weight.move(160, 145)

        label_legend_height = QLabel(self)
        label_legend_height.setText("height (in metres)")
        label_legend_height.move(160, 95)

        # Connect button to function on_click
        self.cal_button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):

        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())

            if (weight / (height * height)) < 18.5:
                QMessageBox.information(self, 'Result', "Your BMI result is: " + str(
                    '%.2f' % (weight / (height * height))) + "\n Category: Underweight", QMessageBox.Ok)

            elif (weight / (height * height) < 25) and (weight / (height * height) >= 18.5):
                QMessageBox.information(self, 'Result', "Your BMI result is: " + str(
                    '%.2f' % (weight / (height * height))) + "\n Category: Normal weight", QMessageBox.Ok)

            elif (weight / (height * height) < 30) and (weight / (height * height) >= 25):
                QMessageBox.information(self, 'Result', "Your BMI result is: " + str(
                    '%.2f' % (weight / (height * height))) + "\n Category: Overweight", QMessageBox.Ok)

            else:
                QMessageBox.information(self, 'Result', "Your BMI result is: " + str(
                    '%.2f' % (weight / (height * height))) + "\n Category: Obesity", QMessageBox.Ok)

        except ValueError:
            QMessageBox.warning(self, "Invalid data", "Please check weight and height for validity!", QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
