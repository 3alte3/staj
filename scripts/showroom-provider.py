from datetime import datetime
import requests

url = 'http://127.0.0.1:8000/api/v1/token/'
myobj = {'username': 'asd', "password": "112233Zz"}

access = requests.post(url, json=myobj).json()['access']  # access token

url = 'http://127.0.0.1:8000/api/v1/showroomCharact/' # урла для характеристик
req = requests.get(url, ) # получаем характеристики модели по которым будут подобраны автомобили


for temp in req.json(): # перебор запросов
    urlToGetCars = f'http://127.0.0.1:8000/api/v1/providerListofcars/?search={temp["mark"]},{temp["model"]}' # урла для получения списка машин у поставщиков по конкретной марке и модели
    urlToGetDiscount = f'http://127.0.0.1:8000/api/v1/discount/?search={temp["mark"]},{temp["model"]}' # урла для выбора скидки у поставщика

    xz = requests.get(urlToGetDiscount, headers={"Authorization": f"Bearer {access}"}) # получаем скидки
    xy = requests.get(urlToGetCars, headers={"Authorization": f"Bearer {access}"}) # получаем список машин

    profitable = xy.json()[0] # при подборе самой выгодной машины будем считать , что 1 в списке самое выгодное предложение

    if xz.json() : #если список не пустой
        for temp1 in xy.json():
            for temp2 in xz.json():
                if temp1['providerId'] == temp2['provider_id']:
                    if profitable['price'] > (temp1['price'] * (1 - (temp2['percent'] / 100))):
                        profitable = temp1
                        discount = temp2



        url = f'http://127.0.0.1:8000/api/v1/showroom/?search={int(temp["showroom_id"])}'
        temp1 = requests.get(url, headers={"Authorization": f"Bearer {access}"})

        for y in temp1.json():
            if y['showroom_id'] == temp["showroom_id"]:
                resp1 = y

        id = resp1['id']

        if resp1['balance'] > profitable['price'] * (1 - (discount['percent'] / 100)):  # проверка баланса

            url = f'http://127.0.0.1:8000/api/v1/showroom/{id}/'
            myobj = {"name": requests.get(url).json()['name'], "content": requests.get(url).json()['content'],
                     'balance': int(requests.get(url).json()['balance']) - int(
                         profitable['price'] * (1 - (discount['percent'] / 100))),
                     "location": requests.get(url).json()['location'],
                     "showroom_id": requests.get(url).json()['showroom_id'], }
            # обновление баланса автосалона

            temp1 = requests.put(url, json=myobj, headers={"Authorization": f"Bearer {access}"})

            url = f'http://127.0.0.1:8000/api/v1/showroomCars/?search={temp["showroom_id"]},{temp["model"]},{temp["mark"]}'
            temp1 = requests.get(url, headers={"Authorization": f"Bearer {access}"})

            if temp1.json():
                for y in temp1.json():
                    if y['showroom_id'] == temp["showroom_id"]:
                        resp1 = y

                id = resp1['id']


                url = f'http://127.0.0.1:8000/api/v1/showroomCars/{id}/'


                myobj = {"engine_type": requests.get(url).json()["engine_type"],
                         "max_speed": requests.get(url).json()["max_speed"],
                         "ammount_of_eng": requests.get(url).json()["ammount_of_eng"],
                         "model": requests.get(url).json()["model"],
                         "mark": requests.get(url).json()["mark"],
                         "price": requests.get(url).json()["price"],
                         "showroom_id": requests.get(url).json()["showroom_id"],
                         'ammount_of_cars': int(
                             requests.get(url).json()["ammount_of_cars"]) + 10, }  # добавление машин в автосалон

                temp1 = requests.put(url, json=myobj, headers={"Authorization": f"Bearer {access}"})

                # покупка у выбранного поставщика

                url = f'http://127.0.0.1:8000/api/v1/providerHistory/'
                myobj = {"date": datetime.now().isoformat(), "providerId": profitable['providerId'],
                         "showroom_id": resp1["showroom_id"], "model": resp1['model'], "mark": resp1["mark"], }
                requests.post(url, json=myobj,
                              headers={"Authorization": f"Bearer {access}"})  # добавление в историю провайдера


            else:  # init

                url = f'http://127.0.0.1:8000/api/v1/showroom/{id}/'
                myobj = {"name": requests.get(url).json()['name'], "content": requests.get(url).json()['content'],
                         'balance': int(requests.get(url).json()['balance']) - int(profitable['price']),
                         "location": requests.get(url).json()['location'],
                         "showroom_id": requests.get(url).json()['showroom_id'], }
                # обновление баланса автосалона

                temp1 = requests.put(url, json=myobj, headers={"Authorization": f"Bearer {access}"})

                url = f'http://127.0.0.1:8000/api/v1/showroomCars/'
                myobj = {"engine_type": temp['engine_type'], "max_speed": temp['max_speed'],
                         "ammount_of_eng": temp['ammount_of_eng'],
                         "model": temp['model'], "mark": temp['mark'], "price": 12000,
                         "showroom_id": temp['showroom_id'], "ammount_of_cars": 10, }
                temp1 = requests.post(url, json=myobj, headers={"Authorization": f"Bearer {access}"})

                url = f'http://127.0.0.1:8000/api/v1/showroomCars/?search={temp["showroom_id"]},{temp["model"]},{temp["mark"]}'
                temp1 = requests.get(url, headers={"Authorization": f"Bearer {access}"})

                for y in temp1.json():
                    if y['showroom_id'] == temp["showroom_id"]:
                        resp1 = y

                id = resp1['id']


                url = f'http://127.0.0.1:8000/api/v1/showroomCars/{id}/'


                myobj = {"engine_type": requests.get(url).json()["engine_type"],
                         "max_speed": requests.get(url).json()["max_speed"],
                         "ammount_of_eng": requests.get(url).json()["ammount_of_eng"],
                         "model": requests.get(url).json()["model"],
                         "mark": requests.get(url).json()["mark"],
                         "price": requests.get(url).json()["price"],
                         "showroom_id": requests.get(url).json()["showroom_id"],
                         'ammount_of_cars': int(
                             requests.get(url).json()["ammount_of_cars"]) + 10, }  # добавление машин в автосалон

                temp1 = requests.put(url, json=myobj, headers={"Authorization": f"Bearer {access}"})
                profitable = temp1.json()

                # покупка у выбранного поставщика

                url = f'http://127.0.0.1:8000/api/v1/providerHistory/'
                myobj = {"date": datetime.now().isoformat(), "providerId": profitable['providerId'],
                         "showroom_id": resp1["showroom_id"], "model": resp1['model'], "mark": resp1["mark"], }
                requests.post(url, json=myobj,
                              headers={"Authorization": f"Bearer {access}"})  # добавление в историю провайдера
        else:
            print("No money no honey ")


    else : # если список скидок пустой



        for temp3 in xy.json():
            if profitable['price'] > temp3['price']:
                profitable = temp3


        url = f'http://127.0.0.1:8000/api/v1/showroom/?search={int(temp["showroom_id"])}'
        temp1 = requests.get(url, headers={"Authorization": f"Bearer {access}"})


        for y in temp1.json():
            if y['showroom_id'] == temp["showroom_id"]:
                resp1 = y

        id = resp1['id']

        if resp1['balance'] > profitable['price']  : # проверка баланса

            url = f'http://127.0.0.1:8000/api/v1/showroom/{id}/'
            myobj = {"name":requests.get(url).json()['name'],"content":requests.get(url).json()['content'],
                     'balance': int(requests.get(url).json()['balance']) - int(profitable['price']),
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



                url = f'http://127.0.0.1:8000/api/v1/showroomCars/{id}/'


                myobj = {"engine_type": requests.get(url).json()["engine_type"],
                        "max_speed":requests.get(url).json()["max_speed"],
                "ammount_of_eng":requests.get(url).json()["ammount_of_eng"],
                "model":requests.get(url).json()["model"],
                "mark":requests.get(url).json()["mark"],
                "price":requests.get(url).json()["price"],
                "showroom_id":requests.get(url).json()["showroom_id"],
                'ammount_of_cars': int(requests.get(url).json()["ammount_of_cars"]) + 10,} #добавление машин в автосалон

                temp1 = requests.put(url, json=myobj, headers={"Authorization": f"Bearer {access}"})

                # покупка у выбранного поставщика

                url = f'http://127.0.0.1:8000/api/v1/providerHistory/'
                myobj = {"date":datetime.now().isoformat(),"providerId":profitable['providerId'],
                         "showroom_id":resp1["showroom_id"],"model":resp1['model'],"mark":resp1["mark"],}
                requests.post(url,json=myobj,headers={"Authorization": f"Bearer {access}"}) #добавление в историю провайдера


            else : #init

                url = f'http://127.0.0.1:8000/api/v1/showroom/{id}/'
                myobj = {"name": requests.get(url).json()['name'], "content": requests.get(url).json()['content'],
                         'balance': int(requests.get(url).json()['balance']) - int(profitable['price']),
                         "location": requests.get(url).json()['location'],
                         "showroom_id": requests.get(url).json()['showroom_id'], }
                # обновление баланса автосалона

                temp1 = requests.put(url, json=myobj, headers={"Authorization": f"Bearer {access}"})


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




                url = f'http://127.0.0.1:8000/api/v1/showroomCars/{id}/'


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

                # покупка у выбранного поставщика

                url = f'http://127.0.0.1:8000/api/v1/providerHistory/'
                myobj = {"date": datetime.now().isoformat(), "providerId": profitable['providerId'],
                         "showroom_id": resp1["showroom_id"], "model": resp1['model'], "mark": resp1["mark"], }
                requests.post(url, json=myobj,
                              headers={"Authorization": f"Bearer {access}"})  # добавление в историю провайдера
        else : print("No money no honey ")

