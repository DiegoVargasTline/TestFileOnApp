import pytest
import requests

def testProcess():

    url = 'http://127.0.0.1:5000/onapp'
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

