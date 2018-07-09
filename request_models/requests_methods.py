import requests
import json
from helpers import setup


class REQ():

    def __init__(self):

        self.req = requests.Session()

    def get(self, endpoint):
        """
        This method is used to make a GET Rest request endpoint is needed
        """
        result = self.req.get(endpoint, headers=setup.headers)
        rs_code = result.status_code
        rs_body = result.json()


        return [rs_code, rs_body]


    def post(self, endpoint, payload):
        """
        This method is used to make a POST Rest request endpoint is needed
        """

        result = self.req.post(setup.base_url+endpoint, headers=setup.headers, data=payload)
        rs_code = result.status_code
        rs_body = result.json()

        print("I am the item body {}".format(rs_body))
        return [rs_code, rs_body]

