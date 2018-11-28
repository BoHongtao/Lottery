# encoding: utf-8
# @author: John
# @contact: BoHongtao@yeah.net
# @software: PyCharm
# @time: 2018/11/15 20:38

import urllib.request
import urllib.parse
import time
import pymysql.cursors
import json
import requests
from bs4 import BeautifulSoup

class Spilser:
    MYSQL_HOSTS = '127.0.0.1'
    MYSQL_USER = 'maxh5_com'
    MYSQL_PASSWORD = 'tWy3NyejyYXk6Z8n'
    MYSQL_PORT = '3306'
    MYSQL_DB = 'maxh5_com'
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
    # 十一运夺金
    def getdata(self):
        url = "https://kaijiang.aicai.com/open/kcResultByDate.do"
        self.NOWTIME = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        gameIndex = 303
        postdata = urllib.parse.urlencode({
            "gameIndex": gameIndex,
            "searchDate": self.NOWTIME
        }).encode("utf-8")
        req = urllib.request.Request(url, postdata)
        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safri/537.36")
        data = urllib.request.urlopen(req).read().decode("utf-8")
        self.CONTENT = data.replace('{"resultHtml":"','').replace('"}','').replace('期','').replace("<tr class='bg'>","</tr><tr class='bg'>")
        self.CONTENT = self.CONTENT+'</tr>'
        self.CONTENT = json.dumps(self.CONTENT)
        self.save_data()

    # 保存十一夺运金数据
    def save_data(self):
        # 获取游标
        connect = pymysql.Connect(user=self.MYSQL_USER, password=self.MYSQL_PASSWORD, host=self.MYSQL_HOSTS,database=self.MYSQL_DB, charset=self.MYSQL_CHARACTERS)
        cur = connect.cursor()
        sql = "REPLACE INTO lottery_phoenix_tree (id,time,content) VALUES ( '%s', '%s', %s)"
        value = (1, self.NOWTIME,self.CONTENT)
        cur.execute(sql % value)
        connect.commit()

    # 双色球
    def getSsqData(self):
        interface_url = "https://kaijiang.aicai.com/open/historyIssue.do"
        # 获取期数
        request_url = "https://kaijiang.aicai.com/fcssq/"
        response = requests.get(request_url, headers=self.headers).text
        gameIndex = '101'
        issue_no = BeautifulSoup(response, 'lxml').find('select', id='jq_last10_issue_no').findAll('option')[0].getText().strip()
        postdata = urllib.parse.urlencode({
            "gameIndex": gameIndex,
            "issueNo": issue_no
        }).encode("utf-8")
        req = urllib.request.Request(interface_url, postdata)
        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safri/537.36")
        data = urllib.request.urlopen(req).read().decode("utf-8")
        open_time = json.loads(data)['openTime']
        open_result = json.loads(data)['openResult'].replace("'","")
        self.save_data_ssq(open_time,open_result)

    # 保存双色球
    def save_data_ssq(self,open_time,open_result):
        # 获取游标
        connect = pymysql.Connect(user=self.MYSQL_USER, password=self.MYSQL_PASSWORD, host=self.MYSQL_HOSTS,database=self.MYSQL_DB, charset=self.MYSQL_CHARACTERS)
        cur = connect.cursor()
        sql = "REPLACE INTO lottery_phoenix_tree_ssq (id,open_time,content) VALUES ( '%s','%s', '%s')"
        value = (1, open_time,open_result)
        cur.execute(sql % value)
        connect.commit()

spider = Spilser()
spider.getdata()
spider.getSsqData()
