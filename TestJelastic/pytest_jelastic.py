import requests
import pytest

def test_jelastic():
    url = 'https://pydevc6.paasmx.connectnow.global/jelas'
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

    responseJelas = requests.post(url + '/purchase', json = data)
    assert responseJelas.status_code == 200
    dataJelas = responseJelas.json()
    print(dataJelas)

    assert dataJelas["Success"] == 1

    print('\n---------------------------')
    print('\nInicio prueba de suspension') 
    
    email = dataJelas['Msg']
    suspendJelas = requests.post(url + '/suspend', json = email)
    assert suspendJelas.status_code == 200
    
    print('\n---------------------------')
    print('\nInicio prueba de activacion')

    resumeJelas = requests.post(url + '/resume', json  = email)
    assert resumeJelas.status_code == 200

    print('\n---------------------------')
    print('\nInicio prueba de cancelacion')

    cancelJelas = requests.post(url + '/cansel', json = email)
    assert cancelJelas.status_code == 200