# coding:utf-8
import sys

sys.path.append("/Users/wangxiaonian/Desktop/Flyclouds/HiXC_API/")
# sys.path.append('../')  # 新加入的
from util.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependdentData
from util.send_email import SendEmail
from util.operation_header import OperationHeader
from util.operation_json import OperetionJson


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_mail = SendEmail()

    # 程序执行的
    def go_on_run(self):
        global expect
        expect = True
        res = None
        pass_count = []
        fail_count = []
        # 10  0,1,2,3
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                # expect = self.data.get_expcet_data_for_mysql(i)
                expect = self.data.get_expcet_data(i)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                if depend_case is not None:
                    self.depend_data = DependdentData(depend_case)
                    # 获取的依赖响应数据
                    # for depend_response_data_list in
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    if len(depend_response_data) == 1:
                        request_data_result = "".join(depend_response_data)
                    else:
                        request_data_result = ",".join([str(i) for i in depend_response_data])
                    # 获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    depend_key_list = depend_key.split(",")
                    print(type(depend_key_list))
                    for (key_list, key) in zip(request_data_result.split(","), depend_key_list):
                        print(key_list, key)
                        if method == "Post" or method == "Get" or method == "Put_Add" or method == "Put":
                            # print(key)
                            request_data[key] = key_list
                        else:
                            request_data = depend_response_data
                            break


                contentType = "application/json"

                if header == 'write':
                    header = {
                        'Content-Type': contentType
                    }
                    res = self.run_method.run_main(method, url, data=request_data, header=header)
                    op_header = OperationHeader(res)
                    op_header.write_token()

                elif header == 'yes':
                    op_json = OperetionJson('../dataconfig/token.json')
                    token = op_json.get_data('token')
                    header = {
                        'Content-Type': contentType,
                        'Authorization': token
                    }
                    # print("request_data=======%s" % request_data)
                    res = self.run_method.run_main(method, url, request_data, header=header)
                elif header == 'write_user':
                    header = {
                        'Content-Type': contentType,
                    }
                    res = self.run_method.run_main(method, url, request_data, header=header)
                    op_header = OperationHeader(res)
                    op_header.write_user_token()
                elif header == 'weChat':
                    op_json = OperetionJson('../dataconfig/weChatToken')
                    token = op_json.get_data('token')
                    header = {
                        'Content-Type': contentType,
                        'Authorization': token
                    }
                    res = self.run_method.run_main(method, url, request_data, header=header)
                else:
                    res = self.run_method.run_main(method, url, request_data)

            if self.com_util.is_contain(expect, res) == 0:
                self.data.write_result(i, 'pass')
                pass_count.append(i)
            else:
                self.data.write_result(i, res)
                fail_count.append(i)

        # self.send_mail.send_main(pass_count, fail_count)


# 将执行判断封装
# def get_cookie_run(self,header):


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()
