import json

def read_data():
    try:
        with open("data/player.json", "r", encoding ="utf-8") as file:
            data = json.load(file)
            return data
    except:
        data = {
            "skin": "assets/rocket.png",
            "money": 0,
            "range": 300,
            "attack_speed": 700
        }
        return data

def writing_data(data):
    with open("data/player.json", "w", encoding ="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)

def writing_shop_data(price):
    with open('data/shop_elements.py', "w") as file:
        file.write(price)