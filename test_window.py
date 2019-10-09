import sys
from PyQt5 import QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from test_ui import Ui_MainWindow as ui_class

class CMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_class()
        self.ui.setupUi(self)
        self.model = QtGui.QStandardItemModel()
        self.table = self.ui.tableWidget
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.graphic = QtWidgets.QVBoxLayout(self.ui.widget)
        self.graphic.addWidget(self.canvas)
        self.table.setColumnCount(5)
        self.ui.ButtonLoad.pressed.connect(self.file_load)
        self.ui.ButtonUpdate.pressed.connect(self.column_var_load)
        self.ui.ButtonSave.pressed.connect(self.file_save)
        self.ui.ButtonGraph.pressed.connect(self.SelectColumn)

    def file_load(self):
        self.sum_itog_result = []
        self.table.setRowCount(0)
        with open("test_in.txt", "r") as self.file_in_massiv:
            self.in_massiv = [line.strip().split(" ") for line in
                          self.file_in_massiv]
        self.massiv = self.in_massiv
        self.in_massiv = []
        for item in self.massiv:
            item_v = []
            for item_var in item:
                item_v.append(int(item_var))
            self.in_massiv.append(item_v)
            self.sum_itog_result.append(0)
        self.sum_itog_result = np.array(self.sum_itog_result)
        self.in_massiv = np.array(self.in_massiv)
        self.col_var = 0
        for item in self.in_massiv[0]:
            self.col_var += 1
        self.table.setColumnCount(self.col_var + 3)
        self.table.setItemDelegateForColumn(self.col_var, ComboBoxDelegate(self))
        self.table_load()

    def file_save(self):
        if self.table.rowCount():
            for row in range(self.table.rowCount()):
                for col in range(self.table.columnCount()):
                    with open("test_out.txt", "+a") as self.file_out_save:
                        self.file_out_save.write(self.table.item(row, col).text() + " ")
                with open("test_out.txt", "+a") as self.file_out_save:
                    self.file_out_save.write("\n")
        QtWidgets.QMessageBox.information(self, QtWidgets.qApp.tr("Сохранение в файл"),
                                           QtWidgets.qApp.tr("Данные сохранены в файл {}".format("test_out.txt")),
                                           QtWidgets.QMessageBox.Ok)
    def table_load(self):
        row = 0
        for item in self.massiv:
            self.table.setRowCount(row + 1)
            for index, fields in enumerate(item):
                self.table.setItem(row ,index , QtWidgets.QTableWidgetItem (str(fields)))
            row += 1

    def massiv_run(self):
        self.sum_in_massiv = self.in_massiv.sum(axis=1)
        #   # последний результитрующий столбец
        self.sum_itog = self.sum_in_massiv + self.column_table_var  # столбец суммирования
        self.sum_itog_result += self.sum_itog
        # print("Получили следующий массив")
        self.massiv = np.column_stack((self.in_massiv, self.column_table_var, self.sum_itog, self.sum_itog_result))
        self.table_load()

    def column_var_load(self):
        self.column_table_var = []
        for row in range(self.table.rowCount()):
            if self.table.item(row, self.col_var):
                self.column_table_var.append((int(self.table.item(row, self.col_var).text())))
            else:
                self.column_table_var.append(0)
        self.column_table_var = np.array(self.column_table_var)
        self.massiv_run()

    def SelectColumn(self):
        Columns = []
        for item in self.table.selectedItems():
            Columns.append(item.column())
        self.select_Columns = set(Columns)
        self.graphic_load()

    def graphic_load(self):
        # очистить график
        self.figure.clear()
        if self.select_Columns:
            """ Вариант по заданию """
            # # Сформировать данные по выбранным столбцам
            # data = [[],[]]
            # i = 0
            # for index, col in enumerate(self.select_Columns):
            #     if i < 2:
            #         for row in range(self.table.rowCount()):
            #             data[i].append(int(self.table.item(row, col).text()))
            #     i += 1
            #
            # if index > 0:# проверка выбора не менее 2 столбцов
            #     # открыть оси
            #     ax = self.figure.add_subplot(111)
            #     ax.plot(data[0], data[1])
            #     # обновить canvas
            #     self.canvas.draw()

            """ Вариант нескольких графиков по каждому выбранному столбцу """
            # Сформировать данные по выбранным столбцам
            data = []
            for row in range(self.table.rowCount()):
                temp = []
                for col in self.select_Columns:
                    try:
                        temp.append(int(self.table.item(row, col).text()))
                    except:
                        temp.append(0)
                data.append(temp)

            # открыть оси
            ax = self.figure.add_subplot(111)
            ax.plot(data, '*-')
            # обновить canvas
            self.canvas.draw()

# ComboBox для изменяемого столбца от 1 до 5
class ComboBoxDelegate(QtWidgets.QItemDelegate):
    def __init__(self, parent):
        super(ComboBoxDelegate, self).__init__(parent)
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QComboBox(parent)
        editor.addItems(["1","2","3","4","5"])        #Загрузить в список свои данные
        return editor
    def setEditorData(self, editor, index):
        pos = 0
        editor.setCurrentIndex(pos)
    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText())

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CMainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()