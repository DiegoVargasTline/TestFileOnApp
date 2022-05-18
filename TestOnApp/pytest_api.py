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
    dataTest = responsePurchase.json()
    assert dataTest['Success'] == 1
    assert len(dataTest['Visible']) > 0
    assert len(dataTest['Msg']) > 0

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
    suspend = r.json()
    assert suspend['Success'] == 1

    print('\nTest suspend account is successful')
    print('\nFin prueba de suspension')

    print('\n---------------------------')
    print('\nInicio prueba de activacion')

    r = requests.post(url + '/resume', json = customer)
    assert  r.status_code == 200
    resume = r.json()
    assert resume['Success'] == 1

    print('\nTest Activate account is successful')
    print('\nfin prueaba de activacion')

    print('\n---------------------------')
    print('\nInicio prueba de cancelacion')

    r = requests.post(url + '/cancel', json = customer)
    assert r.status_code == 200
    cancel = r.json()
    assert cancel['Success'] == 1

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
    dataTest = responsePurchaseMex.json()
    assert dataTest['Success'] == 1
    assert len(dataTest['Visible']) > 0
    assert len(dataTest['Msg']) > 0

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
    suspend = rMX.json()
    assert suspend['Success'] == 1

    print('\nTest suspend account is successful')
    print('\nFin prueba de suspension')

    print('\n---------------------------')
    print('\nInicio prueba de activacion')

    rMX = requests.post(url + '/resume', json = customerMX)
    assert  rMX.status_code == 200
    resume = rMX.json()
    assert resume['Success'] == 1

    print('\nTest Activate account is successful')
    print('\nfin prueaba de activacion')

    print('\n---------------------------')
    print('\nInicio prueba de cancelacion')

    rMX = requests.post(url + '/cancel', json = customerMX)
    assert rMX.status_code == 200
    cancel = rMX.json()
    assert cancel['Success'] == 1

    print('\nTest cancel is successful')
    print('\n---------------------------')



def test_billingDetail():

    url = 'https://pydevc6.paasmx.connectnow.global/onapp'

    data = {
            "Customer": {
                "UserId": "7",
                "Email": "yarko_email@test.com",
                "BucketId": "11",
                "User_GroupId": "34",
                "FirstName": "Yarko",
                "LastName": "Test",
                "Status": "active",
                "Password": "CakN(Ai#82ke",
                "UserName": "yarko_login",
                "Cluster": "UK"
            },
            "StartDate": "2022-04-01",
            "EndDate": "2022-04-31"
    }

    print('\n---------------------------')
    print('\nInicio prueba Billing UK\n')

    getBillingOnApp = requests.get(url + '/BillingDetail', json = data)
    assert getBillingOnApp.status_code == 200

    print(getBillingOnApp.json())


def test_billingDetailMX():

    url = 'https://pydevc6.paasmx.connectnow.global/onapp'

    data = {
        "Customer": {
            "UserId": "1",
            "Email": "admin@example.com",
            "BucketId": "11",
            "User_GroupId": "34",
            "FirstName": "Admin",
            "LastName": "OnApp",
            "Status": "active",
            "Password": "CakN(Ai#82ke",
            "UserName": "admin",
            "Cluster": "MX"
        },
        "StartDate": "2022-04-01",
        "EndDate": "2022-04-31"
    }

    print('\n---------------------------')
    print('\nInicio prueba Billing MX\n')

    getBillingOnApp = requests.get(url + '/BillingDetail', json = data)
    assert getBillingOnApp.status_code == 200

    print(getBillingOnApp.json())