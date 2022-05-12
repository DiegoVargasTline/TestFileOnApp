import pytest
import requests

def testProcess():

    url = 'https://pydevc6.paasmx.connectnow.global/onapp'
    data = {
        "subscription":11,
        "customer":{
            "id":8,
            "name":"Unit test",
            "street":"xxxx",
            "email":"test@test.com"
        },
        "params":{
            "project":{
                "login":"unittest",
                "email":"test@test.com",
                "first_name":"Unit",
                "last_name":"Test",
                "password":"",
                "name_package":"LiveWire Plan",
                "id_package":"19",
                "cluster": "UK"
            }
        },
        "mp": "onapp"
    }

    print('\n---------------------------')
    print('\nInicio de prueba de compra')

    responsePurchase = requests.post(url + '/purchase', json = data)
    assert responsePurchase.status_code == 200

    print("\n")
    print(responsePurchase.json())

    print('\nTest Purchase is successful')
    print('\nFin prueba de compra')

    print('\n---------------------------')
    print('\nInicio prueba de suspension')

    data = responsePurchase.json()

    customer = data['Msg']

    r = requests.post(url + '/suspend', json = customer)
    assert r.status_code == 200

    print('\nTest suspend account is successful')
    print('\nFin prueba de suspension')

    print('\n---------------------------')
    print('\nInicio prueba de activacion')

    r = requests.post(url + '/resume', json = customer)
    assert  r.status_code == 200

    print('\nTest Activate account is successful')
    print('\nfin prueaba de activacion')

    print('\n---------------------------')
    print('\nInicio prueba de cancelacion')

    r = requests.post(url + '/cancel', json = customer)
    assert r.status_code == 200

    print('\nTest cancel is successful')
    print('\n---------------------------')


def testProcesMx():

    url = 'https://pydevc6.paasmx.connectnow.global/onapp'
    dataMX = {
        "subscription":11,
        "customer":{
            "id":8,
            "name":"Diego Vargas",
            "street":"xxxx",
            "email":"test@test.com"
        },
        "params":{
            "project":{
                "login":"testJenkins",
                "email":"test@test.com",
                "first_name":"test",
                "last_name":"test",
                "password":"",
                "name_package":"LiveWire Plan",
                "id_package":"3",
                "cluster": "MX"
            }
        },
        "mp": "onapp"
    }

    print('\n---------------------------')
    print('\nInicio de prueba de compra')

    responsePurchaseMex = requests.post(url + '/purchase', json = dataMX)
    assert responsePurchaseMex.status_code == 200

    print("\n")
    print(responsePurchaseMex.json())

    print('\nTest Purchase is successful')
    print('\nFin prueba de compra')

    print('\n---------------------------')
    print('\nInicio prueba de suspension')

    dataMX = responsePurchaseMex.json()

    customerMX = dataMX['Msg']

    rMX = requests.post(url + '/suspend', json = customerMX)
    assert rMX.status_code == 200

    print('\nTest suspend account is successful')
    print('\nFin prueba de suspension')

    print('\n---------------------------')
    print('\nInicio prueba de activacion')

    rMX = requests.post(url + '/resume', json = customerMX)
    assert  rMX.status_code == 200

    print('\nTest Activate account is successful')
    print('\nfin prueaba de activacion')

    print('\n---------------------------')
    print('\nInicio prueba de cancelacion')

    rMX = requests.post(url + '/cancel', json = customerMX)
    assert rMX.status_code == 200

    print('\nTest cancel is successful')
    print('\n---------------------------')
