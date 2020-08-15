import requests


class Testappsent:

    def test_get_appsent(self):
        r = requests.get("https://httpbin.testing-studio.com/")
        print(r.status_code)
        if (r.status_code == 200):
            print("ok")
        else :
            print("fail")



