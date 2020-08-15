import requests


class TestHttp():
    def test_http_get(self):
        r = requests.get(url='http://api.github.com/events')
        print(r.text)
        print(r.status_code)
        assert r.status_code == 200

    def test_http_post(self):
        r1 = requests.post('http://httpbin.org/post', data={"fan1": "fan1"})
        r2 = requests.post('http://httpbin.org/post', json={"fan2": "fan2"})
        print(r1.json())
        print(r2.json())
        print(r2.json()['headers']['User-Agent'])