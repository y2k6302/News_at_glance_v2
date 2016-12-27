# -*- coding: UTF-8 -*-

from pymongo import MongoClient

import jieba
jieba.set_dictionary('D:/TextMining/dict.txt.big.txt')  # 切換至中文繁體字庫
jieba.load_userdict("D:/TextMining/dict_keyw.txt")  # 加入自建詞庫
jieba.load_userdict("D:/TextMining/ptt.txt")  # 加入PTT詞庫


# Create your models here.

class News:
    # 透過__init__建立實體時，就順變進行資料庫連線 & 匯入jieba
    def __init__(self):
        self.client = MongoClient('127.0.0.1', 27017)
        db = self.client.test  # databaseName
        self.collection = db.news  # tableName
        self.collection2 = db.ptt  # tableName
        self.client.close()  # 資料庫關閉

    # 定義多重條件查詢方法
    def getNews(self, search_keyword):

        # 裝取所有新聞資料
        news_list = []
        ptt_list = []
        for post in self.collection.find(
                {'title': {"$regex": search_keyword}}).sort("date", 1).limit(50
                                                                             ):
            news_list.append(post)
        for post in self.collection2.find(
                {'title': {"$regex": search_keyword}}).sort("date", 1).limit(50
                                                                             ):
            ptt_list.append(post)
        return news_list, ptt_list
