# coding: utf-8
import json


class OperetionJson:

    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = '../dataconfig/request.json'
        else:
            self.file_path = file_path
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(self.file_path, "rb") as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取数据
    def get_data(self, id):
        # print(type(self.data))
        if id is not None:
            return self.data[id]
        else:
            return None

    # 写json
    def write_data(self, data):
        with open('../dataconfig/token.json', 'w') as fp:
            fp.write(json.dumps(data))

    def write_user_data(self, data):
        with open('../dataconfig/weChatToken', 'w') as fp:
            fp.write(json.dumps(data))


if __name__ == '__main__':
    opjson = OperetionJson()
    print(opjson.get_data('searchLease'))
