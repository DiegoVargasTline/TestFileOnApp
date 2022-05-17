import pytest
import requests


def test_Acronis():

    url = 'https://pydevc6.paasmx.connectnow.global/acronis'

    data = {
        "subscription":382,
        "customer":{
            "id":15,
            "name":"Test Jenkins",
            "street":"REFORMA 404",
            "email":"test@test.com"
        },
        "params":{
            "project":{
                "email":"testjenkins@testjenkins.com",
                "first_name":"Test",
                "last_name":"Jenkins",
                "nameTenant":"Tenant Test from Jenkins",
                "gigabytes":10,
                "addons":{
                        "advance_secutiry":0,
                        "advance_backup":{
                            "workstation":0,
                            "servers":0,
                            "vm":0,
                            "webhosting":0
                        },
                    "advance_email_security":0,
                    "advance_edr":0,
                    "advance_management":0,
                    "advance_disaster":0,
                    "file_and_sync":0
                }
            }
        },
        "mp":"ecommerse"
    }


    print('\n---------------------------')
    print('\nInicio de prueba de compra')

    responseAcronis = requests.post(url + '/purchase', json  = data)
    assert responseAcronis.status_code == 200
    dataAcronis = responseAcronis.json()
    assert dataAcronis['Success'] == 1
    assert len(dataAcronis['Visible']) > 0
    assert len(dataAcronis['Msg']) > 0

    print("\n")
    print(dataAcronis)


    print('\n---------------------------')
    print('\nInicio prueba de suspension')

    customer = dataAcronis['Msg']
    suspendAcronis = requests.post(url + '/suspend', json = customer)
    assert suspendAcronis.status_code == 200    

    print('\n---------------------------')
    print('\nInicio prueba de activacion') 

    activateAcronis = requests.post(url + '/resume', json = customer)
    assert activateAcronis.status_code == 200

    print('\n---------------------------')
    print('\nInicio prueba de cancelacion')

    cancelAcronis = requests.post(url + '/cancel', json = customer)
    assert cancelAcronis.status_code == 200    