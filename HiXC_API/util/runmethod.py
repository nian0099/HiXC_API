# coding:utf-8
import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DEV_URL = "https://dev.baojiahuxing.com/api/app"
ADMIN_URL = "https://admin.baojiahuxing.com/api/app"
TEST_URL = "http://192.168.10.14:8765/api/app"


class RunMethod:

    def post_main(self, url, data, header=None):
        res = None
        postData = json.dumps(data)
        if header != None:
            res = requests.post(url=url, data=postData, headers=header, verify=False)

        return res.json()

    def post_add_main(self, url, data=None, header=None):
        res = None
        # getData = json.dumps(data)
        if header is not None:
            res = requests.post(url=url + data[0], headers=header, verify=False)

        return res.json()

    def post_safe(self, url, data=None, header=None):
        res = None
        if header is not None:
            res = requests.post(url=url + data[0] + "?is_flag=1", headers=header, verify=False)

        return res.json()

    def post_cancel(self, url, data=None, header=None):
        res = None
        # getData = json.dumps(data)
        if header is not None:
            res = requests.post(url=url + data[0] + "/1a86f7c4f6df4082b47932cab368e69f", headers=header, verify=False)
        return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        # getData = json.dumps(data)
        if header is not None:
            res = requests.get(url=url, params=data, headers=header, verify=False)

        return res.json()

    def get_add_main(self, url, data=None, header=None):
        res = None
        # getData = json.dumps(data)
        if header is not None:
            print(header)
            if len(data) == 1:
                res = requests.get(url=url + data[0], headers=header, verify=False)
            else:
                res = requests.get(url=url + data[0] + "/" + data[1], headers=header, verify=False)
        else:
            res = requests.get(url=url + data, verify=False)
        return res.json()

    def delete_main(self, url, data=None, header=None):
        res = None
        if header is not None:
            res = requests.delete(url=url + data[0], headers=header, verify=False)
        else:
            res = requests.delete(url=url + data[0], verify=False)
        return res.json()

    def put_add_main(self, url, data=None, header=None):
        res = None
        putData = json.dumps(data["status"])
        if header is not None:
            res = requests.put(url=url + data["id"], data=putData, headers=header, verify=False)
        else:
            res = requests.put(url=url + data, verify=False)
        return res.json()

    def put_main(self, url, data=None, header=None):
        res = None
        putData = json.dumps(data)
        print(putData)
        if header is not None:
            res = requests.put(url=url, data=putData, headers=header, verify=False)
        else:
            res = requests.put(url=url + data, verify=False)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        res = None
        url = DEV_URL + url
        if method == 'Post':
            res = self.post_main(url, data, header)
        elif method == 'Post_Add':
            res = self.post_add_main(url, data, header)
        elif method == 'Get':
            res = self.get_main(url, data, header)
        elif method == 'Get_Add':
            res = self.get_add_main(url, data, header)
        elif method == 'Delete':
            res = self.delete_main(url, data, header)
        elif method == 'Put_Add':
            res = self.put_add_main(url, data, header)
        elif method == "Post_cancel":
            res = self.post_cancel(url, data, header)
        elif method == "Post_safe":
            res = self.post_safe(url, data, header)
        else:
            res = self.put_main(url, data, header)

        print("每次的请求头====%s\n"
              "每次请求的url=====%s\n"
              "每次请求的参数====%s\n"
              "每次请求的结果======%s" % (header, url, data, res))
        return json.dumps(res, ensure_ascii=False)
    # return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)


if __name__ == '__main__':
    # url = 'https://dev.baojiahuxing.com/api/app/account/agency/leaseAgency/getBatteryStockAndDispatching/' + data
    data = {
        "orderCode": "0001AA1000000000050P",
        "orderType": "1"
    }
    # data = "e6be515552824764a21eeed80aaf6837"
    # # url = 'https://dev.baojiahuxing.com/api/app/account/agency/leaseAgency/getBatteryStockAndDispatching/'
    header = {
        "Content-Type": "application/json",
        # "Content-Type":"form-data",
        "Authorization": "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxODEwMTM2NzcwOSIsInVzZXJJZCI6Ijk0OTAxNzc4Y2MzZjRiNDY5N2UxNjAwODcyYTAxYTcxIiwibmFtZSI6IuaxquWIqeW_tSIsImV4cCI6MTU3NDU4MDA0NX0.HzSft7QAwoJY_oRm8A2nz8dFyjEdDqxbbv3gpmG4F-_meGyYHCrq_AKwOj3OsnpGPRhy60AffrvwedhXg6QM-uFV_xjc-PbGYvWLHXkmRAvK39rX9BzNd2eYQ0Aev1uPy6UuYrNXFSxOTgC8vKrOvU2e7BC5O53gl3nJbIMrPig"
    }
    run = RunMethod()
    # res = run.run_main("Get", url,data= data, header=header)
    test = {
        "id": "b74c31fa65dd40cd9a5c9eb2ecad50c4",
        "type": "1",
        "front": "/Users/wangxiaonian/Desktop/Play/IMG_0171.jpg",
        "back": "/Users/wangxiaonian/Desktop/Play/IMG_0171.jpg"

    }

    aa = {
        "id": "1a86f7c4f6df4082b47932cab368e69f",
        "type": "1"
    }

    filePath = test["front"]
    param = list(test.keys())[list(test.values()).index(filePath)]
    # print(param)
    # with open(filePath, "rb") as file:
    #     data = {
    #         param: file.read(),
    #         "back": file.read()
    #     }
    # print(data)
    url = "https://dev.baojiahuxing.com/api/app/battery/batterymana/leaseBatteryManagement/rent/"
    # print(url)
    # res = requests.request(
    #     method="post",
    #     url=url,
    #     headers=header,
    #     files=data
    # )
    # print(res.content.decode("utf-8"))
    # res = run.run_main("Get", url, data, header)
    # print(res)
