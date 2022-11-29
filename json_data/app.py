import json

with open('/Users/shaheempp/Developer/python_practice/json_data/data.json') as file:
    data = json.load(file)
user_name = data['cart_list'][0]['cart']['user']['name']
vendor_pic = data['cart_list'][0]['cart']['vendor']['logo']
name = '-'.join(user_name.split()).lower()
print(name)

file = vendor_pic.split('.', -1)
extension = file[-1]
print(extension)
print(file)

point = data['cart_list'][0]['cart']['vendor']['point']
points = point.split()
latitude, longitude = points[1], points[2]
srid = points[0]
chars = [" ", "=", "SRID", ";", "POINT"]
for c in chars:
    srid = srid.replace(c, "")

chars = [' ', '\'', '(', ')']
for c in chars:
    latitude = latitude.replace(c, "")
    longitude = longitude.replace(c, "")

print(srid, latitude, longitude)

new_data = {
        "cart": {
                "id": 8,
                "qr_code": "/media/qr_code/qr16696161493396301.png",
                "user": {
                        "id": 3,
                        "name": "Uchiha Itachi",
                        "phone": "919801726349"
                },
                "vendor": {
                        "id": 12,
                        "title": "Max",
                        "logo": "/static/image-404/photo-unavailable.png",
                        "image": "/static/image-404/photo-unavailable.png",
                        "vendor_category": {
                                "id": 1,
                                "title": "mall"
                        },
                        "point": "SRID=4326;POINT (76.311371 10.023286)",
                        "location": None,
                        "phone": None
                }
        },
        "open_status": {
                "is_opened": False,
                "opening_time": "closed",
                "closing_time": "closed"
        },
        "products": [
                {
                        "product": {
                                "id": 6,
                                "image": "/media/product/f1109164213nikcra.png",
                                "title": "leaf shirt",
                                "stock": 10
                        },
                        "quantity": 10
                }
        ]
}

data.update(new_data)

with open('data.json', 'w') as fp:
    json.dump(data, fp)

print("!!!JSON FILE UPDATED!!!")
