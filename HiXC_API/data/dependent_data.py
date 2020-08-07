# coding:utf-8
import sys
import json

#项目地址
sys.path.append('/Users/wangxiaonian/Desktop/Flyclouds/HiXC_API')
from util.operation_excel import OperationExcel
from util.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath, parse
from util.operation_json import OperetionJson


class DependdentData:
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data = GetData()

    # 通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    # 执行依赖测试，获取结果
    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        depend_case = self.data.is_depend(row_num)
        method = self.data.get_request_method(row_num)
        if depend_case is not None:
            self.depend_data = DependdentData(depend_case)
            # 获取的依赖响应数据
            # for depend_response_data_list in
            depend_response_data = self.depend_data.get_data_for_key(row_num)
            if len(depend_response_data) == 1:
                request_data_result = "".join(depend_response_data)
            else:
                request_data_result = ",".join([str(i) for i in depend_response_data])
            # 获取依赖的key
            depend_key = self.data.get_depend_field(row_num)
            depend_key_list = depend_key.split(",")
            for (key_list, key) in zip(request_data_result.split(","), depend_key_list):
                # print(key_list, key)
                if method == "Post" or method == "Get":
                    # print(key)
                    request_data[key] = key_list
                else:
                    request_data = depend_response_data
                    break
        # print("依赖request_data===========%s" % request_data)
        header = self.data.is_header(row_num)
        op_json = OperetionJson('../dataconfig/weChatToken')
        contentType = "application/json"
        token = op_json.get_data('token')
        if header == 'write':
            header = {
                'Content-Type': contentType
            }
        elif header == 'yes':
            op_json = OperetionJson('../dataconfig/token.json')
            token = op_json.get_data('token')
            header = {
                'Content-Type': contentType,
                'Authorization': token
            }
        elif header == 'weChat':
            header = {
                'Content-Type':  contentType,
                "Authorization": token
            }
        # print(header)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        res = run_method.run_main(method, url, request_data, header)
        return json.loads(res)

    # 根据依赖的key去获取执行依赖测试case的响应,然后返回
    def get_data_for_key(self, row):
        # 定义一个空数组,用来返回依赖case对应的响应结果
        denpent_key_result = []
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        # print("response_data=======%s" % response_data)
        # 把依赖数据根据"，"切割成数组遍历
        depend_data_list = depend_data.split(",")
        for data in depend_data_list:
            json_exe = parse(data)
            madle = json_exe.find(response_data)
            # 得到依赖key对应的值
            denpent_key = [math.value for math in madle][0]
            # 将依赖key对应的结果依次放入结果集里
            denpent_key_result.append(denpent_key)
        # 返回依赖key对应的结果
        return denpent_key_result


if __name__ == '__main__':
    response = {
        "code": 200,
        "extra": {},
        "data": {
            "token": "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMzgxMjM0NTY3OCIsInVzZXJJZCI6ImU2YmU1MTU1NTI4MjQ3NjRhMjFlZWVkODBhYWY2ODM3IiwibmFtZSI6IuaZj-a0quWGmyIsImV4cCI6MTU2ODIwMzQ3N30.f3TkEIVTkWpjLS91Czv5uXvgK8RT1JHNmrHeFhFWuMKzafjLVny2Bhz1v-kLGDy4KOZJYHTg0qfP65D51x0-797xMOtkdW28DSKjxbJw-c0Tj_nJhEKjXJ0zghn1xZNYyTTAuyZ83bB2zNoWEh9mhJ7Ihw2GmQ7eQpaWHjNIexs",
            "type": "1",
            # "needChangPass": false,
            "user": {
                "ts": "2018-09-10 16:55:40",
                "dr": "0",
                "id": "e6be515552824764a21eeed80aaf6837"
            }
        }
    }
    test = {
    "code": 1,
    "msg": None,
    "extra": {},
    "data": {
        "total": 1,
        "reqCode": None,
        "pageNo": 1,
        "rows": [
            {
                "billCode": "BHDAA1000000000007W",
                "id": "6888e4315c6041188b0efd2ab80b063c",
                "name": "补货单:BHDAA1000000000007W",
                "orderTime": "2018-11-14 09:32:06",
                "arriveTime": None,
                "goodsStatus": "2"
            }
        ]
    }
}
    res = ["data.rows[0].id"]
    list = ["data.rent", "data.serviceCost", "data.deposit"]
    for i in res:
        json_exe = parse(i)
        madle = json_exe.find(test)
        print([math.value for math in madle][0])
    print(test["code"],test["data"])
