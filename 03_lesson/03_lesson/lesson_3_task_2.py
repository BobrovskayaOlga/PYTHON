from smartphone import Smartphone

catalog = [
    Smartphone("Poco", "M3", "+79504568452"),
    Smartphone("Samsung Galaxy", "S25", "+79058236457"),
    Smartphone("Xiaomi", "14T Pro", "+79562342158"),
    Smartphone("realme", "GT7 Pro", "+79564236559"),
    Smartphone("Oppo", "Reno13", "+79507451253")
]

for smartphone in catalog:
    print(f"{smartphone.phone_brand} {smartphone.phone_model} {smartphone.subscriber_number}")