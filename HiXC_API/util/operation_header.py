# coding:utf-8
import requests
import json
from util.operation_json import OperetionJson


class OperationHeader:

    def __init__(self, response):
        self.response = json.loads(response)

    def get_response_url(self):
        '''
		获取登录返回的token的url
		'''
        url = self.response['data']['token'][0]
        return url

    def get_token(self):
        '''
        获取登录返回的token做参数化处理
        '''
        token = self.response['data']
        return token

    def get_cookie(self):
        '''
		获取cookie的jar文件
		'''
        url = self.get_response_url() + "&callback=jQuery21008240514814031887_1508666806688&_=1508666806689"
        cookie = requests.get(url).cookies
        return cookie

    def write_cookie(self):
        cookie = requests.utils.dict_from_cookiejar(self.get_cookie())
        op_json = OperetionJson()
        op_json.write_data(cookie)

    def write_token(self):
        token = self.get_token()
        op_json = OperetionJson()
        op_json.write_data(token)

    def write_user_token(self):
        token = self.get_token()
        op_json = OperetionJson()
        op_json.write_user_data(token)


if __name__ == '__main__':
    url = "https://dev.baojiahuxing.com/api/app/account/common/app/login"
    data = {
        "username": "18256564640",
        "password": "123"
    }
    header = {
        "Content-Type": "application/json;utf-8"
    }
    postData = json.dumps(data)
    res = json.dumps(requests.request("POST", url, data=postData, headers=header).json())
    op_header = OperationHeader(res)
    token = op_header.write_token()
    print("token ====== %s"%token)