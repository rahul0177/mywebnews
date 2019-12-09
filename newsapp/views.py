from django.shortcuts import render
from django.http import HttpResponse
from newsapp.models import News,Headnews
import requests
import json

# Create your views here.
# def hello(request):
#     news=News.objects.all()
#     head=Headnews.objects.all()
#     return render(request,'index.html',{'news':news,'head':head})



def movie(request):
    url='https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=a61031f5666c4b859c01d83f873d5edd'
    r=requests.get(url).json()
    full=[]
    for i in r['articles']:
        news={
            
            'title':i['title'],
            'description':i['description'],
            'image':i['urlToImage'],
            'date':i['publishedAt'],
            'content':i['content'],
            'url':i['url'],

        }
        full.append(news)
    #context={'news':news}
    return render(request,'movies.html',{'news':full})
def science(request):
    url='https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=a61031f5666c4b859c01d83f873d5edd'
    r=requests.get(url).json()
    full=[]
    for i in r['articles']:
        news={
            'title':i['title'],
            'description':i['description'],
            'image':i['urlToImage'],
            'date':i['publishedAt'],
            'content':i['content'],
            'url':i['url']
        }
        full.append(news)
    #context={'news':news}
    return render(request,'science.html',{'news':full})


def hello(request):
    url='https://newsapi.org/v2/top-headlines?country=in&apiKey=a61031f5666c4b859c01d83f873d5edd'
    r=requests.get(url).json()
    
    full=[]
    for i in r['articles']:
        news={
            'name':i["source"]["name"],
            'title':i['title'],
            'description':i['description'],
            'image':i['urlToImage'],
            'date':i['publishedAt'],
            'content':i['content'],
            'url':i['url']
        }
        full.append(news)
    #context={'news':news}
    return render(request,'index.html',{'news':full})
def sports(request):
    url='https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=a61031f5666c4b859c01d83f873d5edd'
    r=requests.get(url).json()
    full=[]
    for i in r['articles']:
        news={
            'title':i['title'],
            'description':i['description'],
            'image':i['urlToImage'],
            'date':i['publishedAt'],
            'content':i['content'],
            'url':i['url']
        }
        full.append(news)
    #context={'news':news}
    return render(request,'sports.html',{'news':full})
def business(request):
    url='https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=a61031f5666c4b859c01d83f873d5edd'
    r=requests.get(url).json()
    full=[]
    for i in r['articles']:
        news={
            'title':i['title'],
            'description':i['description'],
            'image':i['urlToImage'],
            'date':i['publishedAt'],
            'content':i['content'],
            'url':i['url']
        }
        full.append(news)
    #context={'news':news}
    return render(request,'business.html',{'news':full})
def health(request):
    url='https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=a61031f5666c4b859c01d83f873d5edd'
    r=requests.get(url).json()
    full=[]
    for i in r['articles']:
        news={
            'title':i['title'],
            'description':i['description'],
            'image':i['urlToImage'],
            'date':i['publishedAt'],
            'content':i['content'],
            'url':i['url']
        }
        full.append(news)
    #context={'news':news}
    return render(request,'health.html',{'news':full})
def technolgy(request):
    url='https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=a61031f5666c4b859c01d83f873d5edd'
    r=requests.get(url).json()
    full=[]
    for i in r['articles']:
        news={
            'title':i['title'],
            'description':i['description'],
            'image':i['urlToImage'],
            'date':i['publishedAt'],
            'content':i['content'],
            'url':i['url']
        }
        full.append(news)
    #context={'news':news}
    return render(request,'tech.html',{'news':full})
def world(request):
    url='https://newsapi.org/v2/top-headlines?sources=google-news-uk&apiKey=a61031f5666c4b859c01d83f873d5edd'
    r=requests.get(url).json()
    full=[]
    for i in r['articles']:
        news={
            'title':i['title'],
            'description':i['description'],
            'image':i['urlToImage'],
            'date':i['publishedAt'],
            'content':i['content'],
            'url':i['url']
        }
        full.append(news)
    #context={'news':news}
    return render(request,'world.html',{'news':full})


