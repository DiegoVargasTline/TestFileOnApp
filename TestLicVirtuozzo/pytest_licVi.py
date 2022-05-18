import pytest
import requests
    
url = 'https://pydevc6.paasmx.connectnow.global/licvi'

def test_LicVi():
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


def test_vendorBilling():

    print('\n---------------------------')
    print('\nInicio prueba de vendorBilling\n')

    vendorBilling = requests.get(url + '/vendorBilling')

    assert vendorBilling.status_code == 200

    print(vendorBilling.json())


def test_providerBilling():

    print('\n---------------------------')
    print('\nInicio prueba de providerBilling\n')

    providerBilling = requests.get(url + '/providerBilling')

    assert providerBilling.status_code == 200

    print(providerBilling.json())