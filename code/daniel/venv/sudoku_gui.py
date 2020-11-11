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
# game logic module
from build_sudoku import Sudoku as Sud
# assign to variable
var = Sud() 
# runmodule to generate game numbers
sudoku_board = var.print_board()

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
        self._createSudokuBoard()

    def _createDisplay(self):
        '''Create the display'''
        # Display widget
        self.name_display = QLabel('Player Name')
        # display properties
        self.name_display.setFixedSize(150,20)
        self.name_display.setAlignment(Qt.AlignLeft)
        self.name_display.setFont(QFont('Times', 16))
        self.generalLayout.addWidget(self.name_display)

    def _createSudokuBoard(self):
        '''Create the grid for Sudoku board'''
        # store of button
        self.buttons = {}
        # assign layout to variable
        buttonsLayout = QGridLayout()
        buttonsLayout.setSpacing(0)
        # generate buttons with assigned values and locations within grid layout
        for i, row in enumerate(sudoku_board):
            for j, num in enumerate(row):
                index = (i, j)
                self.buttons[index] = QPushButton(str(num), self)
                self.buttons[index].setFixedSize(45,45)
                buttonsLayout.addWidget(self.buttons[index], i, j)
        self.generalLayout.addLayout(buttonsLayout)
       
class PlaySudoku:
    '''Controller Class'''
    def __init__(self, view):
        '''Controller initializer'''
        # Allow PlaySudoku to see Sudoku view
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _inputNum(self, key):
        '''Update button text'''
        while True:
            text, ok = QInputDialog.getText(self._view, 'Enter Number', '')
            if ok != True:
                break
            elif text not in ['1','2','3','4','5','6','7','8','9', '']:
                continue
            else:
                break
        if ok:
            self._view.buttons[key].setText(str(text))
        
    def _connectSignals(self):
        '''Connect signals and slots'''
        for btnNum, btn in self._view.buttons.items():
            btn.clicked.connect(partial(self._inputNum, btnNum))

def main():
    """Main function"""
    # Create an instance of QApplication
    sudoku_game = QApplication(sys.argv)
    # Show the calculator's GUI
    view = Sudoku()
    view.show()
    PlaySudoku(view=view)
    # Execute the calculator's main loop
    sys.exit(sudoku_game.exec_())

if __name__ == '__main__':
    main()       