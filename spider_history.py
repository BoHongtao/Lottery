# encoding: utf-8
# @author: John
# @contact: BoHongtao@yeah.net
# @software: PyCharm
# @time: 2018/12/9 15:14
import urllib.request
import urllib.parse
import time
import pymysql.cursors
import json
import requests
from bs4 import BeautifulSoup

class Spilser:
    MYSQL_HOSTS = '127.0.0.1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_PORT = '3306'
    MYSQL_DB = 'spider'
    MYSQL_CHARACTERS = 'utf8'
    NOWTIME = ''
    CONTENT = ''
    headers = {
        'Connection': 'keep-alive',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    data = []

    # 十一运夺金历史数据
    def getdata(self):
        url = "http://zst.aicai.com/gaopin_11ydj/?q=d3"
        print("访问的URl"+url)
        response = requests.get(url,headers=self.headers).text
        res_table = BeautifulSoup(response,'lxml').find('table',id='chartsTable').tbody.findAll('tr')
        for tr in res_table:
            tds = tr.findAll('td')
            if len(tds)==1:
                continue
            print("---------------------------------------------------")
            self.data.clear()
            self.data.append(tds[0].get_text().strip())
            self.data.append(tds[1].get_text().strip())
            self.data.append(tds[2].get_text().strip())
            self.data.append(tds[3].get_text().strip())
            self.data.append(tds[4].get_text().strip())
            self.data.append(tds[5].get_text().strip())
            # print(self.is_save())
            # exit()
            if(self.is_save()==()):
                self.save_data()

    def is_save(self):
        # 获取游标
        connect = pymysql.Connect(user=self.MYSQL_USER, password=self.MYSQL_PASSWORD, host=self.MYSQL_HOSTS,
                                  database=self.MYSQL_DB, charset=self.MYSQL_CHARACTERS)
        cur = connect.cursor()
        sql = "select * from lottery_dyj where lottery_no = %s"
        value = (self.data[0])
        cur.execute(sql % value)
        print(sql % value)
        return cur.fetchall()

    # 保存十一夺运金数据
    def save_data(self):
        # 获取游标
        connect = pymysql.Connect(user=self.MYSQL_USER, password=self.MYSQL_PASSWORD, host=self.MYSQL_HOSTS,
                                  database=self.MYSQL_DB, charset=self.MYSQL_CHARACTERS)
        cur = connect.cursor()
        sql = "INSERT INTO lottery_dyj (id,lottery_no,first_no,second_no,three_no,four_no,five_no,lottery_time) VALUES ( %s, %s, %s,%s, %s, %s,%s, %s)"
        value = (0, self.data[0], self.data[1],self.data[2],self.data[3],self.data[4],self.data[5],int(time.time()))
        cur.execute(sql % value)
        print(sql % value)
        connect.commit()

spider = Spilser()
spider.getdata()