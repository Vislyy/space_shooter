from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from saving_manager import read_data

def shop_window():
    window = QDialog()
    data = read_data()
    money = data["money"]
    
    main_line = QHBoxLayout()
    
    elements = [
        {
            "name": "Дальність",
            "img": "assets/bullet.png",
            "price": 100,
            "image_width": 100,
            "image_height": 150
        },
        {
            "name": "Швидкість атаки",
            "img": "assets/atk_speed.png",
            "price": 150,
            "image_width": 116,
            "image_height": 40
        }
    ]

    #money_lbl = QLabel(f"Гроші: {money}")

    #main_line.addWidget(money_lbl)
    for element in elements:
        line = QVBoxLayout()
        name_lbl = QLabel(element["name"])
        img_lbl = QLabel()
        image_manager = QPixmap(element["img"])
        image_manager = image_manager.scaledToWidth(element["image_width"])
        image_manager = image_manager.scaledToHeight(element["image_height"])
        img_lbl.setPixmap(image_manager)
        price_lbl = QLabel(str(element["price"]))
        buy_btn = QPushButton("Купити")

        line.addWidget(name_lbl)
        line.addWidget(img_lbl)
        line.addWidget(price_lbl)
        line.addWidget(buy_btn)

        main_line.addLayout(line)

    window.setLayout(main_line)
    window.show()
    window.exec()