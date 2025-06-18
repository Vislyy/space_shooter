from PyQt6.QtWidgets import *
from main import start_game

app = QApplication([])
window = QWidget()

main_line = QVBoxLayout()
start_btn = QPushButton('Start')
shop_btn = QPushButton('Shop')
option_btn = QPushButton('Option')
exit_btn = QPushButton('Exit')

main_line.addWidget(start_btn)
main_line.addWidget(shop_btn)
main_line.addWidget(option_btn)
main_line.addWidget(exit_btn)

start_btn.clicked.connect(start_game)

window.setLayout(main_line)
window.show()
app.exec()