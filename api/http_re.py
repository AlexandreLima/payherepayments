import requests
import json

class HttpRequest(object):
    def __init__(self, *args):
        super(HttpRequest, self).__init__(*args)

    def get(self, url, params, headers):
        response = requests.get(url = url, params = params, headers = headers)
        return response.json()

    def post(self, url, data, headers):
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response.json()

    def put(self, url, headers):
        pass

    def delete(self, url, params, headers):
        pass
