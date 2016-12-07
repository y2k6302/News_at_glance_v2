#-*- coding: UTF-8 -*-
from django.db import models
from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import re
import jieba
jieba.set_dictionary('D:/TextMining/dict.txt.big.txt')  # 切換至中文繁體字庫
jieba.load_userdict("D:/TextMining/dict_keyw.txt")  # 加入自建詞庫
jieba.load_userdict("D:/TextMining/ptt.txt")  # 加入PTT詞庫



# Create your models here.

class News:
    # 資料庫連線 & 匯入jieba
    def __init__(self):
        self.client = MongoClient('127.0.0.1', 27017)
        db = self.client.test  # databaseName
        self.collection = db.news  # tableName
        self.collection2 = db.ptt  # tableName
        self.client.close()  # 資料庫關閉

    # 定義多重條件查詢方法
    def getNews(self, search_keyword):

        # 裝取所有新聞資料
        newsList = []
        for post in self.collection.find(
                {'title': {"$regex": search_keyword}}).sort("date", 1).limit(50
                                                                             ):
            newsList.append(post)

        return newsList
