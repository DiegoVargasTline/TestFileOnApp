import requests
import pytest

urlJelastic ='https://pydevc6.paasmx.connectnow.global/jelas'

def test_jelastic():
    data ={
        "subscription": 0,
        "customer": {
            "id": 0,
            "name": "Py test",
            "street": "calle prueba",
            "email": "test@test.com"
        },
        "params": {
            "project": {
            "email": "test1@test1.com"
            }
        },
        "mp": "ecommerse"
    }

    print('\n---------------------------')
    print('\nInicio de prueba de compra')

    responseJelas = requests.post(urlJelastic + '/purchase', json = data)
    assert responseJelas.status_code == 200
    dataJelas = responseJelas.json()
    print(dataJelas)

    assert dataJelas["Success"] == 1

    print('\n---------------------------')
    print('\nInicio prueba de suspension') 
    
    email = dataJelas['Msg']
    suspendJelas = requests.post(urlJelastic + '/suspend', json = email)
    assert suspendJelas.status_code == 200
    
    print('\n---------------------------')
    print('\nInicio prueba de activacion')

    resumeJelas = requests.post(urlJelastic + '/resume', json  = email)
    assert resumeJelas.status_code == 200

    print('\n---------------------------')
    print('\nInicio prueba de cancelacion')

    cancelJelas = requests.post(urlJelastic + '/cansel', json = email)
    assert cancelJelas.status_code == 200


def test_Billing():

    pay = {
        "subscription":2,
        "customer":{
            "id":8,
            "name":"",
            "street":"",
            "email":""
        },
        "params":{
            "project":{
                "email":"diego.vargas@tline.com",
                "method":"PAY",
                "amount":"400.00"
            }
        }
    }

    data = {
        "subscription":2,
        "customer":{
            "id":8,
            "name":"",
            "street":"",
            "email":""
        },
        "params":{
            "project":{
                "email":"diego.vargas@tline.com",
                "method":"DATA",
                "period":"MONTH",
                "starttime":"2021-01-26 00:00:00",
                "endtime":"2022-05-17 00:00:00"
            }
        }
    }

    print('\n---------------------------')
    print('\nInicio de prueba de fondeo para jelastic\n')

    postPayBilling = requests.post(urlJelastic + '/billing', json = pay)
    assert postPayBilling.status_code == 200
    dataBilling = postPayBilling.json()
    assert dataBilling["Success"] == 1
    print(postPayBilling.json())

    print('\n---------------------------')
    print('\nInicio de prueba billing\n')

    getBilling = requests.post(urlJelastic + '/billing', json = data)
    assert getBilling.status_code == 200
    datagetBilling = getBilling.json()
    assert datagetBilling["Success"] == 1
    print(getBilling.json())


def test_Reseller():

    data = {
        "subscription":2,
        "customer":{
            "id":8,
            "name":"Test Jenkins",
            "street":"12-34:56/89",
            "email":"diego.vargas@tline.com"
        },
        "params":{
            "project":{
                "email":"diego.vargas@tline.com",
                "reseller":{
                    "name":"testJenkis",
                    "ownerUid":"508",
                    "comment":"test"
                },
                "platform":{
                    "domain":"testJenkins.paasmx.connectnow.global",
                    "sslEnabled":True,
                    "sslType":"LETSENCRYPT"
                },
                "regions":[
                    {
                    "regionId":1,
                    "domain":"testJenkins.paasmx.connectnow.global",
                    "sslEnabled":True,
                    "sslType":"LETSENCRYPT"
                    }
                ]
            }
        }
    }

    print('\n---------------------------')
    print('\nInicio de prueba de reseller\n')    

    getReseller = requests.post(urlJelastic + '/reseler', json= data)
    assert getReseller.status_code == 200

    print(getReseller.json())
