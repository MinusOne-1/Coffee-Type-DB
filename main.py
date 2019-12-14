import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem, QPushButton, QSpinBox
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from addEditCoffeeForm import Ui_MainWindow as addEdit
from main_1 import Ui_MainWindow as main_window


class DBCoffee(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_window()
        self.ui.setupUi(self)
        self.con = sqlite3.connect('data/coffee.db')
        self.ui.showAll_b.clicked.connect(self.showAllCoffe)
        self.ui.add_b.clicked.connect(self.addCofee)
        self.ui.edit_b.clicked.connect(self.editCofee)

    def editCofee(self):
        win = addEditCoffeeFormClass(self, True)
        win.show()

    def addCofee(self):
        win = addEditCoffeeFormClass(self)
        win.show()

    def showAllCoffe(self):
        cur = self.con.cursor()
        result = cur.execute(
            '''Select name, stepen, type, cost, val from coffe WHERE id BETWEEN 0 AND 1001''').fetchall()
        self.ui.tableWidget.setRowCount(len(result) + 1)
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem('Название'))
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem('Степень обжарки'))
        self.ui.tableWidget.setItem(0, 2, QTableWidgetItem('Молотый/Зерновой'))
        self.ui.tableWidget.setItem(0, 3, QTableWidgetItem('Цена'))
        self.ui.tableWidget.setItem(0, 4, QTableWidgetItem('Объём'))
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.ui.tableWidget.setItem(i + 1, j, QTableWidgetItem(str(val).capitalize()))
        self.ui.tableWidget.resizeColumnsToContents()


class addEditCoffeeFormClass(QMainWindow):
    def __init__(self, main=None, edit=False):
        super().__init__(main)
        self.ui = addEdit()
        self.ui.setupUi(self)
        self.con = sqlite3.connect('data/coffee.db')
        self.ui.add.clicked.connect(self.add_m)
        self.ui.update_.clicked.connect(self.update_m)
        if edit:
            self.choseID()

    def add_m(self):
        error_find = False
        name = self.ui.name.text()
        step = self.ui.step.text()
        mol_zern = self.ui.mol_zern.text()
        descr = self.ui.descr.toPlainText()
        val = self.ui.val.text()
        cost = self.ui.cost.text()
        self.ui.errors.setText('')
        if name == '':
            error_find = True
            self.ui.errors.setText(self.ui.errors.toPlainText() + '\nError: Название - пустая строка')
        if not step.isdigit():
            error_find = True
            self.ui.errors.setText(self.ui.errors.toPlainText() + '\nError: Степень обжарки не числовое значение')
        if not cost.isdigit():
            error_find = True
            self.ui.errors.setText(self.ui.errors.toPlainText() + '\nError: Цена не числовое значение')
        if not val.isdigit():
            error_find = True
            self.ui.errors.setText(self.ui.errors.toPlainText() + '\nError: Объём не числовое значение')
        if cost == '':
            error_find = True
            self.ui.errors.setText(self.ui.errors.toPlainText() + '\nError: Цена - пустая строка')
        if val == '':
            error_find = True
            self.ui.errors.setText(self.ui.errors.toPlainText() + '\nError: Объём - пустая строка')
        if error_find:
            return -1
        cur = self.con.cursor()
        cur.execute('INSERT INTO coffe(name, stepen, type, descrip, cost, val) VALUES(?, ?, ?, ?, ?, ?)',
                    (name, step, mol_zern, descr, val, cost))
        self.con.commit()
        # добавляет в базу данных новый кофе с автоинкрементным ID
        self.close()

    def update_m(self):
        error_find = False
        name = self.ui.name.text()
        step = self.ui.step.text()
        mol_zern = self.ui.mol_zern.text()
        descr = self.ui.descr.toPlainText()
        val = self.ui.val.text()
        cost = self.ui.cost.text()
        self.ui.errors.setText('')
        if name == '':
            error_find = True
            self.ui.errors.setText(self.ui.errors.toPlainText() + '\nError: Название - пустая строка')
        if not step.isdigit():
            error_find = True
            self.ui.errors.setText(self.ui.errors.toPlainText() + '\nError: Степень обжарки не числовое значение')
        if not cost.isdigit():
            error_find = True
            self.ui.errors.setText(self.ui.errors.toPlainText() + '\nError: Цена не числовое значение')
        if not val.isdigit():
            error_find = True
            self.ui.errors.setText(self.ui.errors.toPlainText() + '\nError: Объём не числовое значение')
        if cost == '':
            error_find = True
            self.ui.errors.setText(self.ui.errors.toPlainText() + '\nError: Цена - пустая строка')
        if val == '':
            error_find = True
            self.ui.errors.setText(self.ui.errors.toPlainText() + '\nError: Объём - пустая строка')
        if error_find:
            return -1
        cur = self.con.cursor()
        cur.execute('''UPDATE coffe
                SET name = ?
                WHERE id = ?''', (name, int(self.ui.id_l.text())))
        cur.execute('''UPDATE coffe
                        SET stepen = ?
                        WHERE id = ?''', (step, int(self.ui.id_l.text())))
        cur.execute('''UPDATE coffe
                SET type = ?
                WHERE id = ?''', (mol_zern, int(self.ui.id_l.text())))
        cur.execute('''UPDATE coffe
                        SET descrip = ?
                        WHERE id = ?''', (descr, int(self.ui.id_l.text())))
        cur.execute('''UPDATE coffe
                        SET cost = ?
                        WHERE id = ?''', (cost, int(self.ui.id_l.text())))
        cur.execute('''UPDATE coffe
                        SET val = ?
                        WHERE id = ?''', (val, int(self.ui.id_l.text())))
        self.con.commit()
        self.close()

    def choseID(self):
        # выводит окно, в котором выбирается индекс, заполняет поля соответственно из БД
        cur = self.con.cursor()
        maxx = sorted(cur.execute(
            '''Select id from coffe WHERE id BETWEEN 0 AND 1001''').fetchall(), key=lambda u: u[0])[-1][-1]
        win = ChooseID(self, maxx)
        win.show()
        self.ui.add.setEnabled(False)
        self.ui.update_.setEnabled(True)

    def editFormSet(self, id):
        cur = self.con.cursor()
        res = cur.execute(
            '''Select * from coffe WHERE id = ?''', (id,)).fetchall()[0]
        self.ui.id_l.setText(str(id))
        self.ui.name.setText(res[1])
        self.ui.step.setText(str(res[2]))
        self.ui.mol_zern.setText(res[3])
        self.ui.descr.setText(res[4])
        self.ui.val.setText(str(res[5]))
        self.ui.cost.setText(str(res[6]))


class ChooseID(QMainWindow):
    def __init__(self, main=None, maxx=1):
        super().__init__(main)
        self.id_ = 1
        self.main = main
        self.initUI(maxx)

    def initUI(self, maxx):
        self.setGeometry(300, 300, 415, 400)  # окно
        self.setWindowTitle('Форма выбора')

        self.new_game_b = QPushButton('Выбрать', self)  # кнопка заказа
        self.new_game_b.resize(self.new_game_b.sizeHint())
        self.new_game_b.move(150, 165)
        self.new_game_b.clicked.connect(self.take_order)

        self.id = QSpinBox(self)
        self.id.resize(self.new_game_b.sizeHint())
        self.id.move(150, 200)
        self.id.setMaximum(maxx)
        self.id.setMinimum(1)

    def take_order(self):
        self.main.editFormSet(self.id.value())
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBCoffee()
    ex.show()
    sys.exit(app.exec())
