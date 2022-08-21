from datetime import datetime

import requests

url = 'http://127.0.0.1:8000/api/v1/token/'
myobj = {'username': 'asd',"password":"112233Zz"} # login

x = requests.post(url, json = myobj)
access = x.json()['access'] # access token
id = requests.get("http://127.0.0.1:8000/api/v1/auth/users/me/",headers={"Authorization":f"Bearer {access}"}).json()['id']


url = 'http://127.0.0.1:8000/api/v1/createoffer/'
myobj = {'buyerId': id,"maxPrice":"25000","mark":"bmw","model":"f30"} #url and object to create object

url1 = f'http://127.0.0.1:8000/api/v1/buyers/{id}/' #url to get buyer with buyerId from offer
temp = requests.get(url1,headers={"Authorization":f"Bearer {access}"})
a = temp.json()
print(a)
if int(a['balance']) >= int(myobj['maxPrice']):
    x= requests.post(url, json = myobj,headers={"Authorization":f"Bearer {access}"}) #url to create offer

    urlToGetCars = f'http://127.0.0.1:8000/api/v1/showroomCars/?search={x.json()["mark"]},{x.json()["model"]}'
    urlToGetDiscount = f'http://127.0.0.1:8000/api/v1/showroomDiscount/?search={x.json()["mark"]},{x.json()["model"]}'

    response = requests.get(urlToGetCars,headers={"Authorization":f"Bearer {access}"})
    response1 = requests.get(urlToGetDiscount,headers={"Authorization":f"Bearer {access}"})

    profitable = response.json()[0]

    if response1.json() :
        for i in response.json():
            for k in response1.json():
                if i['showroom'] == k['showroom']:
                    if profitable['price'] > (i['price'] * (1 - (k['percent']/100))):
                        profitable = i
                        discount = k
        if (int(myobj['maxPrice']) >= int(profitable['price'])*(1-(discount["percent"]/100))) \
                and (int(profitable['ammount_of_cars']) > 0):

            url = f'http://127.0.0.1:8000/api/v1/buyers/?search={myobj["buyerId"]}' # ищем пользователя с байер айди
            resp = requests.get(url,headers={"Authorization":f"Bearer {access}"}).json()

            myobj = {'name':resp["name"],'surname':resp["surname"],
                             'email':resp["email"],'phoneNumber':resp["phoneNumber"],'id':resp["id"],
                            'balance' : resp['balance'] - (profitable['price'] * (1 - (discount['percent']/100)))}

            url = f'http://127.0.0.1:8000/api/v1/buyers/{id}/'
            xz = requests.put(url, json=myobj, headers={"Authorization": f"Bearer {access}"}) #обновление баланса пользователя
            print(xz.json())

            url = f'http://127.0.0.1:8000/api/v1/showroom/{profitable["id"]}/'

            myobj = {'name': requests.get(url, headers={"Authorization": f"Bearer {access}"}).json()['name'],
                     'content': requests.get(url, headers={"Authorization": f"Bearer {access}"}).json()['content'],
                     'balance': int(
                         requests.get(url, headers={"Authorization": f"Bearer {access}"}).json()['balance']) +
                                profitable['price'],
                     'location': requests.get(url, headers={"Authorization": f"Bearer {access}"}).json()[
                         'location'],
                     'showroom': requests.get(url, headers={"Authorization": f"Bearer {access}"}).json()[
                         'showroom']
                     }
            rofl = requests.put(url, json=myobj, headers={"Authorization": f"Bearer {access}"})

            url = f'http://127.0.0.1:8000/api/v1/buyersHistory/'

            myobj = {'buyer':resp['id'],'price':profitable['price'] * (1 - (discount['percent']/100))
                ,'showroom':profitable['showroom']}

            xz = requests.post(url, json=myobj, headers={"Authorization": f"Bearer {access}"})
            print(xz.json()) # обновление истории пользователя

            url = f'http://127.0.0.1:8000/api/v1/showroomCars/{profitable["id"]}/'

            myobj = {'engine_type': profitable["engine_type"], 'max_speed': int(profitable["max_speed"]),
                     'ammount_of_eng': int(profitable["ammount_of_eng"]),'model': profitable["model"],
                     'mark': profitable["mark"],'showroom': int(profitable["showroom"]),
                     'price': int(profitable["price"]),'ammount_of_cars': int(profitable["ammount_of_cars"])-1,}
            xz = requests.put(url, json=myobj, headers={"Authorization": f"Bearer {access}"})
            print(xz.json()) #обновление количества машин в автосалоне

            url = f'http://127.0.0.1:8000/api/v1/history/'

            myobj = {'buyer': a["id"], 'price': profitable['price'] * (1 - (discount['percent']/100)),
                     'showroom': int(profitable["showroom"])}

            xz = requests.post(url, json=myobj, headers={"Authorization": f"Bearer {access}"})
            print(xz.json())  # добавление покупки в историю покупок автосалона

            url = f'http://127.0.0.1:8000/api/v1/showroomUniqueBuyers/{a["buyerId"]}/'


            if(requests.get(url,headers={"Authorization": f"Bearer {access}"})):
                myobj = {'buyer': a["id"], 'showroom': int(profitable["showroom"]),
                         'amount_of_purchase':
                             int(requests.get
                                 (url, headers={"Authorization": f"Bearer {access}"}).json()['amount_of_purchase']) + 1
                         }

                xz = requests.put(url, json=myobj, headers={"Authorization": f"Bearer {access}"})
                print(xz.json())  # обновление количества покупок уникального покупателя
            else :
                myobj = {'buyer': a["id"], 'showroom': int(profitable["showroom"]),
                         'amount_of_purchase': 1}

                xz = requests.post(url, json=myobj, headers={"Authorization": f"Bearer {access}"})
                print(xz.json())  # добавление уникального покупателя

        else : print("Not enough money")




    else:
        for xy in response.json():
            if xy['price'] < profitable['price']:
                profitable=xy

        if (int(myobj['maxPrice']) >= int(profitable['price'])) and (int(profitable['ammount_of_cars']) > 0):
            url = f'http://127.0.0.1:8000/api/v1/buyers/{id}/' # ищем пользователя с байер айди
            resp = requests.get(url,headers={"Authorization":f"Bearer {access}"}).json()


            myobj = {'name':resp["name"],'surname':resp["surname"],
                             'email':resp["email"],'phoneNumber':resp["phoneNumber"],'buyer':resp["id"],
                            'balance' : f"{resp['balance']-profitable['price']}"}
            url = f'http://127.0.0.1:8000/api/v1/buyers/{id}/'
            xz = requests.put(url, json=myobj, headers={"Authorization": f"Bearer {access}"}) #обновление баланса пользователя


            url = f'http://127.0.0.1:8000/api/v1/buyersHistory/'
            myobj = {'buyer':resp['id'],'price':profitable['price'],'showroom':profitable['showroom'],'date':datetime.now().isoformat()}
            xz = requests.post(url, json=myobj, headers={"Authorization": f"Bearer {access}"})
             # обновление истории пользователя


            url=f'http://127.0.0.1:8000/api/v1/showroom/{profitable["showroom"]}/'

            myobj={'name':requests.get(url,headers={"Authorization": f"Bearer {access}"}).json()['name'],
                   'content':requests.get(url,headers={"Authorization": f"Bearer {access}"}).json()['content'],
                   'balance':int(requests.get(url,headers={"Authorization": f"Bearer {access}"}).json()['balance'])+profitable['price'],
                   'location':requests.get(url,headers={"Authorization": f"Bearer {access}"}).json()['location'],
                   }
            rofl = requests.put(url,json=myobj,headers={"Authorization": f"Bearer {access}"})


            url = f'http://127.0.0.1:8000/api/v1/showroomCars/{profitable["showroom"]}/'
            myobj = {'engine_type': profitable["engine_type"], 'max_speed': int(profitable["max_speed"]),
                     'ammount_of_eng': int(profitable["ammount_of_eng"]),'model': profitable["model"],
                     'mark': profitable["mark"],'showroom': int(profitable["showroom"]),
                     'price': int(profitable["price"]),'ammount_of_cars': int(profitable["ammount_of_cars"])-1,}
            xz = requests.put(url, json=myobj, headers={"Authorization": f"Bearer {access}"})
             #обновление количества машин в автосалоне

            url = f'http://127.0.0.1:8000/api/v1/history/'

            myobj = {'buyer': a["id"], 'price': int(profitable["price"]),
                     'showroom': int(profitable["showroom"]),'date':datetime.now().isoformat()}
            xz = requests.post(url, json=myobj, headers={"Authorization": f"Bearer {access}"})
              # добавление покупки в историю покупок автосалона

            url = f'http://127.0.0.1:8000/api/v1/showroomUniqueBuyers/{a["id"]}/'

            # re = requests.get(url,headers={"Authorization": f"Bearer {access}"}).json()
            # re_id = re[0]['id']

            if(requests.get(url,headers={"Authorization": f"Bearer {access}"}).json()):
                myobj = {'buyer': a["id"], 'showroom': int(profitable["showroom"]),
                         'amount_of_purchase': int(requests.get(url, headers={"Authorization": f"Bearer {access}"}).json()['amount_of_purchase']) + 1}
                url = f'http://127.0.0.1:8000/api/v1/showroomUniqueBuyers/{a["id"]}/'
                xz = requests.put(url, json=myobj, headers={"Authorization": f"Bearer {access}"})
                  # обновление количества покупок уникального покупателя
            else :
                myobj = {'buyer': a["id"], 'showroom': int(profitable["showroom"]),
                         'amount_of_purchase': 1}

                xz = requests.post(url, json=myobj, headers={"Authorization": f"Bearer {access}"})
                  # добавление уникального покупателя

        else : print("Not enough money")


