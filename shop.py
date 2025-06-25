from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from saving_manager import *
from shop_functions import *
from data.shop_elements import *

def shop_window():
    window = QDialog()
    data = read_data()
    money = data["money"]
    
    main_line = QHBoxLayout()

    #money_lbl = QLabel(f"Гроші: {money}")

    #main_line.addWidget(money_lbl)
    for element in elements:
        if element["type_of_card"] == "Boost":
            line = QVBoxLayout()
            name_lbl = QLabel(element["name"])
            img_lbl = QLabel()
            image_manager = QPixmap(element["img"])
            image_manager = image_manager.scaledToWidth(element["image_width"])
            image_manager = image_manager.scaledToHeight(element["image_height"])
            img_lbl.setPixmap(image_manager)
            price_lbl = QLabel(str(element["price"]))
            buy_btn = QPushButton("Купити")
            buy_btn.clicked.connect(lambda _,price=element["price"], type_of_item="attack_speed"
                                    if element["name"] == "Швидкість атаки" else "range":
                                    buy_boost(price, type_of_item))

            line.addWidget(name_lbl)
            line.addWidget(img_lbl)
            line.addWidget(price_lbl)
            line.addWidget(buy_btn)

            main_line.addLayout(line)

    window.setLayout(main_line)
    window.show()
    window.exec()