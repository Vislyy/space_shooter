from saving_manager import *

def buy_skin(price, img):
    data = read_data()
    if data["money"] >= price:
        data["skin"] = img
        data["money"] -= price
        writing_data(data)
    else:
        print("Недостатньо коштів")

def buy_boost(price, type):
    data = read_data()
    element_data = read_shop_data()
    if data["money"] >= price:
        data["money"] -= price
        data[type] -= 20
        print(f"Ви купили предмет")
        writing_data(data)
    else:
        print("Недостатньо коштів")