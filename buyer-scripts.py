import requests

url = 'http://127.0.0.1:8000/api/v1/token/'
myobj = {'username': 'asd',"password":"112233Zz"} # login

x = requests.post(url, json = myobj)
access = x.json()['access'] # access token


url = 'http://127.0.0.1:8000/api/v1/createoffer/'
myobj = {'buyerId': '121',"maxPrice":"1234889","mark":"bmw","model":"c39"} #url and object to create object

url1 = f'http://127.0.0.1:8000/api/v1/buyers/?search={myobj["buyerId"]}' #url to get buyer with buyerId from offer
temp = requests.get(url1,headers={"Authorization":f"Bearer {access}"})

for a in temp.json():
    if (int(a['buyerId']) == int(myobj['buyerId'])) and (int(a['balance']) >= int(myobj['maxPrice'])): #
        x= requests.post(url, json = myobj,headers={"Authorization":f"Bearer {access}"}) #url to create offer

        url = f'http://127.0.0.1:8000/api/v1/showroomCars/?search={x.json()["mark"]},{x.json()["model"]}'

        response = requests.get(url,headers={"Authorization":f"Bearer {access}"})
        print(response.json()) # получаем запись с авто из списка машин автосалона
        profitable = response.json()[0]
        for xy in response.json():
            if xy['price'] < profitable['price']:
                profitable=xy
        if (int(myobj['maxPrice']) >= int(profitable['price'])) and (int(profitable['ammount_of_cars']) > 0):
            url = f'http://127.0.0.1:8000/api/v1/buyers/?search={myobj["buyerId"]}' # ищем пользователя с байер айди
            resp = requests.get(url,headers={"Authorization":f"Bearer {access}"}).json()
            for y in resp:
                if y['buyerId'] == myobj["buyerId"]:
                    resp1=y
            balance = resp1['balance']
            id=resp1['id']
            myobj = {'name':resp1["name"],'surname':resp1["surname"],
                             'email':resp1["email"],'phoneNumber':resp1["phoneNumber"],'buyerId':resp1["buyerId"],
                            'balance' : f"{balance-profitable['price']}"}
            url = f'http://127.0.0.1:8000/api/v1/buyers/{id}/'
            xz = requests.put(url, json=myobj, headers={"Authorization": f"Bearer {access}"}) #обновление баланса пользователя
            print(xz.json())

            url = f'http://127.0.0.1:8000/api/v1/buyersHistory/'
            myobj = {'buyerId':resp1['buyerId'],'price':profitable['price'],'showroom_id':profitable['showroom_id']}
            xz = requests.post(url, json=myobj, headers={"Authorization": f"Bearer {access}"})
            print(xz.json()) # обновление истории пользователя

            url = f'http://127.0.0.1:8000/api/v1/showroomCars/{profitable["id"]}/'

            myobj = {'engine_type': profitable["engine_type"], 'max_speed': int(profitable["max_speed"]),
                     'ammount_of_eng': int(profitable["ammount_of_eng"]),'model': profitable["model"],
                     'mark': profitable["mark"],'showroom_id': int(profitable["showroom_id"]),
                     'price': int(profitable["price"]),'ammount_of_cars': int(profitable["ammount_of_cars"])-1,}
            xz = requests.put(url, json=myobj, headers={"Authorization": f"Bearer {access}"})
            print(xz.json()) #обновление количества машин в автосалоне

            url = f'http://127.0.0.1:8000/api/v1/history/'

            myobj = {'buyer': a["buyerId"], 'price': int(profitable["price"]),
                     'showroom_id': int(profitable["showroom_id"])}
            xz = requests.post(url, json=myobj, headers={"Authorization": f"Bearer {access}"})
            print(xz.json())  # добавление покупки в историю покупок автосалона

            url = f'http://127.0.0.1:8000/api/v1/showroomUniqueBuyers/?search={a["buyerId"]}'


            if(requests.get(url,headers={"Authorization": f"Bearer {access}"})):
                myobj = {'buyer_id': a["buyerId"], 'showroom_id': int(profitable["showroom_id"]),
                         'amount_of_purchase':
                             int(requests.get
                                 (url, headers={"Authorization": f"Bearer {access}"}).json()['amount_of_purchase']) + 1
                         }

                xz = requests.put(url, json=myobj, headers={"Authorization": f"Bearer {access}"})
                print(xz.json())  # обновление количества покупок уникального покупателя
            else :
                myobj = {'buyer_id': a["buyerId"], 'showroom_id': int(profitable["showroom_id"]),
                         'amount_of_purchase': 1}

                xz = requests.post(url, json=myobj, headers={"Authorization": f"Bearer {access}"})
                print(xz.json())  # добавление уникального покупателя

        else : print("Not enough money")



