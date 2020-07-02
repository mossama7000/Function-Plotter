import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from sympy import *
import pyqtgraph as pg
import numpy as np


app = QApplication(sys.argv)

plotWidget = pg.plot(title="Figure")

#Main window
win = QMainWindow()
win.setGeometry(500,300,400,280)
win.setWindowTitle("Function Plotter")

#--------------function of x-----------------
#label
label1 = QLabel(win)
label1.setText("Enter a function of variable x")
label1.setGeometry(20,20,165,20)
label1.setFont(QFont('Arial', 10))

#text
t_func = QLineEdit(win)
t_func.setGeometry(20,40,150,20)
t_func.setFont(QFont('Arial', 10))

#-------------------minimum value--------------------
#label
label2 = QLabel(win)
label2.setText("Min value of x")
label2.setGeometry(20,90,100,20)
label2.setFont(QFont('Arial', 10))

#text
t_min = QLineEdit(win)
t_min.setGeometry(20,110,150,20)
t_min.setFont(QFont('Arial', 10))

#-------------------maximum value----------------------
#label
label3 = QLabel(win)
label3.setText("Max value of  x")
label3.setGeometry(230,90,100,20)
label3.setFont(QFont('Arial', 10))

t_max = QLineEdit(win)
t_max.setGeometry(230,110,150,20)
t_max.setFont(QFont('Arial', 10))

msg = QMessageBox()
msg.setWindowTitle("Error Message")
msg.setGeometry(600,400,300,50)


def showmsg():
    t_func_value = t_func.text()
    t_minvalue = t_min.text()
    t_maxvalue = t_max.text()
    x = symbols("x")
    yval = []
    # first try statement to ensure minimum value is integer
    try:
        min_v = int(t_minvalue)
    except ValueError:
        msg.setText("Minimum value is invalid")
        m = msg.exec_()
    else:

    # second try statement to ensure maximum value is integer
    # and minimum value is less than maximum value
        try:
            max_v = int(t_maxvalue)
            if min_v >= max_v:
                raise Exception
        except ValueError:
            msg.setText("Maximum value is invalid")
            m = msg.exec_()
        except Exception:
            msg.setText("Minimum value is greater than or equal Maximum value")
            m = msg.exec_()
        else:
            xval = np.arange(min_v,max_v,0.1)
            try:
                if t_func_value == "":
                    raise TypeError
                else:
                    func = sympify(t_func_value)

                for i in xval:
                    y = func.subs(x,i)
                    if y == zoo:
                        yval = [i]
                        raise ZeroDivisionError
                    yval.append(y)

                k = int(sum(yval))

            except ZeroDivisionError:
                msg.setText("function tends to infinity at x = "+str(yval[0]))
                m = msg.exec_()
            except Exception:
                msg.setText("Input function is invalid")
                m = msg.exec_()

            else:
                plotWidget.plot(np.array(xval, dtype=float), np.array(yval, dtype=float))
                plotWidget.setLabel('left', "<span style=\"color:red;font-size:16px\">Y</span>")
                plotWidget.setLabel('bottom', "<span style=\"color:red;font-size:20px\">X</span>")

#----------PLOT------------
b1 = QPushButton(win)
b1.setText("Plot")
b1.setGeometry(130,180,130,60)
b1.setFont(QFont('Times', 18))
b1.clicked.connect(showmsg)

win.show()

app.exec_()
