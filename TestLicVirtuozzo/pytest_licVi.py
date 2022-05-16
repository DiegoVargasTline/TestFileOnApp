import pytest
import requests

def test_LicVi():
    url = 'https://pydevc6.paasmx.connectnow.global/licvi'
    data = {
        "subscription": 0,
        "customer": {
            "id": 0,
            "name": "Test ",
            "street": " street Test",
            "email": "test@test.com"
        },
        "params": {
            "project": {
                "user": "julio_luna",
                "password": "ggXjnPEfWhKCtwGSr2zzIrcxxz6QgDgZ",
                "ip": "172.16.24.219",
                "mac": "00:0c:29:13:d0:8e",
                "cliente": "1037896251",
                "product": "VIRTUOZZO-7-PAYG"
            }
        },
        "mp": "ecommerse"
    }

    print('\n---------------------------')
    print('\nInicio de prueba de compra')

    compraLicVi = requests.post(url + '/purchase', json = data)
    assert compraLicVi.status_code == 200
    print(compraLicVi.json())
    dataLicVi = compraLicVi.json()
    assert dataLicVi['Success'] == 1

    print('\n---------------------------')
    print('\nInicio prueba de cancelacion')

    dataLicVi = compraLicVi.json()
    _data = dataLicVi['Msg']

    cancelLicVi = requests.post(url + '/cancel', json =_data)
    assert cancelLicVi.status_code == 200