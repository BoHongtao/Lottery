# 爬取高频彩票的信息，入库并展示在web端 #
## 环境要求： ##
	1. python 3.4+
	2. php 7.0+
	3. mysql 5.5+
## 配置 ##
spider.py放到/home/code下；
配置好web（基于ThinkPHP5.1）站点，启动nginx or apache
访问域名/public/index.php，可实现实时抓取显示；
数据库仅保存一条数据
