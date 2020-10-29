import sys
# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from functools import partial

class Sudoku(QMainWindow):
    '''Sudoku's View (GUI)'''
    def __init__(self):
        '''View initializer'''
        super().__init__()
        # Main window properties
        self.setWindowTitle('Sudoku')
        self.setFixedSize(350,450)
        # Central widget and general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create display
        self._createDisplay()
        # self._createSudokuBoard()

    def _createDisplay(self):
        '''Create the display'''
        # Display widget
        self.name_display = QLabel('Player Name')
        # display properties
        self.name_display.setFixedSize(150,20)
        self.name_display.setAlignment(Qt.AlignLeft)
        self.name_display.setFont(QFont('Times', 16))
        self.generalLayout.addWidget(self.name_display)
        dialog, ok = QInputDialog.getText(self, "hi", "goodbye")
        self.name_display.setText(dialog)

def main():
    """Main function"""
    # Create an instance of QApplication
    sudoku = QApplication(sys.argv)
    # Show the calculator's GUI
    view = Sudoku()
    view.show()
    # PlaySudoku(view=view)
    # Execute the calculator's main loop
    sys.exit(sudoku.exec_())

if __name__ == '__main__':
    main()  