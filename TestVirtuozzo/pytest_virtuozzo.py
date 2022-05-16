import requests
import pytest

@pytest.mark.parametrize("type", [("FREE")])
def test_Virtuozzo(type):
    url = 'https://pydevc6.paasmx.connectnow.global/vi'
    data = {
        "subscription": 0,
        "customer": {
            "id": 0,
            "name": "Test",
            "street": "calle de prueba",
            "email": "test@test.com"
        },
        "params": {
            "project": {
                "domain_name": "Prueba Virtuozzo",
                "domain_description": "Prueba QA",
                "project_name": "Test QA",
                "project_description": "string",
                "user_name": "TestVir",
                "password": "Tline123",
                "type": "FREE"
            },
            "vm": {
                "CPU": 1,
                "Storage": 10,
                "RAM": 2,
                "FloatingIp": 0,
                "LoadBalancer": 0,
                "K8sass": 0
            },
            "server": "Mexico"
        },
        "mp": "ecommerse"
    }

    if data["params"]["project"]:
        data["params"]["project"]['type'] = type
    
    print("\nInicio prueba de compra Virtuozzo")
    responseVi = requests.post(url + '/purchase', json = data)
    assert responseVi.status_code == 200
    dataResponse = responseVi.json()
    assert dataResponse['Success'] == 1


    print("\nInicio prueba de suspension")
    
    customer = responseVi['Msg']
    suspendVi = requests.post(url + '/suspend_project', json = customer)
    assert suspendVi.status_code == 200

    print("\nInicio prueba de cancelacion")
    cancelVi = requests.post(url + '/cancel_domains', json = data)
    assert cancelVi.status_code == 200