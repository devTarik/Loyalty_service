from celery_app.clickhouse_models import TotalBalance
from datetime import datetime
import requests


def balance():
    try:
        response = requests.get("http://localhost:8000/api/v1/points/nopermition/all/").json()
        point = 0
        for item in response:
            point += item['points']
        try:
            TotalBalance.objects.create(balance=point, datetime=datetime.now())
            print('Total balance save to ClickHouse')
        except:
            print('Can`t save to ClickHouse')
    except:
        print('No connent with server')


def control_balance(client_id):
    try:
        response = requests.get(f"http://localhost:8000/api/v1/points/nopermition/detail/{client_id}").json()
        if response['points'] >= 1000 or response['points'] == 0:
            print (f"""ID = {str(response['id'])}\
                    \nName = {str(response['name'])}\
                    \nPoints = {str(response['points'])}""")
    except:
        print('No connent with server')