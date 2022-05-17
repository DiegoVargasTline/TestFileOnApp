import pytest
import requests

url = 'https://pydevc6.paasmx.connectnow.global/jelas/purchase_wp'

def test_Wordpress():
    data= {
        "subscription":2,
        "customer":{
            "id":8,
            "name":"",
            "street":"",
            "email":"XXXX"
        },
        "params":{
            "project":{
                "email":"testWp2@testWP2.com"
            }
        }
    }

    print('\n---------------------------')
    print('\nInicio de prueba de compra\n')
    
    wp_ = requests.post(url , json= data)
    assert wp_.status_code == 200

    #print(wp_.json())