import requests
from datetime import datetime

def makeStatisticsForSales():

    myobj = {'username': 'asd', "password": "112233Zz"}  # login

    access = requests.post('http://127.0.0.1:8000/api/v1/token/', json=myobj).json()['access']  # access token

    urlToGetShowrooms = 'http://127.0.0.1:8000/api/v1/showroom/'

    showrooms = requests.get(urlToGetShowrooms, headers={"Authorization": f"Bearer {access}"}).json()

    for temp in showrooms:
        urlToGetHistory = f'http://127.0.0.1:8000/api/v1/history/?search={temp["showroom_id"]}'
        amount = len(requests.get(urlToGetHistory, headers={"Authorization": f"Bearer {access}"}).json())

        urlToMakeStatistics = f'http://127.0.0.1:8000/api/v1/statistics/'
        myobj = {'name': f"showroom {temp['showroom_id']} sales statistics",
                 'desc': 'Отображает количество продаж в определенном автосалоне',
                 'content': f'количество продаж : {amount}',
                 'date':datetime.now().isoformat()}
        requests.post(urlToMakeStatistics, json=myobj, headers={"Authorization": f"Bearer {access}"})

def makeStatisticsForProfit():
    myobj = {'username': 'asd', "password": "112233Zz"}  # login

    access = requests.post('http://127.0.0.1:8000/api/v1/token/', json=myobj).json()['access']  # access token

    urlToGetShowrooms = 'http://127.0.0.1:8000/api/v1/showroom/'

    showrooms = requests.get(urlToGetShowrooms, headers={"Authorization": f"Bearer {access}"}).json()
    profit = 0

    for temp in showrooms:
        urlToGetHistory = f'http://127.0.0.1:8000/api/v1/history/?search={temp["showroom_id"]}'
        for temp1 in requests.get(urlToGetHistory,headers={"Authorization": f"Bearer {access}"}).json():
            profit +=temp1['price']

        urlToMakeStatistics = f'http://127.0.0.1:8000/api/v1/statistics/'
        myobj = {'name': f"showroom {temp['showroom_id']} profit statistics",
                 'desc': 'Отображает прибыль определенного автосалона',
                 'content': f'прибыль : {profit}',
                 'date':datetime.now().isoformat()}
        requests.post(urlToMakeStatistics, json=myobj, headers={"Authorization": f"Bearer {access}"})

def makeStatisticsForUnique():
    myobj = {'username': 'asd', "password": "112233Zz"}  # login

    access = requests.post('http://127.0.0.1:8000/api/v1/token/', json=myobj).json()['access']  # access token

    urlToGetShowrooms = 'http://127.0.0.1:8000/api/v1/showroom/'

    showrooms = requests.get(urlToGetShowrooms, headers={"Authorization": f"Bearer {access}"}).json()

    for temp in showrooms:
        urlToGetHistory = f'http://127.0.0.1:8000/api/v1/showroomUniqueBuyers/?search={temp["showroom_id"]}'
        amount = len(requests.get(urlToGetHistory, headers={"Authorization": f"Bearer {access}"}).json())

        urlToMakeStatistics = f'http://127.0.0.1:8000/api/v1/statistics/'
        myobj = {'name': f"showroom {temp['showroom_id']} unique buyers statistics",
                 'desc': 'Отображает количество уникальных покупателей в определенном автосалоне',
                 'content': f'количество покупателей : {amount}',
                 'date': datetime.now().isoformat()}
        requests.post(urlToMakeStatistics, json=myobj, headers={"Authorization": f"Bearer {access}"})








