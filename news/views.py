#-*- coding: UTF-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from models import News

# Create your views here.


def post_list(request):

    return render_to_response('post_list.html', locals())


def get_list(request):

    search_list = request.GET['search']  # 我
    news_list = News().getNews(search_list)

    # return render(request,'post_list.html',{})
    return render_to_response('post_list.html', locals())
