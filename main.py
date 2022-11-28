import sys

from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

from myCalcUI import Ui_MainWindow
from stack import infix_to_suffix, compute_suffix, infix, brackets_legal
from MyError import brackets_error


class MyCalculator(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MyCalculator, self).__init__()
        self.setupUi(self)
        self.connecter()
        self.show()
        # 为计算器创造结果变量存储结果,flag变量用于再次输入数值时清空结果
        self.flag = 0
        self.result = float(0)

    # 连接按钮和对应的函数
    def connecter(self):
        self.pushButton_0.clicked.connect(self.press_0)
        self.pushButton_1.clicked.connect(self.press_1)
        self.pushButton_2.clicked.connect(self.press_2)
        self.pushButton_3.clicked.connect(self.press_3)
        self.pushButton_4.clicked.connect(self.press_4)
        self.pushButton_5.clicked.connect(self.press_5)
        self.pushButton_6.clicked.connect(self.press_6)
        self.pushButton_7.clicked.connect(self.press_7)
        self.pushButton_8.clicked.connect(self.press_8)
        self.pushButton_9.clicked.connect(self.press_9)
        self.pushButton_plus.clicked.connect(self.press_plus)
        self.pushButton_sub.clicked.connect(self.press_sub)
        self.pushButton_mul.clicked.connect(self.press_mul)
        self.pushButton_div.clicked.connect(self.press_div)
        self.pushButton_equal.clicked.connect(self.press_equal)
        self.pushButton_DEL.clicked.connect(self.press_del)
        self.pushButton_AC.clicked.connect(self.press_ac)
        self.pushButton_left.clicked.connect(self.press_left)
        self.pushButton_right.clicked.connect(self.press_right)
        self.pushButton_point.clicked.connect(self.press_point)
        self.pushButton_sqrt.clicked.connect(self.press_sqrt)
        self.pushButton_power.clicked.connect(self.press_power)

    # 根据flag值判断再次输入数字时是否要清空数值
    def re_enter(self):
        if self.flag != 0:
            self.press_ac()

    # 按钮0
    def press_0(self):
        self.re_enter()
        self.lineEdit.insert("0")

    # 按钮1
    def press_1(self):
        self.re_enter()
        self.lineEdit.insert("1")

    # 按钮2
    def press_2(self):
        self.re_enter()
        self.lineEdit.insert("2")

    # 按钮3
    def press_3(self):
        self.re_enter()
        self.lineEdit.insert("3")

    # 按钮4
    def press_4(self):
        self.re_enter()
        self.lineEdit.insert("4")

    # 按钮5
    def press_5(self):
        self.re_enter()
        self.lineEdit.insert("5")

    # 按钮6
    def press_6(self):
        self.re_enter()
        self.lineEdit.insert("6")

    # 按钮7
    def press_7(self):
        self.re_enter()
        self.lineEdit.insert("7")

    # 按钮8
    def press_8(self):
        self.re_enter()
        self.lineEdit.insert("8")

    # 按钮9
    def press_9(self):
        self.re_enter()
        self.lineEdit.insert("9")

    # 按钮(
    def press_left(self):
        self.re_enter()
        self.lineEdit.insert("(")

    # 按钮)
    def press_right(self):
        self.re_enter()
        self.lineEdit.insert(")")

    # 按钮.
    def press_point(self):
        self.re_enter()
        self.lineEdit.insert(".")

    # 按钮^
    def press_power(self):
        self.re_enter()
        self.lineEdit.insert("^")

    # 按钮sqrt
    def press_sqrt(self):
        self.re_enter()
        self.lineEdit.insert("sqrt(")

    # 按钮+
    def press_plus(self):
        if self.flag == 2:
            self.press_ac()
        self.flag = 0
        self.lineEdit.insert("+")

    # 按钮-
    def press_sub(self):
        if self.flag == 2:
            self.press_ac()
        self.flag = 0
        self.lineEdit.insert("-")

    # 按钮×
    def press_mul(self):
        if self.flag == 2:
            self.press_ac()
        self.flag = 0
        self.lineEdit.insert("×")

    # 按钮÷
    def press_div(self):
        if self.flag == 2:
            self.press_ac()
        self.flag = 0
        self.lineEdit.insert("÷")

    # 按钮=
    def press_equal(self):
        text = self.lineEdit.text()
        try:
            # 先判断括号合法性
            if not brackets_legal(infix(text)):
                raise brackets_error("括号有误")
            # result表示结果
            self.result = compute_suffix(infix_to_suffix(infix(text)))
            self.flag = 1
            self.lineEdit.setText(str(self.result))
        # except brackets_error:
        #     self.flag = 2
        #     self.lineEdit.setText("Invalid brackets, check your input brackets!")
        except:
            self.flag = 2
            self.lineEdit.setText("Invalid syntax!")

    # 按钮DEL
    def press_del(self):
        text = self.lineEdit.text()
        nexttext = ''
        for i in range(len(text)):
            if i != len(text)-1:
                nexttext += text[i]
        self.lineEdit.setText(nexttext)
        if self.flag == 2:
            self.press_ac()
        self.flag = 0

    # 按钮AC
    def press_ac(self):
        self.flag = 0
        self.lineEdit.setText("")


def main():
    app = QApplication(sys.argv)
    calc = MyCalculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
