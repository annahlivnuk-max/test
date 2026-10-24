# крок 1 
import sys
from PyQt5.QtWidgets import (QApplication, QWidget , QLabel , QPushButton , QVBoxLayout , QRadioButton , QToolButton , QButtonGroup)
from PyQt5.QtCore import Qt
#  с.пр.клас 2
class AnimalQuiz(QWidget):
    # створюємо почят. налаштування 3
    def __init__(self):
        super().__init__()
        # саме вікно 4
        self.setWindowTitle("Яка ти тваринка ?")
        self.setGeometry(300,150,500,400)
# дизайн  5
        self.setStyleSheet("""bakground-color: #C084FC"
        QLabel { color: white; 
                font-size: 22px; 
                font-weight: bold; }""")
# змінні для питань 6
        self.question_number = 0
        self.answers = []
# Питання + результат 7/8
        self.questions = [("Що ти найбільш любиш робити ?" , ["Спати" ,"Пригоди","Бути з друзями ","Спостерігати за всім"])]
        self.animals = {0:"кеішка",
                        1:"лисиця",
                        2:"кролик",
                        3:"вовк"} 
# місце для елементів + текст петання 9/10
        self.layout = QVBoxLayout()
        self.question_lebel = QLabel()
        self.question_lebel.setAlignment(Qt.AlignCenter)
# створення кнопок 11 
        self.button_group = QButtonGroup()
        self.radio_buttons = []
        for i in range(4): # повторити 4 рази
            radio = QRadioButton ()
            self.button_group.addButton(radio,1)
            