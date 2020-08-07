# coding:utf-8
import pymysql.cursors
import json


class OperationMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host='dev.baojiahuxing.com',
            port=3306,
            user='demo',
            passwd='demo',
            db='battery-lease',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    # 查询一条数据
    def search_one(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        # result = json.dumps(result)
        return result


if __name__ == '__main__':
    op_mysql = OperationMysql()
    res = op_mysql.search_one("select * from t_lease_user WHERE mobile = '18101367709'")

    print(res)
