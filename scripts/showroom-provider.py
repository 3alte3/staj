import requests

url = 'http://127.0.0.1:8000/api/v1/token/'
myobj = {'username': 'asd', "password": "112233Zz"}

x = requests.post(url, json=myobj)
access = x.json()['access']  # access token

url = 'http://127.0.0.1:8000/api/v1/showroomCharact/'
x = requests.get(url, )


for temp in x.json():
    url = f'http://127.0.0.1:8000/api/v1/providerListofcars/?search={temp["mark"]},{temp["model"]}'
    xy = requests.get(url, headers={"Authorization": f"Bearer {access}"})
    profitable = xy.json()[0]
    for temp1 in xy.json():
        if profitable['price'] > temp1['price']:
            profitable = temp1


    url = f'http://127.0.0.1:8000/api/v1/showroom/?search={int(temp["showroom_id"])}'
    temp1 = requests.get(url, headers={"Authorization": f"Bearer {access}"})


    for y in temp1.json():
        if y['showroom_id'] == temp["showroom_id"]:
            resp1 = y

    id = resp1['id']



    url = f'http://127.0.0.1:8000/api/v1/showroom/{id}/'
    myobj = {"name":requests.get(url).json()['name'],"content":requests.get(url).json()['content'],
             'balance': int(requests.get(url).json()['balance']) - int((profitable['price'])),
             "location":requests.get(url).json()['location'],"showroom_id":requests.get(url).json()['showroom_id'],}
    #обновление баланса автосалона

    temp1 = requests.put(url, json=myobj, headers={"Authorization": f"Bearer {access}"})

    url = f'http://127.0.0.1:8000/api/v1/showroomCars/?search={temp["showroom_id"]},{temp["model"]},{temp["mark"]}'
    temp1 = requests.get(url, headers={"Authorization": f"Bearer {access}"})

    if temp1.json():
        for y in temp1.json():
            if y['showroom_id'] == temp["showroom_id"]:
                resp1 = y

        id = resp1['id']
        print(url)
        print(temp1.json())
        print(id)



        url = f'http://127.0.0.1:8000/api/v1/showroomCars/{id}/'
        print(url)

        myobj = {"engine_type": requests.get(url).json()["engine_type"],
                "max_speed":requests.get(url).json()["max_speed"],
        "ammount_of_eng":requests.get(url).json()["ammount_of_eng"],
        "model":requests.get(url).json()["model"],
        "mark":requests.get(url).json()["mark"],
        "price":requests.get(url).json()["price"],
        "showroom_id":requests.get(url).json()["showroom_id"],
        'ammount_of_cars': int(requests.get(url).json()["ammount_of_cars"]) + 10,} #добавление машин в автосалон

        temp1 = requests.put(url, json=myobj, headers={"Authorization": f"Bearer {access}"})
        profitable = temp1.json()
        print(" ")
        # покупка у выбранного поставщика

    else : #init
        url = f'http://127.0.0.1:8000/api/v1/showroomCars/'
        myobj={"engine_type":temp['engine_type'],"max_speed":temp['max_speed'],"ammount_of_eng":temp['ammount_of_eng'],
               "model":temp['model'],"mark":temp['mark'],"price":12000,
               "showroom_id":temp['showroom_id'],"ammount_of_cars":10,}
        temp1 = requests.post(url, json=myobj,headers={"Authorization": f"Bearer {access}"})

        url = f'http://127.0.0.1:8000/api/v1/showroomCars/?search={temp["showroom_id"]},{temp["model"]},{temp["mark"]}'
        temp1 = requests.get(url, headers={"Authorization": f"Bearer {access}"})

        for y in temp1.json():
            if y['showroom_id'] == temp["showroom_id"]:
                resp1 = y

        id = resp1['id']
        print(url)
        print(temp1.json())
        print(id)



        url = f'http://127.0.0.1:8000/api/v1/showroomCars/{id}/'
        print(url)

        myobj = {"engine_type": requests.get(url).json()["engine_type"],
                "max_speed":requests.get(url).json()["max_speed"],
        "ammount_of_eng":requests.get(url).json()["ammount_of_eng"],
        "model":requests.get(url).json()["model"],
        "mark":requests.get(url).json()["mark"],
        "price":requests.get(url).json()["price"],
        "showroom_id":requests.get(url).json()["showroom_id"],
        'ammount_of_cars': int(requests.get(url).json()["ammount_of_cars"]) + 10,} #добавление машин в автосалон

        temp1 = requests.put(url, json=myobj, headers={"Authorization": f"Bearer {access}"})
        profitable = temp1.json()
        print(" ")
        # покупка у выбранного поставщика

