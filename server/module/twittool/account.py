import requests
import json

from requests.api import head, request

def _read_api_data():
    with open("data/twitterApi.json", 'r', encoding='utf8') as r_file :
        r_file = json.load(r_file)
        return dict(r_file)

def _write_api_result(content : str):
    with open("result.json", 'w', encoding='utf8') as w_file:
        json.dump(content, w_file)

class _Client_Data :    
    def __init__(self) :
        self.BASE_URL = "https://api.twitter.com/1.1/users/show.json?"
        self.api_log = _read_api_data()
        self.parameters = {
            "screen_name" : None
        }
        self.headers = {
            "authorization": f"Bearer {self.api_log['bearer_token']}"
        }

    def d_request(self, at : str, dev = False):
        self.parameters['screen_name'] = at
        d_result = requests.get(
            url = self.BASE_URL, 
            headers = self.headers, 
            params= self.parameters
        )

        if dev :
            _write_api_result(d_result.json())

        return d_result.json()


class Account :
    
    def __init__(self, arobase : str):
        self.at = arobase
        self._client_instance = _Client_Data()
        self._account_data = self._client_instance.d_request(self.at)
        
    def serialize(self):
        self.id = self._account_data['id']
        self.name = self._account_data['name']
        self.description = self._account_data['description']

