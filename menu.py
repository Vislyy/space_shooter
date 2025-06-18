from PyQt6.QtWidgets import *
from main import start_game
from shop import shop_window

app = QApplication([])
window = QWidget()

window.setObjectName("window")

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
shop_btn.clicked.connect(shop_window)

app.setStyleSheet("""

        QWidget#window {
            background-image: url(assets/galaxy.jpg);
            background-position: center;
            background-size: cover;
            filter: brightness(60%);
        }
        
    """)
window.setLayout(main_line)
window.show()
app.exec()