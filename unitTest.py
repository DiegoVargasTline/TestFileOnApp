import unittest
import requests


class TestOnApp(unittest.TestCase):
    url = 'http://env-0752280.paasmx.connectnow.global/onapp'
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
    resp = ''

    customer = {
            "Customer": {
            "UserId": "187",
            "Email": "test@test.com",
            "BucketId": "263",
            "User_GroupId": "51",
            "FirstName": "Unit ",
            "LastName": "Test",
            "Status": "active",
            "Password": "2ZkH#Hyvbnzq",
            "UserName": "unittest",
            "Cluster": "UK"
        }
    }

    def testPurchaseOnapp(self):
        urlpurchase =self.url + '/purchase'
        self.resp = requests.post(urlpurchase, json = self.data)
        self.assertEqual(self.resp.status_code, 200)
        print('Test Purchase is successful')

    def testCancelOnapp(self):
        resp = requests.post(self.url+ '/cancel', json = self.customer)
        self.assertEqual(resp.status_code, 200)
        print('Test cancel is successful')
    
    def testSuspend(self):
        #suspendurl = f"{self.url}/suspend"
        resp = requests.post(self.url + '/suspend', json = self.customer)
        self.assertEqual(resp.status_code, 200)
        print('Test suspend account is successful')
    
    def testActivate(self):
        resp = requests.post(self.url + '/resume', json = self.customer)
        self.assertEqual(resp.status_code, 200)
        print('Test Activate account is successful')

    def testProcess(self):
        print('\n---------------------------')
        print('\nInicio de prueba de compra')
        respPurchase = requests.post(self.url + '/purchase', json = self.data)
        self.assertEqual(respPurchase.status_code, 200)
        print('\nTest Purchase is successful')
        print('\nFin prueba de compra')
       
        print('\n---------------------------')
        print('\nInicio prueba de suspension')
        data = respPurchase.json()
        customer = data['Msg']
        resp = requests.post(self.url + '/suspend', json = customer)
        self.assertEqual(resp.status_code, 200)
        print('\nTest suspend account is successful')
        print('\nFin prueba de suspension')

        print('\n---------------------------')
        print('\nInicio prueba de activacion')
        resp = requests.post(self.url + '/resume', json = customer)
        self.assertEqual(resp.status_code, 200)
        print('\nTest Activate account is successful')
        print('\nfin prueaba de activacion')

        print('\n---------------------------')
        print('\nInicio prueba de cancelacion')
        resp = requests.post(self.url+ '/cancel', json = customer)
        self.assertEqual(resp.status_code, 200)
        print('\nTest cancel is successful')
        print('\n---------------------------')




if __name__ == "__main__":
    tester = TestOnApp()

    #tester.testPurchaseOnapp()
    #tester.testCancelOnapp()
    #tester.testSuspend()
    #tester.testActivate()
    tester.testProcess()

 #comando para arrancar las pruebas
 # pasar a ambiente virtual
 # venv/Script/activate
 # en consola ir al directorio donde estan las pruebas
 # python unitTest.py